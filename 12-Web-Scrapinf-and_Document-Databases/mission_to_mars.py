#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup 
from splinter import Browser
import requests
import pandas as pd
#executable_path = {"executable_path": "\Users\Chandler\Anaconda\Anaconda3\Lib\site-packages\splinter"}
#browser = Browser("chrome", **executable_path, headless=False)


# In[2]:


#Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. 
#Assign the text to variables that you can reference later
# URL of page to be scraped
url = 'https://mars.nasa.gov/news/'
image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
twitter_url = 'https://twitter.com/MarsWxReport'
facts_url = 'https://space-facts.com/mars/'
hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
executable_path = {'executable_path': 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Retrieve page with the requests module
response = requests.get(url)


# In[4]:


# Create BeautifulSoup object; parse with 'html.parser'
# soup = BeautifulSoup(response.text, 'html.parser')
soup = BeautifulSoup(response.text, 'lxml')


# In[5]:


results = soup.find_all('div', class_='image_and_description_container')


# In[6]:


results[0]
titles = soup.find_all('div', class_='content_title')
pgs = soup.find_all('div', class_='rollover_description_inner')
news_title = titles[0].text
news_p = pgs[0].text


# In[7]:


print(news_title)


# In[8]:


print(news_p)


# In[9]:


#get featured image
browser.visit(image_url)
# HTML object
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all elements that contain book information
sections = soup.find_all('section', class_='primary_media_feature')
a = sections[0].find('article')
print(a['style'])
print('-----------')
jpg = a['style'].split('\'')[1]
featured_image_url = image_url + jpg
print(featured_image_url)


# In[10]:


#get twitter
browser.visit(twitter_url)
# HTML object
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all elements that contain book information
items = soup.find_all('li', class_='js-stream-item')
a = items[0]
mars_weather = a.find('p', class_='tweet-text').text
print(mars_weather)


# In[11]:


tables = pd.read_html(facts_url)
tables


# In[12]:


facts_table = tables[0].to_html()
facts_table


# In[13]:


hemisphere_image_urls = [
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
]


# In[ ]:





# In[ ]:




