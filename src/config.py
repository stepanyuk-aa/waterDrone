# Request library
# loguru
# pymysql
# flask
# ESC

class dataBaseConfig():
    def __init__(self):
        self.ip = "localhost"
        self.user = "admin"
        self.password = "123456"
        self.dbName = "Dron"

class ESC_config():
    def __init__(self):
        self.SAMPLE_TIME = 2.0
        self.ESC_GPIO = 17

class Frontend_config():
    def __init__(self):
        self.ip = "192.168.208.128"
        self.port = "5001"
        self.socket = self.ip + ":" + self.port
        self.service_name = "dron_frontend"
        self.path_link = "/etc/systemd/system"
        self.path_service = "/opt/waterDrone/src/modules/services"

