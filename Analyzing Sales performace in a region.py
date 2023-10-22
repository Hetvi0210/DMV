#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


# Load the retail sales data from the CSV file
data = pd.read_csv(r"C:\Users\hp\Desktop\customer_shopping_data.csv")


# In[3]:


# Explore the dataset
print(data.head())


# In[7]:


# To check the count of records grouped by region/branch of the mall
data.groupby("shopping_mall").count()


# In[9]:


# To check the count of records grouped by the product categories
data.groupby("category").count()


# In[11]:


# total sales for each mall branch
branch_sales = data.groupby("shopping_mall").sum()


# In[12]:


# total sales for each category of product
category_sales = data.groupby("category").sum()


# In[13]:


#to get the top performing branches
branch_sales.sort_values(by = "price", ascending = False)


# In[14]:


# to get the top selling categories
category_sales.sort_values(by = "price", ascending = False)


# In[16]:


# to get total sales for each combination of branch and product_category
combined_branch_category_sales = data.groupby(["shopping_mall", "category"]).sum()


# In[17]:


# pie chart for sales by branch
plt.pie(branch_sales["price"], labels = branch_sales.index)
plt.show()


# In[18]:


# pie chart for sales by product category
plt.pie(category_sales["price"], labels = category_sales.index)
plt.show()


# In[20]:


combined_pivot = data.pivot_table(index="shopping_mall", columns="category", values="price", aggfunc="sum")


# In[21]:


# grouped bar chart for sales of different categories at different branches
combined_pivot.plot(kind="bar", figsize=(10, 6))
plt.show()

