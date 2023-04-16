import pandas as pd

def rawData(gender, marital, university, ocupation, children, class_dep, class_anx, class_str, age, grad_period, num_cols):

    cat_cols = pd.DataFrame({'Gender': [gender], 'Marital_Status': [marital], 'University': [university], 'Ocupation': [ocupation], 'Children': [children], 'Classify_Dep': [class_dep], 'Classify_Anx': [class_anx], 'Classify_Str': [class_str]})

    num_cols = pd.DataFrame({'Age': [age], 'Grad_Period': [grad_period]})

    rawdata = cat_cols.join(num_cols, how = 'left')
    rawdata['Age'] =  rawdata['Age'].fillna(0)
    rawdata['Grad_Period'] =  rawdata['Grad_Period'].fillna(0)

    return rawdata

def numCols(age, grad_period):
    num_cols = pd.DataFrame({'Age': [age], 'Grad_Period': [grad_period]})
    return num_cols

def catCols(gender, marital, university, ocupation, children, class_dep, class_anx, class_str):
    cat_cols = pd.DataFrame({'Gender': [gender], 'Marital_Status': [marital], 'University': [university], 'Ocupation': [ocupation], 'Children': [children], 'Classify_Dep': [class_dep], 'Classify_Anx': [class_anx], 'Classify_Str': [class_str]})

    return cat_cols