
# coding: utf-8

# # Boston Crime Data Analysis

# In[17]:


#Import all the 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[18]:


boston =  pd.read_csv('crime.csv',encoding = "ISO-8859-1")


# In[19]:


#Lets look at the data
boston.head()


# In[20]:


#Lets look at the data type and the object. Looks like there are some missing values. 
boston.info()


# In[21]:


boston['DISTRICT_ID'] = boston['DISTRICT']


# In[22]:


#Let us drop the null values
boston.dropna(subset=['DISTRICT', 'REPORTING_AREA', 'OCCURRED_ON_DATE','UCR_PART','STREET','Lat','Location' ], how='any', inplace=True)


# In[23]:


#Now the data looks much cleaner
boston.info()


# In[24]:


# Replace missing values and 'Y' with 1 in shooting column
boston['SHOOTING'] = boston['SHOOTING'].fillna(0)
boston['SHOOTING'] = boston['SHOOTING'].replace('Y',1)


# ## Step 1 : Pre-processing

# In[25]:


#District code
District = {'A1' : 'Downtown', 'A15': 'Charlestown','A7': 'East Boston','B2': 'Roxbury','B3': 'Mattapan','C6': 'South Boston','C11': 'Dorchester','D4': 'South End','D14': 'Brighton','E5': 'West Roxbury','E13': 'Jamaica Plain','E18': 'Hyde Park','HTU': 'Human Traffic Unit'}

#Replace code into names
boston['DISTRICT'] = boston['DISTRICT'].replace(District)


# In[26]:


#We will drop columns that are not of much use in the analysis
boston.drop(['REPORTING_AREA','UCR_PART','Location','OFFENSE_CODE'],axis=1,inplace=True)


# In[27]:


#A function to check if it is day or night
def isNight(hour) :
    if hour >= 20 or hour <= 5:
        return 1
    else :
        return 0

#Create a new column    
boston['IS_NIGHT'] = boston['HOUR'].apply(lambda x : isNight(x))


# In[28]:


boston.head(20)


# In[29]:


#Writing data into csv
boston.to_csv('boston_crime_clean.csv',encoding = "ISO-8859-1")


# In[30]:


#Cheking unique values of district
boston.DISTRICT.value_counts()


# In[31]:


boston.OFFENSE_CODE_GROUP.value_counts()

