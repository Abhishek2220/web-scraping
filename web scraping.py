#!/usr/bin/env python
# coding: utf-8

# In[4]:


from bs4 import BeautifulSoup
import requests


# In[5]:


website='https://subslikescript.com/movie/Titanic-120338'


# In[6]:


result=requests.get(website)


# In[7]:


content=result.text


# In[8]:


soup=BeautifulSoup(content,'lxml')
#print(soup.prettify())


# In[9]:


box = soup.find('article', class_='main-article')


# In[10]:


title=box.find('h1').get_text()


# In[11]:


print(title)


# In[12]:


transcript=box.find('div',class_='full-script').get_text(strip=True,separator='')


# In[13]:


print(title)
print(transcript)


# In[31]:


with open(f'{title}.txt','w',encoding='utf-8') as file:
    file.write(transcript)


# In[ ]:





# In[ ]:




