import pandas as pd
from sklearn import preprocessing

def cluster_inference(kmeans_model,
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
      'Gender': [gender],
      'Marital_Status': [marital_status],
      'University': [university],
      'Ocupation': [ocupation],
      'Children': [children],
      'Age': [age],
      'Grad_Period': [grad_period],
      'S1': [s1],
      'A2': [a2],
      'D3': [d3],
      'A4': [a4],
      'D5': [d5],
      'S6': [s6],
      'A7': [a7],
      'S8': [s8],
      'A9': [a9],
      'D10': [d10],
      'S11': [s11],
      'S12': [s12],
      'D13': [d13],
      'S14': [s14],
      'A15': [a15],
      'D16': [d16],
      'D17': [d17],
      'S18': [s18],
      'A19': [a19],
      'A20': [a20],
      'D21': [d21]
  }
  num_columns = ['Age', 'Grad_Period', 'S1', 'A2', 'D3', 'A4', 'D5', 'S6', 'A7', 'S8', 'A9', 'D10', 'S11', 'S12', 'D13', 'S14', 'A15', 'D16', 'D17', 'S18', 'A19', 'A20', 'D21']
  columns_to_keep=['Gender', 'Marital_Status','University','Ocupation','Children']

  dados_df = pd.DataFrame(novo_aluno, columns = columns_to_keep + num_columns)
  categorical_normalizer = "Gender&Feminino,Gender&Masculino,Gender&Outro,Marital_Status&Casada(o),Marital_Status&Solteira(o),University&FEMPAR,University&FPP,University&FPS,University&Federal do Paraná ,University&PUCPR,University&UFPR,University&UFPR ,University&UNICESUMAR,University&UNISUL,University&UNIVALI,University&UNOESTE,University&UP,University&Unicesumar ,University&ufpr,Ocupation&Estudante,Ocupation&Estudante e Trabalho,Children&0,Children&1"
  joined_data = pd.DataFrame(columns=categorical_normalizer.split(',') + num_columns)
  categorical_student_data = dados_df.drop(columns=num_columns)
  numeric_student_data = dados_df[num_columns]

  categorical_student_data = pd.get_dummies(categorical_student_data,prefix_sep='&')
  joined_student_data = pd.concat([joined_data,categorical_student_data],sort=False, ignore_index=True)

  normalizador = preprocessing.MinMaxScaler().fit(numeric_student_data)
  numeric_student_data = normalizador.transform(numeric_student_data)
  

  #Recompor o data frame, a partir dos dados normalizados
  numeric_student_data = pd.DataFrame(numeric_student_data, columns=num_columns)
  joined_student_data = categorical_student_data.join(numeric_student_data, how='left')
  joined_data = pd.concat([joined_data,joined_student_data],sort=False, ignore_index=True )
  joined_data = joined_data.fillna(0)

  
  designated_cluster = kmeans_model.predict(joined_data.values.tolist())

  return str(designated_cluster)