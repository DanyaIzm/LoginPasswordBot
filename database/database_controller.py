from sqlite3 import connect


class DatabaseController:
    def __init__(self):
        # Connection and cursor
        self.connection = connect(database="database.db")
        self.cursor = self.connection.cursor()

        # Create tables
        self._create_table_users()
        self._create_table_accounts()

    def _create_table_users(self):
        query = "CREATE TABLE IF NOT EXISTS " \
                "Users(id NUMBER, first_name TEXT, last_name TEXT, username TEXT, status BOOL, PRIMARY KEY(id))"
        self.cursor.execute(query)
        self.connection.commit()

    def _create_table_accounts(self):
        query = "CREATE TABLE IF NOT EXISTS " \
                "Accounts(id INTEGER PRIMARY KEY AUTOINCREMENT, user NUMBER, " \
                "service TEXT, login TEXT, password TEXT, " \
                "FOREIGN KEY(user) REFERENCES Users(id))"
        self.cursor.execute(query)
        self.connection.commit()

    def is_user_exists(self, user_id) -> bool:
        query = f"SELECT * FROM Users WHERE id = {int(user_id)}"
        self.cursor.execute(query)

        if self.cursor.fetchone():
            return True
        else:
            return False

    def add_user(self, data: dict) -> None:
        query = f"INSERT INTO Users(`id`, `first_name`, `last_name`, `username`, `status`) " \
                f"VALUES({int(data['id'])}, '{data['first_name']}', '{data['last_name']}', '{data['username']}', 0)"
        self.cursor.execute(query)
        self.connection.commit()

    def get_status(self, user_id) -> bool:
        query = f"SELECT status FROM Users WHERE id = {int(user_id)}"
        self.cursor.execute(query)

        return bool(self.cursor.fetchone()[0])

    def get_from_accounts(self, content: str, user_id, service: str = None):
        query = f"SELECT service, login, password FROM Accounts WHERE user = {int(user_id)}"
        self.cursor.execute(query)

        fetch = self.cursor.fetchall()
        data = []

        for item in fetch:
            data.append({
                'service': item[0],
                'login': item[1],
                'password': item[2]
            })

        if content == "everything":
            return data
        elif content == "service":
            new_data = []
            for item in data:
                if item['service'] == service:
                    new_data.append(item)
            return new_data
        else:
            return None

    def delete_account(self, user_id, service: str, login: str = None) -> int:
        if login:
            select_query = f"SELECT * FROM Accounts WHERE user = '{int(user_id)}' AND service = '{service}' AND login = '{login}'"
            delete_query = f"DELETE FROM Accounts WHERE user = '{int(user_id)}' AND service = '{service}' AND login = '{login}'"
        else:
            select_query = f"SELECT * FROM Accounts WHERE user = '{int(user_id)}' AND service = '{service}'"
            delete_query = f"DELETE FROM Accounts WHERE user = '{int(user_id)}' AND service = '{service}'"

        amount_of_records = 0

        try:
            self.cursor.execute(select_query)
            amount_of_records = len(self.cursor.fetchall())
        except Exception as e:
            pass

        self.cursor.execute(delete_query)
        self.connection.commit()

        return amount_of_records

    def get_accounts_amount(self, user_id, service: str) -> int:
        query = f"SELECT * FROM Accounts WHERE `user` = '{int(user_id)}' AND `service` = '{service}'"
        self.cursor.execute(query)
        return len(self.cursor.fetchall())

    def change_password(self, user_id, new_password: str, service: str, login: str = None):
        if login:
            query = f"UPDATE Accounts SET password = '{new_password}' " \
                           f"WHERE user = '{int(user_id)}' AND service = '{service}' AND login = '{login}'"
        else:
            query = f"UPDATE Accounts SET password = '{new_password}' " \
                           f"WHERE user = '{int(user_id)}' AND service = '{service}'"

        self.cursor.execute(query)
        self.connection.commit()
