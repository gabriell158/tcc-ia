from sklearn.cluster import KMeans
from normalize import normalize
from elbow import metodo_cotovelo
from pickle import  dump
import pandas as pd
def getCentroids():
    cluster_number = metodo_cotovelo()
    data_norm = normalize()
    dados_kmeans_model = KMeans(n_clusters=cluster_number).fit(data_norm)
    dump(dados_kmeans_model,open('dados_kmeans_model.pkl','wb'))

    return dados_kmeans_model

def clusterAnalysis(dados_kmeans_model):
    data_norm = normalize()
    cluster_data=pd.DataFrame(dados_kmeans_model.cluster_centers_, columns=data_norm.columns)
    return cluster_data
