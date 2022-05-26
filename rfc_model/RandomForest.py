#!/usr/bin/env python
# coding: utf-8

# In[20]:


# Import dependencies
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from path import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import pickle
import requests
import json


# In[21]:


# Load Data
source = "Resources/final_housing.csv"
df_data = pd.read_csv(source)
df_data.tail()
df_data = df_data.dropna()
df_data


# In[22]:


# Establish the spending bins and group names.
sale_bins = [0, 250000, 400000, 600000, 800000, 1000000, 1500000, 2000000]
bin_names = ["<250k", "250k-400k", "400k-600k", "600k-800k", "800k-1M", "1M-1.5M" , "1.5M-2M"]
# Categorize spending based on the bins.
df_data["Sale Price Ranges"] = pd.cut(df_data['Sale Price'], sale_bins, labels=bin_names)

df_data


# In[23]:


# Define the features set.
X = df_data.copy()
X = X.drop("Sale Price", axis=1)
X = X.drop("Sale Date", axis=1)
X = X.drop("City", axis=1)
X = X.drop("Zip Code", axis=1)
X = X.drop("Zip Population", axis=1)
X = X.drop("Zip SqMi", axis=1)
X = X.drop("Sale Price Ranges", axis=1)
X_list = list(X.columns)
X


# In[24]:


# Define the target set.
y = df_data["Sale Price Ranges"].values
y[:13956]


# In[25]:


# Splitting into Train and Test sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)
X_train.shape, X_test.shape


# In[26]:


# Creating a StandardScaler instance.
scaler = StandardScaler()
# Fitting the Standard Scaler with the training data.
X_scaler = scaler.fit(X_train)

# Scaling the data.
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)


# In[27]:


# Create a random forest classifier.
rf_model = RandomForestClassifier(n_estimators=128, random_state=78) 


# In[28]:


# Fitting the model
rf_model = rf_model.fit(X_train_scaled, y_train)


# In[29]:


# Making predictions using the testing data.
predictions = rf_model.predict(X_test_scaled)


# In[30]:


predictions


# In[31]:


# Calculating the confusion matrix
cm = confusion_matrix(y_test, predictions)

# Create a DataFrame from the confusion matrix
cm_df = pd.DataFrame(
    cm, index=["<250k", "250k-400k", "400k-600k", "600k-800k", "800k-1M", "1M-1.5M" , "1.5M-2M"], columns=["P<250k", "P250k-400k", "P400k-600k", "P600k-800k", "P800k-1M", "P1M-1.5M" , "P1.5M-2M"])

cm_df


# In[32]:


# Calculating the accuracy score.
acc_score = accuracy_score(y_test, predictions)
print (acc_score)


# In[33]:


# Export our model as pickle file
pickle.dump(rf_model, open('rf_model.pkl','wb'))


# In[36]:


model = pickle.load(open('rf_model.pkl','rb'))
print(model.predict([[1998, 3, 2, 2000, 3000, 10, 5000, 90000]]))


# In[ ]:





# In[ ]:




