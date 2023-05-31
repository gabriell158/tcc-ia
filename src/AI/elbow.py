from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import numpy as np
import math

def elbow_method(data_normalized, raw_data):
    distortions = []
    K = range(1, 30)
    kmeans_models = {}
    shape = raw_data.shape[0]
    data_normalized = data_normalized.astype(float)
    for k in K:
        kmeans_models[k] = KMeans(n_clusters=k, random_state=42).fit(data_normalized)
        clusters_centers = kmeans_models[k].cluster_centers_
        clusters_centers.astype(float)
        dist = cdist(data_normalized,clusters_centers,'euclidean')
        distortions.append(sum(np.min(dist, axis =1)/shape))

    x0 = K[0]
    y0 = distortions[0]

    x1 = K[len(K)-1]
    y1 = distortions[len(distortions)-1]

    distances = []
    for i in range(len(distortions)):
        x = K[i]
        y = distortions[i]
        numerator = abs((y1-y0)*x - (x1-x0)*y + x1*y0 - y1*x0)
        denominator = math.sqrt((y1-y0)**2 + (x1-x0)**2)
        distances.append(numerator/denominator)

    optimal_cluster_number =K[distances.index(np.max(distances))]
    return kmeans_models[optimal_cluster_number]
