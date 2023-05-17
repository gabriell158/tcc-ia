from flask import Flask, request
from src.AI.train import train
from src.AI.duplicated import formatting_data
import pandas as pd
import firebase_admin
import traceback
from firebase_admin import firestore, credentials, storage
from datetime import datetime
from src.AI.new_student import cluster_inference

cred = credentials.Certificate('tcc-mental-health-credentials.json')
firebase_admin.initialize_app(cred, {'storageBucket': 'tcc-mental-health.appspot.com'})
db = firestore.client()
models_ref = db.collection(u'Models')
trackings_ref = db.collection(u'Trackings')
bucket = storage.bucket()

app = Flask(__name__)

@app.route("/model",methods=["POST","GET"])

def model3():
  if request.method == "POST":
      try:
        #puxar os normalizadores quando escolher a modelo pra utilizar
        form = bucket.blob('questionario.csv')
        form.download_to_filename('questionario.csv')
        df = pd.read_csv('questionario.csv')

        formated_data = formatting_data(df)
        clusters, kmeans_model, denormalized = train(formated_data)
        # pkl_file = pd.read_pickle('clusters_description.pkl')
        # pkl_file.to_csv('clusters_description.csv')

        storage_models = ['cat_normal_definition.model', 'num_normalizer.model', 'data_kmeans_model.pkl']
        date = datetime.now()
        date_format = date.strftime("%d-%m-%Y-%H:%M")
        
        for model in storage_models:
          models = bucket.blob('models/' + date_format + '/' + model)
          models.upload_from_filename(model)

        firebase_admin.firestore.client(app=None)
        response = {
          u'date': datetime.now(),
          u'selected': False,
          u'clusters': clusters
          }
       
        models_ref.add(response)

        return response
      
      except Exception:
        traceback.print_exc()
        return 'Something went wrong'

  if request.method == "GET":
    #listar modelo treinado
    docs = models_ref.get()
    for doc in docs:
        data = doc.to_dict()

    return data

@app.route("/model/<string:model_id>",methods=["POST","DELETE"])
def model2(model_id):
  document_ref = models_ref.document(model_id)
  document = document_ref.get()
  if request.method == "POST":
    # Iterar sobre os documentos e imprimir todos os dados
    if document.exists:
      data = document.to_dict()
      return data
    else:
      return f"Modelo com ID {model_id} não encontrado."
  
  if request.method == "DELETE":
    if document.exists:
      # Excluir o documento
      document_ref.delete()
      return f"Modelo com ID {model_id} excluído com sucesso."
    
    else:
      return f"Modelo com ID {model_id} não encontrado."

@app.route("/tracking",methods=["POST"])
def tracking():
  if request.method == "POST":
    # faz a inferencia e salva no banco o resultado
    # retorna o resultado da inferencia
    df = pd.read_csv('teste.csv')
    formated_data = formatting_data(df)
    clusters, kmeans_model, denormalized_clusters = train(formated_data)
    print(kmeans_model)
    student_tracking = cluster_inference(kmeans_model, 'Masculino','Solteira(o)','UFPR','Estudante e Trabalho','0','26','4', '1', '0', '1', '1', '2', '2', '0', '1', '1', '0', '2', '2', '2', '0', '0', '0', '0', '1', '2', '2', '0')
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
          u'anxiety': tracking_obj["anxiety"],
          u'depression': tracking_obj["depression"],
          u'stress': tracking_obj["stress"]
          }
    trackings_ref.add(response)
    return response

@app.route("/form",methods=["GET"])
def form():
  if request.method == "GET":
    # lista os formulários preenchidos
    return