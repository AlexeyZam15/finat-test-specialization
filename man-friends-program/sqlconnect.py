import mysql.connector


class SQLConnect:
    def __init__(self, host: str, user: str, passwd: str):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
        )
        self.c = self.mydb.cursor()

    def execute_from_file(self, file_name: str):
        with open(file_name, "r") as f:
            query = ""
            for line in f:
                query += line
                if line.find(';') != -1:
                    self.c.execute(query.replace("\n", ""))
                    query = ""

    def execute(self, query: str):
        self.c.execute(query)
        return self.c.fetchall()

    def __del__(self):
        self.mydb.commit()
        self.mydb.close()


if __name__ == '__main__':
    db = SQLConnect("localhost", "root", input("Enter password: "))
    db.execute_from_file("man-friends-db.sql")
    print(db.execute("SELECT * FROM parent_class;"))
