#!/usr/bin/python3.9
import sys
sys.path.append("/opt/waterDrone/src")
import config
from base import dataBase 
from triggers import triggers

class triggers_run():
    def __init__(self):
        self.triggers = triggers(config)
        self.database = dataBase(config.dataBaseConfig())

        self.Sonar_get()
        self.GPS_get()

    def Sonar_get(self):
        data = self.triggers.Sonar.get_dist()
        # print(data)
        self.database.write(
            table = "USR", 
            field = "distance", 
            data = data
        )

    def GPS_get(self):
        try:
            data = self.triggers.GPS.getPosition().get()
        except:
            print("GPS Error")
            data = False

        if data:
            self.database.write(
                table = "GPS", 
                field = "coordinates", 
                data = data
            )

if __name__ == "__main__":
    trigs = triggers_run()