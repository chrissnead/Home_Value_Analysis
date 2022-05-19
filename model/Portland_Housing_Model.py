#!/usr/bin/env python
# coding: utf-8

# In[32]:


#Import joined house sale data and zip code data, mockup will be from github, final will be from AWS
source = "Resources/combined_housing.csv"
data = pd.read_csv(source)


# In[33]:


X = data[['Square Feet', 'Zip Mean HHI', 'Zip Pop Density','Lot Size','Bed','Bath','Year Built']]
y = data['Sale Price']


# In[34]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

regressor = LinearRegression()

regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)


# In[35]:


# Export our model to HDF5 file
# HDF5 didn't work, trying pickle
pickle.dump(regressor, open('portland_housing_model.pkl','wb'))


# In[36]:


# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([['1400','50000','50','100','20','5','2003']]))


# In[ ]:




