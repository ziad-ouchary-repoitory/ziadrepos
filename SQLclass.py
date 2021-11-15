import pyodbc


class SQLConnection:


    def __init__(self,server, db):
        self.s = server
        self.d = db
        global conn 
        self.conn = pyodbc.connect(driver='{SQL Server Native Client 11.0}',
                              host=self.s, database=self.d, trusted_connection='yes')
        global cursor
        self.cursor = self.conn.cursor()

    def select(self,query):
        self.cursor.execute(query)
        for row in self.cursor:
            print(row)

    def operation(self, query, values):
        self.cursor.execute(query, values)
        self.cursor.commit()

    def get_conn(self):
        return self.conn

    def get_closeConn(self):
        return self.conn.close()