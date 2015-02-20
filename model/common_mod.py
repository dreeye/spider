import pymysql

class Common:

    conn = None
    c = None

#    def __init__(self):
 #       self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='feshare',charset="utf8")
  #      self.c = self.conn.cursor()

    def insert_movie(self,**parm):
        self.__connect()
        try:
            v = ('超能特工队',parm['origin_title'],'movie',parm['year'],parm['photos'][0])
            #print(v)
            #exit()
            self.c.execute("insert into movie (title,original_title,subtype,year,image) values (%s,%s,%s,%s,%s)", v)
            m_id = self.conn.insert_id()
            for s_aka in parm['aka']:
                fw = (m_id,s_aka)
                self.c.execute("insert into aka (m_id,name) values (%s,%s)", fw)
            for wid in parm['w_id']:
                add_writer_m = (m_id,wid)
                self.c.execute("insert into writers_m (m_id,w_id) values (%s,%s)", add_writer_m)
            self.conn.commit()
        except pymysql.Error as e:
            # Rollback in case there is any error
            self.conn.rollback()
            print('Got error {!r}, errno is {}'.format(e, e.args[0]))
        # 关闭数据库连接
        self.c.close()
        self.conn.close()

    def add_writers(self,writers):
        """检查电影编剧是否入库,没有添加,有就返回w_id"""
        self.__connect()
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
        self.c.close()
        self.conn.close()
        return w_id
      
    def __connect(self):         
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='feshare',charset="utf8")
        self.c = self.conn.cursor()
