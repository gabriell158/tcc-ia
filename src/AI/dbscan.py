from sklearn.cluster import DBSCAN, KMeans
import numpy as np
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
#If the data has more than two dimensions, the min sample per cluster should be: 
#Min_sample(MinPoints) = 2 * Data dimension
def dbscan(data_normalized):
    clustering = DBSCAN(eps=2, min_samples=56)
    labels = clustering.fit_predict(data_normalized)
    print(clustering.labels_)
    unique_labels = np.unique(labels)
    num_clusters = len(unique_labels) - 1  # Exclude noise points (label -1)
    print('num_clusters', num_clusters)
    kmeans_clusters = []
    clusters = {}
    for label in unique_labels:
        if label == -1:  # Noise points
            continue
        clusters[label] = data_normalized[labels == label]

    for label, cluster in clusters.items():
        print("Cluster", label)
        print(cluster)
    
    # distances = NearestNeighbors(n_neighbors=2).fit(data_normalized).kneighbors()[0][:, 1]
    # sorted_distances = np.sort(distances)
    # plt.plot(sorted_distances)
    # plt.xlabel('Data Points')
    # plt.ylabel('Distance to kth nearest neighbor')
    # plt.title('Knee point to determine min_samples')
    # plt.savefig('teste.png')
    # neighb = NearestNeighbors(n_neighbors=2)
    # nbrs=neighb.fit(data_normalized)
    # distances,indices=nbrs.kneighbors(data_normalized)
    # distances = np.sort(distances, axis = 0) # sorting the distances
    # distances = distances[:, 1] # taking the second column of the sorted distances
    # plt.rcParams['figure.figsize'] = (5,3) # setting the figure size
    # plt.plot(distances) # plotting the distances
    # 
    # plt.show()