import config
from base import base

from triggers.triggers import triggers
from modules.modules import modules
from drivers.drivers import drivers


class kernel(base):
	def __init__(self):
		# self.logger.info("kernel > init")
		# print("kernel > init")
		# self.drivers = drivers()
		self.triggers = triggers(config)
		self.modules = modules(self.drivers)

		self.modules.frontend.run()
		self.modules.frontend.start_service()
		self.modules.backend.run()


kl = kernel()