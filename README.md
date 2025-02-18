# Vestis

This repository contains scripts for processing, clustering, and analyzing fashion images (men and women) using machine learning techniques. The project involves preprocessing images, extracting features using a pre-trained deep learning model, clustering the images, and visualizing the results.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Setup](#setup)
3. [Data Preparation](#data-preparation)
4. [Script Execution Order](#script-execution-order)
5. [Google Drive Data](#google-drive-data)
6. [Contributing](#contributing)
7. [License](#license)

---

## Prerequisites

Before running the scripts, ensure you have the following installed:

- Python 3.x
- Required Python libraries (install via `pip install -r requirements.txt`):
  ```bash
  numpy
  tensorflow
  scikit-learn
  matplotlib
  pillow
  ```
- Git (for version control)
- [Any other tools or dependencies]


## Data Preparation

The data for this project is stored on Google Drive. Follow these steps to download and prepare the data:

1. Download the data from the Google Drive link: [Insert Google Drive Link Here].
2. Place the downloaded data in the `Vestis_Data/` directory (create the directory if it doesn't exist).
3. The data should be organized as follows:
   ```
   Vestis_Data/
   ├── men_fashion/
   │   ├── image1.jpg
   │   ├── image2.jpg
   │   └── ...
   └── women_fashion/
       ├── image1.jpg
       ├── image2.jpg
       └── ...
   ```

---

## Script Execution Order

Run the scripts in the following order:

### 1. **Preprocess Images**
   - Script: `preprocess.py`
   - Description: Resizes all images to a consistent size (224x224) and saves them in the `ProcessedImages/` directory.
   - Command:
     ```bash
     python preprocess.py
     ```

### 2. **Extract Features**
   - Script: `extract.py`
   - Description: Uses a pre-trained EfficientNetB4 model to extract features from the preprocessed images and saves the features as `.npy` files.
   - Command:
     ```bash
     python extract.py
     ```

### 3. **Cluster Images**
   - Script: `cluster.py`
   - Description: Performs PCA dimensionality reduction and clusters the images using MiniBatchKMeans. Saves the cluster labels.
   - Command:
     ```bash
     python cluster.py
     ```

### 4. **Verify Clusters**
   - Script: `verify_clusters.py`
   - Description: Visualizes the clusters using t-SNE and prints cluster distribution statistics.
   - Command:
     ```bash
     python verify_clusters.py
     ```

### 5. **Check Largest Cluster**
   - Script: `check_largest_cluster.py`
   - Description: Identifies the largest cluster and displays sample images from it.
   - Command:
     ```bash
     python check_largest_cluster.py
     ```

### 6. **Cluster Fix Notebook**
   - Notebook: `cluster_check.ipynb`
   - Description: A Jupyter notebook for further analysis, sub-clustering, and validation of clusters. Follow the steps in the notebook to refine the clusters.

### 7. **Initialize Notebook**
   - Script: `initialize_notebook.py`
   - Description: Initializes version control for cluster labels and sets up the environment for the notebook.
   - Command:
     ```bash
     python initialize_notebook.py
     ```

---

## Google Drive Data

The data used in this project is available on Google Drive. You can access it using the following link:  
[Insert Google Drive Link Here] //will add soon

Once downloaded, place the data in the `Vestis_Data/` directory as described in the [Data Preparation](#data-preparation) section.

---

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
