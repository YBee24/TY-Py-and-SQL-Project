import mysql.connector

# This function opens the box and lets us put things in or take things out.
def create_connection():
    return mysql.connector.connect(
        host="localhost",  # The name of the box
        user="root",  # The key to open the box
        password="root",  # The secret code for the box
        database="symphonic_kora_library"  # The specific box we want to play with
    )
