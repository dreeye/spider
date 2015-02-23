#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

#from bs4 import BeautifulSoup
#from lib.douban import Douban_api as doulib
import requests, re, json, time


headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip',
'Connection':'close',
'Referer':None #注意如果依然不能抓取的话，这里可以设置抓取网站的host
}
search_dic = {'count': 2, 'start': 0, 'subjects': [{'images': {'medium': 'http://img5.douban.com/view/movie_poster_cover/spst/public/p1910917507.jpg', 'large': 'http://img5.douban.com/view/movie_poster_cover/lpst/public/p1910917507.jpg', 'small': 'http://img5.douban.com/view/movie_poster_cover/ipst/public/p1910917507.jpg'}, 'directors': [{'avatars': {'medium': 'http://img5.douban.com/img/celebrity/medium/42527.jpg', 'large': 'http://img5.douban.com/img/celebrity/large/42527.jpg', 'small': 'http://img5.douban.com/img/celebrity/small/42527.jpg'}, 'alt': 'http://movie.douban.com/celebrity/1056047/', 'id': '1056047', 'name': '让-雅克·阿诺'}], 'id': '1291868', 'collect_count': 94268, 'subtype': 'movie', 'year': '1992', 'original_title': "L'amant", 'casts': [{'avatars': {'medium': 'http://img5.douban.com/img/celebrity/medium/47857.jpg', 'large': 'http://img5.douban.com/img/celebrity/large/47857.jpg', 'small': 'http://img5.douban.com/img/celebrity/small/47857.jpg'}, 'alt': 'http://movie.douban.com/celebrity/1031995/', 'id': '1031995', 'name': '珍·玛奇'}, {'avatars': {'medium': 'http://img5.douban.com/img/celebrity/medium/746.jpg', 'large': 'http://img5.douban.com/img/celebrity/large/746.jpg', 'small': 'http://img5.douban.com/img/celebrity/small/746.jpg'}, 'alt': 'http://movie.douban.com/celebrity/1118167/', 'id': '1118167', 'name': '梁家辉'}, {'avatars': {'medium': 'http://img3.douban.com/img/celebrity/medium/49590.jpg', 'large': 'http://img3.douban.com/img/celebrity/large/49590.jpg', 'small': 'http://img3.douban.com/img/celebrity/small/49590.jpg'}, 'alt': 'http://movie.douban.com/celebrity/1099447/', 'id': '1099447', 'name': 'Arnaud Giovaninetti'}], 'alt': 'http://movie.douban.com/subject/1291868/', 'title': '情人', 'genres': ['传记', '剧情', '爱情'], 'rating': {'min': 0, 'average': 8, 'max': 10, 'stars': '40'}}, {'images': {'medium': 'http://img3.douban.com/mpic/s3697190.jpg', 'large': 'http://img3.douban.com/lpic/s3697190.jpg', 'small': 'http://img3.douban.com/spic/s3697190.jpg'}, 'directors': [{'avatars': None, 'alt': None, 'id': None, 'name': 'Peter Hoar'}], 'id': '2373118', 'collect_count': 1465, 'subtype': 'tv', 'year': '2008', 'original_title': 'Mistresses', 'casts': [{'avatars': None, 'alt': None, 'id': None, 'name': 'Sarah Parish'}, {'avatars': None, 'alt': None, 'id': None, 'name': 'Shelley Conn'}, {'avatars': None, 'alt': None, 'id': None, 'name': 'Sharon Small'}], 'alt': 'http://movie.douban.com/subject/2373118/', 'title': '情人 第一季', 'genres': ['剧情'], 'rating': {'min': 0, 'average': 8.1, 'max': 10, 'stars': '40'}}], 'title': '搜索 "情人" 的结果', 'total': 541}
#q = '情人'
#count = 2

def search(q,count):

    #apikey = '09ceb279878b4ac71d6c176c96a1e055'
    #from_host = 'api.douban.com'
    #search_url = '/v2/movie/search?q='

    #r = requests.get('%s%s%s%s%s%s%s%s' % ('http://',from_host,search_url,q,'&count=',count,'&apikey=',apikey),headers=headers)
    #if r.status_code != 200 :
    #    print('requests is error status code is %s' % r.status_code)
    #    return False

    #response = r.text
    #test data 
    #search_dic = json.loads(response)
    #print(search_dic)
    #exit()
    if search_dic['subjects']:
        for x in search_dic['subjects']:
            #print(x['year'])
            return True
    else:
        print('search data was error,response is %s' % response)
        return False



if __name__ == '__main__':
    #n = 1
    #while n < 20:
    search('情人','2')
    #time.sleep(60)
    #n = n+1
    #exit()
