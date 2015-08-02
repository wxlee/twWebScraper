
# coding: utf-8

# In[8]:

import requests

url = ''


def web_request(url):
    # Set header
    hder = {
         'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
         'referer': url
         }

    # set session
    s = requests.Session()
    
    s.get(url, headers=hder)
    
    r = s.get(url, headers=hder)
    
    # print Server response headers
    #print r.headers
    
    # print Client request headers
    #print r.request.headers
    
    return r


res = web_request(url)

print res.content


