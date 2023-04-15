import pandas as pd
from pickle import load

from normalize import normalize, numNormalize, catNormalize
from raw_data import catCols, numCols
from centroids import getCentroids
from new_student import cluster_infer

def denormalize():
    dados_kmeans_model = getCentroids()
    dados_norm = normalize()
    colunas_cat_norm = catNormalize()
    colunas_cat = catCols()
    colunas_num = numCols()

    cluster_data=pd.DataFrame(dados_kmeans_model.cluster_centers_, columns=dados_norm.columns)
    cluster_cat_data = cluster_data[colunas_cat_norm.columns].round(0).abs().astype(int)==1

#original cat
    clusters_description = pd.DataFrame(columns = colunas_cat.columns)

#Descrição dos clusters
    cluster_desc = {}

    for i in range(0,len(cluster_cat_data)):
        cluster = cluster_cat_data.filter(items=[i], axis = 0)
    for c in cluster.columns:
        if c.find('&')>=0:
            if (cluster[c].values):
                c = (c.split('&'))
                cluster_desc[c[0]]=c[1]
        
        else:
            cluster_desc[c] = str(cluster[c].values[0])
    clusters_description=clusters_description.append(cluster_desc, ignore_index=True)

    num_normalize = numNormalize()
    cluster_data=pd.DataFrame(dados_kmeans_model.cluster_centers_, columns=dados_norm.columns)

    dados_normalizer = load(open('/content/num_normalizer.model', 'rb'))
    denormalized_data = dados_normalizer.inverse_transform(cluster_data[num_normalize.columns])
    denormalized_data = pd.DataFrame(denormalized_data, columns = num_normalize.columns).round(0).astype(int)

    c = cluster_infer('Feminino','Casada(o)','UP','Estudante e Trabalho','1','Extremely Severe','Mild','Moderate','32','8')

    return clusters_description