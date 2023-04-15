from sklearn.cluster import KMeans
from normalize import normalize
from raw_data import rawData

from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt
import math


def metodo_cotovelo():
    distorcoes = []
    norm_data = normalize()
    raw_data = rawData()
    K = range(1,39)
    for k in K:
        kmeans_model = KMeans(n_clusters=k, random_state=42).fit(norm_data)
        distorcoes.append(
            sum(np.min(cdist(
            norm_data,kmeans_model.cluster_centers_,'euclidean'), axis =1)/raw_data.shape[0])
  )

    fig, ax = plt.subplots()
    ax.plot(K, distorcoes)
    ax.set(xlabel = 'n Clusters', ylabel = 'Distorcao', title = 'Elbow Method')
    fig.savefig('alunos_distorcao_.png')
    plt.show()

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
    return n_clusters_otimo