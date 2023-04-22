from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt
import math

def elbow_method(norm_data, raw_data):
    distorcoes = []
    K = range(1,39)
    kmeans_models = {}
    shape = raw_data.shape[0]
    norm_data = norm_data.astype(float)
    for k in K:
        kmeans_models[k] = KMeans(n_clusters=k, random_state=42).fit(norm_data)
        centroids = kmeans_models[k].cluster_centers_
        centroids.astype(float)
        dist = cdist(norm_data,centroids,'euclidean')
        distorcoes.append(sum(np.min(dist, axis =1)/shape))
    #Calcular o número ideal de clusters
    x0 = K[0]
    y0 = distorcoes[0]

    x1 = K[len(K)-1]
    y1 = distorcoes[len(distorcoes)-1]

    distancias = []
    for i in range(len(distorcoes)):
        x = K[i]
        y = distorcoes[i]
        numerador = abs((y1-y0)*x - (x1-x0)*y + x1*y0 - y1*x0)
        denominador = math.sqrt((y1-y0)**2 + (x1-x0)**2)
        distancias.append(numerador/denominador)

    #maior distância
    n_clusters_otimo =K[distancias.index(np.max(distancias))]
    return kmeans_models[n_clusters_otimo]