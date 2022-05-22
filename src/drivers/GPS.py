from gps import *
import time

class coordinates():
    def __init__(self, lat, lon):
        # Широта
        self.latitude = lat
        # Долгота
        self.longitude = lon
    
    def get(self):
        return f"{self.latitude}:{self.longitude}"

class GPS_driver():
    def __init__(self):
        # self.config = GPS_config
        self.gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

    def getPosition(self):
        i = 0
        nx = self.gpsd.next()
        while nx['class'] != 'TPV' or i > 10: 
            print(nx['class'])
            nx = self.gpsd.next()
            i += 1

        if nx['class'] == 'TPV':
            lat = getattr(nx,'lat', "Unknown")     
            lon = getattr(nx,'lon', "Unknown") 
            return coordinates(lat, lon)

        return False
    
if __name__ == "__main__":
    print("Start Check GPS!")
    running = True
    GPS = GPS_driver()

    try:
        i = 0
        while running:
            print(i)
            GPS.getPosition()
            # time.sleep(1.0)
            i+=1
    except (KeyboardInterrupt):
        running = False