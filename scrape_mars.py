
# coding: utf-8

# In[6]:


from splinter import Browser 
from bs4 import BeautifulSoup
import pandas as pd 


# NASA Mars News

# In[127]:

def scraped_info(): 
   executable_path={'executable_path': 'chromedriver.exe'}
   browser = Browser('chrome', **executable_path, headless=False)

   url = 'https://mars.nasa.gov/news/'
   browser.visit(url)

   html = browser.html
   soup = BeautifulSoup(html, 'html.parser')

   result_slide = soup.select_one('ul.item_list li.slide')
   #print(result_slide)

   news_title = result_slide.find('div', class_='content_title').get_text()


   news_p = result_slide.find('div', class_='article_teaser_body').get_text()
   print(news_title)
   print(news_p)


   # JPL Mars Space Images - Featured Image

   # In[10]:


   executable_path={'executable_path': 'chromedriver.exe'}
   browser = Browser('chrome', **executable_path, headless=False)


   url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
   browser.visit(url2)


   full_image_click = browser.find_by_id('full_image')
   full_image_click.click()


   more_info = browser.is_element_present_by_text('more info', wait_time=10)
   more_info = browser.find_link_by_partial_text('more info')
   more_info.click()


   image_html = browser.html
   image_soup = BeautifulSoup(image_html, 'html.parser')

   featured_image = image_soup.select_one('figure.lede a img').get('src')


   final_featured_image = 'https://www.jpl.nasa.gov' + featured_image
   print(final_featured_image)


   # Mars Weather

   # In[85]:


   executable_path={'executable_path': 'chromedriver.exe'}
   browser = Browser('chrome', **executable_path, headless=False)

   url = 'https://twitter.com/marswxreport'
   browser.visit(url)

   html = browser.html
   soup = BeautifulSoup(html, 'html.parser')

   results = soup.find('div', class_='js-tweet-text-container')
   #print(results)

   mars_weather = results.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
         
   print('mars_weather = ' + mars_weather)


   # Mars Facts

   # In[112]:


   url = 'https://space-facts.com/mars/'


   tables= pd.read_html(url)[1]

   mars2_df= tables


   mars2_df.columns = ['description', 'value']
   mars2_df.set_index('description', inplace = True)
   print(mars2_df)

   html_table = mars2_df.to_html()

   mars_table =html_table.replace('\n', '')
   #print(mars_table)


   #mars_table.to_html('table.html')


   # Mars Hemispheres 

   # In[110]:


   executable_path={'executable_path': 'chromedriver.exe'}
   browser = Browser('chrome', **executable_path, headless=False)




   url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
   browser.visit(url)


   hemispheres_image_urls = []
   links= browser.find_by_css('a.product-item h3')


   for i in range(len(links)):
      hemisphere = {}

      # We have to find the elements on each loop to avoid a stale element exception
      browser.find_by_css("a.product-item h3")[i].click()

      # Next, we find the Sample image anchor tag and extract the href
      sample_element = browser.find_link_by_text('Sample').first
      hemisphere['img_url'] = sample_element['href']

      # Get Hemisphere title
      hemisphere['title'] = browser.find_by_css("h2.title").text

      # Append hemisphere object to list
      hemispheres_image_urls.append(hemisphere)

      # Finally, we navigate backwards
      browser.back()

   print(hemispheres_image_urls)

   result = {
      'news_title': news_title,
      'news_paragraph': news_p,
      'featured_image': final_featured_image,
      'mars_weather' : mars_weather,
      'mars_table': mars_table,
      'mars_hemispheres': hemispheres_image_urls
   }
   print(result)
   return result 


