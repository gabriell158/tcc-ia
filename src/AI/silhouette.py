from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np


def silhouette(data_normalized):
    max_clusters = 10
    best_score = -1
    best_num_clusters = 0

    for num_clusters in range(2, max_clusters+1):
        kmeans = KMeans(n_clusters=num_clusters)
        kmeans.fit(data_normalized)
        labels = kmeans.labels_
        score = silhouette_score(data_normalized, labels)
        
        if score > best_score:
            best_score = score
            best_num_clusters = num_clusters

    print(f"O número ideal de clusters é: {best_num_clusters}")