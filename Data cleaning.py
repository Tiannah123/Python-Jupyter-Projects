#!/usr/bin/env python
# coding: utf-8

# # Data Science Journey

# In[1]:


import pandas as pd


# In[6]:


dsj = pd.read_csv("Data science 01.csv", header=0, sep=",")
print(dsj)


# In[7]:


dsj.dropna(axis=0, inplace=True)
print(dsj)


# In[8]:


print(dsj.info())


# In[15]:


pd.set_option('display.max_columns',None)
print(dsj.describe())


# In[ ]:




