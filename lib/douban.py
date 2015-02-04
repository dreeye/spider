import requests, re, json
from bs4 import BeautifulSoup

class Douban_api:
    
    def movie_search(start,count,title):
        #print('http://api.douban.com/v2/movie/search?start=%d&count=%d&q=%s' % (start,count,title))
        #exit()
        reponse = requests.get('http://api.douban.com/v2/movie/search?start=%d&count=%d&q=%s' % (start,count,title))
        return json.loads(reponse.text)
