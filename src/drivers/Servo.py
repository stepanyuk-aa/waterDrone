import RPi.GPIO as IO    # подключение библиотеки для работы с контактами ввода/вывода
import time              # подключение библиотеки для работы с задержками

class Servo_driver():
    def __init__(self, Servo_config):
        self.config = Servo_config

        IO.setwarnings(False)  
        IO.setmode (IO.BCM)      
        IO.setup(self.config.GPIO,IO.OUT)      
        
        self.servo_port = IO.PWM(self.config.GPIO,50)    
        self.servo_port.start(7.5)             

    def set_rotate(self, rotate):
        if rotate >= 2.5 and rotate <= 12.5:
            print(f"Rotate on {rotate}")
            self.servo_port.ChangeDutyCycle(rotate)  
            time.sleep(1)    

    def set_left(self):
        self.set_rotate(2.5)

    def set_right(self):
        self.set_rotate(12.5)

    def set_direct(self):
        self.set_rotate(7.5)