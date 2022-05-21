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

Given that we have identified multiple independent variables that can help predict the sale price, a multivariable regression model or a random forest regressor will most accurately predict values based on the data. We followed the processes below for both, In the linear regression model we cleaned data and selected the right variables until we got the best R squared value output (slightly over 71%), indicating a fairly accurate prediction given our constraints. For the random forest model we took again all variables, but interestingly enough the model ended up choosing the same variables as we chose for the prior model. This model seems to boost accuracy from the linear regression to 86% (and potentially 88% without limiting the depth). With both models it takes very simple inputs and provides an estimate with reasonable accuracy 71% vs 86%. Some of the limitations of the models might include (1) size of dataset which could be mitigated by pulling data for a longer period of time though timing could be another independant variable in high growth or decline markets, (2) additional variables not included could allow for better accuracy including crime counts, school ratings, etc. These variables are not as easily available without a cost. See both models below:

The machine learning or multivariable linear regression process will include the following steps (for reference see [Multiple_Linear_Regression.ipynb](https://github.com/klcollins503/Data_Bootcamp_Final_Project/blob/main/Multiple_Linear_Regression.ipynb)):

-Note: note that we included below the model without splitting the data into train and test but we have rerun in the jupiter notebook file linked above a version of the same model splitting into test and train, please look for lines 9 to 12 in: [Multiple_Linear_Regression.ipynb](https://github.com/klcollins503/Data_Bootcamp_Final_Project/blob/main/Multiple_Linear_Regression.ipynb)

#### -Import dependencies, load and clean data.

![image](https://user-images.githubusercontent.com/96096924/169199304-36107437-9051-490c-a5e4-cff6c909f17d.png)


#### -Define variables.
Y or dependant variable will be the estimated home price which the X or dependant variables will be testing include: home characteristic variables like home type, year built, # bed, # bath, sqft , lot size , and location/demographic variables like zip code, crime rate, income, population density. Keep in mind the png below just shows the final variable selection which took multiple iterations or combinations being tested first.

![image](https://user-images.githubusercontent.com/96096924/169199373-169ba359-d65e-4545-ae4c-422875bfa77b.png)

#### -Create an instance of the linear regression model. Train model or fit with Dataset.

![image](https://user-images.githubusercontent.com/96096924/169199488-da33daf8-138e-45ba-9b98-232624574c3e.png)

#### -Evaluate model coefficients and R2.
Evaluate each variable cofficient and R squared to decide is there are some variables that have low influence and worth dropping and restarting the process. In this process we decided for to use the following variables that provided the highest R squared (slightly over 0.7): 'Square Feet', 'Zip Mean HHI', 'Zip Pop Density','Lot Size','Year Built'. To get here we iterated through this process multiple times with different set of variables but just showing the final one.

![image](https://user-images.githubusercontent.com/96096924/169199597-d4a8719f-3301-415e-b9f5-bbb55d0d1850.png)


#### -Use predict method.

![image](https://user-images.githubusercontent.com/96096924/169199790-12ded49d-38fd-4c88-9fcf-28bb979897ad.png)

The machine learning or random forest regression process will include the following steps (for reference see [Random_Forest_Regressor_MaxDepth5.ipynb](https://github.com/klcollins503/Data_Bootcamp_Final_Project/blob/main/Random_Forest_Regressor_MaxDepth5.ipynb):

#### -Import dependencies, load and clean data. 
Note: only showing the import dependencies as the rest is same as prior model

![image](https://user-images.githubusercontent.com/96096924/169628745-81afcd75-8e6a-49c7-aee7-70bb1479d5c9.png)

#### -Define the feature and target set.

![image](https://user-images.githubusercontent.com/96096924/169628810-175e67fb-5754-4975-bd30-0fde7c8cea81.png)

#### -Split into Train and Test sets.

![image](https://user-images.githubusercontent.com/96096924/169628847-ca4f1762-0504-428b-a2a2-be5dd5fd4fab.png)

#### -Scaling and Fiting model.

![image](https://user-images.githubusercontent.com/96096924/169628893-d43be3f5-ca20-4082-b46a-fd00401a940d.png)

#### -Running and making predictions.

![image](https://user-images.githubusercontent.com/96096924/169628939-58e0b79a-2a59-4dce-8ff6-181f9005d9f9.png)

#### -Calculating accuracy.

![image](https://user-images.githubusercontent.com/96096924/169628970-b56a0e00-e4d7-40f7-8fb7-3273bdbe8709.png)

#### -Printing decision tree.

![image](https://user-images.githubusercontent.com/96096924/169629001-06d556f2-009b-4205-9139-8f5fc26e95cb.png)

### 5. Predictive Model Flask 

In order to simplify user inputs in the Flask app we dropped a few variables. With this, the main 2 variables the user must provide are square footage and zip code. The model R squared only drops one point so we consider this a very good trade off of a little bit of accuracy in exchange for a more user friendly input requirement.

The app.py file uses the pickle model output to predict home value of user inputs. We will use a dictionary to retrieve the zip code characteristics as the user input.

### 6. Market Trend Analysis & Mapping

We have created interactive maps and graphs in Tableau: [Link to Tableau](https://public.tableau.com/views/FinalProject_16528921784890/Map1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)

We also have created a summary presentation that includes the maps and graphs in Google Slides: [Link to Google](https://docs.google.com/presentation/d/e/2PACX-1vROMHIh3D-UCJORpKo2s_XneHiCjf_OwLdKasuqfTai19b0_DwvtW7NHxBnI65dGvVG4HDaQPs5sPa-/pub?start=true&loop=true&delayms=3000&slide=id.g12c77fac72e_0_1)

## Resources
- Datasets: [Kaggle](https://www.kaggle.com/datasets/threnjen/portland-housing-prices-sales-jul-2020-jul-2021?select=portland_housing.csv), [Portland Police](https://www.portlandoregon.gov/police/71978), [Portland on the market](https://www.portlandonthemarket.com/), [Census Population Density](https://data.census.gov/cedsci/table?q=B01003&g=0400000US41%241500000&tid=ACSDT5Y2020.B01003), [Census Income](https://data.census.gov/cedsci/table?q=income&g=0400000US41%241500000&tid=ACSDT5Y2020.B19001), [ArcGis](https://www.arcgis.com/home/item.html?id=8d2012a2016e484dafaac0451f9aea24)
- Language(s): Python, SQL
- Tools: Jupyter Notebook, Flask, pgAdmin, PostgreSQL, Excel, Tableau, Google Slides
- Libraries: Pandas, Scikit-learn
