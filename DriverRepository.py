from typing import List, Optional
from decimal import Decimal
from Driver import Driver
from DriverShort import DriverShort
from DriverStrategy import DriverStrategy

class DriverRepository:
    """Базовый класс для репозиториев с общей логикой работы с данными."""
    def __init__(self, strategy: DriverStrategy):
        self._data = []
        self._strategy = strategy
        self.read_data()

    def read_all(self) -> List[Driver]:
        """Чтение всех записей с использованием стратегии."""
        self._data = self._strategy.read()

    def write_all(self, drivers: List[Driver]) -> None:
        """Запись всех записей с использованием стратегии."""
        self._strategy.write(self._data)
      
    def get_all(self) -> list:
        """Получить все объекты."""
        return self._data
      
    def get_by_id(self, driver_id: int) -> Optional[Driver]:
        """Получить объект по ID."""
        for driver in self._data:
            if driver['driver_id'] == driver_id:
                return Driver.create_from_dict(driver)
        raise ValueError(f"Объект с ID {driver_id} не найден.")
      
    def add_driver(self, driver: Driver):
        """Добавить объект в репозиторий."""
        unique_fields = ("license_number")
        for existing_driver in self._data:
            if all(existing_driver.get(field) == driver.get(field) for field in unique_fields):
                raise ValueError(f"Водитель с такими данными уже существует: {driver}")
        new_id = max((item.get("id", 0) for item in self._data), default=0) + 1
        driver["id"] = new_id
        self.data.append(driver)
      
    def delete_by_id(self, driver_id: int):
        """Удалить объект по ID."""
        driver = self.get_by_id(driver_id)
        if not driver:
            raise ValueError(f"Водитель с ID {driver_id} не найден.")
        self.data = [p for p in self.data if p['driver_id'] != driver_id]
      
    def replace_by_id(self, driver_id: int, first_name=None, last_name=None, patronymic=None, experience=None, license_number=None):
        """Заменить объект по ID."""
        driver = self.get_by_id(driver_id)
        if not driver:
            raise ValueError(f"Водитель с ID {driver_id} не найден.")
        drivers = [Driver.create_from_dict(driver) for driver in self._data]
        if first_name:
            driver.first_name = first_name
        if last_name:
            driver.last_name = last_name
        if patronymic:
            driver.patronymic = patronymic
        if experience:
            driver.experience = experience
        if license_number:
            driver.license_number = license_number
        for i, p in enumerate(self.data):
            if p['driver_id'] == driver_id:
                self.data[i] = driver.to_dict()
                break
      
    def get_k_n_short_list(self, k: int, n: int) -> list[DriverShort]:
        """Получить k по счету n объектов."""
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
        """Сортировать данные по указанному полю."""
        if field not in ['driver_id', 'first_name', 'last_name', 'patronymic', 'experience', 'license_number']:
            raise ValueError(f"Invalid field '{field}' for sorting.")
        self._data.sort(key=lambda x: x.get(field), reverse=reverse)
        return [Driver.create_from_dict(driver) for driver in self._data]
      
    def get_count(self) -> int:
        """Получить количество объектов."""
        return len(self._data)
