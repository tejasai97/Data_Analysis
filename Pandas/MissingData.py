
# coding: utf-8



# In[2]:

import numpy as np
import pandas as pd


# In[3]:

df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})


# In[4]:

df


# In[5]:

df.dropna()


# In[6]:

df.dropna(axis=1)


# In[7]:

df.dropna(thresh=2)


# In[15]:

df.fillna(value='FILL VALUE')


# In[17]:

df['A'].fillna(value=df['A'].mean())

