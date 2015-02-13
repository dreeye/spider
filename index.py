from bs4 import BeautifulSoup
#from lib.douban import Douban_api as doulib
import requests, re


r = requests.get('http://www.dy2018.com/1/')
soup = BeautifulSoup(r.content)




#获得所有class为unlink并且有title属性的a标签,并遍历
for link in soup.find_all('a', attrs={'class':'ulink','title':True}):
    title = re.findall('《(.*)》',link.get('title'))
    href = link.get('href')
    source = {'title':title[0],'href':href}
    #repo = doulib.movie_search(start=0,count=1,title=title[0])
#    print(repo)
 #   exit()
print(source)


