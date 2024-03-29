from flask import Flask, request
from flasgger import Swagger
from src.AI.train import train
import pandas as pd
import firebase_admin
import traceback
from firebase_admin import firestore, credentials, storage
from datetime import datetime
from src.AI.new_student import cluster_inference
from src.AI.duplicated import formatting_data
from dotenv import load_dotenv
from src.AI.reliability import reliability
from os import environ
from src.AI.dass_sum import *
from flasgger.utils import swag_from

load_dotenv()

my_credentials = {
    "type": environ.get("TYPE"),
    "project_id": environ.get("PROJECT_ID"),
    "private_key_id": environ.get("PRIVATE_KEY_ID"),
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCtGml8AreghAHz\nl1DwAZg89ckBf8qD0UdYqcJluwW57h1CVjOFRW9edghqBDiV2pn9VgQSg2ZlfvR2\nNjAOgntLVU1XJXx4Nm2itpQqkzqs2oh/575i3nhCCXAnfOWGZLqKNmRNGzy8pRmL\niANlyWCvFUpI3yL9ZUY9JGegEQeOe2kOUApZi6XQB1327ylMvldGHQWUyWbEAJBl\npdjk12P1naZ8vS/5cKT544P53X1oPC++9ijOOF1isra9XfFExhgeEyTCc70oLaSi\nFNOIBJs2jTrRW+fDmrWSDjctCcP/DWY3DAdpy1DsafqKsFiEmhCm5yqQPz45GR4G\nQdB+rjL7AgMBAAECggEAJmY3hCTuKxNdg3XLpJIV/V/giQ6aFAe2tfpif0KvkIE7\nyF1q7GNswx2X3Dy3eLaXdlVAbgLsEhPJkveOTYmwZBO2JmDQbbJVO8UYtSEX4QRR\nR15XI4OKVcvWL0xLdjaeEs7iDSC/pnFRa1xutIOpiO1GH0gwcNmobSPIQP/GF1r3\nh5Vo1QP7HxekHaWZGO/u53NpFACDRcGq0x9rNqgWSeqShM9JsT+lfjvQTSpNCwcV\nsPkZX+QU5xjx3OjNUNHha5lq6CiYitspVG1dfY0S8Kg6Rszem48U05cGUfZh4sPE\nml0laC8BFcLRz3EWg/760BegFlZrw2A9/KZkwUTDEQKBgQDbVVsnHTHfK2w22l/B\nhL48hXDTo0V7IprDcyOxqt/QumVN+pa0TJcQEpbrib+NumrvdyhGnp+bOGLDG0Md\n1Ago28VdgmV/oZIAEaBXDxHrLIv86sd/bSWtMLyze1Xj0m41ajzVUyuYa1hHcJm0\n5GeXrvq6neFE7EOrRCLM19Yj9wKBgQDKCpNTieLypYske5VhHZjrHQtGRkrYQXt8\nEp9746jzqIWSPd2ttemgxivVUA7S8+8sfKcRL0ENMbX2IuKvNSrKE/EuYEn1MpU6\n2NDdV1cM6e+Uw/m0gb7g0YaW8OgbUgeNht7oLXAeaWd/ksPOm6Cw1zLDuyvkWVYK\nZDkfDqzgHQKBgQCJBWPypYx4bPonsnjLvo/R41M/A+ruKAojPBT6c1NrZGbRNlFb\nxdVBlzttXhqrAeC4ROqGY6Y2JB2e4bMmOUX3sIQ2DLY368n3/Qr8GFALaULy+AE1\nnAxDjAT244Ae2WE8QWhLpK/Bgp4d0zxTA7WrzwaX+vW2RxtnLSPIcLY4tQKBgETZ\nd70HBvSDHzhueMggauTr/9SRzZ2GKwtr2TdBrGhj7CiatnkkvZmRDozhfDu87qst\nS01a2gMiBoz69F6acptsUkroeyt4ckwcaIiU49A9w+vhIK23bRF1tTSooZ/1wyci\nZ8GdAlEKwD9EBz/X3tmEbAMxPFLTcrOV1bVUreqtAoGBANGOJwMQsJ8cIOmntXKj\nYFWiYdjsoUPptj/5EZXMkdx2cRE9ms3PaZ7IVCDYspMlPwb6wJiyE96h4l++OLqv\njzvxkGBFRYW6kchu8BMUUqKMwpGSWsBwH9ne3il4xoyGtc6yebF+vnzGLxnC204E\nOsPAmnhSUCkoGAjL9NmbyIMM\n-----END PRIVATE KEY-----\n",
    "client_email": environ.get("CLIENT_EMAIL"),
    "client_id": environ.get("CLIENT_ID"),
    "auth_uri": environ.get("AUTH_URI"),
    "token_uri": environ.get("TOKEN_URI"),
    "auth_provider_x509_cert_url": environ.get("AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": environ.get("CLIENT_X509_CERT_URL"),
}

cred = credentials.Certificate(my_credentials)
firebase_admin.initialize_app(cred, {"storageBucket": "tcc-mental-health.appspot.com"})
db = firestore.client()
models_ref = db.collection("Models")
trackings_ref = db.collection("Trackings")
bucket = storage.bucket()
storage_models = [
    "cat_normal_definition.model",
    "num_normalizer.model",
    "data_kmeans_model.pkl",
]
application = Flask(__name__)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",
    "swagger_ui": True,
    "specs_route": "/",
}
Swagger(application, config=swagger_config)

