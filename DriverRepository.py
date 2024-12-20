class DriverRepository:

    def __init__(self, strategy: DriverStrategy):
        self._strategy = strategy

    def get_by_id(self, driver_id: int):
        data = self._strategy.read()
        for driver in data:
            if driver['driver_id'] == driver_id:
                return driver
        return None

    def get_k_n_short_list(self, k, n):
        data = self._strategy.read()
        start_index = (n - 1) * k
        end_index = start_index + k
        return data[start_index:end_index]

    def sort_elem(self, attribute):
        data = self._strategy.read()
        return sorted(data, key=lambda p: p[attribute])

    def add_driver(self, first_name, last_name, patronymic, license_number, experience):
        data = self._strategy.read()
        new_id = -1
        for driver in data:
            new_id = max(driver['driver_id'], new_id)
        new_id += 1

        if not self.unique_code(license_number, data):
            raise ValueError(f"Водитель с таким номером водительского удостоверения уже существует.")

        new_driver = {
            'driver_id': new_id,
            'first_name': first_name,
            'last_name': last_name,
            'patronymic': patronymic,
            'license_number': license_number,
            'experience': experience,
        }

        data.append(new_driver)
        self._strategy.write(data)

    def replace_by_id(self, driver_id: int, driver: Driver):
        current_driver = self.get_by_id(driver_id)
        if not current_driver:
            raise ValueError(f"Водитель с ID {driver_id} не найден.")
        if driver.first_name:
            current_driver['first_name'] = driver.first_name
        if driver.last_name:
            current_driver['last_name'] = driver.last_name
        if driver.patronymic:
            current_driver['patronymic'] = driver.patronymic
        if driver.experience:
            current_driver['experience'] = driver.experience
        if driver.license_number:
            current_driver['license_number'] = driver.license_number

        for i, p in enumerate(data):
            if p['driver_id'] == driver_id:
                data[i] = current_driver
                break

    def delete_by_id(self, driver_id: int):
        data = self._strategy.read()
        entity = self.get_by_id(driver_id)
        if entity:
            data.remove(entity)
            self._strategy.write(data)
        else:
            raise ValueError(f"Водитель с ID {driver_id} не найден.")

    def get_count(self):
        data = self._strategy.read()
        return len(data)

    def unique_code(self, license_number, data):
        return all(driver['license_number'] != license_number for driver in data)
