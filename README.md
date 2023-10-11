[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/SGWUF1eE)
# Generic Real Estate Consulting Project

## Research Goal

## Timeline

## Pipeline

To run the pipeline, please follow the instructions below:

Please run ```cd scripts``` first
1. run ```python __init__.py``` from terminal: This script downloads SA2 shape files, LGA shape files, 2016 census data and 2021 census data from ABS and extract them into `data/shapefile`, `data/landing/census2016` and `data/landing/census2021`.
2. run ```python scrape.py```: This script scrapes property data from `www.domain.com.au` and store them into `data/landing/property.json`

Notebooks:
0. `notebooks/mapping.ipynb`: Map the SA2 to LGA.
1. `notebooks/preprocessing_properties.ipynb`: Run this for properties data preprocessing
2. `notebooks/find_proximity.ipynb`: This notebook will aggregate properties data with other proximities.
3. `notebooks/feature_selection.ipynb`: This notebook will list out the most correlated feature to the rent.
4. `notebooks/properties_aggregation.ipynb`: This notebook will aggregate the data based on LGA levels and then merge population, affluence and offence count to the properties data.
5. `notebooks/modelling.ipynb`: This note book will predict the future three years rent.
5. `notebooks/scoring.ipynb`: As what it is.

