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
mysqlpass = input('Please input you mysql password :')

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
        href = link.get('href').strip()
        r = requests.get('%s%s%s' % ('http://',from_host,href),headers=headers)
        if r.status_code != 200 :
            print('error status %s' % r.status_code)
        soup = BeautifulSoup(r.content,from_encoding="gbk")
        content = soup.get_text()
        prettify = soup.prettify()
        
        #加载dygod library
        _dygod = dygod.Dygod(content,prettify)
        origin_title = _dygod.get_origin_title()
        year = _dygod.get_year()
        download = _dygod.get_download(title,n)
        photos = _dygod.get_photos()
        subtitle = _dygod.get_subtitle()
        lang = _dygod.get_lang()
        print(title)
        print(origin_title)
        print(year)
        print(download)
        print(photos)
        print(subtitle)
        print(lang)
        print(href)
        #print(durations)
        #exit()
        #添加编剧并获取w_id
        common_mod = Common_mod.Common(mysqlpass)
        insert_data = {'title':title,'origin_title':origin_title,'year':year,'photos':photos,'download':download,'href':href,'from_host':from_host,'subtitle':subtitle,'lang':lang}
        common_mod.insert_movie(**insert_data)
        #time.sleep(5)
    #common_mod.close_connect()
    time.sleep(10)
