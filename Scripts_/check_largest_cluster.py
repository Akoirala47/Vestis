import numpy as np
import matplotlib.pyplot as plt
import os

# Paths
base_dir = os.path.dirname(os.path.dirname(__file__))
processed_dir = os.path.join(base_dir, "ProcessedImages")

# Load cluster labels
labels = np.load(os.path.join(processed_dir, "cluster_labels_v1.npy"))

# Find largest cluster
cluster_ids, counts = np.unique(labels, return_counts=True)
largest_cluster = cluster_ids[np.argmax(counts)]
print(f"Largest cluster: {largest_cluster} ({np.max(counts)} outfits)")

# Get sample indices
sample_indices = np.random.choice(
    np.where(labels == largest_cluster)[0], 
    size=5, 
    replace=False
)

# Get all image paths in order (men first, then women)
men_dir = os.path.join(processed_dir, "men_fashion")
women_dir = os.path.join(processed_dir, "women_fashion")

men_images = sorted([os.path.join(men_dir, f) 
                    for f in os.listdir(men_dir) 
                    if f.endswith((".jpg", ".png"))])
women_images = sorted([os.path.join(women_dir, f) 
                      for f in os.listdir(women_dir) 
                      if f.endswith((".jpg", ".png"))])
all_images = men_images + women_images

# Display samples
plt.figure(figsize=(15, 5))
for i, idx in enumerate(sample_indices):
    try:
        img = plt.imread(all_images[idx])
        plt.subplot(1, 5, i+1)
        plt.imshow(img)
        plt.title(f"Index: {idx}")
        plt.axis('off')
    except Exception as e:
        print(f"Error loading image {idx}: {str(e)}")

plt.suptitle(f"Samples from Largest Cluster ({largest_cluster})", fontsize=16)
plt.show()