import pandas as pd
from pickle import load

from raw_data import catCols, numCols


def cluster_infer(
    gender = '',
    marital_status = '',
    university = '',
    ocupation = '',
    children = '',
    classify_dep = '',
    classify_anx = '',
    classify_str = '',
    age = '',
    grad_period = ''
    ):
  novo_aluno = {
      'Gender': gender,
      'Marital_Status': marital_status,
      'University': university,
      'Ocupation': ocupation,
      'Children': children,
      'Classify_Dep': classify_dep,
      'Classify_Anx': classify_anx,
      'Classify_Str': classify_str,
      'Age': age,
      'Grad_Period': grad_period
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

  print(e)
  return cluster_designado