@application.route("/model", endpoint="model", methods=["POST", "GET"])
@swag_from("src/swagger/create_model.yml", endpoint="model", methods=["POST"])
@swag_from("src/swagger/get_models.yml", endpoint="model", methods=["GET"])
def model3():
    users_ref = db.collection("Users")
    forms_ref = db.collection("Forms")
    forms_data = forms_ref.get()
    users_data = users_ref.get()

    if request.method == "POST":
        try:
            users = []
            forms = {}
            for x in forms_data:
                forms[x.id] = x.get("disorder")

            for x in users_data:
                user = {
                    "id": x.id,
                    "Age": x.get("Age"),
                    "Gender": x.get("Gender"),
                    "Marital_Status": x.get("Marital_Status"),
                    "Grad_Period": x.get("Grad_Period"),
                    "Ocupation": x.get("Ocupation"),
                    "Children": x.get("Children"),
                }
                user_forms = x.get("UserForms").get("Forms")
                for y in user_forms:
                    user[forms[y.get("formId")]] = y.get("answer")
                users.append(user)
            dataset_users = pd.DataFrame(users)
            clusters = train(dataset_users)

            firebase_admin.firestore.client(app=None)
            response = {"date": datetime.now(), "selected": False, "clusters": clusters}

            update_time, model_ref = models_ref.add(response)
            for model in storage_models:
                models = bucket.blob("models/" + model_ref.id + "/" + model)
                models.upload_from_filename(model)
            response["id"] = model_ref.id
            return response

        except Exception:
            traceback.print_exc()
            return "Something went wrong"

    if request.method == "GET":
        docs = models_ref.get()
        data = []
        for doc in docs:
            model = {
                'id': doc.id,
                'model': doc.to_dict()
            }
            data.append(model)
        return data


@application.route(
    "/model/<string:model_id>", endpoint="model/id", methods=["POST", "DELETE"]
)
@swag_from("src/swagger/select_model.yml", endpoint="model/id", methods=["POST"])
@swag_from("src/swagger/delete_model.yml", endpoint="model/id", methods=["DELETE"])
def model2(model_id):

    document_ref = models_ref.document(model_id)
    document = document_ref.get()
    if request.method == "POST":
        if document.exists:
            kmeans_model = bucket.blob("models/" + model_id + "/data_kmeans_model.pkl")
            num_normalizer = bucket.blob("models/" + model_id + "/num_normalizer.model")
            cat_normal = bucket.blob(
                "models/" + model_id + "/cat_normal_definition.model"
            )

            kmeans_model.download_to_filename("data_kmeans_model.pkl")
            num_normalizer.download_to_filename("num_normalizer.pkl")
            cat_normal.download_to_filename("cat_normal_definition.pkl")

            return "Modelos Baixados"
        else:
            return (f"Modelo com ID {model_id} não encontrado.", 404)

    if request.method == "DELETE":
        if document.exists:
            document_ref.delete()
            for file in storage_models:
                blob = bucket.blob("models/" + model_id + "/" + file)
                blob.delete()
            return f"Modelo com ID {model_id} excluído com sucesso."

        else:
            return (f"Modelo com ID {model_id} não encontrado.", 404)


@application.route("/tracking/<string:user_id>", endpoint="tracking", methods=["POST"])
@swag_from("src/swagger/tracking.yml", endpoint="tracking", methods=["POST"])
def tracking(user_id):
    users_ref = db.collection("Users")
    forms_ref = db.collection("Forms")
    forms_data = forms_ref.get()

    if request.method == "POST":
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
            'Grad_Period': user_data['Grad_Period'],
            'Ocupation': user_data['Ocupation'],
            'Children': user_data['Children']
        }
            
        user_forms = user_data['UserForms']['Forms']
        for y in user_forms:
            user[forms[y['formId']]] = y['answer']
        inference_data.append(user)

        student_tracking = cluster_inference(
            user['Gender'] ,user['Marital_Status'], user['Ocupation'], user['Children'], user['Age'],
            user['Grad_Period'], user['S1'], user['A2'], user['D3'], user['A4'], user['D5'], user['S6'], user['A7'], user['S8'],
            user['A9'], user['D10'], user['S11'], user['S12'], user['D13'], user['S14'], user['A15'], user['D16'], user['D17'],
            user['S18'], user['A19'], user['A20'], user['D21']
        )

        ##DASS-21 TRACKING
        #Dep: d3, d5, d10, d13, d16, d17, d21
        #Anx: a2, a4, a7, a9, a15, a19, a20
        #Str: s1, s6, s8, s11, s12, s14, s18

        dep_sum = user["D3"] + user["D5"] + user["D10"] + user["D13"] + user["D16"] + user["D17"] + user["D21"]
        dass_dep_tracking = classify_depression_score(dep_sum)
        anx_sum = user["A2"] + user["A4"] + user["A7"] + user["A9"] + user["A15"] + user["A19"] + user["A20"]
        dass_anx_tracking = classify_anxiety_score(anx_sum)
        str_sum = user["S1"] + user["S6"] + user["S8"] + user["S11"] + user["S12"] + user["S14"] + user["S18"]
        dass_str_tracking = classify_stress_score(str_sum)

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
                "level": tracking[0]
            },
            "depression": {
                "level": tracking[1]
            },
            "stress": {
                "level": tracking[2]
            }
        }
        response = {
            u'date': datetime.now(),
            u'userId': user_id,
            u'anxiety': tracking_obj["anxiety"],
            u'depression': tracking_obj["depression"],
            u'stress': tracking_obj["stress"],
            u'DASS_Dep': dass_dep_tracking,
            u'DASS_Anx': dass_anx_tracking,
            u'DASS_Str': dass_str_tracking
        }
        trackings_ref.add(response)
        return response

if __name__ == "__main__":
    application.run(
        host=environ.get("API_HOST"),
        port=environ.get("API_PORT"),
        debug=environ.get("DEBUG"),
    )
