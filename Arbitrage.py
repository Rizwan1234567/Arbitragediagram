
# coding: utf-8

# In[1]:


import requests


# In[2]:


import numpy as np


# In[3]:


import pandas as pd


# In[4]:


import matplotlib.pyplot as plt


# In[62]:


api_data=requests.get("https://api.cryptonator.com/api/full/btc-usd").json()


# In[67]:


mkt_data=api_data["ticker"]["markets"]


# In[68]:


df=pd.DataFrame(mkt_data)
markets=df["market"]


# In[69]:


print(df)


# In[19]:


price = df["price"]


# In[20]:


np_price=np.array(price)


# In[24]:


volume = df["volume"]


# In[25]:


np_volume=np.array(volume)


# In[26]:


max_price=np.max(np_price)


# In[27]:


min_price=np.min(np_price)


# In[31]:


max_mkt = np.argmax(np_price)


# In[32]:


min_mkt = np.argmin(np_price)


# In[38]:


print(markets[max_mkt])


# In[42]:


difference = float(max_price)-float(min_price)


# In[46]:


print("market", markets[max_mkt], "has max price" +str(max_price))


# In[47]:


print("market", markets[min_mkt], "has min price" +str(min_price))


# In[50]:


print("differnce in price is: ", difference)


# In[79]:


plt.figure(figsize=(20,10))
plt.scatter(price,volume)
plt.ylabel("volume")
plt.ylabel("price")
for i in (markets.index):
    plt.annotate(markets[i],xy=(price[i],volume[i]),xytext=(price[i],volume[i]))


# In[59]:




