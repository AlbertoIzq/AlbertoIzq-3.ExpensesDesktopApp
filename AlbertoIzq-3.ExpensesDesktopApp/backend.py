import sqlite3

class Database:
    """Class to connect and manage a table in a MySQL database"""

    def __init__(self, db): # Constructor
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS expense (id INTEGER PRIMARY KEY, year integer, month integer, day integer, category text, value real, concept text)")
        self.conn.commit()

    def insert(self, year, month, day, category, value, concept):
        # If year is not an int or value is not a real number, then skip inserting
        try:
            year = int(year)
            value = float(value)
        except ValueError:
            return
        self.cur.execute("INSERT INTO expense VALUES (NULL,?,?,?,?,?,?)", (year, month, day, category, value, concept)) # With NULL Python understands that has to increment id automatically
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * from expense")
        rows = self.cur.fetchall()
        return rows

    # Or search: By one entry or by all at the same time
    def search(self, year = "", month = "", day = "", category = "", value = "", concept = ""): # With default empty strings you allow to search by only one those arguments
        self.cur.execute("SELECT * FROM expense WHERE year = ? OR month = ? OR day = ? OR category = ? OR value = ? OR concept = ?", (year, month, day, category, value, concept))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id): # We're gonna get id from tuple and index 0
        self.cur.execute("DELETE FROM expense WHERE id = ?", (id,))
        self.conn.commit()
        
    def update(self, id, year, month, day, category, value, concept):
        if not isinstance(year, int) or not isinstance(value, float): # If year is not an int or value is not a real number, then skip updating
            return
        self.cur.execute("UPDATE expense SET year = ?, month = ?, day = ?, category = ?, value = ?, concept = ? WHERE id = ?", (year, month, day, category, value, concept, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()