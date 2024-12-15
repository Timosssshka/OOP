from DriverRepBase import  DriverRepBase
class Adapter:
    def __init__(self, driver_rep_base: DriverRepBase):
        self._driver_rep_base = driver_rep_base
    def get_k_n_short_list(self, k, n):
        return self._driver_rep_base.get_k_n_short_list(k, n)
    def get_by_id(self, driver_id):
        return self._driver_rep_base.get_by_id(driver_id)
    def delete_by_id(self, driver_id):
        self._driver_rep_base.delete_by_id(driver_id)
        
    def update_by_id(self, driver_id, updates: dict):
        self._driver_rep_base.replace_by_id(driver_id, updates)
    def add(self, driver: dict):
        self._driver_rep_base.add_student(driver)
    def get_count(self):
        return self._driver_rep_base.get_count()
