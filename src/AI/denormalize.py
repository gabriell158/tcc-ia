import pandas as pd
from pickle import load
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import joblib


from src.AI.dass_sum import classify_anxscore, classify_depscore, classify_strscore

def denormalize(dados_kmeans_model, dados_norm, colunas_cat_norm, colunas_cat):
    cluster_data = pd.DataFrame(dados_kmeans_model.cluster_centers_, columns=dados_norm.columns)
    cluster_cat_data = cluster_data[colunas_cat_norm.columns].round(0).abs().astype(int)==1

    clusters_description = pd.DataFrame(columns=colunas_cat.columns)

    for i in range(0, len(cluster_cat_data)):
        cluster = cluster_cat_data.filter(items=[i], axis=0)
        cluster_desc = {}
        for c in cluster.columns:
            if c.find('&')>=0:
                if (cluster[c].values):
                    c = (c.split('&'))
                    cluster_desc[c[0]]=c[1]
            else:
                cluster_desc[c] = str(cluster[c].values[0])
        clusters_description = pd.concat([clusters_description, pd.DataFrame([cluster_desc])], ignore_index=True)

    cluster_data=pd.DataFrame(dados_kmeans_model.cluster_centers_, columns=dados_norm.columns)

    dados_normalizer = load(open('num_normalizer.model', 'rb'))
    num_normalize = pd.read_pickle('num_normalize.pkl')

    denormalized_data = dados_normalizer.inverse_transform(cluster_data[num_normalize.columns])
    denormalized_data = pd.DataFrame(denormalized_data, columns = num_normalize.columns).round(0).astype(int)

    clusters_description = clusters_description.join(denormalized_data, how='left', lsuffix='_left', rsuffix='_right')

    dep_sum = clusters_description['D3'] + clusters_description['D5'] + clusters_description['D10'] + clusters_description['D13'] + clusters_description['D16'] + clusters_description['D17'] + clusters_description['D21']
    anx_sum = clusters_description['A2'] + clusters_description['A4'] + clusters_description['A7'] + clusters_description['A9'] + clusters_description['A15'] + clusters_description['A19'] + clusters_description['A20']
    str_sum = clusters_description['S1'] + clusters_description['S6'] + clusters_description['S8'] + clusters_description['S11'] + clusters_description['S12'] + clusters_description['S14'] + clusters_description['S18']
    clusters_description['Depression_Score'] = dep_sum
    clusters_description['Anxiety_Score'] = anx_sum
    clusters_description['Stress_Score'] = str_sum

    clusters_description['Classify_Dep'] = clusters_description['Depression_Score'].apply(classify_depscore)
    clusters_description['Classify_Anx'] = clusters_description['Anxiety_Score'].apply(classify_anxscore)
    clusters_description['Classify_Str'] = clusters_description['Stress_Score'].apply(classify_strscore)
    clusters_description.to_pickle('clusters_description.pkl')

    return 'foi'