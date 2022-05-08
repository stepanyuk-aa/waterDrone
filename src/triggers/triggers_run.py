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

    def Sonar_get(self):
        data = self.triggers.Sonar.get_dist()
        print(data)
        self.database.write(
            table = "USR", 
            field = "distance", 
            data = data
        )
        # GPS
        # Servo
    

    # self.database

if __name__ == "__main__":
    trigs = triggers_run()