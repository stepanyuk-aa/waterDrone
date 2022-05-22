import config
from base import dataBase

from triggers.triggers import triggers
from modules.modules import modules
from drivers.drivers import drivers


class kernel():
	def __init__(self):
		self.database = dataBase(config.dataBaseConfig())
		self.drivers = drivers()
		self.triggers = triggers(config)
		self.modules = modules(self.drivers)

		# self.modules.frontend.run()
		# self.modules.frontend.start_service()
		self.modules.getTriggers.run(self.database, self.modules.backend)
		self.modules.backend.run()



kl = kernel()