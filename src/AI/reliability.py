from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import cross_validate
import pandas as pd

def reliability():
    data = pd.read_csv('clusters_description.csv')

    # Removendo Colunas Desnecessárias
    drop_scores = ['Depression_Score','Anxiety_Score','Stress_Score']
    data = data.drop(columns=drop_scores)

    # Colunas Categoricas
    classes_columns = ['Classify_Dep', 'Classify_Anx', 'Classify_Str']
    categorical_columns = ['Gender', 'Marital_Status','University','Ocupation']
    classes = data[classes_columns]

    # Normalizando Colunas Categóricas para utilizar o tree.fit()
    normalized_cat = pd.get_dummies(data[categorical_columns], prefix_sep = '&')
    normalized_classes = pd.get_dummies(classes, prefix_sep = '&')

    # Normalizando Colunas Numéricas para utilizar o tree.fit()
    scaler = MinMaxScaler()
    numeric_drop = classes_columns + categorical_columns
    numeric_columns = data.drop(columns=numeric_drop)
    normalized_attr = scaler.fit_transform(numeric_columns)

    # Recompondo Colunas Numéricas normalizadas para DataFrame
    normalized_attr_df = pd.DataFrame(normalized_attr, index=numeric_columns.index, columns=numeric_columns.columns)

    # Juntando Colunas Categóricas e Numéricas normalizadas
    attributes = normalized_cat.join(normalized_attr_df, how='left')

    # Treinar Modelo
    tree = DecisionTreeClassifier()
    kmeans_tree_cross = tree.fit(attributes, normalized_classes)

    # Scoring
    scoring = ['precision_macro','recall_macro']
    scores_cross = cross_validate(kmeans_tree_cross, normalized_attr_df, normalized_classes, cv=3, scoring = scoring)

    return 'Especificidade: ' + str(scores_cross['test_precision_macro'].mean()) + '\n' + 'Sensibilidade : ' + str(scores_cross['test_recall_macro'].mean())