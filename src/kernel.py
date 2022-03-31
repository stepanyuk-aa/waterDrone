# from loguru import logger
from base import base

from modules.modules import modules
from drivers.drivers import drivers

# logger.add("debug.log", format="{time} {level} {message}",
#    level = "DEBUG", roatation="10 KB", compression="zip")

class kernel(base):
	def __init__(self):
		# self.logger.info("kernel > init")
		# print("kernel > init")
		self.drivers = drivers()
		self.modules = modules(self.drivers)

		self.modules.frontend.run()
		self.modules.frontend.start_service()
		

kl = kernel()