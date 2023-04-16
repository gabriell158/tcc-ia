from flask import Flask, request

app = Flask(__name__)

@app.route("/model",methods=["POST","GET"])
def model1():
  if request.method == "POST":
    # treinar um novo modelo
    return
  if request.method == "GET":
    # listar os modelos treinados
    return

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