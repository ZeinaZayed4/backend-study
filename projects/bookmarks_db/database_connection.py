import psycopg2


class DatabaseConnection:
    def __init__(
        self, dbname="bookmarks_db", user="postgres", password="1234", host="localhost"
    ):
        self.conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host
        )
        self.cursor = self.conn.cursor()

    def execute(self, query, params=None):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()
