from flask import Flask, request
from src.AI.train import train
from src.AI.duplicated import duplicated
import pandas as pd
import firebase_admin
import traceback
from firebase_admin import firestore, credentials
from datetime import datetime


app = Flask(__name__)
@app.route("/model",methods=["POST","GET"])
def model1():
  if request.method == "POST":
      try:

        df = pd.read_csv('teste.csv')
        new_df = duplicated(df)
        clusters = train(new_df)
        cred = credentials.Certificate('tcc-mental-health-credentials.json')

        firebase_admin.initialize_app(cred)
        db = firestore.client()
        pkl_file = pd.read_pickle('clusters_description.pkl')
        pkl_file.to_csv('clusters_description.csv')
        
        firebase_admin.firestore.client(app=None)
        response = {
          u'date': datetime.now(),
          u'selected': False,
          u'clusters': clusters
          }
       
        db.collection(u'Models').add(response)
        return response
      except Exception:
        traceback.print_exc()
        return 'fodeus'
    #teste = train(request.data)
  if request.method == "GET":
    #listar modelo treinado
    return 'salve'

@app.route("/model/<int:model_id>",methods=["POST","DELETE"])
def model2():
  if request.method == "POST":
    # seleciona o modelo para ser usado para inferencia
    return
  if request.method == "DELETE":
    # exclui o modelo
    return

@app.route("/tracking",methods=["POST"])
def tracking():
  if request.method == "POST":
    # faz a inferencia e salva no banco o resultado
    # retorna o resultado da inferencia
    return

@app.route("/form",methods=["GET"])
def form():
  if request.method == "GET":
    # lista os formulários preenchidos
    return