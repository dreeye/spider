import pymysql

class Common:

    conn = None
    c = None

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='feshare',charset="utf8")
        self.c = self.conn.cursor()

    def insert_movie(self,**parm):
    #    self.__connect()
        try:
            v = ('超能特工队',parm['origin_title'],'movie',parm['year'],parm['photos'][0],parm['summary'])
            #print(v)
            #exit()
            self.c.execute("insert into movie (title,original_title,subtype,year,image,summary) values (%s,%s,%s,%s,%s,%s)", v)
            m_id = self.conn.insert_id()
            for s_aka in parm['aka']:
                fw = (m_id,s_aka)
                self.c.execute("insert into aka (m_id,name) values (%s,%s)", fw)
            for wid in parm['w_id']:
                add_writer_m = (m_id,wid)
                self.c.execute("insert into writers_m (m_id,w_id) values (%s,%s)", add_writer_m)
            for cid in parm['c_id']:
                add_cast_m = (m_id,cid)
                self.c.execute("insert into casts_m (m_id,c_id) values (%s,%s)", add_cast_m)
            for did in parm['d_id']:
                add_director_m = (m_id,did)
                self.c.execute("insert into directors_m (m_id,d_id) values (%s,%s)", add_director_m)
            for url in parm['photos'][1:]:
                add_photos_m = (m_id,url)
                self.c.execute("insert into photos_m (m_id,url) values (%s,%s)", add_photos_m)
            for url in parm['download']:
                add_download_m = (m_id,url)
                self.c.execute("insert into download_m (m_id,url) values (%s,%s)", add_download_m)
            for counid in parm['coun_id']:
                add_countries_m = (m_id,counid)
                self.c.execute("insert into countries_m (m_id,coun_id) values (%s,%s)", add_countries_m)
            self.conn.commit()
        except pymysql.Error as e:
            # Rollback in case there is any error
            self.conn.rollback()
            print('Got error {!r}, errno is {}'.format(e, e.args[0]))
        # 关闭数据库连接
        #self.c.close()
        #self.conn.close()

    def add_writers(self,writers):
        """检查电影编剧是否入库,没有添加,有就返回w_id"""
        #self.__connect()
        w_id = []
        for w in writers:
            try:
                sql_get_wid = "SELECT id FROM writers WHERE name='%s' " % w
                self.c.execute(sql_get_wid)
                data = self.c.fetchone()
                if data:
                    w_id.append(data[0])
                else:
                    sql_add_writer = "INSERT INTO writers (name) values ('%s') " % w  
                    self.c.execute(sql_add_writer)
                    w_id.append(self.conn.insert_id())
                self.conn.commit()
            except pymysql.Error as e:
                self.conn.rollback()
                print('Got error {!r}, errno is {}'.format(e, e.args[0]))
        # 关闭数据库连接
        #self.c.close()
        #self.conn.close()
        return w_id

    def add_casts(self,casts):
        """检查电影编剧是否入库,没有添加,有就返回w_id"""
        #self.__connect()
        c_id = []
        for c in casts:
            try:
                sql_get_cid = "SELECT id FROM casts WHERE name='%s' " % c 
                self.c.execute(sql_get_cid)
                data = self.c.fetchone()
                if data:
                    c_id.append(data[0])
                else:
                    sql_add_casts = "INSERT INTO casts (name) values ('%s') " % c  
                    self.c.execute(sql_add_casts)
                    c_id.append(self.conn.insert_id())
                self.conn.commit()
            except pymysql.Error as e:
                self.conn.rollback()
                print('Got error {!r}, errno is {}'.format(e, e.args[0]))
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
                sql_get_did = "SELECT id FROM directors WHERE name='%s' " % d 
                self.c.execute(sql_get_did)
                data = self.c.fetchone()
                if data:
                    d_id.append(data[0])
                else:
                    sql_add_directors = "INSERT INTO directors (name) values ('%s') " % d  
                    self.c.execute(sql_add_directors)
                    d_id.append(self.conn.insert_id())
                self.conn.commit()
            except pymysql.Error as e:
                self.conn.rollback()
                print('Got error {!r}, errno is {}'.format(e, e.args[0]))
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
                sql_get_counid = "SELECT id FROM countries WHERE name='%s' " % coun 
                self.c.execute(sql_get_counid)
                data = self.c.fetchone()
                if data:
                    coun_id.append(data[0])
                else:
                    sql_countries = "INSERT INTO countries (name) values ('%s') " % coun  
                    self.c.execute(sql_countries)
                    coun_id.append(self.conn.insert_id())
                self.conn.commit()
            except pymysql.Error as e:
                self.conn.rollback()
                print('Got error {!r}, errno is {}'.format(e, e.args[0]))
        # 关闭数据库连接
        #self.c.close()
        #self.conn.close()
        return coun_id
      
    def close_connect(self):         
        self.c.close()
        self.conn.close()
