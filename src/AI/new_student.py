import pandas as pd
from pickle import *
import numpy as np
from sklearn.metrics import silhouette_score, silhouette_samples
import matplotlib.pyplot as plt
NUM_COLUMNS = ['Age', 'Grad_Period', 'Children', 'S1', 'A2', 'D3', 'A4', 'D5', 'S6', 'A7', 'S8', 'A9', 'D10', 'S11', 'S12', 'D13', 'S14', 'A15', 'D16', 'D17', 'S18', 'A19', 'A20', 'D21']
CAT_COLUMNS = ['Gender', 'Marital_Status','Ocupation']
NEW_DF = CAT_COLUMNS + NUM_COLUMNS

def cluster_inference(
    gender = '',
    marital_status = '',
    #university = '',
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
      #'University': [university],
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

  #Dados precisam vir do arquivo train.py
  dados_df = pd.DataFrame(novo_aluno, columns = NEW_DF)
  attr_normalizer = open('cat_normal_definition_joined_forms.model', 'r')
  joined_data = pd.DataFrame(columns=attr_normalizer.read().split(',') + NUM_COLUMNS)

  categorical_student_data = dados_df.drop(columns=NUM_COLUMNS)
  numeric_student_data = dados_df[NUM_COLUMNS]

  categorical_student_data = pd.get_dummies(categorical_student_data,prefix_sep='&')
  joined_student_data = pd.concat([joined_data,categorical_student_data],sort=False, ignore_index=True)

  normalizer = load(open('num_normalizer_joined_forms.model', 'rb'))
  numeric_student_data = normalizer.transform(numeric_student_data)

  #Recompor o data frame, a partir dos dados normalizados
  numeric_student_data = pd.DataFrame(numeric_student_data, columns=NUM_COLUMNS)
  joined_student_data = categorical_student_data.join(numeric_student_data, how='left')
  joined_data = pd.concat([joined_data,joined_student_data],sort=False, ignore_index=True )
  joined_data = joined_data.fillna(0)
  
  cluster_model = load(open('data_kmeans_model_joined_forms.pkl', 'rb'))
  #TODO: Retornar os dados do DASS além do cluster que pertence
  joined_data.iloc[:, :51].values
  designated_cluster = cluster_model.predict( joined_data.iloc[:, :34].values.tolist())



  X = joined_data.iloc[:, :34].values.tolist()

  silhouette_scores = []
  df = pd.read_csv('normalized_data_joined_forms.csv')

# Tente diferentes números de clusters
  for n_clusters in range(1, 17):
    # Crie um modelo K-Means com o número atual de clusters
    kmeans = cluster_model
    cluster_labels = kmeans.fit_predict(df)
    
    # Calcule a silhueta média para este número de clusters
    silhouette_avg = silhouette_score(df, cluster_labels)
    silhouette_scores.append(silhouette_avg)
    
    # Calcule as silhuetas individuais para cada ponto de dados
    sample_silhouette_values = silhouette_samples(df, cluster_labels)
    
    # Plote as silhuetas individuais
    plt.figure(figsize=(6, 4))
    plt.title(f'Número de Clusters = {n_clusters}')
    plt.xlabel('Valor da Silhueta')
    plt.ylabel('Cluster')
    
    y_lower = 10
    for i in range(n_clusters):
        ith_cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]
        ith_cluster_silhouette_values.sort()
        
        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i
        
        color = plt.cm.Spectral(float(i) / n_clusters)
        plt.fill_betweenx(np.arange(y_lower, y_upper),
                          0, ith_cluster_silhouette_values,
                          facecolor=color, edgecolor=color, alpha=0.7)
        
        plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
        
        y_lower = y_upper + 10
    
    plt.axvline(x=silhouette_avg, color="red", linestyle="--")
    plt.yticks([])
    plt.xlim([-0.1, 1])
    plt.ylim([0, len(df) + (n_clusters + 1) * 10])
    plt.savefig('Pure_Data.png')

  return str(designated_cluster)