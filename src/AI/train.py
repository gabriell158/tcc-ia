from src.AI.normalize import normalize, catNormalize, numNormalize
from src.AI.elbow import elbow_method
from src.AI.raw_data import rawData, catCols, numCols
from src.AI.denormalize import denormalize

def train(gender, marital, university, ocupation, children, class_dep, class_anx, class_str, age, grad_period, s1, a2, d3, a4, d5, s6, a7, s8, a9, d10, s11, s12, d13, s14, a15, d16, d17, s18, a19, a20, d21):
    cat_cols = catCols(gender, marital, university, ocupation)
    num_cols = numCols(age, grad_period, s1, a2, d3, a4, d5, s6, a7, s8, a9, d10, s11, s12, d13, s14, a15, d16, d17, s18, a19, a20, d21)
    cat_normalized = catNormalize(cat_cols)
    num_normalized = numNormalize(num_cols)
    
    normalized = normalize(cat_cols, num_cols)
    raw_data = rawData(gender, marital, university, ocupation, children, class_dep, class_anx, class_str, age, grad_period, num_cols, s1, a2, d3, a4, d5, s6, a7, s8, a9, d10, s11, s12, d13, s14, a15, d16, d17, s18, a19, a20, d21)
    model = elbow_method(normalized, raw_data)
    cluster_description = denormalize(model, normalized, cat_normalized, cat_cols, num_normalized)

    return cluster_description

