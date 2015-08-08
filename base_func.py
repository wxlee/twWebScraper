
# coding: utf-8

# In[11]:

import requests

from bs4 import BeautifulSoup

#url = 'https://tw.search.buy.yahoo.com/search/shopping/product?p=windows+10&qt=product&cid=0&clv=0'
url = 'https://tw.taobao.com/search/search.htm?_ksTS=1438526274940_101&spm=a213z.1224559.20141209.1&_input_charset=utf-8&navigator=all&json=on&q=%E5%8C%85%E5%8C%85&callback=__jsonp_cb&cna=XmXODdjnLBUCAQEio4ygSxSY&abtest=_AB-LR492-LR501-LR517-PR492-PR501-PR517'

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

r = web_request(url)
r.encoding = r.apparent_encoding
print r.text

soup = BeautifulSoup(r.text, "html.parser")

for item in soup.select('.info'):
    print item.select('strong')

