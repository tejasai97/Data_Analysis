
# coding: utf-8

# ___


# In[1]:

import numpy as np
import pandas as pd


# ## CSV
# 
# ### CSV Input

# In[2]:

df = pd.read_csv('example')
df


# ### CSV Output

# In[3]:

df.to_csv('example',index=False)



# ### Excel Input

# In[35]:

pd.read_excel('Excel_Sample.xlsx',sheetname='Sheet1')


# ### Excel Output

# In[33]:

df.to_excel('Excel_Sample.xlsx',sheet_name='Sheet1')


# ## HTML

# In[5]:

df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')


# In[7]:

df[0]



# In[4]:

from sqlalchemy import create_engine


# In[5]:

engine = create_engine('sqlite:///:memory:')


# In[6]:

df.to_sql('data', engine)


# In[7]:

sql_df = pd.read_sql('data',con=engine)


# In[8]:

sql_df


# # Great Job!
