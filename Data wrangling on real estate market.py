#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
matplotlib.rcParams["figure.figsize"] = (20,10)


# In[2]:


# Load the dataset
data = pd.read_csv(r"C:\Users\hp\Desktop\Bengaluru_House_Data.csv")


# In[3]:


data.head()


# In[4]:


data.shape


# In[5]:


data.columns


# In[6]:


data['area_type']


# In[7]:


data['area_type'].unique()


# In[8]:


data['area_type'].value_counts()


# In[9]:


#Drop features that are not required to build our model
df = data.drop(['area_type','society','balcony','availability'],axis='columns')
df.shape


# In[10]:


df.isnull().sum()


# In[11]:


df.shape


# In[12]:


df3 = df.dropna()
df3.isnull().sum()


# In[13]:


df3.shape


# In[14]:


df3['size'].unique()


# In[15]:


df3['bhk'] = df3['size'].apply(lambda x: int(x.split(' ')[0]))


# In[16]:


df3.head()


# In[17]:


df3.bhk.unique()


# In[18]:


df3.total_sqft.unique()


# In[21]:


# Explore the 'total_sqft' feature
def is_float(x):
    try:
        float(x)
        return True
    except:
        return False


# In[22]:


df3[~df3['total_sqft'].apply(is_float)].head(10)


# In[24]:


def convert_sqft_to_num(x):
    # Split values like '1000 - 2000' and calculate the average
    tokens = x.split('-')
    if len(tokens) == 2:
        return (float(tokens[0]) + float(tokens[1])) / 2
    try:
        # Try to convert other values to float
        return float(x)
    except:
        # Return None if the conversion is not possible
        return None


# In[25]:


convert_sqft_to_num('2100 - 2850')


# In[26]:


convert_sqft_to_num('34.46Sq. Meter')


# In[27]:


df4 = df3.copy()
df4.total_sqft = df4.total_sqft.apply(convert_sqft_to_num)
df4


# In[28]:


df4 = df4[df4.total_sqft.notnull()]
df4


# In[29]:


df4.loc[30]


# In[30]:


df5 = df4.copy()
df5['price_per_sqft'] = df5['price']*100000/df5['total_sqft']
df5.head()


# In[31]:


df5_stats = df5['price_per_sqft'].describe()
df5_stats


# In[32]:


df5.to_csv("bhp.csv",index=False)


# In[33]:


len(df5.location.unique())


# In[34]:


df5.location = df5.location.apply(lambda x: x.strip())
location_stats = df5['location'].value_counts(ascending=False)


# In[35]:


location_stats


# In[36]:


len(location_stats[location_stats>10])


# In[37]:


len(location_stats)


# In[38]:


len(location_stats[location_stats<=10])


# In[39]:


location_stats_less_than_10 = location_stats[location_stats<=10]
location_stats_less_than_10


# In[40]:


len(df5.location.unique())


# In[41]:


df5.location = df5.location.apply(lambda x: 'other' if x in location_stats_less_than_10 else x)
len(df5.location.unique())


# In[42]:


df5.head(10)


# In[43]:


df5[df5.total_sqft/df5.bhk<300].head()


# In[44]:


df6 = df5[~(df5.total_sqft/df5.bhk<300)]
df6.shape


# In[45]:


df6.columns


# In[46]:


plt.boxplot(df6['total_sqft'])
plt.show()


# In[48]:


Q1 = np.percentile(df6['total_sqft'], 25.) # 25th percentile of the data of the given feature
Q3 = np.percentile(df6['total_sqft'], 75.) # 75th percentile of the data of the given feature
IQR = Q3-Q1 #Interquartile Range
ll = Q1 - (1.5*IQR)
ul = Q3 + (1.5*IQR)
upper_outliers = df6[df6['total_sqft'] > ul].index.tolist()
lower_outliers = df6[df6['total_sqft'] < ll].index.tolist()
bad_indices = list(set(upper_outliers + lower_outliers))
drop = True
if drop:
    df6.drop(bad_indices, inplace = True, errors = 'ignore')


# In[49]:


plt.boxplot(df6['bath'])
plt.show()


# In[50]:


plt.boxplot(df6['price'])
plt.show()
Q1 = np.percentile(df6['price'], 25.) # 25th percentile of the data of the given feature
Q3 = np.percentile(df6['price'], 75.) # 75th percentile of the data of the given feature
IQR = Q3-Q1 #Interquartile Range
ll = Q1 - (1.5*IQR)
ul = Q3 + (1.5*IQR)
upper_outliers = df6[df6['price'] > ul].index.tolist()
lower_outliers = df6[df6['price'] < ll].index.tolist()
bad_indices = list(set(upper_outliers + lower_outliers))
drop = True
if drop:
    df6.drop(bad_indices, inplace = True, errors = 'ignore')


# In[51]:


plt.boxplot(df6['bhk'])
plt.show()
Q1 = np.percentile(df6['bhk'], 25.) # 25th percentile of the data of the given feature
Q3 = np.percentile(df6['bhk'], 75.) # 75th percentile of the data of the given feature
IQR = Q3-Q1 #Interquartile Range
ll = Q1 - (1.5*IQR)
ul = Q3 + (1.5*IQR)
upper_outliers = df6[df6['bhk'] > ul].index.tolist()
lower_outliers = df6[df6['bhk'] < ll].index.tolist()
bad_indices = list(set(upper_outliers + lower_outliers))
drop = True
if drop:
    df6.drop(bad_indices, inplace = True, errors = 'ignore')


# In[52]:


plt.boxplot(df6['price_per_sqft'])
plt.show()
Q1 = np.percentile(df6['price_per_sqft'], 25.) # 25th percentile of the data of the given feature
Q3 = np.percentile(df6['price_per_sqft'], 75.) # 75th percentile of the data of the given feature
IQR = Q3-Q1 #Interquartile Range
ll = Q1 - (1.5*IQR)
ul = Q3 + (1.5*IQR)
upper_outliers = df6[df6['price_per_sqft'] > ul].index.tolist()
lower_outliers = df6[df6['price_per_sqft'] < ll].index.tolist()
bad_indices = list(set(upper_outliers + lower_outliers))
drop = True
if drop:
    df6.drop(bad_indices, inplace = True, errors = 'ignore')


# In[ ]:




