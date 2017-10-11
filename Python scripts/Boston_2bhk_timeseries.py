
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import datetime as dt


# In[2]:


boston_2bhk = pd.read_csv('boston_2BHK.csv')


# In[3]:


boston_2bhk.head()


# In[4]:


#Filtering city as boston
boston_2bhk = boston_2bhk[boston_2bhk['City'] == 'Boston']


# In[5]:


#Dropping columns that are not needed for analysis
boston_2bhk.drop(['RegionID','Metro','State','Metro','SizeRank','City','CountyName'],axis=1,inplace=True)


# In[6]:


boston_2bhk.head()


# In[7]:


#Converting date columns in rows
boston_2bhk_ts = pd.melt(boston_2bhk, id_vars=["RegionName"], var_name="Date", value_name="House Prices")


# In[8]:


boston_2bhk_ts.head()


# In[9]:


#Converting the Date column into datetime format
boston_2bhk_ts['Date'] = boston_2bhk_ts.Date.apply(lambda x : str(x)+'-01')

boston_2bhk_ts['Date'] = boston_2bhk_ts.Date.apply(lambda x : dt.datetime.strptime(x, '%Y-%m-%d').date())


# In[10]:


#Pivoting the table
#boston_2bhk_ts = pd.pivot_table(boston_2bhk_ts, values='House Prices', index=['Date'], columns=['RegionName'], aggfunc=np.sum)


# In[11]:


#Awesome!!
#boston_2bhk_ts.head()


# In[12]:


#import into csv
boston_2bhk_ts.to_csv('boston_2bhk_timeseries_clean.csv')

