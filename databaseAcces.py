import sqlite3
from sqlite3 import Error

        


#database connection

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn
    
def extract_users():
    
    conn = create_connection("base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.commit()
    conn.close()

    return rows

def dbExtract(table, column, argument = ""):
    conn = create_connection("base.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT {column} FROM {table} {argument}")
    rows = cursor.fetchall()
    conn.commit()
    conn.close()

    return rows

def dbInsert(table, values):
    conn = create_connection("base.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {table} VALUES {values}")
    conn.commit()
    conn.close()

def dbExecute(command):
    conn = create_connection("base.db")
    cursor = conn.cursor()
    cursor.execute(command)
    conn.commit()
    conn.close()

def dbTableSize(table):
    conn = create_connection("base.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    size = cursor.fetchall()
    conn.commit()
    conn.close()

    return size

def dbGetID(table):
    conn = create_connection("base.db")
    cursor = conn.cursor()
    command = f"PRAGMA table_info({table})"
    cursor.execute(command)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()

    return rows



