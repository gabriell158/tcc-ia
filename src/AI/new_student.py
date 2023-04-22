import pandas as pd
from pickle import load
from sklearn import preprocessing
from src.AI.raw_data import get_scalar_categorical_data, get_scalar_numeric_data, get_numeric_data
from src.AI.normalize import normalize_categorical_data, normalize_numeric_data, normalize_data

def cluster_inference(
    gender = '',
    marital_status = '',
    university = '',
    ocupation = '',
    children = '',
    age = '',
    grad_period = '',
    s1 = '',
    a2 = '',
    d3 = '',
    a4 = '',
    d5 = '',
    s6 = '',
    a7 = '',
    s8 = '',
    a9 = '',
    d10 = '',
    s11 = '',
    s12 = '',
    d13 = '',
    s14 = '',
    a15 = '',
    d16 = '',
    d17 = '',
    s18 = '',
    a19 = '',
    a20 = '',
    d21 = ''
    ):
  new_student = {
      'Gender': gender,
      'Marital_Status': marital_status,
      'University': university,
      'Ocupation': ocupation,
      'Children': children,
      'Age': age,
      'Grad_Period': grad_period,
      'S1': s1,
      'A2': a2,
      'D3': d3,
      'A4': a4,
      'D5': d5,
      'S6': s6,
      'A7': a7,
      'S8': s8,
      'A9': a9,
      'D10': d10,
      'S11': s11,
      'S12': s12,
      'D13': d13,
      'S14': s14,
      'A15': a15,
      'D16': d16,
      'D17': d17,
      'S18': s18,
      'A19': a19,
      'A20': a20,
      'D21': d21
  }
  df_new_student = pd.DataFrame([new_student])
  numeric_columns = get_scalar_numeric_data(age, grad_period, s1, a2, d3, a4, d5, s6, a7, s8, a9, d10, s11, s12, d13, s14, a15, d16, d17, s18, a19, a20, d21)

  categorical_data=['Gender', 'Marital_Status','University','Ocupation','Children']
#numéricas
  numeric_data = ['Age', 'Grad_Period', 'S1', 'A2', 'D3', 'A4', 'D5', 'S6', 'A7', 'S8', 'A9', 'D10', 'S11', 'S12', 'D13', 'S14', 'A15', 'D16', 'D17', 'S18', 'A19', 'A20', 'D21']
  #numeric_data = get_scalar_numeric_data(age, grad_period, s1, a2, d3, a4, d5, s6, a7, s8, a9, d10, s11, s12, d13, s14, a15, d16, d17, s18, a19, a20, d21)
  #categorical_data = get_scalar_categorical_data(gender, marital_status, university, ocupation, children) 
 
  data = pd.DataFrame(columns = categorical_data)
  data = pd.concat([data, df_new_student], ignore_index=True)
  e_cat = data.drop(columns=numeric_data)
  normalized_categorical = pd.get_dummies(e_cat, prefix_sep = '&')
  categorical_normalizer = ','.join(str(s) for s in normalized_categorical.columns.values.tolist())
  joined_data = pd.DataFrame(columns=categorical_normalizer.split(',') + numeric_data)
  normalized_numeric = data[numeric_data]
  normalizador = preprocessing.MinMaxScaler()
  

  numerico = normalizador.fit(numeric_data)

  concat_data = pd.concat([joined_data,normalized_categorical],sort=False, ignore_index=True)
  normalized_numeric = numerico.transform(normalized_numeric)

  #print(normalized_numeric)
  #Recompor o data frame, a partir dos dados normalizados
  normalized_numeric = pd.DataFrame(normalized_numeric, columns=numeric_data)
  concat_data = normalized_categorical.join(normalized_numeric, how='left')
  joined_data = pd.concat([joined_data,concat_data],sort=False, ignore_index=True )
  joined_data = joined_data.fillna(0)

  cluster_model = load(open('/content/dados_kmeans_model.pkl', 'rb'))
  designated_cluster = cluster_model.predict(joined_data.values.tolist())

  return designated_cluster

