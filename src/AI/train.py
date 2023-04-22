from src.AI.normalize import normalize_data, normalize_categorical_data, normalize_numeric_data
from src.AI.elbow import elbow_method
from src.AI.raw_data import get_categorical_data, get_numeric_data
from src.AI.denormalize import denormalize_data

def train(data):
    gender = data['Gender']
    age = data['Age']
    marital = data['Marital_Status']
    university = data['University']
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
    
    categorical_columns = get_categorical_data(gender, marital, university, ocupation, children)
    numeric_columns = get_numeric_data(age, grad_period, s1, a2, d3, a4, d5, s6, a7, s8, a9, d10, s11, s12, d13, s14, a15, d16, d17, s18, a19, a20, d21)
    categorical_normalized = normalize_categorical_data(categorical_columns)
    numeric_normalized, numeric = normalize_numeric_data(numeric_columns)
    normalized_data, numeric_model = normalize_data(numeric_columns, numeric_normalized, categorical_normalized)
    kmeans_model = elbow_method(normalized_data, categorical_columns)
    denormalized_clusters = denormalize_data(kmeans_model, normalized_data, categorical_normalized, categorical_columns, numeric, numeric_model)
    response = []
    i = 0
    for cluster in denormalized_clusters.values.tolist():        
        response.append({
            'number': i,
            'depression': cluster[-3],
            'anxiety': cluster[-2],
            'stress': cluster[-1]
        })
        i+=1
    return response

