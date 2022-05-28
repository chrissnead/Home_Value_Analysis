#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Import dependencies
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from path import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import pickle
import requests
import json


# In[19]:


# Load Data
source = "Resources/final_housing.csv"
df_data = pd.read_csv(source)
df_data.tail()
df_data = df_data.dropna()
df_data


# In[20]:


df_data.dtypes


# In[21]:


# Define the features set.
X = df_data.copy()
X = X.drop("Sale Price", axis=1)
X = X.drop("Sale Date", axis=1)
X = X.drop("City", axis=1)
X = X.drop("Zip Code", axis=1)
X = X.drop("Zip Population", axis=1)
X = X.drop("$/SF", axis=1)
X = X.drop("Bed", axis=1)
X = X.drop("Bath", axis=1)
X = X.drop("Year Built", axis=1)
X = X.drop("Zip Pop Density", axis=1)
X = X.drop("Lot Size", axis=1)
X = X.drop("Zip SqMi", axis=1)
X_list = list(X.columns)
X


# In[22]:


# Define the target set.
y = df_data["Sale Price"].values
y[:14113]


# In[23]:


# Splitting into Train and Test sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
X_train.shape, X_test.shape


# In[24]:


# Creating a StandardScaler instance.
scaler = StandardScaler()
# Fitting the Standard Scaler with the training data.
X_scaler = scaler.fit(X_train)

# Scaling the data.
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)


# In[25]:


# Create a random forest regressor.
rf_model = RandomForestRegressor(n_estimators=20, random_state=42, max_depth = 5)


# In[26]:


# Fitting the model
rf_model = rf_model.fit(X_train_scaled, y_train)


# In[27]:


# Making predictions using the testing data.
predictions = rf_model.predict(X_test_scaled)


# In[28]:


predictions


# In[29]:


# Calculate the absolute errors
errors = abs(predictions - y_test)


# In[30]:


print('Average error: ', round(np.mean(errors), 2))


# In[31]:


# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / y_test)

# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')


# In[32]:


# Import tools needed for visualization
from sklearn.tree import export_graphviz
import pydot

# Pull out one tree from the forest
tree = rf_model.estimators_[5]
# Import tools needed for visualization
from sklearn.tree import export_graphviz
import pydot
# Pull out one tree from the forest
tree = rf_model.estimators_[5]
# Export the image to a dot file
export_graphviz(tree, out_file = 'tree3.dot', feature_names = X_list, rounded = True, precision = 1)
# Use dot file to create a graph
(graph, ) = pydot.graph_from_dot_file('tree3.dot')
# Write graph to a png file
graph.write_png('tree3.png')


# In[33]:


# Get numerical feature importances
importances = list(rf_model.feature_importances_)
# List of tuples with variable and importance
feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(X_list, importances)]
# Sort the feature importances by most important first
feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)
# Print out the feature and importances 
[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances];


# In[34]:


plt.figure(figsize=(10,10))
plt.scatter(y_test, predictions, c='crimson')
#plt.yscale('log')
#plt.xscale('log')

p1 = max(max(predictions), max(y_test))
p2 = min(min(predictions), min(y_test))
plt.plot([p1, p2], [p1, p2])
plt.xlabel('Sale Price', fontsize=15)
plt.ylabel('Predictions', fontsize=15)
plt.axis('equal')
plt.show()


# In[40]:


# Export our model as pickle file
pickle.dump(rf_model, open('rf_model.pkl','wb'))


# In[42]:


model = pickle.load(open('rf_model.pkl','rb'))
print(model.predict([[8000, 140000]]))


# In[ ]:




