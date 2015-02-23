import requests, pymysql, re
from bs4 import BeautifulSoup
from lib.common import Comm
from lib import dygod
from model import Common_mod

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip',
'Connection':'close',
'Referer':None #注意如果依然不能抓取的话，这里可以设置抓取网站的host
}
from_host = 'www.dy2018.com'
href = '/html/gndy/dyzz/20070812/4789.html'
title = '圣人文森特'
r = requests.get('%s%s%s' % ('http://',from_host,href),headers=headers)
soup = BeautifulSoup(r.content,from_encoding="gbk")
#print(soup)
#exit()
content = soup.get_text()
prettify = soup.prettify()

#加载dygod library
_dygod = dygod.Dygod(content,prettify)
#exit()
aka = _dygod.get_aka(title)
origin_title = _dygod.get_origin_title()
directors = _dygod.get_directors()
writers = _dygod.get_writers()
casts = _dygod.get_casts()
summary = _dygod.get_summary()
genres = _dygod.get_genres()
countries = _dygod.get_countries()
year = _dygod.get_year()
download = _dygod.get_download(title,1)
photos = _dygod.get_photos()
subtitle = _dygod.get_subtitle()
lang = _dygod.get_lang()
durations = _dygod.get_durations()
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
print(subtitle)
print(lang)
print(durations)

exit()
#添加编剧并获取w_id
common_mod = Common_mod.Common()
w_id = common_mod.add_writers(writers)
c_id = common_mod.add_casts(casts)
d_id = common_mod.add_directors(directors)
coun_id = common_mod.add_countries(countries)
g_id = common_mod.add_genres(genres)

#print(g_id)
#exit()
insert_data = {'title':title,'origin_title':origin_title,'year':year,'photos':photos,'aka':aka,'writers':writers,'w_id':w_id,'c_id':c_id,'summary':summary,'d_id':d_id,'countries':countries,'download':download,'href':href,'from_host':from_host,'coun_id':coun_id,'g_id':g_id,'durations':durations,'subtitle':subtitle,'lang':lang}
common_mod.insert_movie(**insert_data)
