import RPi.GPIO as GPIO    # подключение библиотеки для работы с контактами ввода/вывода
import time              # подключение библиотеки для работы с задержками

class UltraSonic_driver():
    def __init__(self):
        # self.config = UltraSonic_config
        self.TRIG = 16
        self.ECHO = 18
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.TRIG, GPIO.OUT, initial=0)
        GPIO.setup(self.ECHO, GPIO.IN)
        
    def get_dist(self):
        GPIO.output(self.TRIG,1)
        time.sleep(0.00001)
        GPIO.output(self.TRIG,0)


        while GPIO.input(self.ECHO) == 0:
            pass
        start = time.time()

        while GPIO.input(self.ECHO) == 1:
            pass
        stop = time.time()

        print ("Distance = ",(stop - start) * 17000,"sm")


if __name__ == "__main__":
    print("Start Check distance!")
    sonic = UltraSonic_driver()
    while(True):
        sonic.get_dist()
        time.sleep(1)
