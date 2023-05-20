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

@app.route("/model",methods=["POST","GET"])

def model3():
  if request.method == "POST":
      try:
        #TODO: buscar os dados do firestore
        form = bucket.blob('questionario.csv')
        form.download_to_filename('questionario.csv')
        df = pd.read_csv('questionario.csv')
        
        formated_data = formatting_data(df)
        #TODO: remover csv formatted data
        formated_data.to_csv('formated_data.csv')
        clusters = train(formated_data)

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
    #TODO: Buscar os UserForms com esse user_id
    #TODO: Ordenar UserForms por data
    #TODO: Pegar último respondido
    #TODO: Usar o último UserForms para inferência
    #TODO: Pegar os dados do usuário do Firestore em Users
    #reli = reliability()
                                        # 1    2    3    4    5    6    7    8    9   10    11   12  13   14   15   16   17   18   19   20   21
    student_tracking = cluster_inference('Masculino','Solteira(o)','UFPR','Estudante','0','26','8', '2', '1', '1', '1', '2', '1', '0', '2', '0', '0', '2', '2', '2', '2', '0', '1', '2', '2', '1', '2', '1')
  
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