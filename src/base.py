# from multiprocessing import connection
import pymysql.cursors

class dataBase():
    def __init__(self, config):
        self.config = config
        
    def db_connect(self):
        self.connection = pymysql.connect(
            host=self.config.ip,
            user=self.config.user,
            password=self.config.password,
            database=self.config.dbName,
            cursorclass=pymysql.cursors.DictCursor
        ) 

        self.cursor = self.connection.cursor()

    def write(self, table, field, data):
        #      INSERT INTO `Dron`.`gps` VALUES ('23423423');
        #      INSERT INTO Product VALUES ('B', 1157, 'PC');
        sql = 'INSERT INTO `Dron`.`{0}` (`{1}`) VALUES ("{2}");'.format(table,field,data)
        self.db_connect()
        self.cursor.execute(sql)
        self.connection.commit()
        self.cursor.close()

    def read(self, table):
        sql = "SELECT * FROM {0}".format(table)

        self.db_connect()
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        self.cursor.close()

        return rows

    def read_last(self, table, count = 0):
        self.db_connect()

        sql = f"SELECT MAX(ID)  FROM {table}"
        self.cursor.execute(sql)
        max_id = self.cursor.fetchall()[0]['MAX(ID)']

        if count == 0:
            sql = f"SELECT * FROM {table} WHERE ID = ({max_id})"
        else:
            max_id = str(int(max_id) - count)
            sql = f"SELECT * FROM {table} WHERE ID > ({max_id})"

        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        self.cursor.close()

        return rows

class base():
    def __init__(self):
        print("Hello, it's base!")
        self.logger = logger


##################################################################
# from config import dataBaseConfig
# db = dataBase(dataBaseConfig())
# db.write(table="GPS", field="coordinates", data="Hello")
# data = db.read("GPS", 5)

