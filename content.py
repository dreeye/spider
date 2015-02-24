import requests, pymysql, re, time
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
'Referer':'http://www.dy2018.com/' #注意如果依然不能抓取的话，这里可以设置抓取网站的host
}
#test = '<a class="ulink" href="/html/gndy/jddy/20120508/37683.html" title="1024分辨率《全球热恋》HD国语中字">1024分辨率《全球热恋》HD国语中字</a>'
#title = re.findall('《(.*)》',test.get('title'))[0].strip()
#print(title) 


from_host = 'www.dy2018.com'
genres = 0 
n = 1 
while n <= 50:
    if n == 1:
        r = requests.get('%s%s/%s/' % ('http://',from_host,genres),headers=headers)
    else:
        r = requests.get('%s%s/%s/index_%s.html' % ('http://',from_host,genres,n),headers=headers)
   #     print(r)
    #    exit()
    n = n+1
    if r.status_code != 200 :
        print('all page was finished')
        exit()
    soup = BeautifulSoup(r.content,from_encoding="gbk")
    #获得所有class为unlink并且有title属性的a标签,并遍历
    page_list = soup.find_all('a', attrs={'class':'ulink','title':True})
    for link in page_list:
        title = re.findall('《(.*)》',link.get('title'))
        title = ''.join(title) 
        print(title) 
    #exit()
    for link in page_list:
        title_re = re.findall('《(.*)》',link.get('title'))
        title = ''.join(title_re).strip()
        if title == '':
            continue 
        title_list = title.split('/')
        if len(title_list) > 1:
            title = title_list[0]
        #print(title)
        #exit()
        href = link.get('href').strip()
        #print(title)
        #print(href)
        #print(r.encoding.lower())
        #exit()
        r = requests.get('%s%s%s' % ('http://',from_host,href),headers=headers)
        if r.status_code != 200 :
            print('error status %s' % r.status_code)
        soup = BeautifulSoup(r.content,from_encoding="gbk")
        #print(soup)
        #exit()
        content = soup.get_text()
        prettify = soup.prettify()
        
        #加载dygod library
        _dygod = dygod.Dygod(content,prettify)
        #exit()
        #aka = _dygod.get_aka(title)
        origin_title = _dygod.get_origin_title()
        #directors = _dygod.get_directors()
        #writers = _dygod.get_writers()
        #casts = _dygod.get_casts()
        #summary = _dygod.get_summary()
        #genres = _dygod.get_genres()
        #countries = _dygod.get_countries()
        year = _dygod.get_year()
        download = _dygod.get_download(title,n)
        photos = _dygod.get_photos()
        subtitle = _dygod.get_subtitle()
        lang = _dygod.get_lang()
        #durations = _dygod.get_durations()
        #print(aka)
        print(title)
        print(origin_title)
        #print(writers)
        #print(casts)
        #print(summary)
        #print(directors)
        #print(genres)
        #print(countries)
        print(year)
        print(download)
        print(photos)
        print(subtitle)
        print(lang)
        print(href)
        #print(durations)
        #exit()
        #添加编剧并获取w_id
        common_mod = Common_mod.Common()
        #w_id = common_mod.add_writers(writers)
        #c_id = common_mod.add_casts(casts)
        #d_id = common_mod.add_directors(directors)
        #coun_id = common_mod.add_countries(countries)
        #g_id = common_mod.add_genres(genres)

        #print(g_id)
        #exit()
        #insert_data = {'title':title,'origin_title':origin_title,'year':year,'photos':photos,'aka':aka,'writers':writers,'w_id':w_id,'c_id':c_id,'summary':summary,'d_id':d_id,'countries':countries,'download':download,'href':href,'from_host':from_host,'coun_id':coun_id,'g_id':g_id,'durations':durations,'subtitle':subtitle,'lang':lang}
        insert_data = {'title':title,'origin_title':origin_title,'year':year,'photos':photos,'download':download,'href':href,'from_host':from_host,'subtitle':subtitle,'lang':lang}
        common_mod.insert_movie(**insert_data)
        #time.sleep(5)
    #common_mod.close_connect()
    time.sleep(10)
