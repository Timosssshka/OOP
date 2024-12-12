import json
from decimal import Decimal
from typing import List
from Driver import Driver
from DriverRepository import DriverRepository
class DriverRepJson(DriverRepository):
    def __init__(self, filename: str):
        super().__init__()
        self.filename = filename
        self.drivers = self._read_all()
    def _read_all(self) -> List[Driver]:
        try:
            with open(self.filename, 'r', encoding='cp1251') as file:
                data = json.load(file)
                return [Driver.create_from_json(json.dumps(driver)) for driver in data]
        except FileNotFoundError:
            return []
    def _write_all(self):
        with open(self.filename, 'w', encoding='cp1251') as file:
            json.dump([json.loads(driver.to_json()) for driver in self.drivers], file, ensure_ascii=False, indent=4)
