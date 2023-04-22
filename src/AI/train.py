from src.AI.normalize import normalize, catNormalize, numNormalize
from src.AI.elbow import elbow_method
from src.AI.raw_data import catCols, numCols
from src.AI.denormalize import denormalize

def train(df):
    gender = df['Gender']
    age = df['Age']
    marital = df['Marital_Status']
    university = df['University']
    ocupation = df['Ocupation']
    children = df['Children']
    grad_period = df['Grad_Period']
    s1 =  df['S1']
    a2 =  df['A2']
    d3 =  df['D3']
    a4 =  df['A4']
    d5 =  df['D5']
    s6 =  df['S6']
    a7 =  df['A7']
    s8 =  df['S8']
    a9 =  df['A9']
    d10 =  df['D10']
    s11 =  df['S11']
    s12 =  df['S12']
    d13 =  df['D13']
    s14 =  df['S14']
    a15 =  df['A15']
    d16 =  df['D16']
    d17 =  df['D17']
    s18 =  df['S18']
    a19 =  df['A19']
    a20 =  df['A20']
    d21 =  df['D21']
    
    cat_cols = catCols(gender, marital, university, ocupation, children)
    num_cols = numCols(age, grad_period, s1, a2, d3, a4, d5, s6, a7, s8, a9, d10, s11, s12, d13, s14, a15, d16, d17, s18, a19, a20, d21)
    cat_normalized = catNormalize(cat_cols)
    num_normalized, numerico = numNormalize(num_cols)
    print(numerico)
    
    normalized = normalize(num_cols, num_normalized, cat_normalized)
    model = elbow_method(normalized, cat_cols)
    cluster_description = denormalize(model, normalized, cat_normalized, cat_cols, numerico)
    response = []
    i = 0
    for cluster in cluster_description.values.tolist():        
        response.append({
            'number': i,
            'depression': cluster[-3],
            'anxiety': cluster[-2],
            'stress': cluster[-1]
        })
        i+=1
    return response

