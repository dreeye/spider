#from lib.douban import Douban_api
import requests, re
from bs4 import BeautifulSoup
from lib.common import Comm

#send request and get page Dom 
r = requests.get('http://www.dy2018.com/i/94539.html')
soup = BeautifulSoup(r.content)
content = soup.get_text()

#去掉中文unicode特殊字符,如空格,可以使用str.split(' ')查看特殊字符
#把所有换行符\n替换成'|',统一成同一行
content = Comm.replace(content,('\u3000','\xa0',' '),'')
content = Comm.replace(content,('\n'),'/')

#Get all message in movie content
title = re.findall("◎剧名(.*?)◎",content)[0].strip('/').split('/') 
directors = re.findall("◎导演(.*?)◎",content)[0].strip('/').split('/') 
print(directors)
exit()
writers = re.findall("◎编剧(.*?)◎",content)[0].strip('/') 
casts = re.findall("◎演员(.*?)◎",content)[0].strip('/') 
summary = re.findall("◎简介(.*?)◎",content)[0].strip('/') 
#for introd in soup.find_all("p",text=re.compile("◎")):
#    into = introd.get_text()
#    text = Comm.replace(into,('\u3000','\xa0',' ','◎'),'')
#    print(text[0:2])
    #exit()
