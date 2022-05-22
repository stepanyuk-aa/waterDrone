from math import *

class getTriggers():
    def __init__(self):
        self.database = None
        self.backend = None

    def run(self, database, backend):
        self.database = database
        self.backend = backend

        self.get_triggers()

    def get_triggers_USR(self):
        return self.database.read_last("USR")[0]

    def get_triggers_Speed(self):
        data = self.database.read_last("GPS", 4)
        try:
            coorStart = data[0]
            coorStart["coordinates"] = coorStart["coordinates"].split(':')
            coorStart["coordinates"] = [float(coorStart["coordinates"][0]), float(coorStart["coordinates"][1])]
            
            coorEnd = data[len(data)-1]
            coorEnd["coordinates"] = coorEnd["coordinates"].split(':')
            coorEnd["coordinates"] = [float(coorEnd["coordinates"][0]), float(coorEnd["coordinates"][1])]
            
            time = coorEnd['mydate'] - coorStart['mydate']
            time = time.total_seconds()

            dist = self._get_dist_in_m(coorStart["coordinates"], coorEnd["coordinates"])
            speed = dist / time
        except:
            return "Unknown"
        # print(coorStart)
        # print(coorEnd)
        # print(time)
        # print(dist)

        return speed, coorEnd['coordinates']

    def get_triggers(self):
        @self.backend.app.route('/get/triggers', methods=['GET'])
        def get_triggers():
            data = {
                'coordinates': [],
                'speed': 0,
                'usr': 0,
            }

            speed, coordinates = self.get_triggers_Speed()

    
            data['coordinates'] = [round(coordinates[0],2),round(coordinates[1],2)]
            data['speed'] = round(speed,2)
            data['usr'] = round(float(self.get_triggers_USR()['distance']),2)            
            return data
        

    def _get_dist_in_m(self, coor1,coor2):
        R = 6371000 # Radius of the earth in m
        dLat = radians(coor2[0]-coor1[0])
        dLon = radians(coor2[1]-coor1[1])
        rLat1 = radians(coor1[0])
        rLat2 = radians(coor2[0])
        a = sin(dLat/2) * sin(dLat/2) + cos(rLat1) * cos(rLat2) * sin(dLon/2) * sin(dLon/2) 
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        d = R * c # Distance in m
        return d



