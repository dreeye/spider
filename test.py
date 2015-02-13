#from tornado.ioloop import IOLoop
#from tornado import gen
import tormysql

pool = tormysql.ConnectionPool(
    max_connections = 20,
    host = "127.0.0.1",
    user = "root",
    passwd = "",
    db = "test",
    charset = "utf8"
)
conn = pool.Connection()
cursor = conn.cursor()
print(cursor)
exit()
cursor.execute("SELECT * FROM ww")
datas = cursor.fetchall()
cursor.close()
conn.close()
print(datas)

#@gen.coroutine
def connect():
    conn = yield pool.Connection()
    cursor = conn.cursor()
    yield cursor.execute("SELECT * FROM ww")
    datas = cursor.fetchall()
    yield cursor.close()
    conn.close()

    print(datas)
def start():
    connect()

connect()
#ioloop = IOLoop.instance()
#ioloop.add_callback(start)
#ioloop.start()
