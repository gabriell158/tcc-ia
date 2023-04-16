import pandas as pd
from pickle import load

from src.AI.raw_data import catCols, numCols

def cluster_infer(
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
  novo_aluno = {
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

  num_columns = numCols()
  columns_to_keep = catCols() 
  dados_df = pd.DataFrame(columns = columns_to_keep)
  dados_df = dados_df.append(novo_aluno, ignore_index = True)

  attr_normalizer = open('/content/cat_normal_definition.model', 'r')
  e = pd.DataFrame(columns=attr_normalizer.read().split(',') + num_columns)
  
  e_cat = dados_df.drop(columns=num_columns)
  e_num = dados_df[num_columns]

  e_cat = pd.get_dummies(e_cat,prefix_sep='&')
  # print(e_cat)
  e_ = pd.concat([e,e_cat],sort=False, ignore_index=True)
  # =print(e_)

  school_normalizer = load(open('/content/num_normalizer.model', 'rb'))
  e_num = school_normalizer.transform(e_num)
  

  #Recompor o data frame, a partir dos dados normalizados
  e_num = pd.DataFrame(e_num, columns=num_columns)
  e_ = e_cat.join(e_num, how='left')
  e = pd.concat([e,e_],sort=False, ignore_index=True )
  e = e.fillna(0)

  cluster_model = load(open('/content/dados_kmeans_model.pkl', 'rb'))
  cluster_designado = cluster_model.predict(e.values.tolist())

  #print(e)
  return cluster_designado

