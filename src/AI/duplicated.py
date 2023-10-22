import pandas as pd
def formatting_data():
    df = pd.read_csv("form2.csv")
    df = pd.DataFrame(df)
    #df.columns["Stamp", "Email", "Terms", "Age", "Gender", "Marital_Status", "University", "Course", "Grad_Period", "Ocupation", "Children", "Income", "Financial_Support", "Emotional_Support", "Race", "Scholarship", "Lose_Scholarship", "Transport", 'S1', 'A2', 'D3', 'A4', 'D5', 'S6', 'A7', 'S8', 'A9', 'D10', 'S11', 'S12', 'D13', 'S14', 'A15', 'D16', 'D17', 'S18', 'A19', 'A20','D21']
    
    df = df.drop(columns=['Stamp', 'Email', 'Terms'])
    print(df)
#     df.columns = ['Stamp', 'Email', 'Terms', 'Age', 'Gender', 'Marital_Status', 'Dob', 'University', 'Course', 'Grad_Period', 'Ocupation', 'Children', 'S1', 'A2', 'D3', 'A4', 'D5', 'S6', 'A7', 'S8', 'A9', 'D10', 'S11', 'S12', 'D13', 'S14', 'A15', 'D16', 'D17', 'S18', 'A19', 'A20', 'D21']

#     university_rename = {'Up': 'UP', 
#                         'Positivo': 'UP', 
#                         'positivo': 'UP',
#                         'Universidade Positivo': 'UP',
#                         'Universidade positivo': 'UP',
#                         'Universidade Positivo ': 'UP',
#                         'Universidade positivo ': 'UP',
#                         'unisul pb': 'UNISUL',
#                         'UNISUL PB': 'UNISUL',
#                         'Unisul': 'UNISUL',
#                         'Unicesumar': 'UNICESUMAR',
#                         'Unisul - Pedra Branca ': 'UNISUL',
#                         'UNISUL PEDRA BRANCA ': 'UNISUL',
#                         'Universidade do Sul de Santa Catarina': 'UNISUL',
#                         'Unisul Pedra Branca': 'UNISUL',
#                         'Unisul- Tubarão': 'UNISUL',
#                         'Unisul TB': 'UNISUL',
#                         'Unisul': 'UNISUL',
#                         'unisul pedra branca ': 'UNISUL',
#                         'Univali Itajaí': 'UNIVALI',
#                         'Univali': 'UNIVALI',
#                         'UNIVALI SC': 'UNIVALI',
#                         'Universidade Tuiuti do Paraná (UTP)': 'UTP',
#                         'Unisul PB': 'UNISUL',
#                         'Unisul Tubarão ': 'UNISUL',
#                         'PUCPR ': 'PUCPR',
#                         'pucpr': 'PUCPR',
#                         'Fpp': 'FPP',
#                         'Fempar ': 'FEMPAR',
#                         'Unoeste': 'UNOESTE',
#                         'Federal do Paraná': 'UFPR',
#                         'Ufpr': 'UFPR',
#                         'pucpr': 'PUCPR',
#                         'Pucpr': 'PUCPR',
#                         }
#     df['University'].replace(university_rename,inplace=True)

#     #Corrigindo respostas duplicadas da coluna Children e Age
#     children_rename = {'Não': '0', 
#                     'Não ': '0',
#                     'Nao': '0', 
#                     'Nenhum': '0',
#                     'Sim': '1'
#                     }
#     df['Children'].replace(children_rename,inplace=True)
#     age_rename = {'22 anos': '22'}
#     df['Age'].replace(age_rename,inplace=True)
#     #Atribuindo coluna Age como int
#     df['Age'] = df['Age'].astype(int)

