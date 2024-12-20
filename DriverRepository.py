from typing import List, Optional
from decimal import Decimal
from Driver import Driver
from DriverShort import DriverShort
from DriverStrategy import DriverStrategy

class DriverRepository:
    def __init__(self, strategy: DriverStrategy):
        self._data = []
        self._strategy = strategy
        self.read_data()

    def read(self) -> List[Driver]:
        self._data = self._strategy.read()

    def write(self, drivers: List[Driver]) -> None:
        self._strategy.write(self._data)
      
    def get(self) -> list:
        return self._data
      
    def get_by_id(self, driver_id: int) -> Optional[Driver]:
        for driver in self._data:
            if driver['driver_id'] == driver_id:
                return Driver.create_from_dict(driver)
        raise ValueError(f"Объект с ID {driver_id} не найден.")
      
    def add_driver(self, driver: Driver):
        driver_dict = driver.to_dict()
        drivers = [Driver.create_from_dict(driver) for driver in self.data]
        if not self.unique_code(driver, drivers):
            raise ValueError(f"Водитель уже существует.")
        self.data.append(driver_dict)

    def unique_code(self, driver, drivers):
        for driver_data in drivers:
            if driver_data == drivert:
                 raise ValueError(f"Водитель уже существует.")
        return True
      
    def delete_by_id(self, driver_id: int):
        driver = self.get_by_id(driver_id)
        if not driver:
            raise ValueError(f"Водитель с ID {driver_id} не найден.")
        self.data = [p for p in self.data if p['driver_id'] != driver_id]
      
    def replace_by_id(self, driver_id: int, driver : Driver):
        driver = self.get_by_id(driver_id)
        if not driver:
            raise ValueError(f"Водитель с ID {driver_id} не найден.")
        if driver.first_name:
            driver.first_name = driver.first_name
        if driver.last_name:
            driver.last_name = driver.last_name
        if driver.patronymic:
            driver.patronymic = driver.patronymic
        if driver.experience:
            driver.experience = driver.experience
        if driver.license_number:
            driver.license_number = driver.license_number
        for i, p in enumerate(self.data):
            if p['driver_id'] == driver_id:
                self.data[i] = driver.to_dict()
                break
      
    def get_k_n_short_list(self, k: int, n: int) -> list[DriverShort]:
        start_index = (n - 1) * k
        end_index = start_index + k
        return [
            DriverShort(
                driver_id=driver['driver_id'],
                first_name=driver['first_name'],
                last_name=driver['last_name'],
                patronymic=driver['patronymic'],
                license_number=driver['license_number']
            )
            for driver in self._data[start_index:end_index]
        ]
      
    def sort_by_field(self, field: str, reverse: bool = False) -> List[Driver]:
        if field not in ['driver_id', 'first_name', 'last_name', 'patronymic', 'experience', 'license_number']:
            raise ValueError(f"Invalid field '{field}' for sorting.")
        self._data.sort(key=lambda x: x.get(field), reverse=reverse)
        return [Driver.create_from_dict(driver) for driver in self._data]
      
    def get_count(self) -> int:
        return len(self._data)
