from config import ESC_config1#, ESC_config2
from config import Servo_config

from base import base 
from drivers.ESC import ESC_driver
from drivers.Servo import Servo_driver

class drivers(base):
    def __init__(self):
        self.ESC = ESC_driver(ESC_config1())
        # self.ESC2 = ESC_driver(ESC_config=ESC_config2())
        self.Servo = Servo_driver(Servo_config())