#     #pd.set_option('display.max_rows', None)
# #Corrigindo respostas duplicadas da coluna Children e Age
#     period_rename = {'9°': '9',
#                     '9º período ': '9',
#                     '1 fase ': '1',
#                     '1 fase': '1',
#                     '1 semestre ': '1',
#                     '1º': '1',
#                     '1º semestre': '1',
#                     '1° fase': '1',
#                     '5° semestre': '5',
#                     'Primeiro período ': '1',
#                     '5 fase': '5',
#                     '2023- 2028': '1',
#                     '1°': '1',
#                     '5º período.': '5',
#                     'quarto período': '4',
#                     '4° período': '4',
#                     'quarto ': '4',
#                     'Quarto': '4',
#                     '4º P': '4',
#                     '4°': '4',
#                     '1 periodo': '1',
#                     '7° Período ': '7',
#                     '6 período ': '6',
#                     'Segundo ': '2',
#                     '2º período ': '2',
#                     'Segundo periodo': '2',
#                     '2020 - 2024': '7',
#                     '6° período ': '6',
#                     '5°': '5',
#                     '5º': '5',
#                     'Terceiro ': '3',
#                     '3o semestre': '3',
#                     '3 período ': '3',
#                     '3°': 3
#                     }
#     df['Grad_Period'].replace(period_rename,inplace=True)
#     #Atribuindo coluna Grad_Period como int
#     df['Grad_Period'] = df['Grad_Period'].astype(int)

#     ocupation_rename = {'Estudante ': 'Estudante',
#                     'estudante ': 'Estudante',
#                     'estudante': 'Estudante',
#                     'Estudante de Medicina ': 'Estudante',
#                     'Estudante, auxiliar administrativa e monitora em festas infantis': 'Estudante e Trabalho',
#                     'Geólogo': 'Estudante e Trabalho',
#                     'Nenhuma': 'Estudante e Trabalho',
#                     'Estudante / servidora pública ': 'Estudante e Trabalho',
#                     'Estudante universitário ': 'Estudante e Trabalho',
#                     'Professor': 'Estudante e Trabalho',
#                     'Professora de biologia a noite ': 'Estudante e Trabalho'
#                     }
#     df['Ocupation'].replace(ocupation_rename,inplace=True)

#     #Atribuindo valores do DASS 21 para as respostas
#     dass_rename = {'Nunca': 0,
#                 '0': 0,
#                 'Algumas vezes': 1,
#                 '1': 1,
#                 'Frequentemente': 2, 
#                 '2': 2,
#                 'Quase sempre': 3,
#                 '3': 3
#                 }
#     #'S1','A2', 'D3', 'A4', 'D5', 'S6', 'A7', 'S8', 'A9', 'D10', 'S11', 'S12', 'D13'
#     #'S14', 'A1', 'D16', 'D17', 'S18', 'A19', 'A20', 'D21'
#     df['S1'].replace(dass_rename,inplace=True)
#     df['A2'].replace(dass_rename,inplace=True)
#     df['D3'].replace(dass_rename,inplace=True)
#     df['A4'].replace(dass_rename,inplace=True)
#     df['D5'].replace(dass_rename,inplace=True)
#     df['S6'].replace(dass_rename,inplace=True)
#     df['A7'].replace(dass_rename,inplace=True)
#     df['S8'].replace(dass_rename,inplace=True)
#     df['A9'].replace(dass_rename,inplace=True)
#     df['D10'].replace(dass_rename,inplace=True)
#     df['S11'].replace(dass_rename,inplace=True)
#     df['S12'].replace(dass_rename,inplace=True)
#     df['D13'].replace(dass_rename,inplace=True)
#     df['S14'].replace(dass_rename,inplace=True)
#     df['A15'].replace(dass_rename,inplace=True)
#     df['D16'].replace(dass_rename,inplace=True)
#     df['D17'].replace(dass_rename,inplace=True)
#     df['S18'].replace(dass_rename,inplace=True)
#     df['A19'].replace(dass_rename,inplace=True)
#     df['A20'].replace(dass_rename,inplace=True)
#     df['D21'].replace(dass_rename,inplace=True)

#     course_rename = {'Medicina ': 'Medicina'
#                     }
#     df['Course'].replace(course_rename,inplace=True)
#     df = df.drop(df[df.Course != 'Medicina'].index)

#     return df

formatting_data()