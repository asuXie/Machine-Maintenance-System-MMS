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

