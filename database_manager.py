import sqlite3 as sq
import json


class DatabaseManager:
    def __init__(self):
        self.con = sq.connect('main.db')
        self.cur = self.con.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.con.commit()
        self.con.close()

    def create_database(self):
        self.cur.executescript("""
        DROP TABLE IF EXISTS cosmo_info;
        CREATE TABLE cosmo_info (
            data TEXT
        )
        """)

    def add_data(self, data):
        self.cur.execute("""
        INSERT INTO cosmo_info (data)
        VALUES (?)
        """, [json.dumps(data)])

    def get_data(self):
        self.cur.execute("""
        SELECT data
        FROM cosmo_info
        """)

        return json.loads(self.cur.fetchone()[0])


if __name__ == '__main__':
    with DatabaseManager() as db:
        db.create_database()

        db.add_data({'test': 'test'})

