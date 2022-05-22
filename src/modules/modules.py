from base import base
from modules.frontend.frontend import frontend
from modules.backend.backend import backend
# from modules.control2ESC import control
from modules.controlServo import control
from modules.getTriggers import getTriggers
from modules.scripts import scripts


class modules(base):
    def __init__(self, drivers, config):
        self.drivers = drivers

        self.frontend = frontend()
        self.backend = backend()
        self.getTriggers = getTriggers()
        self.scripts = scripts(config.Scripts_config(), self.backend)
        # self.control = control(
        #     ESC=drivers.ESC,
        #     Servo=drivers.Servo,
        #     backend=self.backend
        # )
        ## 
        # self.control = control(
        #     ESC1=self.drivers.ESC1, 
        #     ESC2=self.drivers.ESC2, 
        #     backend=self.backend
        # )
        

