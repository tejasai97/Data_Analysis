
# coding: utf-8



# In[1]:

import pandas as pd
import numpy as np


# In[2]:

from numpy.random import randn
np.random.seed(101)


# In[3]:

df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())


# In[4]:

df


# ## Selection and Indexing
# 

# In[11]:

df['W']


# In[6]:

# Pass a list of column names
df[['W','Z']]


# In[7]:

# SQL Syntax (NOT RECOMMENDED!)
df.W


# DataFrame Columns are just Series

# In[8]:

type(df['W'])


# **Creating a new column:**

# In[9]:

df['new'] = df['W'] + df['Y']


# In[192]:

df


# ** Removing Columns**

# In[193]:

df.drop('new',axis=1)


# In[194]:

# Not inplace unless specified!
df


# In[195]:

df.drop('new',axis=1,inplace=True)


# In[196]:

df


# Can also drop rows this way:

# In[197]:

df.drop('E',axis=0)


# ** Selecting Rows**

# In[198]:

df.loc['A']


# Or select based off of position instead of label 

# In[199]:

df.iloc[2]


# ** Selecting subset of rows and columns **

# In[200]:

df.loc['B','Y']


# In[201]:

df.loc[['A','B'],['W','Y']]


# ### Conditional Selection
# 
# An important feature of pandas is conditional selection using bracket notation, very similar to numpy:

# In[202]:

df


# In[203]:

df>0


# In[204]:

df[df>0]


# In[13]:

df[df['W']>0]


# In[206]:

df[df['W']>0]['Y']


# In[207]:

df[df['W']>0][['Y','X']]


# For two conditions you can use | and & with parenthesis:

# In[208]:

df[(df['W']>0) & (df['Y'] > 1)]


# ## More Index Details
# 

# In[209]:

df


# In[210]:

# Reset to default 0,1...n index
df.reset_index()


# In[211]:

newind = 'CA NY WY OR CO'.split()


# In[212]:

df['States'] = newind


# In[213]:

df


# In[214]:

df.set_index('States')


# In[215]:

df


# In[216]:

df.set_index('States',inplace=True)


# In[218]:

df


# ## Multi-Index and Index Hierarchy
# 

# In[16]:

# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[17]:

hier_index


# In[18]:

df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
df



# In[260]:

df.loc['G1']


# In[263]:

df.loc['G1'].loc[1]


# In[19]:

df.index.names


# In[266]:

df.index.names = ['Group','Num']


# In[267]:

df


# In[270]:

df.xs('G1')


# In[271]:

df.xs(['G1',1])


# In[273]:

df.xs(1,level='Num')


