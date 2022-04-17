from base import base

import pigpio
from time import sleep
import RPi.GPIO as GPIO

class ESC_driver():
    def __init__(self, ESC_config):
        # ESC_GPIO = 17, ESC_GPIO_2 = 27
        self.config = ESC_config

        self.SAMPLE_TIME = self.config.SAMPLE_TIME
        self.ESC_GPIO = self.config.ESC_GPIO
        # self.ESC_GPIO_2 = ESC_GPIO_2

        print(self.config.ESC_GPIO)
        print(self.config.max)
        try:
            self.connect()
            self.calibrate()

        except:
            print("_______ESC Have ERROR. Please STOP IT!!!_______")

    def connect(self):
        self.pi = pigpio.pi()

    def disconect(self):
        self.pi.stop()

    def calibrate(self):
        # self.connect()
        GPIO.setmode(GPIO.BCM)
        print("_______Step 1: Calibrate ESC")
        # Calibrate ESC
        print("_______Set max")
        self.pi.set_servo_pulsewidth(self.ESC_GPIO, self.config.max) # Maximum throttle.
        sleep(self.SAMPLE_TIME)
        print("_______Set min")
        self.pi.set_servo_pulsewidth(self.ESC_GPIO, self.config.min) # Minimum throttle.
        sleep(self.SAMPLE_TIME)

        print("_______Stop")
        self.set_speed(0)
        # self.disconect()

    def set_speed(self, speed):
        speed = int(speed)
               
        if  speed >= self.config.min and speed <= self.config.max or speed == 0:
            print(f"speed = {speed}")
            # self.connect()
            self.pi.set_servo_pulsewidth(self.ESC_GPIO, speed)
            # self.pi.set_servo_pulsewidth(self.ESC_GPIO_2, speed)
            sleep(self.SAMPLE_TIME)
            # self.disconect()
        else:
            print(f"ESC > set_speed > ERROR SPEED = {speed}")

    def stop(self):
        self.set_speed(0)
        self.disconect()
