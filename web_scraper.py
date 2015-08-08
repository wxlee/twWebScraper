
# coding: utf-8

# In[2]:

##%%timeit
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

keyword = 'apple'

url = 'http://search.ruten.com.tw/search/s000.php?searchfrom=indexbar&k={0}&t=0'.format(keyword)

dcap = dict(DesiredCapabilities.PHANTOMJS)

dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87"
)

browser = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--load-images=no'])
#browser = webdriver.PhantomJS(desired_capabilities=dcap)


browser.get(url)

#print browser.page_source

soup = BeautifulSoup(browser.page_source, "html.parser")

for item in soup.findAll('span', {'class': 'price'}):
    print item

