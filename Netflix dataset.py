#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


data=pd.read_csv(r"C:\Users\ASUS\Downloads\8. Netflix Dataset.csv")


# In[3]:


data


# In[4]:


data.head()


# In[5]:


data.tail()


# In[7]:


data.shape


# In[8]:


data.size


# In[9]:


data.columns


# In[10]:


data.dtypes


# In[11]:


data.info()


# In[12]:


#Task 1:Is there any duplicate? If yes than remove the duplicates.
data.head()


# In[13]:


data.shape


# In[15]:


data[data.duplicated()]


# In[17]:


data.drop_duplicates(inplace=True)


# In[18]:


data[data.duplicated()]


# In[19]:


data.shape


# In[20]:


#Task 2:Is there any null value present in column? Show with heat-map
data.head()


# In[22]:


data.isnull()


# In[24]:


data.isnull().sum()


# In[25]:


import seaborn as sns


# In[26]:


sns.heatmap(data.isnull())


# In[27]:


#Task 3:For "House of Cards" what is the show id and how is the director of this show?
#Method 1
data.head()


# In[28]:


data[data['Title'].isin(['House of Cards'])]


# In[30]:


#Method 2
data[data['Title'].str.contains('House of Cards')]


# In[33]:


#Task 4:In which year highest number of TV shows and movies were released? Show with bar graph
data.dtypes


# In[39]:


data['Date_N']= pd.to_datetime(data['Release_Date'])


# In[40]:


data.head()


# In[41]:


data.dtypes


# In[42]:


data['Date_N'].dt.year.value_counts()


# In[43]:


data['Date_N'].dt.year.value_counts().plot(kind='bar')


# In[45]:


#Task 5:How many Movies and TV shows are in dataset? Show with the bar graph
data.head(2)


# In[47]:


data.groupby('Category').Category.count()


# In[61]:


sns.countplot(data=data, x='Category')


# In[62]:


#Task 6:Show all the movies that are released in yera 2000
data.head(2)


# In[63]:


data['Year']=data['Date_N'].dt.year


# In[64]:


data.head(2)


# In[74]:


data[(data['Category']== 'Movie') & (data['Year']==2000)]


# In[75]:


data[(data['Category']== 'Movie') & (data['Year']==2020)]


# In[76]:


#Task 7:Show only the titles of all TV shows that were released in India only
data.head(2)


# In[82]:


data[(data['Category']=='TV Show') & (data['Country']== 'India')]['Title']


# In[83]:


#Task 8:Show top 10 directors,who gave the highest number of TV shows and Movies to Netflix
data['Director'].value_counts().head(10)


# In[80]:


#Task 9:Show all the Records,where "category is movie and type is comedies" or "country is United Kingdom"
data[(data['Category']== 'Movie') & (data['Type']=='Comedies')]


# In[81]:


data[(data['Category']== 'Movie') & (data['Type']=='Comedies') | (data['Country']=='United Kingdom')]


# In[84]:


#Task 10:In how many movies/shows, Tom Cruise was cast?
data.head()


# In[86]:


data[data['Cast']=='Tom Cruise']


# In[87]:


data[data['Cast'].str.contains('Tom Cruise')]


# In[88]:


data_new=data.dropna()


# In[89]:


data_new.head(2)


# In[90]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]

