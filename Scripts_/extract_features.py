import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB4
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

# Load pre-trained EfficientNetB4 (without the top classification layer)
base_model = EfficientNetB4(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Define paths
base_dir = os.path.dirname(os.path.dirname(__file__))  # Project root
processed_data_dir = os.path.join(base_dir, "ProcessedImages")

def extract_features(gender_folder):
    """Extract features from all images in a gender folder."""
    gender_dir = os.path.join(processed_data_dir, gender_folder)
    image_files = [f for f in os.listdir(gender_dir) if f.endswith(('.jpg', '.png'))]
    features = []
    
    for img_file in image_files:
        img_path = os.path.join(gender_dir, img_file)
        img = load_img(img_path, target_size=(224, 224))
        img_array = img_to_array(img) / 255.0  # Normalize
        img_batch = np.expand_dims(img_array, axis=0)  # Add batch dimension
        feature = base_model.predict(img_batch)
        features.append(feature.squeeze())  # Remove batch dimension
    
    return np.array(features)

# Extract features for men and women
men_features = extract_features("men_fashion")
women_features = extract_features("women_fashion")

# Save features
np.save(os.path.join(processed_data_dir, "men_features.npy"), men_features)
np.save(os.path.join(processed_data_dir, "women_features.npy"), women_features)

print("Feature extraction complete! Files saved to:", processed_data_dir)