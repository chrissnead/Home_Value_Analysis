# Home Value Analysis 

## Overview
In today's market, housing prices are constantly changing. Whether you're a buyer or a seller, you're looking to get the best value out of your home. This analysis focuses on the Portland housing market by estimating home prices using housing characteristics and location demographics for the area.

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

4. Cleaned and transformed data to load into database. For housing data we used "Sales_Cleaning.ipynb" and for demographic data we used "Income_Cleaning.ipynb". We discarted the crime data as the extent of zip codes in the data was much smaller than the housing and demographic info and was too labor exetensive to gather from multiple police departments. 

5. Join house data with zip code data for model input ("final_housing.csv" under resources)

### 3. Database Creation  (Chris to update?)
Data will be stored on github to avoid AWS RDS charge. CSVs will be moved to AWS RDS toward the middle of the month to meet final grade requirements using this process from Shan: https://github.com/FrankJiang1208/RDS-Tutorial.

[Link to ERD](https://github.com/klcollins503/Data_Bootcamp_Final_Project/blob/main/Resources/EntityRelationshipDiagram.png)

### 4. Machine Learning Model & Flask
Create a multivariable regression model testing all the home characteristics and location/demographic characteristics mentioned above , evaluate and make adjustments to land in the best predictive model. Then create a flask app to interact with model. 

Given that we have identified multiple independant variables that can help predict the sale price we beleive the best approach is a multivariable regression model. We followed the process below using a linear multivariable regression and as we cleaned data and selected the right variables we kept increasing the R squared until getting slightly over 0.7, which we beleive is a pretty good prediction model given the time and data constraints.

The machine learning or multivariable linear regression process will include the following steps (for reference see "Multiple_Linear_Regression.ipynb"):

#### -Define variables:
Y or dependant variable will be the estimated home price which the X or dependant variables will be testing include: home characteristic variables like home type, year built, # bed, # bath, sqft , lot size , and location/demographic variables like zip code, crime rate, income, population density.

![image](https://user-images.githubusercontent.com/96096924/169173489-b3597989-7316-4a92-acf8-c1a5e4f99cec.png)

#### -Split X and Y into training and testing sets.

![image](https://user-images.githubusercontent.com/96096924/169173545-bd5bf9c8-7a58-4291-85b8-b615a3b3b9d9.png)

#### -Create an instance of the linear regression model.

![image](https://user-images.githubusercontent.com/96096924/169173652-8cf3181e-4b5c-493c-ae50-090057b58181.png)

#### -Train model or fit with Dataset.

![image](https://user-images.githubusercontent.com/96096924/169173717-18ab393b-cbd3-49db-bf1b-d0d402b6d999.png)

#### -Create predictions and evaluate R2.
Evaluate each variable cofficient and R squared to decide is there are some variables that have low influence and worth dropping and restarting the process. In this process we decided for to use the following variables that provided the highest R squared (slightly over 0.7): 'Square Feet', 'Zip Mean HHI', 'Zip Pop Density','Lot Size','Year Built'

#### ''''''Question= do we need to add the create prediction: y_pred = model.predict(X) and print(y_pred.shape)????????

![image](https://user-images.githubusercontent.com/96096924/169173768-2c9589f4-f579-463e-a24d-f94cd958a1d0.png)

### 5. Predictive Model Presentation , Market Trend Analysis & Mapping

#### -Home Price Predictive Model (Flask App) (Kim to update?)

#### -Portland Market Analysis 

We have created interactive maps and graphs in tableau: [Link to Tableau](https://public.tableau.com/views/FinalProject_16528921784890/Map1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)

We also have created a summary presentation that includes the maps and graphs in google slides: [Link to Google](https://docs.google.com/presentation/d/e/2PACX-1vROMHIh3D-UCJORpKo2s_XneHiCjf_OwLdKasuqfTai19b0_DwvtW7NHxBnI65dGvVG4HDaQPs5sPa-/pub?start=true&loop=true&delayms=3000&slide=id.g12c77fac72e_0_1)

## Resources
- Datasets: [Kaggle](https://www.kaggle.com/datasets/threnjen/portland-housing-prices-sales-jul-2020-jul-2021?select=portland_housing.csv), [Portland Police](https://www.portlandoregon.gov/police/71978), [Portland on the market](https://www.portlandonthemarket.com/), [Census Population Density](https://data.census.gov/cedsci/table?q=B01003&g=0400000US41%241500000&tid=ACSDT5Y2020.B01003), [Census Income](https://data.census.gov/cedsci/table?q=income&g=0400000US41%241500000&tid=ACSDT5Y2020.B19001), [ArcGis](https://www.arcgis.com/home/item.html?id=8d2012a2016e484dafaac0451f9aea24)
- Language(s): Python, SQL, JSON
- Tools: Jupyter Notebook, Flask, pgAdmin, PostgreSQL, Excel, Tableau, Google Slides
- Libraries: Pandas, Scikit-learn
