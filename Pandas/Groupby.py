
# coding: utf-8



# In[1]:

import pandas as pd
# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}


# In[2]:

df = pd.DataFrame(data)


# In[3]:

df




# In[34]:

df.groupby('Company')


# You can save this object as a new variable:

# In[35]:

by_comp = df.groupby("Company")


# And then call aggregate methods off the object:

# In[36]:

by_comp.mean()


# In[37]:

df.groupby('Company').mean()


# More examples of aggregate methods:

# In[38]:

by_comp.std()


# In[39]:

by_comp.min()


# In[40]:

by_comp.max()


# In[41]:

by_comp.count()


# In[42]:

by_comp.describe()


# In[43]:

by_comp.describe().transpose()


# In[44]:

by_comp.describe().transpose()['GOOG']



