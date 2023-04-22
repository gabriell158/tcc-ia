import pandas as pd
def get_centroids(dados_kmeans_model):
    return dados_kmeans_model.cluster_centers_

def cluster_analysis(dados_kmeans_model, data_norm):
    cluster_data=pd.DataFrame(dados_kmeans_model.cluster_centers_, columns=data_norm.columns)
    return cluster_data
