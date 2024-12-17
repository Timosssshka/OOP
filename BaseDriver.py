import re
import json


class BaseDriver:
    def __init__(self,  last_name: str, first_name: str, patronymic: str, license_number: str, driver_id: int = None):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.license_number = license_number
        self.driver_id = driver_id

    @property
    def driver_id(self):
        return self.__driver_id

    @driver_id.setter
    def driver_id(self, value: int):
        if not self.validate_driver_id(value):
            raise ValueError("Некорректный ID водителя.")
        self.__driver_id = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str):
        if not self.validate_last_name(value):
            raise ValueError("Некорректная фамилия.")
        self.__last_name = value

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        if not self.validate_first_name(value):
            raise ValueError("Некорректное имя.")
        self.__first_name = value

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value: str):
        if not self.validate_patronymic(value):
            raise ValueError("Некорректное отчество.")
        self.__patronymic = value

    @property
    def license_number(self):
        return self.__license_number

    @license_number.setter
    def license_number(self, value: str):
        if not self.validate_license_number(value):
            raise ValueError("Некорректный номер удостоверения.")
        self.__license_number = value

    @staticmethod
    def validate_driver_id(driver_id: int) -> bool:
        return isinstance(driver_id, int) and driver_id > 0

    @staticmethod
    def validate_first_name(first_name: str) -> bool:
        return bool(first_name and re.match(r"^[a-zA-Zа-яА-ЯёЁ\s-]+$", first_name))

    @staticmethod
    def validate_last_name(last_name: str) -> bool:
        return bool(last_name and re.match(r"^[a-zA-Zа-яА-ЯёЁ\s-]+$", last_name))

    @staticmethod
    def validate_patronymic(patronymic: str) -> bool:
        return bool(patronymic and re.match(r"^[a-zA-Zа-яА-ЯёЁ\s-]+$", patronymic))

    @staticmethod
    def validate_license_number(license_number: str) -> bool:
        return bool(re.fullmatch(r"\d{2} \d{2} \d{4}", license_number))

     @classmethod
    def create_new_driver(cls, driver_id: Optional[int], first_name: str, last_name: str, patronymic: str, license_number: str):
        new_driver = cls(driver_id=driver_id, first_name=first_name, last_name=last_name, patronymic=patronymic, license_number=license_number)
        return new_driver
        
    @staticmethod
    def from_string(driver_str: str):
        parts = driver_str.split(',')
        if len(parts) != 5:
            raise ValueError("Строка должна содержать 5 элементов, разделённых запятыми.")
        driver_id = int(parts[0].strip())
        first_name, last_name, patronymic, license_number = map(str.strip, parts[1:])
        return BaseDriver(first_name, last_name, patronymic, license_number,driver_id)

    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)
        return cls(
            driver_id=data.get('driver_id'),
            first_name=data['first_name'],
            last_name=data['last_name'],
            patronymic=data.get('patronymic', ''),
            license_number=data['license_number']
        )

    @classmethod
    def create_from_dict(cls, data: dict):
        return cls(
            driver_id=data.get('driver_id'),
            first_name=data['first_name'],
            last_name=data['last_name'],
            patronymic=data.get('patronymic', ''),
            license_number=data['license_number']
        )
        
    def to_json(self) -> str:
        return json.dumps({
            'driver_id': self.driver_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'patronymic': self.patronymic,  
            'license_number': self.license_number
        }, ensure_ascii=False, indent=4)
        
    @classmethod
    def create_from_yaml(cls, yaml_string: str):
        data = yaml.safe_load(yaml_string)
        return cls(
            driver_id=data.get('driver_id'),
            first_name=data['first_name'],
            last_name=data['last_name'],
            patronymic=data.get('patronymic', ''),
            license_number=data['license_number']
        )
        
    def to_yaml(self) -> str:
        return yaml.dump({
            'driver_id': self.driver_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'patronymic': self.patronymic,  
            'license_number': self.license_number
        }, allow_unicode=True)
    def to_dict(self) -> dict:
        return {
            'driver_id': self.driver_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'patronymic': self.patronymic,  
            'license_number': self.license_number
        }

    def __eq__(self, other):
        if not isinstance(other, BaseDriver):
            return False
        return (self.license_number == other.license_number)

    def short_description(self):
        return f"{self.last_name} {self.first_name[0]}. {self.patronymic[0]}."

    def __str__(self):
        return (f"ID: {self.driver_id}\n"
                f"Фамилия: {self.last_name}\n"
                f"Имя: {self.first_name}\n"
                f"Отчество: {self.patronymic}\n"
                f"Номер ВУ: {self.license_number}")


class Driver(BaseDriver):
    def __init__(self, driver_id: None, last_name: str, first_name: str, patronymic: str, experience: int,
                 license_number: str):
        super().__init__(last_name, first_name, patronymic, license_number,driver_id)
        self.experience = experience

    @property
    def experience(self):
        return self.__experience

    @staticmethod
    def validate_experience(experience: int) -> bool:
        return isinstance(experience, int) and 0 <= experience <= 100

    @experience.setter
    def experience(self, value: str):
        if not self.validate_experience(value):
            raise ValueError("Некорректный стаж работы.")
        self.__experience = value

    def __str__(self):
        return (f"Полная информация о водителе:\n"
                f"{super().__str__()}\n"
                f"Стаж: {self.experience} лет")


class DriverShort(BaseDriver):
    def __init__(self, driver: Driver):
        super().__init__(driver.last_name, driver.first_name, driver.patronymic, driver.license_number)

    @classmethod
    def from_driver(cls, driver: Driver):
        if not isinstance(driver, Driver):
            raise TypeError("Аргумент должен быть объектом класса Driver.")
        return cls(
            driver_id=driver.driver_id,
            first_name=driver.first_name,
            last_name=driver.last_name,
            patronymic=driver.patronymic,
            license_number=driver.license_number
        )

    def get_brief_name(self):
        first_initial = f"{self.first_name[0]}." if self.first_name else ""
        patronymic_initial = f"{self.patronymic[0]}." if self.patronymic else ""
        return f"{self.last_name} {first_initial}{patronymic_initial}"

    def __str__(self):
        return f"Водитель: {self.get_brief_name()}, ID: {self.driver_id}, Телефон: {self.license_number}"


# Пример использования
if __name__ == "__main__":
    # Попробуем создать водителя с разными данными
    valid_driver_id = 1
    valid_last_name = "Иванов"
    valid_first_name = "Иван"
    valid_patronymic = "Иванович"
    valid_experience = 5
    valid_license_number = "12 34 5678"

    if Driver.validate_driver_id(valid_driver_id) and \
            Driver.validate_experience(valid_experience) and \
            BaseDriver.validate_license_number(valid_license_number):
        driver = Driver(valid_driver_id, valid_last_name, valid_first_name, valid_patronymic, valid_experience,
                        valid_license_number)
        print(driver)
    else:
        print("Некорректные данные для водителя.")
