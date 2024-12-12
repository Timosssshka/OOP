from abc import ABC, abstractmethod
import json
import yaml 
class DriverRepository(ABC):
    """Базовый класс для репозиториев с общей логикой работы с данными."""
    def __init__(self):
        self.drivers = []
    
    @abstractmethod
    def _read_all(self) -> List[Driver]:
        pass
      
    @abstractmethod
    def _write_all(self):
        pass
      
    def get_all(self) -> list:
        """Получить все объекты."""
        return self._data
      
    def get_by_id(self, driver_id: int) -> dict:
        """Получить объект по ID."""
        for driver in self._data:
            if driver.get("id") == driver_id:
                return driver
        raise ValueError(f"Объект с ID {driver_id} не найден.")
      
    def add_student(self, driver: dict):
        """Добавить объект в репозиторий."""
        new_id = max((item.get("id", 0) for item in self.data), default=0) + 1
        driver["id"] = new_id
        self._data.append(driver)
        self._write_all()
      
    def delete_by_id(self, driver_id: int):
        """Удалить объект по ID."""
        self.data = [driver for driver in self._data if driver.get("id") != driver_id]
        self._write_all()
      
    def replace_by_id(self, driver_id: int, updates: dict):
        """Заменить объект по ID."""
        driver = self.get_by_id(driver_id)
        valid_keys = {"id", "last_name", "first_name", "patronymic", "license_number", "experience"}
        updates = {k: v for k, v in updates.items() if k in valid_keys}
        driver.update(updates)
        self._write_all()
      
    def get_k_n_short_list(self, k: int, n: int) -> list[DriverShort]:
        """Получить k по счету n объектов."""
        start_index = (n - 1) * k
        end_index = start_index + k
        return self._data[start_index:end_index]
      
    def sort_by_field(self, field: str, reverse: bool = False) -> List[Driver]:
        """Сортировать данные по указанному полю."""
        if not self._data or field not in self._data[0]:
            raise ValueError(f"Invalid field '{field}' for sorting.")
        self._data.sort(key=lambda x: x.get(field), reverse=reverse)
        return [Driver.create_from_dict(driver) for driver in self._data]
      
    def get_count(self) -> int:
        """Получить количество объектов."""
        return len(self._data)
