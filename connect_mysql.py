import mysql.connector
from mysql.connector import Error

def connect_db():
    db_name = "library_management_system"
    user = "root"
    password = "[Enter Your Password]"
    host = "localhost"

    try:
        conn=mysql.connector.connect(
            database = db_name,
            user=user,
            password=password,
            host=host
        )

        if conn.is_connected():
            print ("Connected to MySQL database successfully")
            return conn
    except Error as e:
        print(f"Error: {e}")