class DriverRepDB:
    
    def __init__(self, host, user, password, database, port=3306):
        self.db_connection = DBConnection(host, user, password, database, port)
    
    def get_by_id(self, driver_id: int) -> dict:
        conn = self.db_connection.get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM drivers WHERE id = %s", (driver_id,))
            driver = cursor.fetchone()
            if not driver:
                raise ValueError(f"Водитель с ID {driver_id} не найден.")
            return dict(driver)
    
    def get_k_n_short_list(self, k: int, n: int):
        offset = (n - 1) * k
        conn = self.db_connection.get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM drivers ORDER BY id LIMIT %s OFFSET %s", (k, offset))
            return [dict(row) for row in cursor.fetchall()]
    
    def add_driver(self, driver: Driver):
        conn = self.db_connection.get_connection()
        try:
            query = """
                INSERT INTO drivers (first_name, last_name, patronymic, license_number) VALUES (%s, %s, %s, %s)
            """
            values = (driver.first_name, driver.last_name, driver.patronymic, driver.license_number)
            with conn.cursor() as cursor:
                cursor.execute(query, values)
                conn.commit()
                driver.driver_id = cursor.lastrowid
            self.notify_observers()

        except MySQLError as e:
            if e.args[0] == 1062:
                raise ValueError(f"Водитель с удостоверением {driver.license_number} уже существует.")
            else:
                raise Exception("При добавлении водителя произошла непредвиденная ошибка.")
    
    def replace_by_id(self, driver_id: int, new_driver: dict):
        valid_keys = {"first_name", "last_name", "patronymic", "license_number"}
        updates = {k: v for k, v in updates.items() if k in valid_keys}
        if not updates:
            raise ValueError("Нет валидных полей для обновления.")
        conn = self.db_connection.get_connection()
        set_clause = ", ".join([f"{key} = %s" for key in updates.keys()])
        values = list(updates.values()) + [driver_id]
        
        with conn.cursor() as cursor:
            cursor.execute(f"UPDATE drivers SET {set_clause} WHERE id = %s", values)
            conn.commit()
    
    def delete_by_id(self, driver_id: int):
        conn = self.db_connection.get_connection()
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM drivers WHERE id = %s", (driver_id,))
            conn.commit()
    
    def get_count(self) -> int:
        conn = self.db_connection.get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM drivers")
            return cursor.fetchone()[0]
