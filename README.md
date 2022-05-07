# Data_Bootcamp_Final_Project

## Overview
In today's market, housing prices are constantly changing. Whether you're a buyer or a seller, you're looking to get the best value out of your home. This analysis focuses on the Portland housing market by estimating home prices using housing characteristics and location demographics for the area.

## Project Outline
## Roles 
* Square - Kim
* Triangle - Sebastian, Kim
* Circle - Christopher

## Goal
Build a model that estimates home prices in Portland based on housing characteristics (bed, bath, square feet, year built, etc) and location demographics (zip codes, crime data, average income, population density, etc). In addition to the predictive model, we will also study market trends and draw informative conclusions that will strengthen our home price estimates.

## Process
The proposed process includes the following steps and tools:

### 1. Data Collection
We have gathered housing and location data from several sources including Kaggle, Portland Maps, Portland Police, Bureau of Labor Statistics, Portland on the market, Census.gov, etc.

### 2. Data Cleaning
The data cleaning process includes using Jupyter Notebook and PostgreSQL to perform an ETL process. There are three main data sources we are measuring:

1. **portland_housing.csv** contains most of the housing data. The raw data was downloaded from [Kaggle](https://www.kaggle.com/datasets/threnjen/portland-housing-prices-sales-jul-2020-jul-2021?select=portland_housing.csv) and was cleaned and transformed using Jupyter Notebook (see Portland_House_Sales.ipynb). 

2. **Crimes_by_zip.csv** contains crime data by zip code (a location/demographic characteristic). The raw data comes in three files (crime data by neighborhood and year from the Portland Police in two files (CrimeData-2021.csv and CrimeData-2022.csv) and a file that maps neighborhoods to zip codes from a web source: Zip_Neighborhood.xlsx). The data was loaded, cleaned, and transformed using Jupyter Notebook (see Crime_2021_22_by Zip_clean_transform.ipynb). 

3. Census.gov population by Block Group and Mean Income by ZCTA.
    * Calculate percent overlap of BG with Zip Code polygons using:
    https://gis.stackexchange.com/questions/339929/calculating-percentage-of-overlap-of-two-layers-in-qgis-3
    * Zip Code polygons data source: public dataset maintained by Esri
    * Use percent overlap to calculate population in each zip code (valid based on assumption that population is evenly dispeared in zip code)
    * ZCTA related to zip code based on Largest Overlap. Zip codes assigned mean HHI from ZCTA with most overlap.

4) Join all zip code data into one csv
5) Join house data with zip code data for model input

### 3) Database Creation  
Data will be stored on github to avoid AWS RDS charge. CSVs will be moved to AWS RDS toward the middle of the month to meet final grade requirements using this process from Shan: https://github.com/FrankJiang1208/RDS-Tutorial

### 4) Machine Learning Model & Flask
Create a multivariable regression model testing all the home characteristics and location/demographic characteristics mentioned above , evaluate and make adjustments to land in the best predictive model. Then create a flask app to interact with model. 

The machine learning or multivariable linear regression process will include the following steps:

#### -Define variables:
Y or dependant variable will be the estimated home price which the X or dependant variables will be testing include: home characteristic variables like home type, year built, # bed, # bath, sqft , lot size , and location/demographic variables like zip code, crime rate, income, population density.

#### -Scale and Normalize values if needed & Handle any categorical variables if needed.

#### -Split X and Y into training and testing sets.

#### -Create an instance of the linear regression model.

#### -Train model or fit with Dataset.
Evaluate each variable cofficient and decide is there are some variables that have low influence and worth dropping and restarting the process. 

#### -Create predictions and evaluate R2.

Note or Open questions: Do we need to do the home characteristic model at the zip code level? assume datasets will be too small to analyize by zip so no.

### 5) Market Trend Analysis & Mapping
Perform analysis on market trends and present in tableau or google sheets. Also provide some summaries in heatmap form. 

## Resources
- Datasets: [Kaggle](https://www.kaggle.com/datasets/threnjen/portland-housing-prices-sales-jul-2020-jul-2021?select=portland_housing.csv), [Portland Police](https://www.portlandoregon.gov/police/71978), [Portland on the market](https://www.portlandonthemarket.com/), [Census](https://www.census.gov/), [ArcGis](https://www.arcgis.com/home/item.html?id=8d2012a2016e484dafaac0451f9aea24)
- Language(s): Python, SQL, JSON
- Tools: Jupyter Notebook, Flask, pgAdmin, PostgreSQL, Excel
- Libraries: Pandas, Scikit-learn
