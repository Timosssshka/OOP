import json
from decimal import Decimal
from typing import List
from Driver import Driver
from DriverRepository import DriverRepository
from DriverStrategy import DriverStrategy

class DriverRepJson(DriverStrategy):
     def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def write(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def display(self):
        data = self.read()
        for item in data:
            print(item)

strategy = DriverRepJson('driver.json')
json_repository = DriverRepository(strategy)
