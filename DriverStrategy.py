from abc import ABC, abstractmethod

class DriverStrategy(ABC):
    """Интерфейс стратегии для работы с хранилищем данных."""

    @abstractmethod
    def read(self):
      """Загрузка данных из файла."""
        pass
      
    @abstractmethod
    def write(self, data):
        """Сохранение данных в файл."""
        pass

    @abstractmethod
    def display(self):
        """Отображает содержимое файла."""
        pass
