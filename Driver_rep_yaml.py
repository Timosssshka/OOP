import yaml
import json
from decimal import Decimal
from typing import List
from Driver import Driver
from DriverRepository import DriverRepository
class DriverRepYaml(DriverRepository):
    def __init__(self, filename: str):
        super().__init__()
        self.filename = filename
        self.products = self._read_all()
    
    def _read_all(self) -> List[Driver]:
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
                return [Driver.create_from_json(json.dumps(driver)) for driver in data]
        except FileNotFoundError:
           return []
            
    def _write_all(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            yaml.dump([json.loads(driver.to_json()) for driver in self.drivers], file, allow_unicode=True, default_flow_style=False)
