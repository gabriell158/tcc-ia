from flask import Flask, request
from src.AI.train import train
from src.AI.duplicated import formatting_data
import pandas as pd
import firebase_admin
import traceback
from firebase_admin import firestore, credentials, storage
from datetime import datetime
from src.AI.new_student import cluster_inference
from src.AI.reliability import reliability
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score


cred = credentials.Certificate('tcc-mental-health-credentials.json')
firebase_admin.initialize_app(cred, {'storageBucket': 'tcc-mental-health.appspot.com'})
db = firestore.client()
models_ref = db.collection(u'Models')
trackings_ref = db.collection(u'Trackings')
bucket = storage.bucket()
storage_models = ['cat_normal_definition.model', 'num_normalizer.model', 'data_kmeans_model.pkl']
app = Flask(__name__)
user_forms_ref = db.collection(u'UserForms')
users_ref = db.collection(u'Users')
forms_ref = db.collection(u'Forms')
forms_data = forms_ref.get()
users_data = users_ref.get()

@app.route("/model",methods=["POST","GET"])

def model3():
  if request.method == "POST":
      try:
        users = []
        forms = {}
        for x in forms_data:
          forms[x.id] = x.get('disorder')
        
        for x in users_data: 
          user = {
            'id': x.id,
            'Age': x.get('Age'),
            'Gender': x.get('Gender'),
            'Marital_Status': x.get('Marital_Status'),
            'University': x.get('University'),
            'Course': x.get('Course'),
            'Grad_Period': x.get('Grad_Period'),
            'Ocupation': x.get('Ocupation'),
            'Children': x.get('Children'),
            }
          user_forms = x.get('UserForms').get('Forms')
          for y in user_forms:
            user[forms[y.get('formId')]] = y.get('answer')
          users.append(user)
        dataset_users = pd.DataFrame(users)
        clusters = train(dataset_users)


        firebase_admin.firestore.client(app=None)
        response = {
          u'date': datetime.now(),
          u'selected': False,
          u'clusters': clusters
          }
       
        update_time, model_ref = models_ref.add(response)
        for model in storage_models:
          models = bucket.blob('models/' + model_ref.id + '/' + model)
          models.upload_from_filename(model)

        return response
        #TODO: buscar os dados do firestore -- Feito
        #TODO: remover csv formatted data -- Feito        
      
      except Exception:
        traceback.print_exc()
        return 'Something went wrong'

  if request.method == "GET":
    docs = models_ref.get()
    data = []
    for doc in docs:
        data.append(doc.to_dict())
    return data

@app.route("/model/<string:model_id>",methods=["POST","DELETE"])
def model2(model_id):
  document_ref = models_ref.document(model_id)
  document = document_ref.get()
  if request.method == "POST":
    if document.exists:
      kmeans_model = bucket.blob('models/' + model_id + '/data_kmeans_model.pkl')
      num_normalizer = bucket.blob('models/' + model_id + '/num_normalizer.model')
      cat_normal = bucket.blob('models/' + model_id + '/cat_normal_definition.model')

      kmeans_model.download_to_filename('data_kmeans_model.pkl')
      num_normalizer.download_to_filename('num_normalizer.pkl')
      cat_normal.download_to_filename('cat_normal_definition.pkl')

      return "Modelos Baixados"                                                            
    else:
      return f"Modelo com ID {model_id} não encontrado."
  
  if request.method == "DELETE":
    if document.exists:
      document_ref.delete()
      for file in storage_models:
        blob = bucket.blob('models/' + model_id + '/' + file)
        blob.delete()
      return f"Modelo com ID {model_id} excluído com sucesso."
    
    else:
      return f"Modelo com ID {model_id} não encontrado."

@app.route("/tracking/<string:user_id>",methods=["POST"])
def tracking(user_id):
  if request.method == "POST":
    #TODO: Buscar os UserForms com esse user_id -- Feito
    #TODO: Ordenar UserForms por data
    #TODO: Pegar último respondido
    #TODO: Usar o último UserForms para inferência
    #TODO: Pegar os dados do usuário do Firestore em Users -- Feito
    #TODO: Verificar necessidade de alteração da collection Users pois não da para adicionar vários Forms 
    # (Tentei na mão e ele atualizou os dados e não substituiu)
    user_data = users_ref.get()
    user_data = user_data[0].to_dict()
    inference_data = []
    forms = {}

    for x in forms_data:
      forms[x.id] = x.get('disorder')

    user = {
      'Age': user_data['Age'],
      'Gender': user_data['Gender'],
      'Marital_Status': user_data['Marital_Status'],
      'University': user_data['University'],
      'Course': user_data['Course'],
      'Grad_Period': user_data['Grad_Period'],
      'Ocupation': user_data['Ocupation'],
      'Children': user_data['Children']
    }
    user_forms = user_data['UserForms']['Forms']
    for y in user_forms:
      user[forms[y['formId']]] = y['answer']
    inference_data.append(user)

    student_tracking = cluster_inference(
      user['Gender'] ,user['Marital_Status'], user['University'], user['Ocupation'], user['Children'], user['Age'],
      user['Grad_Period'], user['S1'], user['A2'], user['D3'], user['A4'], user['D5'], user['S6'], user['A7'], user['S8'],
      user['A9'], user['D10'], user['S11'], user['S12'], user['D13'], user['S14'], user['A15'], user['D16'], user['D17'], user['S18'],
      user['A19'], user['A20'], user['D21']
    )

    query = models_ref.get()   
    data = []
    for doc in query:
       doc_data = doc.to_dict()
       clusters_data = doc_data['clusters']
       for cluster in clusters_data:
            data.append(cluster)

    tracking_data = data[int(student_tracking[1])]
    tracking = [tracking_data["anxiety"], tracking_data["depression"], tracking_data["stress"]]
    
    tracking_obj = {
       "anxiety": {
        "level": tracking[0],
        "reliability": 0
      },
       "depression": {
        "level": tracking[1],
        "reliability": 1
      },
       "stress": {
        "level": tracking[2],
        "reliability": 2
      },
     }
    response = {
          u'date': datetime.now(),
          u'userId': user_id,
          u'anxiety': tracking_obj["anxiety"],
          u'depression': tracking_obj["depression"],
          u'stress': tracking_obj["stress"]
        }
    trackings_ref.add(response)
    return response

# Verificar necessidade desse request
# @app.route("/form",methods=["GET"])
# def form():
#   if request.method == "GET":
#     # lista os formulários preenchidos
#     return 