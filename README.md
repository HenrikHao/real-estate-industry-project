[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/SGWUF1eE)
# Generic Real Estate Consulting Project

## Research Goal

## Timeline

## Pipeline

To run the pipeline, please follow the instructions below:

Please run ```cd scripts``` first
1. `scripts/__init__.py`: This script downloads SA2 shape files, 2016 census data and 2021 census data from ABS and extract them into `data/statistical_area_level2`, `data/landing/census2016` and `data/landing/census2021`.
2. `scripts/scrape.py`: This script scrapes property data from `www.domain.com.au` and store them into `data/landing/property.json`

Notebooks:
1. `notebooks/preprocessing_properties.ipynb`: Run this for properties data preprocessing
2. `notebooks/preprocessing_census.ipynb`: This is for census data preprocessing
3. `notebooks/proprocessing_properties.ipynb`: This is for properties data preprocessing
