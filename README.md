# Data_Bootcamp_Final_Project

## Project Outline
## Roles 
* Square - Kim
* Triangle - Sebastian, Kim
* Circle - Christopher


## Goal
Build a model that estimates a home prices in Portland based on home characteristics (bedrm/bath, sqft, year built, etc) and location/demographic characteristics (zip code, crime, income, population density, etc). In addition to the predictive model will also study market trends and draw some informative conclusions to help understand the market. 

## Process
The proposed process includes the following steps and tools:

### 1) Collect Data
We have gathered home prices and home characteristics from Kaggle and complementing with location characteristics from: Portland Maps, Portland Police, Bureau of Labor Statistics, Portland on the market, Census.gov, etc

Add any webscraping??

### 2) Data Cleaning
Data cleaning process includes excel , jupiter notebook processes included in the github repository. 

### 3) Database Creation  
Updload collected and cleaned data to Postgres or SQL, then build relationships and produce and export final dataframe for analysis. Need database mockup by Sun (Kim working on it)

### 4) Machine Learning Model & Flask
Create a multivariable regression model testing all the home characteristics and location/demographic characteristics mentioned above , evaluate and make adjustments to land in the best predictive model. Then reate a flask app to interact with model. 

The machine learning or multivariable linear regression process will include the following steps:

####- Define variables:
Y or dependant variable will be the estimated home price which the X or dependant variables will be testing include: home characteristic variables like home type, year built, # bed, # bath, sqft , lot size , and location/demographic variables like zip code, crime rate, income, population density.
####- Scale and Normalize values if needed & Handle any categorical variables if needed
####- Split X and Y into training and testing sets
####- Create an instance of the linear regression model
####- Train model or fit with Dataset
####- Create predictions and evluate R2

Note or Open questions: Do we need to do the home characteristic model at the zip code level? assume datasets will be too small to analyize by zip so no.

### 5) Market Trend Analysis & Mapping
perform analysis on market trends and present in tableau or google sheets. Also provide some summaries in heatmap form. 
