import requests
from bs4 import BeautifulSoup
from lib.common import Comm
from lib import dygod



#send request and get page Dom 
#r = requests.get('http://www.dy2018.com/i/94539.html')
r = requests.get('http://www.dy2018.com/i/94450.html')
soup = BeautifulSoup(r.content)
content = soup.get_text()
prettify = soup.prettify()

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
exit()

#for introd in soup.find_all("p",text=re.compile("◎")):
#    into = introd.get_text()
#    text = Comm.replace(into,('\u3000','\xa0',' ','◎'),'')
#    print(text[0:2])
    #exit()
