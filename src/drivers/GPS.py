from gps import *
import time

class coordinates():
    def __init__(self, lat, lon):
        # Широта
        self.latitude = lat
        # Долгота
        self.longitude = lon

class GPS_driver():
    def __init__(self):
        # self.config = GPS_config
        self.gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

    def getPosition(self):
        nx = self.gpsd.next()

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
        while running:
            GPS.getPosition()
            time.sleep(1.0)

    except (KeyboardInterrupt):
        running = False