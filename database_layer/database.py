import sqlite3

def init_db():
    conn = sqlite3.connect("farming_ai.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS recommendations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    farmer_name TEXT,
                    recommendation TEXT
                )''')
    conn.commit()
    conn.close()

def store_result(name, recommendation):
    conn = sqlite3.connect("farming_ai.db")
    c = conn.cursor()
    c.execute("INSERT INTO recommendations (farmer_name, recommendation) VALUES (?, ?)", (name, recommendation))
    conn.commit()
    conn.close()
