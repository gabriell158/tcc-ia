import pandas as pd

def rawData(cat_cols, num_cols):
    rawdata = cat_cols.join(num_cols, how = 'left')
    rawdata['Age'] =  rawdata['Age'].fillna(0)
    rawdata['Grad_Period'] =  rawdata['Grad_Period'].fillna(0)
    rawdata['S1'] =  rawdata['S1'].fillna(0)
    rawdata['A2'] =  rawdata['A2'].fillna(0)
    rawdata['D3'] =  rawdata['D3'].fillna(0)
    rawdata['A4'] =  rawdata['A4'].fillna(0)
    rawdata['D5'] =  rawdata['D5'].fillna(0)
    rawdata['S6'] =  rawdata['S6'].fillna(0)
    rawdata['A7'] =  rawdata['A7'].fillna(0)
    rawdata['S8'] =  rawdata['S8'].fillna(0)
    rawdata['A9'] =  rawdata['A9'].fillna(0)
    rawdata['D10'] =  rawdata['D10'].fillna(0)
    rawdata['S11'] =  rawdata['S11'].fillna(0)
    rawdata['S12'] =  rawdata['S12'].fillna(0)
    rawdata['D13'] =  rawdata['D13'].fillna(0)
    rawdata['S14'] =  rawdata['S14'].fillna(0)
    rawdata['A15'] =  rawdata['A15'].fillna(0)
    rawdata['D16'] =  rawdata['D16'].fillna(0)
    rawdata['D17'] =  rawdata['D17'].fillna(0)
    rawdata['S18'] =  rawdata['S18'].fillna(0)
    rawdata['A19'] =  rawdata['A19'].fillna(0)
    rawdata['A20'] =  rawdata['A20'].fillna(0)
    rawdata['D21'] =  rawdata['D21'].fillna(0)
    return rawdata

def get_numeric_data(age, grad_period, s1, a2, d3, a4, d5, s6, a7, s8, a9, d10, s11, s12, d13, s14, a15, d16, d17, s18, a19, a20, d21):
    return pd.DataFrame({'Age': age, 'Grad_Period': grad_period, 'S1': s1, 'A2': a2, 'D3': d3, 'A4': a4, 'D5': d5, 'S6': s6, 'A7': a7, 'S8': s8, 'A9': a9, 'D10': d10, 'S11': s11, 'S12': s12, 'D13': d13, 'S14': s14, 'A15': a15, 'D16': d16, 'D17': d17, 'S18': s18, 'A19': a19, 'A20': a20, 'D21': d21})

def get_categorical_data(gender, marital, ocupation, children):
    return pd.DataFrame({'Gender': gender, 'Marital_Status': marital,'Ocupation': ocupation, 'Children': children})

def get_scalar_numeric_data(age, grad_period, s1, a2, d3, a4, d5, s6, a7, s8, a9, d10, s11, s12, d13, s14, a15, d16, d17, s18, a19, a20, d21):
    return pd.DataFrame({'Age': [age], 'Grad_Period': [grad_period], 'S1': [s1], 'A2': [a2], 'D3': [d3], 'A4': [a4], 'D5': [d5], 'S6': [s6], 'A7': [a7], 'S8': [s8], 'A9': [a9], 'D10': [d10], 'S11': [s11], 'S12': [s12], 'D13': [d13], 'S14': [s14], 'A15': [a15], 'D16': [d16], 'D17': [d17], 'S18': [s18], 'A19': [a19], 'A20': [a20], 'D21': [d21]})

def get_scalar_categorical_data(gender, marital, ocupation, children):
    return pd.DataFrame({'Gender': [gender], 'Marital_Status': [marital], 'Ocupation': [ocupation], 'Children': [children]})
