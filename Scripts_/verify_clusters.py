# verify_clusters.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import os

# Define paths
base_dir = os.path.dirname(os.path.dirname(__file__))  # Project root directory
processed_dir = os.path.join(base_dir, "ProcessedImages")

# Load data from ProcessedImages directory
features = np.load(os.path.join(processed_dir, "all_features_reduced.npy"))
labels = np.load(os.path.join(processed_dir, "cluster_labels_v1.npy"))

# 1. Check cluster distribution
unique_clusters, counts = np.unique(labels, return_counts=True)
print("\n=== Cluster Distribution ===")
print(f"Total clusters: {len(unique_clusters)}")
print(f"Cluster size statistics:")
print(f"- Average: {np.mean(counts):.1f} outfits per cluster")
print(f"- Largest: {np.max(counts)} outfits")
print(f"- Smallest: {np.min(counts)} outfits")
print(f"- Median: {np.median(counts)} outfits")

# 2. Visualize with t-SNE
print("\n=== Running t-SNE Visualization ===")
print("This may take 2-5 minutes for 11k points...")

tsne = TSNE(n_components=2, random_state=42, perplexity=30)
features_2d = tsne.fit_transform(features)

plt.figure(figsize=(14, 10))
scatter = plt.scatter(features_2d[:, 0], features_2d[:, 1], 
                      c=labels, cmap="tab20", s=15, alpha=0.6)
plt.title("Outfit Clusters Visualization (t-SNE Projection)")
plt.xlabel("t-SNE Dimension 1")
plt.ylabel("t-SNE Dimension 2")
plt.colorbar(scatter, label="Cluster ID")
plt.show()