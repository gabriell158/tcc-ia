import pandas as pd
def rawData(gender, marital, university, ocupation, children, class_dep, class_anx, class_str, age, grad_period, num_cols, s1, a2, d3, a4, d5, s6, a7, s8, a9, d10, s11, s12, d13, s14, a15, d16, d17, s18, a19, a20, d21):

    cat_cols = pd.DataFrame({'Gender': [gender], 'Marital_Status': [marital], 'University': [university], 'Ocupation': [ocupation], 'Children': [children], 'Classify_Dep': [class_dep], 'Classify_Anx': [class_anx], 'Classify_Str': [class_str]})

    num_cols = pd.DataFrame({'Age': [age], 'Grad_Period': [grad_period]})

    rawdata = cat_cols.join(num_cols, how = 'left')
    rawdata['Age'] =  rawdata['Age'].fillna(0)
    rawdata['Grad_Period'] =  rawdata['Grad_Period'].fillna(0)

    return rawdata

def numCols(age, grad_period, s1, a2, d3, a4, d5, s6, a7, s8, a9, d10, s11, s12, d13, s14, a15, d16, d17, s18, a19, a20, d21):
    num_cols = pd.DataFrame({'Age': [age], 'Grad_Period': [grad_period],  'S1': [s1], 'A2': [a2], 'D3': [d3], 'A4': [a4], 'D5': [d5], 'S6': [s6], 'A7': [a7], 'S8': [s8], 'A9': [a9], 'D10': [d10], 'S11': [s11], 'S12': [s12], 'D13': [d13], 'S14': [s14], 'A15': [a15], 'D16': [d16], 'D17': [d17], 'S18': [s18], 'A19': [a19], 'A20': [a20], 'D21': [d21]})
    return num_cols

def catCols(gender, marital, university, ocupation):
    cat_cols = pd.DataFrame({'Gender': [gender], 'Marital_Status': [marital], 'University': [university], 'Ocupation': [ocupation], 'Children': [children], 'Classify_Dep': [class_dep], 'Classify_Anx': [class_anx], 'Classify_Str': [class_str]})

    return cat_cols

def dassCols(class_dep, class_anx, class_str):
    dass_cols = pd.DataFrame({'Classify_Dep': [class_dep], 'Classify_Anx': [class_anx], 'Classify_Str': [class_str]})

    return dass_cols