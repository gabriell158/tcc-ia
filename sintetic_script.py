#,Stamp,Email,Terms,Age,Gender,Marital_Status,Dob,University,Course,Grad_Period,Ocupation,Children,S1,A2,D3,A4,D5,S6,A7,S8,A9,D10,S11,S12,D13,S14,A15,D16,D17,S18,A19,A20,D21
import pandas as pd
import random
import numpy as np
from src.AI.normalize import *
from src.AI.train import *
from src.AI.new_student import *
from src.AI.dass_sum import *

#usar append
#criar um novo dataframe e ir adicionando os dados para concatenar com o oficial
sintetic_dataset_size = 1000

df = pd.read_csv('formated_data.csv')
df2 = pd.read_csv('form2.csv')
male_df = pd.read_csv('1000_Sintetic.csv')
df2 = df2.drop(columns=['Income','Financial_Support','Emotional_Support','Race','Scholarship','Lose_Scholarship','Transport'])  
dfs = [df, df2]
df = df._append(df2)
df = df.drop(columns=['Unnamed: 0', 'Stamp', 'Email', 'Terms', 'Dob', 'University', 'Course'])
#df = df._append(male_df)
#print(df)
#print(df)
#print(df)
#train(df)
# student_tracking = cluster_inference(
#             'Masculino','Solteira(o)','Estudante e Trabalho',0,28,2,2,1,2,1,1,2,1,2,2,2,2,2,1,1,2,2,1,2,2,1,1
#         )
# print(student_tracking)

# dep_sum = 1+1+2+1+2+1+1
# dass_dep_tracking = classify_depression_score(dep_sum)
# anx_sum =1+1+1+2+2+2+1
# dass_anx_tracking = classify_anxiety_score(anx_sum)
# str_sum = 2+2+2+2+2+1+2
# dass_str_tracking = classify_stress_score(str_sum)

# print(dass_dep_tracking)
# print(dass_anx_tracking)
# print(dass_str_tracking)

mean_df =  pd.DataFrame()

#Validar a média apenas de amostras masculinas
#criar mais 500 dados sinteticos dos dois generos

#dividir capitulo de resultado em 4 partes
# - plotar graficos das respostas nos dados puros (genero, periodo, ocupação)
# - dados putos - feito (silhueta 0.4)
# - geração de dados sinteticos masculinos - feito (silhueta 0.45 tendendo para 0.5 e 0.6)
# - usando dados sinteticos gerais com a media de todas - feito (silhueta 0.45 tendendo para 0.5 e 0.6)
# - usar a terceira parte tentando balancear a questão de genero
# - citar dificuldade em encontrar pessoas dispostas a responder e nichamos muito e que utilizamos método cientifico (dass-21)
mean_age = df['Age'].mean()
desvio_padrao_age = np.std(df['Age'])
dados_sinteticos_age = np.random.normal(mean_age, desvio_padrao_age, sintetic_dataset_size)
mean_df['Age'] = dados_sinteticos_age

mean_period = df['Grad_Period'].mean()
desvio_padrao_period = np.std(df['Grad_Period'])
dados_sinteticos_period = np.random.normal(mean_period, desvio_padrao_period, sintetic_dataset_size)
mean_df['Grad_Period'] = dados_sinteticos_period


mean_children = df['Children'].mean()
desvio_padrao_children = np.std(df['Children'])
dados_sinteticos_children = np.random.normal(mean_children, desvio_padrao_children, sintetic_dataset_size)
mean_df['Children'] = dados_sinteticos_children


mean_S1 = df['S1'].mean()
desvio_padrao_S1 = np.std(df['S1'])
dados_sinteticos_S1 = np.random.normal(mean_S1, desvio_padrao_S1, sintetic_dataset_size)
mean_df['S1'] = dados_sinteticos_S1


mean_A2 = df['A2'].mean()
desvio_padrao_A2 = np.std(df['A2'])
dados_sinteticos_A2 = np.random.normal(mean_A2, desvio_padrao_A2, sintetic_dataset_size)
mean_df['A2'] = dados_sinteticos_A2



mean_D3 = df['D3'].mean()
desvio_padrao_D3 = np.std(df['D3'])
dados_sinteticos_D3 = np.random.normal(mean_D3, desvio_padrao_D3, sintetic_dataset_size)
mean_df['D3'] = dados_sinteticos_D3


mean_A4 = df['A4'].mean()
desvio_padrao_A4 = np.std(df['A4'])
dados_sinteticos_A4 = np.random.normal(mean_A4, desvio_padrao_A4, sintetic_dataset_size)
mean_df['A4'] = dados_sinteticos_A4


mean_D5 = df['D5'].mean()
desvio_padrao_D5 = np.std(df['D5'])
dados_sinteticos_D5 = np.random.normal(mean_D5, desvio_padrao_D5, sintetic_dataset_size)
mean_df['D5'] = dados_sinteticos_A2


mean_S6 = df['S6'].mean()
desvio_padrao_S6 = np.std(df['S6'])
dados_sinteticos_S6 = np.random.normal(mean_S6, desvio_padrao_S6, sintetic_dataset_size)
mean_df['S6'] = dados_sinteticos_S6


