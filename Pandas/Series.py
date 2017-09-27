
# coding: utf-8



# In[2]:

import numpy as np
import pandas as pd


# ### Creating a Series
# 
# You can convert a list,numpy array, or dictionary to a Series:

# In[3]:

labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}


# ** Using Lists**

# In[4]:

pd.Series(data=my_list)


# In[5]:

pd.Series(data=my_list,index=labels)


# In[6]:

pd.Series(my_list,labels)


# ** NumPy Arrays **

# In[7]:

pd.Series(arr)


# In[8]:

pd.Series(arr,labels)


# ** Dictionary**

# In[9]:

pd.Series(d)


# ### Data in a Series
# 
# A pandas Series can hold a variety of object types:

# In[10]:

pd.Series(data=labels)


# In[11]:

# Even functions (although unlikely that you will use this)
pd.Series([sum,print,len])


# ## Using an Index
# 


# In[12]:

ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])                                   


# In[13]:

ser1


# In[14]:

ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])                                   


# In[15]:

ser2


# In[16]:

ser1['USA']


# Operations are then also done based off of index:

# In[17]:

ser1 + ser2


