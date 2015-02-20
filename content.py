import requests,pymysql
from bs4 import BeautifulSoup
from lib.common import Comm
from lib import dygod
from model import common_mod


#send request and get page Dom 
r = requests.get('http://www.dy2018.com/i/94539.html')
#r = requests.get('http://www.dy2018.com/i/94450.html')
soup = BeautifulSoup(r.content)
content = soup.get_text()
prettify = soup.prettify()
#print(prettify)
#exit()
#加载dygod library
dygod = dygod.Dygod(content,prettify)
aka = dygod.get_aka()
origin_title = dygod.get_origin_title()
directors = dygod.get_directors()
writers = dygod.get_writers()
casts = dygod.get_casts()
summary = dygod.get_summary()
genres = dygod.get_genres_index()
countries = dygod.get_countries()
year = dygod.get_year()
download = dygod.get_download()
photos = dygod.get_photos()
print(aka)
print(origin_title)
print(writers)
print(casts)
print(summary)
print(directors)
print(genres)
print(countries)
print(year)
print(download)
print(photos)

#添加编剧并获取w_id
common_mod = common_mod.Common()
w_id = common_mod.add_writers(writers)
#print(w_id)
#exit()
insert_data = {'origin_title':origin_title,'year':year,'photos':photos,'aka':aka,'writers':writers,'w_id':w_id}
common_mod.insert_movie(**insert_data)

#for introd in soup.find_all("p",text=re.compile("◎")):
#    into = introd.get_text()
#    text = Comm.replace(into,('\u3000','\xa0',' ','◎'),'')
#    print(text[0:2])
    #exit()