mean_A7 = df['A7'].mean()
desvio_padrao_A7 = np.std(df['A7'])
dados_sinteticos_A7 = np.random.normal(mean_A7, desvio_padrao_A7, sintetic_dataset_size)
mean_df['A7'] = dados_sinteticos_A7


mean_S8 = df['S8'].mean()
desvio_padrao_S8 = np.std(df['S8'])
dados_sinteticos_S8 = np.random.normal(mean_S8, desvio_padrao_S8, sintetic_dataset_size)
mean_df['S8'] = dados_sinteticos_S8


mean_A9 = df['A9'].mean()
desvio_padrao_A9 = np.std(df['A9'])
dados_sinteticos_A9 = np.random.normal(mean_A9, desvio_padrao_A9, sintetic_dataset_size)
mean_df['A9'] = dados_sinteticos_A9


mean_D10 = df['D10'].mean()
desvio_padrao_D10 = np.std(df['D10'])
dados_sinteticos_D10 = np.random.normal(mean_D10, desvio_padrao_D10, sintetic_dataset_size)
mean_df['D10'] = dados_sinteticos_D10


mean_S11 = df['S11'].mean()
desvio_padrao_S11 = np.std(df['S11'])
dados_sinteticos_S11 = np.random.normal(mean_S11, desvio_padrao_S11, sintetic_dataset_size)
mean_df['S11'] = dados_sinteticos_S11


mean_S12 = df['S12'].mean()
desvio_padrao_S12 = np.std(df['S12'])
dados_sinteticos_S12 = np.random.normal(mean_S12, desvio_padrao_S12, sintetic_dataset_size)
mean_df['S12'] = dados_sinteticos_S12


mean_D13 = df['D13'].mean()
desvio_padrao_D13 = np.std(df['D13'])
dados_sinteticos_D13 = np.random.normal(mean_D13, desvio_padrao_D13, sintetic_dataset_size)
mean_df['D13'] = dados_sinteticos_D13


mean_S14 = df['S14'].mean()
desvio_padrao_S14 = np.std(df['S14'])
dados_sinteticos_S14 = np.random.normal(mean_S14, desvio_padrao_S14, sintetic_dataset_size)
mean_df['S14'] = dados_sinteticos_S14


mean_A15 = df['A15'].mean()
desvio_padrao_A15 = np.std(df['A15'])
dados_sinteticos_A15 = np.random.normal(mean_A15, desvio_padrao_A15, sintetic_dataset_size)
mean_df['A15'] = dados_sinteticos_A15


mean_D16 = df['D16'].mean()
desvio_padrao_D16 = np.std(df['D16'])
dados_sinteticos_D16 = np.random.normal(mean_D16, desvio_padrao_D16, sintetic_dataset_size)
mean_df['D16'] = dados_sinteticos_D16


mean_D17 = df['D17'].mean()
desvio_padrao_D17 = np.std(df['D17'])
dados_sinteticos_D17 = np.random.normal(mean_D17, desvio_padrao_D17, sintetic_dataset_size)
mean_df['D17'] = dados_sinteticos_D17


mean_S18 = df['S18'].mean()
desvio_padrao_S18 = np.std(df['S18'])
dados_sinteticos_S18 = np.random.normal(mean_S18, desvio_padrao_S18, sintetic_dataset_size)
mean_df['S18'] = dados_sinteticos_S18


mean_A19 = df['A19'].mean()
desvio_padrao_A19 = np.std(df['A19'])
dados_sinteticos_A19 = np.random.normal(mean_A19, desvio_padrao_A19, sintetic_dataset_size)
mean_df['A19'] = dados_sinteticos_A19


mean_A20 = df['A20'].mean()
desvio_padrao_A20 = np.std(df['A20'])
dados_sinteticos_A20 = np.random.normal(mean_A20, desvio_padrao_A20, sintetic_dataset_size)
mean_df['A20'] = dados_sinteticos_A20


mean_D21 = df['D21'].mean()
desvio_padrao_D21 = np.std(df['D21'])
dados_sinteticos_D21 = np.random.normal(mean_D21, desvio_padrao_D21, sintetic_dataset_size)
mean_df['D21'] = dados_sinteticos_D21
mean_df = mean_df.round(0)
mean_df = mean_df.apply(pd.to_numeric)
convert_dict = {'Age': int, 'Grad_Period': int, 'Children': int, 'S1': int, 'A2': int, 'D3': int, 'A4': int, 'D5': int, 'S6': int, 'A7': int, 'S8': int, 'A9': int, 'D10': int, 'S11': int, 'S12': int, 'D13': int, 'S14': int, 'A15': int, 'Age': int, 'D16': int, 'D17': int,'S18': int, 'A19': int, 'A20': int, 'D21': int}
mean_df = mean_df.astype(convert_dict)  
print(mean_df)

#mean_df.to_csv('1000_Sintetic.csv', index=False)
# replace_df = pd.read_csv('Male_Only_Sintetic_Dataframe.csv')
# def replace_nan(value):
#     if value < 0:
#         return 0
#     else:
#         return value
    
# replace_df.loc[replace_df["Age"] < 18, "Age"] = 18

# replace_df = replace_df.applymap(replace_nan)
# print(replace_df)
# replace_df.to_csv('Male_Only_Sintetic_Dataframe.csv', index=False)

#train(df)
# replace_df.to_csv('Sintetic-Dataframe-replaced.csv', index=False)

