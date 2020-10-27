import sqlite3

def connect():
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS expense (id INTEGER PRIMARY KEY, year integer, month integer, day integer, category text, value real, concept text)")
    conn.commit()
    conn.close()

def insert(year, month, day, category, value, concept):
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO expense VALUES (NULL,?,?,?,?,?,?)", (year, month, day, category, value, concept)) # With NULL Python understands that has to increment id automatically
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("SELECT * from expense")
    rows = cur.fetchall()
    conn.close()
    return rows

# Or search: By one entry or by all at the same time
def search(year = "", month = "", day = "", category = "", value = "", concept = ""): # With default empty strings you allow to search by only one those arguments
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM expense WHERE year = ? OR month = ? OR day = ? OR category = ? OR value = ? OR concept = ?", (year, month, day, category, value, concept))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id): # We're gonna get id from tuple and index 0
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM expense WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update(id, year, month, day, category, value, concept):
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("UPDATE expense SET year = ?, month = ?, day = ?, category = ?, value = ?, concept = ? WHERE id = ?", (year, month, day, category, value, concept, id))
    conn.commit()
    conn.close()


connect() # This way, this function will run everytime you run frontend when importing backend into frontend script

#print(view())
#insert(2020, 10, 26, "Transport", 10.25, "T-10 ticket")
#insert(2020, 10, 27, "Food", 5.62, "Iogurts")
#insert(2020, 10, 28, "Food", 5.97, "Iogurts bio")
#update(3, 2021, 10, 4, "Food", 3.48, "Snack")
#print(view())