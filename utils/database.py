import sqlite3

def create_users_table():

    conn = sqlite3.connect("data/users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT,
        branch TEXT,
        year TEXT
    )
    """)

    conn.commit()
    conn.close()