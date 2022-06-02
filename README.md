# Home Value Analysis 

## [Final Team Presentation Link](https://docs.google.com/presentation/d/1AFogpP1hiIdtDXincCRe_QYIVq_nWw8owLANXub_sIY/edit#slide=id.g12ed9266f11_0_3045)

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

2. **(Archived) Crimes_by_zip.csv** contains crime data by zip code (a location/demographic characteristic). The raw data comes in three files (crime data by neighborhood and year from the Portland Police in two files (CrimeData-2021.csv and CrimeData-2022.csv) and a file that maps neighborhoods to zip codes from a web source: Zip_Neighborhood.xlsx). The data was loaded, cleaned, and transformed using Jupyter Notebook (see Crime_2021_22_by Zip_clean_transform.ipynb). 

3. Census.gov population by Block Group and Mean Income by ZCTA.
    * Calculate percent overlap of BG with Zip Code polygons using:
    https://gis.stackexchange.com/questions/339929/calculating-percentage-of-overlap-of-two-layers-in-qgis-3
    * Zip Code polygons data source: public dataset maintained by Esri
    * Use percent overlap to calculate population in each zip code (valid based on assumption that population is evenly dispeared in zip code)
    * ZCTA related to zip code based on Largest Overlap. Zip codes assigned mean HHI from ZCTA with most overlap.

