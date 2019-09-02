import pymysql.cursors
import re


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_project_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select name from mantis_project_table")
            for row in cursor:
                list.append(self.clear(str(row)))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def clear(self, s):
        return re.sub("[() '',]", "", s)

