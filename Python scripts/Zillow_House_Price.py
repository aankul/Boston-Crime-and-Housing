
# coding: utf-8

# In[221]:


import json
import requests
import xml.etree.ElementTree as ET
import pandas as pd
import xmltodict
import json


# In[222]:


#Base URL
api_url = 'http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz18zeeig1h57_5w3uy&state=ma&city=boston&childtype=neighborhood'


# In[223]:


#API call
boston_house = requests.get(api_url)
boston_house


# In[224]:


#Convertig XML to JSON
boston_json = xmltodict.parse(boston_house.content)
boston_json


# In[225]:


#Adding json data to data frame
rows_list = []

for i in boston_json['RegionChildren:regionchildren']['response']['list']['region']:
    if(i.get('zindex') is not None) :
        zillow = {}
        zillow['District'] = i.get('name')
        zillow['Price'] = i.get('zindex').get('#text')
        zillow['latitude'] = i.get('latitude')
        zillow['longitude'] = i.get('longitude')  
        rows_list.append(zillow)
df_boston_house = pd.DataFrame(rows_list)  
df_boston_house


# In[227]:


#Writing it into csv
df_boston_house.to_csv('boston_house_price_current.csv')

