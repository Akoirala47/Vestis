from PIL import Image
import os

def resize_images(input_folder, output_folder, size=(224, 224)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = Image.open(os.path.join(input_folder, filename))
            img = img.resize(size)
            img.save(os.path.join(output_folder, filename))

# Preprocess men's fashion images
resize_images("Vestis_Data/men_fashion", "ProcessedImages/men_fashion")

# Preprocess women's fashion images
resize_images("Vestis_Data/women_fashion", "ProcessedImages/women_fashion")