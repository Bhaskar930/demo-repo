import mysql.connector
from mysql.connector import Error

def get_sql_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",       # Replace with your actual host
            user="root",            # Replace with your actual username
            password="12345678",    # Replace with your actual password
            database="gs"           # Replace with your actual database name
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
        else:
            print("Failed to connect to the database")
            return None
    except Error as e:
        print(f"Error: {e}")
        return None
