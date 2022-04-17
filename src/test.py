import config
from drivers.ESC import ESC_driver 
from time import sleep

conf = config.ESC_config1()

ESC = ESC_driver(conf)
ESC.calibrate()

speed = 1400
while speed < 2000:
    ESC.set_speed(speed)
    sleep(3)
    speed += 50

ESC.stop()
    

# import pigpio
# from time import sleep
# import RPi.GPIO as GPIO

# print("Start")
# pi = pigpio.pi()

# print("Set max")
# pi.set_servo_pulsewidth(17, 2000) 
# sleep(3)
# print("Set min")
# pi.set_servo_pulsewidth(17, 700) 
# sleep(3)
# print("Stop")
# pi.set_servo_pulsewidth(17, 0) 
# sleep(3)


# print("Run")
# try:
#     speed = 800
#     while True:
#         print(speed)
#         pi.set_servo_pulsewidth(17, speed) 
#         speed += 10

#         sleep(3)
#         if speed > 2000:
#             break
# finally:
#     pi.set_servo_pulsewidth(17, 0) 
#     pi.stop()


