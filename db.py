import sqlite3

class DataBase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs(
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        company TEXT,
        start_date TEXT,
        deadline TEXT,
        salary REAL,
        email TEXT
        )
        """)
        self.conn.commit()

    def add(self, add_info):
        self.cursor.execute("""
        INSERT INTO jobs(name, description, company, start_date, deadline, salary, email) VALUES(?, ?, ?, ?, ?, ?, ?)
        """, (add_info.name, add_info.description, add_info.company, add_info.start_date, add_info.deadline, add_info.salary, add_info.email))
        self.conn.commit()

    