# GLD-Road: A Global-Local Decoding Road Network Extraction Model for Remote Sensing Images

This repository contains the experimental results and visualization tools for our paper **"GLD-Road: A Global-Local Decoding Road Network Extraction Model for Remote Sensing Images"**. We provide results on the CityScale and SpaceNet3 datasets, along with scripts for reproducing the visualizations.

## Datasets

### CityScale Dataset

The CityScale dataset is a high-resolution remote sensing image dataset designed for road network extraction tasks. It features diverse urban environments with varying road structures and complexities.

- **Download Link**: [CityScale Dataset](https://drive.google.com/drive/folders/1FlMcO3Jr8W4qboZUwxgRn6AlYc-AuxQ2)

### SpaceNet3 Dataset

The SpaceNet3 dataset is a publicly available dataset that includes high-resolution satellite imagery and corresponding road network labels. It is widely used for training and evaluating road extraction models.

- **Download Link**: [SpaceNet3 Dataset](https://drive.google.com/drive/folders/1uABt127ehNBQyfCnv6OND841ZrUlhmNB)

## Results

### CityScale Results

The results of our model on the CityScale dataset are stored as `.p` files in the following directory:

- **Directory**: `cityscale/results`

These files contain the predicted road networks and associated metadata.

### SpaceNet3 Results

The results of our model on the SpaceNet3 dataset are stored as `.p` files in the following directory:

- **Directory**: `sn3/results`

These files include the model predictions for the SpaceNet3 test images.

## Visualization

We provide a visualization script `vis_p.py` in each dataset folder to help reproduce the visualizations from the paper.

- **CityScale Visualization Script**: `cityscale/vis_P.py`
- **SpaceNet3 Visualization Script**: `sn3/vis_p.py`

### Usage

To visualize the results, navigate to the respective dataset directory and run the visualization script:

```bash
# Visualize CityScale results
cd cityscale
python vis_p.py

# Visualize SpaceNet3 results
cd sn3
python vis_p.py
```

The script will generate visual representations of the extracted road networks.

## Reproducing the Experiments

To reproduce our experimental results, please follow these steps:

1. **Download the Datasets**: Use the provided download links to obtain the CityScale and SpaceNet3 datasets.
2. **Prepare the Environment**: Ensure that all required dependencies are installed.
3. **Visualize the Results**: Use the `vis_p.py` scripts to generate visualizations of the model predictions.

## Contact

For any questions or concerns, please open an issue or contact the authors directly.


Thank you for your interest in our work!