import config
from modules.modules import modules
from drivers.drivers import drivers

drivers = drivers()
modules = modules(drivers, config)

Sonar = drivers.UltraSonic
a = 0
print(a)
a = Sonar.get_dist()
print(a)

