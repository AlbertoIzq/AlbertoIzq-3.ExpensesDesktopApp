import sqlite3

class Database:

    def __init__(self, db): # Constructor
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS expense (id INTEGER PRIMARY KEY, year integer, month integer, day integer, category text, value real, concept text)")
        conn.commit()
        conn.close()

    def insert(self, year, month, day, category, value, concept):
        if not isinstance(year, int) or not isinstance(value, float): # If year is not an int or value is not a real number, then skip inserting
            return
        conn = sqlite3.connect("expenses.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO expense VALUES (NULL,?,?,?,?,?,?)", (year, month, day, category, value, concept)) # With NULL Python understands that has to increment id automatically
        conn.commit()
        conn.close()

    def view(self):
        conn = sqlite3.connect("expenses.db")
        cur = conn.cursor()
        cur.execute("SELECT * from expense")
        rows = cur.fetchall()
        conn.close()
        return rows

    # Or search: By one entry or by all at the same time
    def search(self, year = "", month = "", day = "", category = "", value = "", concept = ""): # With default empty strings you allow to search by only one those arguments
        conn = sqlite3.connect("expenses.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM expense WHERE year = ? OR month = ? OR day = ? OR category = ? OR value = ? OR concept = ?", (year, month, day, category, value, concept))
        rows = cur.fetchall()
        conn.close()
        return rows

    def delete(self, id): # We're gonna get id from tuple and index 0
        conn = sqlite3.connect("expenses.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM expense WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def update(self, id, year, month, day, category, value, concept):
        if not isinstance(year, int) or not isinstance(value, float): # If year is not an int or value is not a real number, then skip updating
            return
        conn = sqlite3.connect("expenses.db")
        cur = conn.cursor()
        cur.execute("UPDATE expense SET year = ?, month = ?, day = ?, category = ?, value = ?, concept = ? WHERE id = ?", (year, month, day, category, value, concept, id))
        conn.commit()
        conn.close()