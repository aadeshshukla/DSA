# clustering_example.py
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 1️⃣ Create sample data (you can replace this with your own array)
X, _ = make_blobs(
    n_samples=300,      # number of points
    centers=4,          # true cluster count
    cluster_std=0.8,    # spread of each blob
    random_state=42,
)

# 2️⃣ Fit K‑Means
k = 4                         # number of clusters you want
kmeans = KMeans(n_clusters=k, random_state=0)
kmeans.fit(X)

# 3️⃣ Results
labels = kmeans.labels_        # cluster assignment for each point
centers = kmeans.cluster_centers_

# 4️⃣ Plot (optional, but handy for verification)
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=30, alpha=0.6)
plt.scatter(centers[:, 0], centers[:, 1],
            c='red', marker='X', s=200, label='centroids')
plt.title('K‑Means clustering')
plt.legend()
plt.show()
