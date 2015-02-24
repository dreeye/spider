import pymysql
from lib.common import Comm

class Common:

    conn = None
    c = None

    def __init__(self,password):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd=password, db='feshare',charset="utf8")
        self.c = self.conn.cursor()

    def insert_movie(self,**parm):
    #    self.__connect()
        try:
            v = (parm['title'],parm['origin_title'],'movie',parm['year'])
            #print(v)
            #exit()
            self.c.execute("insert into movie (title,original_title,subtype,year) values (%s,%s,%s,%s)", v)
            m_id = self.conn.insert_id()
#            if parm['aka']:
#                for s_aka in parm['aka']:
#                    fw = (m_id,s_aka.strip())
#                    self.c.execute("insert into aka (m_id,name) values (%s,%s)", fw)
#            if parm['w_id']:
#                for wid in parm['w_id']:
#                    add_writer_m = (m_id,wid)
#                    self.c.execute("insert into writers_m (m_id,w_id) values (%s,%s)", add_writer_m)
#            if parm['c_id']:
#                for cid in parm['c_id']:
#                    add_cast_m = (m_id,cid)
#                    self.c.execute("insert into casts_m (m_id,c_id) values (%s,%s)", add_cast_m)
#            if parm['d_id']:
#                for did in parm['d_id']:
#                    add_director_m = (m_id,did)
#                    self.c.execute("insert into directors_m (m_id,d_id) values (%s,%s)", add_director_m)
            if parm['photos'][1:]:
                for url in parm['photos'][1:]:
                    add_photos_m = (m_id,url)
                    self.c.execute("insert into screenshot (m_id,url) values (%s,%s)", add_photos_m)
            if parm['download']:
                for url in parm['download']:
                    add_download_m = (m_id,url,parm['from_host'],parm['href'],parm['subtitle'],parm['lang'])
                    self.c.execute("insert into download (m_id,url,from_host,href,subtitle,lang) values (%s,%s,%s,%s,%s,%s)", add_download_m)
#            if parm['coun_id']:
#                for counid in parm['coun_id']:
#                    add_countries_m = (m_id,counid)
#                    self.c.execute("insert into countries_m (m_id,coun_id) values (%s,%s)", add_countries_m)
#            if parm['g_id']:
#                for gid in parm['g_id']:
#                    add_genres_m = (m_id,gid)
#                    self.c.execute("insert into genres_m (m_id,g_id) values (%s,%s)", add_genres_m)
            self.conn.commit()
        except pymysql.Error as e:
            # Rollback in case there is any error
            self.conn.rollback()
            print('Insert Movies Got error {!r}, errno is {}'.format(e, e.args[0]))
            self.close_connect()
            exit()
        # 关闭数据库连接
        #self.c.close()
        #self.conn.close()

    def add_writers(self,writers):
        """检查电影编剧是否入库,没有添加,有就返回w_id"""
        #self.__connect()
        w_id = []
        for w in writers:
            try:
                sql_get_wid = "SELECT id FROM writers WHERE name='%s' " % w.strip()
                self.c.execute(sql_get_wid)
                data = self.c.fetchone()
                if data:
                    w_id.append(data[0])
                else:
                    sql_add_writer = "INSERT INTO writers (name) values ('%s') " % w.strip()  
                    self.c.execute(sql_add_writer)
                    w_id.append(self.conn.insert_id())
                self.conn.commit()
            except pymysql.Error as e:
                self.conn.rollback()
                print('Add writers Got error {!r}, errno is {}'.format(e, e.args[0]))
                self.close_connect()
                exit()
        # 关闭数据库连接
        #self.c.close()
        #self.conn.close()
        return w_id

    def add_casts(self,casts):
        """检查电影编剧是否入库,没有添加,有就返回w_id"""
        #self.__connect()
        c_id = []
        for c in casts:
            #casts_escape = pymysql.escape_string(c)
            try:
                sql_get_cid = "SELECT id FROM casts WHERE name='%s' " % c.strip() 
                self.c.execute(sql_get_cid)
                data = self.c.fetchone()
                if data:
                    c_id.append(data[0])
                else:
                    #print(casts_escape)
                    #exit()
                    sql_add_casts = "INSERT INTO casts (name) values (%s)" 
                    self.c.execute(sql_add_casts,(c.strip()))
                    c_id.append(self.conn.insert_id())
                self.conn.commit()
            except pymysql.Error as e:
                self.conn.rollback()
                print('Add casts Got error {!r}, errno is {}'.format(e, e.args[0]))
                self.close_connect()
                exit()
        # 关闭数据库连接
        #self.c.close()
        #self.conn.close()
        return c_id

    def add_directors(self,directors):
        """检查电影编剧是否入库,没有添加,有就返回w_id"""
        #self.__connect()
        d_id = []
        for d in directors:
            try:
                sql_get_did = "SELECT id FROM directors WHERE name='%s' " % d.strip() 
                self.c.execute(sql_get_did)
                data = self.c.fetchone()
                if data:
                    d_id.append(data[0])
                else:
                    sql_add_directors = "INSERT INTO directors (name) values ('%s') " % d.strip()  
                    self.c.execute(sql_add_directors)
                    d_id.append(self.conn.insert_id())
                self.conn.commit()
            except pymysql.Error as e:
                self.conn.rollback()
                print('Add directors Got error {!r}, errno is {}'.format(e, e.args[0]))
                self.close_connect()
                exit()
        # 关闭数据库连接
        #self.c.close()
        #self.conn.close()
        return d_id

    def add_countries(self,countries):
        """检查电影编剧是否入库,没有添加,有就返回w_id"""
        #self.__connect()
        coun_id = []
        for coun in countries:
            try:
                sql_get_counid = "SELECT id FROM countries WHERE name='%s' " % coun.strip() 
                self.c.execute(sql_get_counid)
                data = self.c.fetchone()
                if data:
                    coun_id.append(data[0])
                else:
                    sql_countries = "INSERT INTO countries (name) values ('%s') " % coun.strip()  
                    self.c.execute(sql_countries)
                    coun_id.append(self.conn.insert_id())
                self.conn.commit()
            except pymysql.Error as e:
                self.conn.rollback()
                print('Add countries Got error {!r}, errno is {}'.format(e, e.args[0]))
                self.close_connect()
                exit()
        # 关闭数据库连接
        #self.c.close()
        #self.conn.close()
        return coun_id

    def add_genres(self,genres):
        """检查电影编剧是否入库,没有添加,有就返回w_id"""
        #self.__connect()
        g_id = []
        for coun in genres:
            try:
                sql_get_gid = "SELECT id FROM genres WHERE name='%s' " % coun.strip() 
                self.c.execute(sql_get_gid)
                data = self.c.fetchone()
                if data:
                    g_id.append(data[0])
                else:
                    sql_genres = "INSERT INTO genres (name) values ('%s') " % coun.strip()  
                    self.c.execute(sql_genres)
                    g_id.append(self.conn.insert_id())
                self.conn.commit()
            except pymysql.Error as e:
                self.conn.rollback()
                print('Add genres Got error {!r}, errno is {}'.format(e, e.args[0]))
                self.close_connect()
                exit()
        # 关闭数据库连接
        #self.c.close()
        #self.conn.close()
        return g_id
      
    def close_connect(self):         
        self.c.close()
        self.conn.close()
