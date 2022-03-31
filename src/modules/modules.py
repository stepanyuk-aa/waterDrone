from base import base
from modules.frontend.frontend import frontend

class modules(base):
    def __init__(self, drivers):
        # self.logger.info("modules > init")
        self.drivers = drivers
        self.frontend = frontend()