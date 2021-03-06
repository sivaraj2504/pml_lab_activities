
# coding: utf-8

# In[34]:


import pandas as pd
df = pd.read_csv('Future50.csv',index_col=0)
df.head(10)


# In[33]:


df.shape


# In[7]:


df.size


# In[29]:


import matplotlib.pyplot as plt
import numpy as np
sales_data=df[['Sales','Units']]


# In[ ]:


sales_data.to_csv()


# In[27]:


sales_data


# In[36]:


plt.plot(sales_data, linestyle = 'dashed')
plt.show()


# In[38]:


import json
f=open('Indian_Number_plates.json',)
data = json.load(f) 

