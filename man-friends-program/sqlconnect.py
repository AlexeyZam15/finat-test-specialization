import mysql.connector

from aux_modules.datecheck import DateCheck


class SQLConnect:
    def __init__(self, host: str, user: str, passwd: str, database: str = None, main_table: str = None):
        self.__host = host
        self.__user = user
        self.__passwd = passwd
        self.__database = database
        self.__mydb = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database,
            autocommit=True
        )
        self.__cursor = self.__mydb.cursor()
        self.__main_table = main_table

    @property
    def database(self):
        return self.__database

    @property
    def main_table(self):
        return self.__main_table

    def execute_from_file(self, file_name: str):
        with open(file_name, "r") as f:
            query = ""
            for line in f:
                query += line
                if line.find(';') != -1:
                    self.__cursor.execute(query.replace("\n", ""))
                    query = ""

    def execute(self, query: str):
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def __del__(self):
        self.__mydb.commit()
        self.__mydb.close()

    def import_from_csv_file(self, table_name: str, file_name: str):
        data = []
        date_col = None
        with open(file_name, "r") as f:
            file = f.readlines()
            if ("дата" or "date") in file[0].lower():
                col = 0
                for i in file[0].lower().split(";"):
                    if ("дата" or "date") in i:
                        date_col = col
                    col += 1
            for line in file[1:]:
                if line != "\n":
                    data.append(line)
        self.import_data(self.__create_values_sql_list(data, date_col))

    def import_data(self, data):
        print(*data, sep="\n")
        for row in data:
            self.__cursor.execute(f"INSERT INTO {self.__main_table} VALUES {row};")

    @staticmethod
    def __create_values_sql_list(values_list: list[str], date_column: int = None):
        new_values_list = []
        if date_column:
            for i in range(len(values_list)):
                row_data = values_list[i].split(";")
                row_data[date_column] = DateCheck.change_date_format(row_data[date_column])
                values_list[i] = ";".join(row_data).replace("\n", "")

        for values in values_list:
            values_string = values.replace(";", "','")
            values_string = "('" + values_string
            values_string += "')"
            new_values_list.append(values_string)
        return new_values_list

    def update(self, field: str, new_value: str, condition: str):
        self.execute(
            f"UPDATE {self.__main_table} SET {field} = '{new_value}' WHERE {condition};")

    def delete(self,condition: str):
        self.execute(
            f"DELETE FROM {self.__main_table} WHERE {condition};")

    def create_objects_from_sql(self, create_object_func, name_class_ratio, exception_class):
        sql_data = self.execute(f"SELECT * FROM {self.__main_table}")
        for data in sql_data:
            try:
                if data[3] != "Не определено":
                    create_object_func(name_class_ratio[data[3]], data[1:3] + data[4:6])
                else:
                    create_object_func(exception_class, data[1:3] + data[4:6])
            except Exception as e:
                raise IOError(f"Ошибка с чтением данных из "
                              f"таблицы {self.__main_table} базы данных {self.__database}")


if __name__ == '__main__':
    db = SQLConnect("localhost", "root", input("Enter mysql password: "), "man_friends_db")
    db.execute_from_file("man-friends-db.sql")
    db.import_from_csv_file("parent_class", "man-friends.csv")
    print(db.execute("SELECT * FROM parent_class;"))
