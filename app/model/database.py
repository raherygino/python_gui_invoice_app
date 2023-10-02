import sqlite3

class Database():

    def __init__(self):
        CONN = sqlite3.connect('database.db')
        self.CURSOR = CONN.cursor()
        self.CURSOR.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, code TEXT, designation TEXT)")

    def fetch(self) -> list:
        self.CURSOR.execute("SELECT * FROM products")
        return self.CURSOR.fetchall()
    
    def query(self, query: str):
        self.CURSOR.execute(query)

