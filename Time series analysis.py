#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

# Load CSV data with 'latin1' encoding
data = pd.read_csv(r"C:\Users\hp\Desktop\sales_data_sample.csv", encoding='latin1')


# In[7]:


# Explore CSV data
data.head()


# In[8]:


data.info()


# In[9]:


data.describe()


# In[10]:


# Handle missing values
data.fillna(0, inplace=True)


# In[11]:


# Remove duplicates
data.drop_duplicates(inplace=True)


# In[14]:


# Example: Calculate total sales
total_sales = data['SALES'].sum()

# Example: Group by product category and calculate average sales
avg_sales_by_category = data.groupby('PRODUCTLINE')['SALES'].mean()


# In[15]:


import matplotlib.pyplot as plt

# Example: Create a bar plot for product categories
plt.bar(avg_sales_by_category.index, avg_sales_by_category.values)
plt.xlabel('Category')
plt.ylabel('Average Sales')
plt.title('Average Sales by Category')
plt.show()


# In[16]:


# Create a bar plot for average sales by product category
avg_sales_by_category = data.groupby('PRODUCTLINE')['SALES'].mean()
plt.figure(figsize=(10, 6))
plt.bar(avg_sales_by_category.index, avg_sales_by_category.values)
plt.xlabel('Product Category')
plt.ylabel('Average Sales')
plt.title('Average Sales by Product Category')
plt.xticks(rotation=45)
plt.show()


# In[17]:


# Create a pie chart to show the distribution of product categories
category_distribution = data['PRODUCTLINE'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(category_distribution, labels=category_distribution.index, autopct='%1.1f%%')
plt.title('Product Category Distribution')
plt.show()


# In[18]:


# Create a box plot to visualize the distribution of sales
plt.figure(figsize=(8, 6))
plt.boxplot(data['SALES'], vert=False)
plt.xlabel('Sales')
plt.title('Sales Distribution')
plt.show()

