
# coding: utf-8

# In[14]:


get_ipython().run_line_magic('config', 'IPCompleter.greedy=True')


# In[2]:


from bs4 import BeautifulSoup
import requests


# Problem
# 
# Count the number of views for all videos on first page of youtube for given keyword

# In[47]:


keyword = input("Enter your keyword:")
url = 'https://www.youtube.com/results?search_query='+keyword
response = requests.get(url)


# In[48]:


bsObj = BeautifulSoup(response.text, 'lxml')


# In[51]:


totalViews = 0
numberOfVideos = 0
ul_list = bsObj.find_all('ul', class_ = 'yt-lockup-meta-info')
for ul in ul_list:
    lis = ul.findChildren()
    for li in lis:
        if li.string.endswith('views'):
            numberOfVideos = numberOfVideos + 1
            temp = li.getText()
            temp = temp.replace(' views', '').replace(',', '')
            totalViews = totalViews + int(temp)


# In[52]:


print("Total Views: " + str(totalViews))
print("Average number of Views: " + str(round(totalViews/numberOfVideos)))

