#!/usr/bin/env python
# coding: utf-8

# # Working on real project with Python
# 

# # Police Dataset

# In[1]:


#Here, data from a police checkpost is given. The dataset is available a csv file.We are going to analyze this dataset using pandas dataframe.


# In[2]:


import pandas as pd


# In[4]:


data = pd.read_csv(r"C:\Users\karth\Downloads\3. Police Data.csv")


# In[5]:


data


# ### Data Cleaning
# 

# In[7]:


#Found Null values 
data.isnull().sum()


# In[8]:


#Removed the column country_name which contained only null values
data.drop(columns = 'country_name',inplace = True)


# In[9]:


data


# In[10]:


#Speeding by Men or Women


# In[11]:


data[data.violation == 'Speeding']


# In[12]:


data[data.violation == 'Speeding'].driver_gender.value_counts()


# In[13]:


#Men were stopped more often for speeding.


# In[14]:


#Does gender affect who gets searched during a stop?


# In[15]:


data.groupby('driver_gender').search_conducted.sum()


# In[16]:


#Women are searched 366 times and men are searched 2113 times.


# In[17]:


data.search_conducted.value_counts()


# In[18]:


#Search was conducted 2479 times and 63056 times search was not conducted.In 2479 times,women are searched 366 times and men are searched 2113 times.


# In[19]:


#Mean stop duration


# In[21]:


data.stop_duration.value_counts()


# In[26]:


data['stop_duration'] = data['stop_duration'].map( {'0-15 Min':7.5,  '16-30 Min': 23,  '30+ Min': 45})


# In[27]:


data


# In[28]:


data.stop_duration.mean()


# In[29]:


#Compare the age distribution for each violation


# In[31]:


data.groupby('violation').driver_age.describe()


# In[ ]:


#For the person who was stopped for say,seat belt violation, number of people stopped is 3,mean age is 30.33, minimum age = 23, max age = 42, also the percentiles and the standard deviation are shown.

