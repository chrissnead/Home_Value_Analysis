#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn
import pickle
import requests
import json


# In[5]:


# Load Data
source = "../Resources/CleanData/clean_housing.csv"
data = pd.read_csv(source)
data.tail()
data = data.dropna()
data


# # multivariable linear regression
# 

# In[13]:


# Define variables
X = data[['Square Feet', 'Zip Mean HHI']]
y = data['Sale Price']


# In[14]:


# Create instance of linear regression model
from sklearn.linear_model import LinearRegression
classifier = LinearRegression()
classifier


# In[15]:


# Train/fit model
classifier.fit(X, y)


# In[16]:


# Evaluate model
print(f"R2 score: {classifier.score(X, y)}")

print(f"Coefficients: { classifier.coef_}")
#X = data[['Square Feet', 'Zip Mean HHI', 'Zip Pop Density','Lot Size','Year Built']]


# In[17]:


# Run predictive model
predictions = classifier.predict(X)


# In[18]:


# Export our model to HDF5 file
# HDF5 didn't work, trying pickle
pickle.dump(classifier, open('mlr_model.pkl','wb'))


# In[20]:


# Loading model to compare the results
model = pickle.load(open('mlr_model.pkl','rb'))
print(model.predict([['1400','50000']]))


# In[ ]:





# In[ ]:




