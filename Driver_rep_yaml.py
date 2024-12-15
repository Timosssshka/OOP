import yaml
import json
from decimal import Decimal
from typing import List
from Driver import Driver
from DriverRepository import DriverRepository

class DriverRepYaml(DriverStrategy):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file) or []

    def write(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, allow_unicode=True, default_flow_style=False)

    def add(self, driver):
        data = self.read()
        data.append(driver.to_dict())
        self.write(data)

    def display(self):
        data = self.read()
        for item in data:
            print(item)

strategy = DriverRepYaml('drivers.yaml')
strategy.display()
