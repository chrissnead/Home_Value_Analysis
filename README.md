# Data_Bootcamp_Final_Project

## Project Outline
## Roles 
* Square - Kim
* Triangle - Sebastian, Kim
* Circle - Christopher


## Goal
Build a model that estimates home prices in Portland based on home characteristics (bed/bath, sqft, year built, etc) and location/demographic characteristics (zip code, crime, income, population density, etc). In addition to the predictive model, we will also study market trends and draw some informative conclusions to help understand the market. 

## Process
The proposed process includes the following steps and tools:

### 1) Data Collection
We have gathered housing data from Kaggle and other location characteristics from the following: Portland Maps, Portland Police, Bureau of Labor Statistics, Portland on the market, Census.gov, etc.

### 2) Data Cleaning
Data cleaning process includes Excel, Jupyter Notebook processes included in the github repository. There are three main data sources we are measuring:

1) **portland_housing.csv** which contains most of the housing characteristics and price data. The raw data was downloaded from [Kaggle](https://www.kaggle.com/datasets/threnjen/portland-housing-prices-sales-jul-2020-jul-2021?select=portland_housing.csv) and was cleaned and transformed using Jupyter Notebook (see Portland_House_Sales.ipynb). 

2) **Crimes_by_zip.csv** which contains crime data by zip code (a location/demographic characteristic). The raw data comes in three files (crime data by neighborhood and year from the Portland Police in two files (CrimeData-2021.csv and CrimeData-2022.csv) and a file that maps neighborhoods to zip codes from a web source: Zip_Neighborhood.xlsx). This raw data was merged,  cleaned and transformes using Jupyter Notebook (see Crime_2021_22_by Zip_clean_transform.ipynb). 

3) Census.gov population by Block Group and Mean Income by ZCTA.
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
- Datasets: [Kaggle](https://www.kaggle.com/datasets/threnjen/portland-housing-prices-sales-jul-2020-jul-2021?select=portland_housing.csv)
- Language(s): Python, SQL, JSON
- Tools: Jupyter Notebook, Flask, pgAdmin, PostgreSQL, Excel
- Libraries: Pandas, Scikit-learn