4. Clean and transform data to load into database. For housing data we used [Sales_Cleaning.ipynb](https://github.com/klcollins503/Data_Bootcamp_Final_Project/blob/main/Sales_Cleaning.ipynb) and for demographic data we used [Income_Cleaning.ipynb](https://github.com/klcollins503/Data_Bootcamp_Final_Project/blob/main/Income_Cleaning.ipynb). We discarded the crime data as the extent of zip codes in the data was much smaller than the housing and demographic info and was too labor exetensive to gather from multiple police departments.

### 3. Database Creation  
Data was cleaned in [Sales_Cleaning.ipynb](https://github.com/klcollins503/Data_Bootcamp_Final_Project/blob/main/Sales_Cleaning.ipynb) and [Income_Cleaning.ipynb](https://github.com/klcollins503/Data_Bootcamp_Final_Project/blob/main/Income_Cleaning.ipynb) and loaded into PostgreSQL using a SQLAlchemy connection. These files were combined through a JOIN which was then exported to [final_housing.csv](https://github.com/klcollins503/Data_Bootcamp_Final_Project/blob/main/Resources/final_housing.csv) for use in our Machine Learning model (see [queries.sql](https://github.com/klcollins503/Data_Bootcamp_Final_Project/blob/main/Queries/queries.sql) for queries performed in PostgreSQL).

[Link to ERD](https://github.com/klcollins503/Data_Bootcamp_Final_Project/blob/main/Resources/EntityRelationshipDiagram.png)

### 4. Machine Learning Model
Create a multivariable model testing home, location, and demographic characteristics mentioned above. The variables will be evaluated to determine best fit for the predictive model which will be represented through a Flask app.

Given that we have identified multiple independent variables that can help predict the sale price, a multivariable regression model or a random forest regressor/classifier will most accurately predict values based on the data. We followed the processes below for all 3, In the linear regression model we cleaned data and selected the right variables through iterations until we got the best R squared value output (slightly over 71%), indicating a fairly accurate prediction given our constraints. For the random forest regressor we took again all variables, then run a variable evaluation and determined square feet and the income where the 2 most determinat variables, going down to those 2 only we did not loose much accuracy in the model only 0.3%. This model seems to boost accuracy from the linear regression to 86% (and potentially 88% without limiting the depth). Finally we created Sale Price buckets and run a Random Forest Classifier which landed the accuracy at 69%. With all models it takes very simple inputs and provides an estimate with reasonable accuracy 71% vs 86% vs 69%. Some of the limitations of the models might include (1) size of dataset which could be mitigated by pulling data for a longer period of time though timing could be another independant variable in high growth or decline markets, (2) additional variables not included could allow for better accuracy including crime counts, school ratings, etc. These variables are not as easily available without a cost. The most accurate model is the Random Forest Regressor [Link to model](https://github.com/klcollins503/Data_Bootcamp_Final_Project/blob/main/Regressor_MaxDepth5.ipynb). See below we show in detail  1 of the 3 models and provide links to the other 2 models below:

1) [Random_Forest_Regressor Model Link](https://github.com/klcollins503/Data_Bootcamp_Final_Project/blob/main/Random_Forest_Regressor_MaxDepth5.ipynb). We posted the model with the limited depth so the decisiont tree was more readable. See [Link Decision Tree](https://github.com/klcollins503/Data_Bootcamp_Final_Project/blob/main/Resources/tree.png). After running the variable evaluation which you can see at the end of the model link just provided we determined we could pretty much go down to only 2 variables and then re-run that way:[Random_Forest_Regressor 2 Model Link](https://github.com/klcollins503/Data_Bootcamp_Final_Project/blob/main/Random_Forest_Regressor_forFlaskApp.ipynb) and produced the corresponding [Decision Tree](https://github.com/klcollins503/Data_Bootcamp_Final_Project/blob/main/Resources/tree3.png)

2) [Random_Forest_Classifier Model Link](https://github.com/klcollins503/Data_Bootcamp_Final_Project/blob/main/Random_Forest_Classifier.ipynb). Also we have a link to the [Decision Tree](https://github.com/klcollins503/Data_Bootcamp_Final_Project/blob/main/Resources/tree2.png)

3) The machine learning or multivariable linear regression process will include the following steps (for reference see [Multiple_Linear_Regression.ipynb](https://github.com/klcollins503/Data_Bootcamp_Final_Project/blob/main/Multiple_Linear_Regression.ipynb)):

-Note: First note that we are including only the final model after we tested multiple iterations and also note that we included below the model without splitting the data into train and test but we have rerun in the jupiter notebook file linked above a version of the same model splitting into test and train, please look for lines 9 to 12 in: [Multiple_Linear_Regression.ipynb](https://github.com/klcollins503/Data_Bootcamp_Final_Project/blob/main/Multiple_Linear_Regression.ipynb)

#### -Import dependencies, load and clean data.

![image](https://user-images.githubusercontent.com/96096924/169199304-36107437-9051-490c-a5e4-cff6c909f17d.png)


#### -Define variables.
Y or dependant variable will be the estimated home price which the X or dependant variables will be testing include: home characteristic variables like home type, year built, # bed, # bath, sqft , lot size , and location/demographic variables like zip code, crime rate, income, population density. Keep in mind the png below just shows the final variable selection which took multiple iterations or combinations being tested first.

![image](https://user-images.githubusercontent.com/96096924/169943000-462de40b-bfd9-4ee5-be5d-2b8c86f77017.png)

#### -Create an instance of the linear regression model. Train model or fit with Dataset.

![image](https://user-images.githubusercontent.com/96096924/169199488-da33daf8-138e-45ba-9b98-232624574c3e.png)

#### -Evaluate model coefficients and R2.
Evaluate each variable cofficient and R squared to decide is there are some variables that have low influence and worth dropping and restarting the process. In this process we decided for to use the following variables that provided the highest R squared (slightly over 0.7): 'Square Feet', 'Zip Mean HHI', 'Zip Pop Density','Lot Size','Year Built'. To get here we iterated through this process multiple times with different set of variables but just showing the final one.

![image](https://user-images.githubusercontent.com/96096924/169199597-d4a8719f-3301-415e-b9f5-bbb55d0d1850.png)


#### -Use predict method.

![image](https://user-images.githubusercontent.com/96096924/169199790-12ded49d-38fd-4c88-9fcf-28bb979897ad.png)

### 5. Predictive Model Flask 

The app.py file in both the multilinear regression model: https://github.com/klcollins503/Data_Bootcamp_Final_Project/tree/main/mlr_model, as well as the Random Forest Classifier model: https://github.com/klcollins503/Data_Bootcamp_Final_Project/tree/main/rfc_model use the pickle model output to predict home value of user inputs. A zip code dictionary was used to retrieve zip code characteristics from the zip code input. We have have created a flask app both for a multilinear regression model and random forest regressor model.  

### 6. Market Trend Analysis & Mapping

We have created interactive maps and graphs in Tableau: [Link to Tableau](https://public.tableau.com/authoring/FinalProject_16528921784890/Map1#2)

We also have created a summary presentation that includes the maps and graphs in Google Slides: [Link to Google](https://docs.google.com/presentation/d/1AFogpP1hiIdtDXincCRe_QYIVq_nWw8owLANXub_sIY/edit?usp=sharing)

## Resources
- Datasets: [Kaggle](https://www.kaggle.com/datasets/threnjen/portland-housing-prices-sales-jul-2020-jul-2021?select=portland_housing.csv), [Portland Police](https://www.portlandoregon.gov/police/71978), [Portland on the market](https://www.portlandonthemarket.com/), [Census Population Density](https://data.census.gov/cedsci/table?q=B01003&g=0400000US41%241500000&tid=ACSDT5Y2020.B01003), [Census Income](https://data.census.gov/cedsci/table?q=income&g=0400000US41%241500000&tid=ACSDT5Y2020.B19001), [ArcGis](https://www.arcgis.com/home/item.html?id=8d2012a2016e484dafaac0451f9aea24)
- Language(s): Python, SQL
- Tools: Jupyter Notebook, Flask, pgAdmin, PostgreSQL, Excel, Tableau, Google Slides
- Libraries: Pandas, Scikit-learn
