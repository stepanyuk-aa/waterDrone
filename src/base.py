# from multiprocessing import connection
from config import dataBaseConfig
from loguru import logger
import pymysql.cursors

class dataBase():
    def __init__(self):
        config = dataBaseConfig()
        
        self.connection = pymysql.connect(
            host=config.ip,
            user=config.user,
            password=config.password,
            database=config.dbName,
            cursorclass=pymysql.cursors.DictCursor
        ) 

        self.cursor = self.connection.cursor()

    @logger.catch
    def write(self, table, field, data):
        #      INSERT INTO `Dron`.`gps` VALUES ('23423423');
        #      INSERT INTO Product VALUES ('B', 1157, 'PC');
        sql = 'INSERT INTO `Dron`.`{0}` (`{1}`) VALUES ("{2}");'.format(table,field,data)
        self.cursor.execute(sql)
        self.connection.commit()

    # @logger.catch
    def read(self, table):
        sql = "SELECT * FROM {0}".format(table)
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        print(rows)

class base():
    def __init__(self):
        print("Hello, it's base!")
        self.logger = logger
# db = dataBase()
# db.write(table="GPS", field="coordinates", data="Hello")
# db.read()