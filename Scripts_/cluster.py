from sklearn.cluster import MiniBatchKMeans
from sklearn.decomposition import PCA
import numpy as np
import os

# Define paths
base_dir = os.path.dirname(os.path.dirname(__file__))
processed_dir = os.path.join(base_dir, "ProcessedImages")

# Load features
men_features = np.load(os.path.join(processed_dir, "men_features.npy"))
women_features = np.load(os.path.join(processed_dir, "women_features.npy"))

# Flatten and concatenate
men_flat = men_features.reshape(men_features.shape[0], -1)
women_flat = women_features.reshape(women_features.shape[0], -1)
all_features = np.concatenate([men_flat, women_flat], axis=0)

# PCA reduction
pca = PCA(n_components=500)
all_features_reduced = pca.fit_transform(all_features)

# Save PCA-reduced features  <-- NEW
np.save(os.path.join(processed_dir, "all_features_reduced.npy"), all_features_reduced)

# Clustering
kmeans = MiniBatchKMeans(n_clusters=100, batch_size=512, max_iter=200, random_state=42, verbose=1)
kmeans.fit(all_features_reduced)

# Save cluster labels
np.save(os.path.join(processed_dir, "cluster_labels.npy"), kmeans.labels_)