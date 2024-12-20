import json
import os

class DriverRepJson:
     def __init__(self,json_file):
        self.json_file = json_file

    def read(self):
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, 'r') as file:
           data = json.load(f
            return data

    def write(self, data):
        with open(self.json_file, 'w') as file:
            json.dump(data, file)

strategy = DriverRepJson('driver.json')
json_repository = DriverRepository(strategy)

