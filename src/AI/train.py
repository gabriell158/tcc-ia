from src.AI.normalize import normalize_data, normalize_categorical_data, normalize_numeric_data
from src.AI.elbow import elbow_method
from src.AI.raw_data import get_categorical_data, get_numeric_data
from src.AI.denormalize import denormalize_data
from src.AI.centroids import get_centroids
from pickle import dump
import pandas as pd

def train(data):
    gender = data['Gender']
    age = data['Age']
    marital = data['Marital_Status']
    ocupation = data['Ocupation']
    children = data['Children']
    grad_period = data['Grad_Period']
    s1 =  data['S1']
    a2 =  data['A2']
    d3 =  data['D3']
    a4 =  data['A4']
    d5 =  data['D5']
    s6 =  data['S6']
    a7 =  data['A7']
    s8 =  data['S8']
    a9 =  data['A9']
    d10 =  data['D10']
    s11 =  data['S11']
    s12 =  data['S12']
    d13 =  data['D13']
    s14 =  data['S14']
    a15 =  data['A15']
    d16 =  data['D16']
    d17 =  data['D17']
    s18 =  data['S18']
    a19 =  data['A19']
    a20 =  data['A20']
    d21 =  data['D21']
    
    num_columns = ['Age', 'Grad_Period', 'S1', 'A2', 'D3', 'A4', 'D5', 'S6', 'A7', 'S8', 'A9', 'D10', 'S11', 'S12', 'D13', 'S14', 'A15', 'D16', 'D17', 'S18', 'A19', 'A20', 'D21']
    cat_cols=['Gender', 'Marital_Status','Ocupation','Children']
    new_df = cat_cols + num_columns

    categorical_columns = get_categorical_data(gender, marital, ocupation, children)
    numeric_columns = get_numeric_data(age, grad_period, s1, a2, d3, a4, d5, s6, a7, s8, a9, d10, s11, s12, d13, s14, a15, d16, d17, s18, a19, a20, d21)
    categorical_normalized = normalize_categorical_data(categorical_columns)
    numeric_normalized, numeric = normalize_numeric_data(numeric_columns)
    normalized_data, numeric_model = normalize_data(numeric_columns, numeric_normalized, categorical_normalized)
    kmeans_model = elbow_method(normalized_data, categorical_columns)
    denormalized_clusters = denormalize_data(kmeans_model, normalized_data, categorical_normalized, categorical_columns, numeric, numeric_model)
    cluster_centers = get_centroids(kmeans_model)

    dump(denormalized_clusters,open('cluster_description.pkl','wb'))
    dump(normalized_data, open('normalized_data.pkl','wb'))
    pkl_file = pd.read_pickle('cluster_description.pkl')
    pkl_file.to_csv('clusters_description.csv')
    pkl_file = pd.read_pickle('normalized_data.pkl')
    pkl_file.to_csv('normalized_data.csv')

    response = []
    i = 0
    for cluster in denormalized_clusters.values.tolist():        
        response.append({
            'number': i,
            'gender': cluster[-33],
            'marital': cluster[-32],
            'ocupation': cluster[-30],
            'children': cluster[-29],
            'age': cluster[-28],
            'grad_period': cluster[-27],
            'depression': cluster[-3],
            'anxiety': cluster[-2],
            'stress': cluster[-1]
        })
        i+=1
    return response

