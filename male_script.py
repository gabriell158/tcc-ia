import pandas as pd
import random
import numpy as np
from src.AI.normalize import *
from src.AI.train import *
from src.AI.new_student import *
from src.AI.dass_sum import *

# sintetic_dataset_size = 500

df = pd.read_csv('formated_data.csv')
df2 = pd.read_csv('form2.csv')
# sintetic_df = pd.read_csv('1000_Sintetic.csv')
df2 = df2.drop(columns=['Income','Financial_Support','Emotional_Support','Race','Scholarship','Lose_Scholarship','Transport'])  
dfs = [df, df2]
df = df._append(df2)
df = df.drop(columns=['Unnamed: 0', 'Stamp', 'Email', 'Terms', 'Dob', 'University', 'Course'])
# df = df._append(sintetic_df)

# df.loc[pd.isna(df["Gender"]), "Gender"] = 'Masculino'
# df.loc[pd.isna(df["Marital_Status"]), "Marital_Status"] = 'Solteira(o)'
# df.loc[pd.isna(df["Ocupation"]), "Ocupation"] = 'Estudante'
# # df.to_csv('Combined_Sintetic_Male_282_Df.csv')
# # combined_df = pd.read_csv('Combined_Sintetic_Male_282_Df.csv')
# df.loc[df["Grad_Period"] > 12, "Grad_Period"] = 12
# df.loc[df["Grad_Period"] < 0, "Grad_Period"] = 1

# print(df)
# df.to_csv('1000_Sintetic.csv', index=False)

# replace_df = pd.read_csv('1000_Sintetic_To_Train.csv')
# replace_df.loc[replace_df["Grad_Period"] < 0, "Grad_Period"] = 1
# def replace_nan(value):
#     if value < 0:
#         return 0
#     else:
#         return value
    
# replace_df.to_csv('1000_Sintetic_To_Train.csv', index=False)

# replace_df = replace_df.applymap(replace_nan)
#print(combined_df)

# sintetic_df = pd.read_csv('1000_Sintetic_To_Train.csv')
train(df)
student_tracking = cluster_inference(
            'Masculino','Solteira(o)','Estudante e Trabalho',0,28,2,2,1,2,1,1,2,1,2,2,2,2,2,1,1,2,2,1,2,2,1,1
        )
print(student_tracking)


#
