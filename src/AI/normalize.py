import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from pickle import dump

def normalize(num_cols, num_normalize, cat_normalize):

    num_normalize = pd.DataFrame(num_normalize, columns=num_cols.columns)
    num_normalize.to_pickle('num_normalize.pkl')
    normalize_data = cat_normalize.join(num_normalize, how = 'left')
    normalize_data['Age'] =  normalize_data['Age'].fillna(0)
    normalize_data['Grad_Period'] =  normalize_data['Grad_Period'].fillna(0)
    normalize_data['S1'] =  normalize_data['S1'].fillna(0)
    normalize_data['A2'] =  normalize_data['A2'].fillna(0)
    normalize_data['D3'] =  normalize_data['D3'].fillna(0)
    normalize_data['A4'] =  normalize_data['A4'].fillna(0)
    normalize_data['D5'] =  normalize_data['D5'].fillna(0)
    normalize_data['S6'] =  normalize_data['S6'].fillna(0)
    normalize_data['A7'] =  normalize_data['A7'].fillna(0)
    normalize_data['S8'] =  normalize_data['S8'].fillna(0)
    normalize_data['A9'] =  normalize_data['A9'].fillna(0)
    normalize_data['D10'] =  normalize_data['D10'].fillna(0)
    normalize_data['S11'] =  normalize_data['S11'].fillna(0)
    normalize_data['S12'] =  normalize_data['S12'].fillna(0)
    normalize_data['D13'] =  normalize_data['D13'].fillna(0)
    normalize_data['S14'] =  normalize_data['S14'].fillna(0)
    normalize_data['A15'] =  normalize_data['A15'].fillna(0)
    normalize_data['D16'] =  normalize_data['D16'].fillna(0)
    normalize_data['D17'] =  normalize_data['D17'].fillna(0)
    normalize_data['S18'] =  normalize_data['S18'].fillna(0)
    normalize_data['A19'] =  normalize_data['A19'].fillna(0)
    normalize_data['A20'] =  normalize_data['A20'].fillna(0)
    normalize_data['D21'] =  normalize_data['D21'].fillna(0)
    return normalize_data


def numNormalize(num_cols):
    scaler = MinMaxScaler()
    numerico = scaler.fit(num_cols)
    num_normalize = scaler.fit_transform(num_cols)
    dump(numerico,open('num_normalizer.model', 'wb'))
    return num_normalize

def catNormalize(cat_cols):
    cat_normalize = pd.get_dummies(cat_cols, prefix_sep = '&')
    f = open('cat_normal_definition.model', 'w')
    f.write(','.join(str(s) for s in cat_normalize.columns.values.tolist()))
    f.close()
    return cat_normalize