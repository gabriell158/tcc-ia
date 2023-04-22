from flask import Flask, request
from src.AI.train import train
from src.AI.duplicated import duplicated
from src.AI.dass_sum import classify_anxscore, classify_depscore, classify_strscore
import traceback
import pandas as pd


app = Flask(__name__)
@app.route("/model",methods=["POST","GET"])
def model1():
  if request.method == "POST":
      df = pd.read_csv('teste.csv')
      new_df = duplicated(df)
      train(new_df)
      return 'Modelo treinado'
    #teste = train(request.data)
  if request.method == "GET":
    clusters = pd.read_pickle('clusters_description.pkl')
    print(clusters)
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