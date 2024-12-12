import yaml


class DriverRepYaml():
    """Стратегия для работы с YAML."""

  def __init__(self, filename: str):
        self.filename = filename
        self.drivers = self._read_all()

    def _read_all(self, file_path: str) -> List[dict]:
         try:
            with open(file_path, 'r') as file:
                return yaml.safe_load(file) or []
        except FileNotFoundError:
            return []

     def _write_all(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            yaml.dump([json.loads(driver.to_json()) for driver in self.drivers], file, allow_unicode=True, default_flow_style=False)

    def _get_by_id(self, driver_id: int) -> dict:
        """Получить объект по ID."""
        for driver in self._data:
            if driver.get("id") == driver_id:
                return driver
        raise ValueError(f"Объект с ID {driver_id} не найден.")

    def _get_k_n_short_list(self, k: int, n: int) -> list[DriverBrief]:
        """Получить k по счету n объектов."""
        start_index = (n - 1) * k
        end_index = start_index + k
        return self._data[start_index:end_index]

    def _sort_by_field(self, field: str, reverse: bool = False) -> List[Driver]:
        """Сортировать данные по указанному полю."""
        if not self.data or field not in self.data[0]:
            raise ValueError(f"Invalid field '{field}' for sorting.")
        self._data.sort(key=lambda x: x.get(field), reverse=reverse)
        return [Driver.create_from_dict(driver) for driver in self._data]
      
    def _add_driver(self, driver: dict):
        """Добавить объект в репозиторий."""
        new_id = max((item.get("id", 0) for item in _self.data), default=0) + 1
        driver["id"] = new_id
        self.data.append(driver)
        self._write_all()

    def _replace_by_id(self, driver_id: int, updates: dict):
        """Заменить объект по ID."""
        driver = self._get_by_id(driver_id)
        valid_keys = {"id", "first_name", "last_name", "patronymic", "phone", "address"}
        updates = {k: v for k, v in updates.items() if k in valid_keys}
        driver.update(updates)
        self._write_all()

    def _delete_by_id(self, driver_id: int):
        """Удалить объект по ID."""
        self._data = [driver for drivers in self._data if driver.get("id") != driver_id]
        self._write_all()

    def _get_count(self) -> int:
        """Получить количество объектов."""
        return len(self._data)
