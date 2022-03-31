from base import base
from config import ESC_config

from time import sleep
import pigpio
import RPi.GPIO as GPIO

class ESC_driver():
    def __init__(self):
        # ESC_GPIO_1 = 17, ESC_GPIO_2 = 27
        self.config = ESC_config()

        self.SAMPLE_TIME = self.config.SAMPLE_TIME
        self.ESC_GPIO_1 = self.config.ESC_GPIO
        # self.ESC_GPIO_2 = ESC_GPIO_2
        try:
            self.pi = pigpio.pi()
            self.connect()
        except:
            pass

    def connect(self):
        self.pi = pigpio.pi()
    def disconect(self):
        self.pi.stop()

    def calibrate(self):
        self.connect()
        GPIO.setmode(GPIO.BCM)
        print("Step 1: Calibrate ESC")
        # Calibrate ESC
        self.pi.set_servo_pulsewidth(self.ESC_GPIO_1, 2000) # Maximum throttle.
        # self.pi.set_servo_pulsewidth(self.ESC_GPIO_2, 2000) # Maximum throttle.
        sleep(2)
        self.pi.set_servo_pulsewidth(self.ESC_GPIO_1, 1000) # Minimum throttle.
        # self.pi.set_servo_pulsewidth(self.ESC_GPIO_2, 1000) # Minimum throttle.
        sleep(2)
        self.stop()
        self.disconect()

    def setSpeed(self, speed):
        self.connect()
        self.pi.set_servo_pulsewidth(self.ESC_GPIO_1, speed)
        # self.pi.set_servo_pulsewidth(self.ESC_GPIO_2, speed)
        sleep(self.SAMPLE_TIME)
        self.disconect()

    def stop(self):
        self.connect()
        self.setSpeed(0)
        self.disconect()