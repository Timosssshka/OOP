import yaml
import os
from DriverRepository import DriverRepository

class DriverRepYaml(DriverStrategy):
    def __init__(self, yamlFile):
        self.yamlFile = yamlFile

    def read(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.yamlFile, 'r', encoding='utf-8') as file:
          data = yaml.safe_load(file)
          return  data

  
    def write(self, data):
        with open(self.yamlFile, 'w') as file:
            yaml.dump(data, file)

  
     def add(self, driver):
       data = self.read()
       data.append(driver.to_dict())
       self.write(data)
