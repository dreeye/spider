import re
from lib.common import Comm

class Dygod:
    
    source = None
    prettify = None
    aka = None
    origin_title = None
    genres = ['喜剧','动作','爱情','科幻','动画','悬疑','惊悚','恐怖','纪录片','剧情','传记','历史','战争','犯罪','奇幻','冒险','灾难','武侠','古装','音乐']

    def __init__(self,content,prettify):
        #去掉中文unicode特殊字符,如空格,可以使用str.split(' ')查看特殊字符
        #把所有换行符\n替换成'|',统一成同一行
        content = Comm.replace(content,('\u3000','\xa0'),'')
        content = Comm.replace(content,('\n'),'/')
        self.source = content
        self.prettify = prettify

    def get_origin_title(self):
        return self.__init_title('origin_title')

    def get_aka(self):
        return self.__init_title('aka')

    def __init_title(self, type):
        """处理页面的两种片名,以列表长度,是否英文为基准"""

        if re.findall("◎片名(.*?)◎",self.source): 
            t1 = re.findall("◎片名(.*?)◎",self.source)[0].strip('/').split('/')
        else:
            t1 = None

        if re.findall("◎又名(.*?)◎",self.source):
            t2 = re.findall("◎又名(.*?)◎",self.source)[0].strip('/').split('/')
        else:
            t2 = None

        if re.findall("◎译名(.*?)◎",self.source):
            t3 =  re.findall("◎译名(.*?)◎",self.source)[0].strip('/').split('/')
        else:
            t3 = None

        title = [t1,t2,t3]  
        for x in title:
            if x != None:
                if len(x)>1 :
                    self.aka = x 
                elif len(x) ==1 and Comm.is_alphabet(x[0]):
                    self.origin_title = x
                else:
                    self.origin_title = x
            else:
                continue

        if(type == 'aka'):
            return self.aka
        elif(type == 'origin_title'): 
            return self.origin_title 
        else:
            print('title type was error')
            exit()

    def get_directors(self):
        """查找导演"""
        return re.findall("◎导演(.*?)◎",self.source)[0].strip('/').split('/') 

    def get_writers(self):
        """查找编剧"""
        is_exit =  re.findall("◎编剧(.*?)◎",self.source)
        if is_exit :
            return re.findall("◎编剧(.*?)◎",self.source)[0].strip('/') 
        else:
            return '' 

    def get_casts(self):
        """查找演员"""
        if re.findall("◎演员(.*?)◎",self.source) : 
            return re.findall("◎演员(.*?)◎",self.source)[0].strip('/').split('/')
        elif re.findall("◎主演(.*?)◎",self.source) : 
            return re.findall("◎主演(.*?)◎",self.source)[0].strip('/').split('/')
        else:
            return ''

    def get_summary(self):
        """查找简介"""
        is_exit = re.findall("◎简介(.*?)◎",self.source)
        if is_exit :
            return re.findall("◎简介(.*?)◎",self.source)[0].strip('/')
        else:
            return ''

    def get_year(self):
        """查找年代""" 
        is_exit =  re.findall("◎年代(.*?)◎",self.source)
        if is_exit :
            return re.findall("◎年代(.*?)◎",self.source)[0].strip('/') 
        else:
            return '' 

    def get_countries(self):
        """查找制片国家""" 
        is_exit =  re.findall("◎国家(.*?)◎",self.source)
        if is_exit :
            return re.findall("◎国家(.*?)◎",self.source)[0].strip('/').split('/') 
        else:
            return '' 
     
    def get_genres_index(self):
        """查找影片类型""" 
        if re.findall("◎类别(.*?)◎",self.source):
            genres =  re.findall("◎类别(.*?)◎",self.source)[0].strip('/').strip(' ').split('/') 
        elif re.findall("◎电影类型(.*?)◎",self.source):
            genres =  re.findall("◎电影类型(.*?)◎",self.source)[0].strip('/').strip(' ').split('/') 
        else:
            return '' 
        #print(genres)
        #exit() 
        gindex = [] 
        for x in genres:
            gindex.append(self.genres.index(x)) 
        return gindex

    def get_download(self):
        """查找下载链接"""
 #       print(self.prettify)
#        exit() 
        ftp =  re.findall("(ftp:.*?///)",self.source)
        if len(ftp) > 1:
            link = []
            for x in ftp:
                a = x.strip('/')
                link.append(a)
        else:
           link = ftp[0].strip('/')  
        return link
