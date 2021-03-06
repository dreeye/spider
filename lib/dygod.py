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

    def get_aka(self,title):
        return self.__init_title('aka',title)

    def __init_title(self, type,title=None):
        """处理页面的两种片名,以列表长度,是否英文为基准"""

        if re.findall("◎片名(.*?)◎",self.source): 
            t1 = re.findall("◎片名(.*?)◎",self.source)[0].strip(' ').strip('/').split('/')
        else:
            t1 = None

        if re.findall("◎又名(.*?)◎",self.source):
            t2 = re.findall("◎又名(.*?)◎",self.source)[0].strip(' ').strip('/').split('/')
        else:
            t2 = None

        if re.findall("◎译名(.*?)◎",self.source):
            t3 = re.findall("◎译名(.*?)◎",self.source)[0].strip(' ').strip('/').split('/')
        else:
            t3 = None

        source = [t1,t2,t3]  
        for x in source:
            if x != None:
                if len(x)>1 :
                    #又名有时会跟title重复
                    try:
                        x.remove(title)
                    except:
                        pass
                    self.aka = x 
                elif len(x) ==1 and Comm.is_alphabet(x[0]):
                    self.origin_title = x[0]
                else:
                    self.origin_title = x[0]
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
        return re.findall("◎导演(.*?)◎",self.source)[0].strip(' ').strip('/').split('/') 

    def get_writers(self):
        """查找编剧"""
        is_exit =  re.findall("◎编剧(.*?)◎",self.source)
        if is_exit :
            return re.findall("◎编剧(.*?)◎",self.source)[0].strip(' ').strip('/').strip(' ').split('/')
        else:
            return '' 

    def get_casts(self):
        """查找演员"""
        if re.findall("◎演员(.*?)◎",self.source) : 
            return re.findall("◎演员(.*?)◎",self.source)[0].strip('/').strip(' ').replace("'","\\'").split('/')
        elif re.findall("◎主演(.*?)◎",self.source) : 
            return re.findall("◎主演(.*?)◎",self.source)[0].strip('/').strip(' ').replace("'","\\'").split('/')
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
            return re.findall("◎年代(.*?)◎",self.source)[0].strip(' ').strip('/') 
        else:
            return '' 
    def get_durations(self):
        """查找片长""" 
        is_exit =  re.findall("◎片长(.*?)◎",self.source)
        if is_exit :
            return re.findall("◎片长(.*?)◎",self.source)[0].strip(' ').strip('/') 
        else:
            return '' 
    def get_lang(self):
        """查找语言""" 
        is_exit =  re.findall("◎语言(.*?)◎",self.source)
        if is_exit :
            return re.findall("◎语言(.*?)◎",self.source)[0].strip(' ').strip('/') 
        else:
            return '' 
    def get_subtitle(self):
        """查找字幕""" 
        is_exit =  re.findall("◎字幕(.*?)◎",self.source)
        if is_exit :
            return re.findall("◎字幕(.*?)◎",self.source)[0].strip(' ').strip('/') 
        else:
            return '' 

    def get_countries(self):
        """查找制片国家""" 
        is_exit =  re.findall("◎国家(.*?)◎",self.source)
        if is_exit :
            return re.findall("◎国家(.*?)◎",self.source)[0].strip(' ').strip('/').split('/') 
        else:
            return '' 
     
    def get_genres(self):
        """查找影片类型""" 
        if re.findall("◎类别(.*?)◎",self.source):
            genres =  re.findall("◎类别(.*?)◎",self.source)[0].strip('/').strip(' ').split('/') 
        elif re.findall("◎电影类型(.*?)◎",self.source):
            genres =  re.findall("◎电影类型(.*?)◎",self.source)[0].strip('/').strip(' ').split('/') 
        else:
            return '' 
        #print(genres)
        #exit() 
        #gindex = [] 
        #for x in genres:
        #    gindex.append(self.genres.index(x)) 
        return genres

    def get_download(self,title,n):
        """查找下载链接"""
 #       print(self.prettify)
#        exit() 
        ftp =  re.findall("(ftp:.*?///)",self.source)
        thun =  re.findall("(thunder:.*?///)",self.source)
        link = []
        print(title)
        print(n)
        if ftp:
            if len(ftp) > 1:
                for x in ftp:
                    a = x.strip('/')
                    link.append(a)
            else:
                url = ftp[0].strip('/') 
                link.append(url)
        if thun:
            if len(thun) > 1:
                for x in thun:
                    a = x.strip('/')
                    link.append(a)
            else:
                url = thun[0].strip('/') 
                link.append(url)
        #print(link)
        #exit()
        return link

    def get_photos(self):
        """海报,截图"""
        return re.findall("src=\"(.*.jpg)",self.prettify)
    
        
