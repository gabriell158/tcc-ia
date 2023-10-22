import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('formated_data.csv')
df2 = pd.read_csv('form2.csv')
df2 = df2.drop(columns=['Income','Financial_Support','Emotional_Support','Race','Scholarship','Lose_Scholarship','Transport'])  
dfs = [df, df2]
df = df._append(df2)
df.to_csv('joined_forms.csv', index=False)

# #By Income
contagem = df2['Income'].value_counts()
plt.figure(figsize=(8, 10))
contagem.plot(kind='bar')
plt.legend()
plt.savefig('Income.png')


contagem = df2['Race'].value_counts()
plt.figure(figsize=(8, 10))
contagem.plot(kind='bar')
plt.legend()
plt.savefig('Race.png')


contagem = df2['Financial_Support'].value_counts()
plt.figure(figsize=(8, 10))
contagem.plot(kind='bar')
plt.legend()
plt.savefig('Financial_Support.png')


contagem = df2['Emotional_Support'].value_counts()
plt.figure(figsize=(8, 10))
contagem.plot(kind='bar')
plt.legend()
plt.savefig('Emotional_Support.png')

contagem = df2['Scholarship'].value_counts()
plt.figure(figsize=(8, 10))
contagem.plot(kind='bar')
plt.legend()
plt.savefig('Scholarship.png')

contagem = df2['Lose_Scholarship'].value_counts()
plt.figure(figsize=(8, 10))
contagem.plot(kind='bar')
plt.legend()
plt.savefig('Lose_Scholarship.png')
# sintetic_df = pd.read_csv('Sintetic-Dataframe-replaced.csv')
# df2 = df2.drop(columns=['Income','Financial_Support','Emotional_Support','Race','Scholarship','Lose_Scholarship','Transport'])  
# dfs = [df, df2]
# df = df._append(df2)

# #By Gender
# contagem = df['Gender'].value_counts()
# plt.figure(figsize=(8, 10))
# contagem.plot(kind='bar', color=['yellow', 'green', 'blue'])

# # Adicionar rótulos e título
# plt.xlabel('Gênero')
# plt.ylabel('Quantidade')
# plt.title('Contagem de Homens e Mulheres')
# plt.savefig('Gender.png')


# #By Ocupation
# contagem = df['Ocupation'].value_counts()
# plt.figure(figsize=(10, 15))
# contagem.plot(kind='bar', color=['yellow', 'blue'])

# # Adicionar rótulos e título
# plt.xlabel('Ocupação')
# plt.ylabel('Quantidade')
# plt.title('Contagem de Estudantes que Trabalham durante a Graduação')
# plt.savefig('Ocupation.png')

# #By Period
# contagem = df['Grad_Period'].value_counts()
# plt.figure(figsize=(8, 8))
# contagem.plot(kind='bar')

# # Adicionar rótulos e título
# plt.xlabel('Período')
# plt.ylabel('Quantidade')
# plt.title('Contagem de Estudantes Por Período')
# plt.savefig('Period.png')