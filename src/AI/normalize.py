import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from pickle import dump
from src.AI.raw_data import catCols, numCols

def normalize():
    cat_cols = catCols()
    num_cols = numCols()
    cat_normalize = pd.get_dummies(cat_cols)
    f = open('cat_normal_definition.model', 'w')
    f.write(','.join(str(s) for s in cat_normalize.columns.values.tolist()))
    f.close()
    
    scaler = MinMaxScaler()
    num_normalize = scaler.fit_transform(num_cols)
    dump(num_normalize,open('num_normalizer.model', 'wb'))

    num_normalize = pd.DataFrame(num_normalize, columns=num_cols.columns)
    normalize_data = cat_normalize.join(num_normalize, how = 'left')
    normalize_data['Age'] =  normalize_data['Age'].fillna(0)
    normalize_data['Grad_Period'] =  normalize_data['Grad_Period'].fillna(0)

    return normalize_data


def numNormalize():
    num_cols = numCols()
    scaler = MinMaxScaler()
    num_normalize = scaler.fit_transform(num_cols)
    return num_normalize

def catNormalize():
    cat_cols = catCols()
    cat_normalize = pd.get_dummies(cat_cols)

    return cat_normalize