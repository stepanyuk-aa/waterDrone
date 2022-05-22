# Request library
# loguru pymysql flask RPi.GPIO pigpio

class dataBaseConfig():
    def __init__(self):
        self.ip = "localhost"
        self.user = "admin"
        self.password = "123456"
        self.dbName = "Dron"

class ESC_default():
    def __init__(self):
        self.SAMPLE_TIME = 2.0
        self.min = 700
        self.max = 2000

class ESC_config1(ESC_default):
    def __init__(self):
        super().__init__()
        self.ESC_GPIO = 17

# class ESC_config2(ESC_default):
#     def __init__(self):
#         self.ESC_GPIO = 27

class Servo_config():
    def __init__(self):
        super().__init__()
        self.GPIO = 27
        

class Backend_config():
    def __init__(self):
        self.ip = "192.168.1.101"
        self.port = "5000"
        self.socket = self.ip + ":" + self.port

class Frontend_config():
    def __init__(self):
        self.ip = "192.168.1.101"
        self.port = "5001"
        self.socket = self.ip + ":" + self.port
        self.service_name = "dron_frontend"
        self.path_link = "/etc/systemd/system"
        self.path_service = "/opt/waterDrone/src/services"
        self.working_directory = "/opt/waterDrone/src/modules/frontend"
        self.backend_port = "5000"

class Triggers_config():
    def __init__(self):
        self.service_name = "dron_triggers"
        self.path_link = "/etc/systemd/system"
        self.path_service = "/opt/waterDrone/src/services"
        self.interval = "1"

class Scripts_config():
    def __init__(self):
        self.path = "/opt/waterDrone/src/scripts"
        
