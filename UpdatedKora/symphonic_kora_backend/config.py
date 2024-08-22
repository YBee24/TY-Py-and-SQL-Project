# Import the mysql.connector module, which provides the interface to connect to MySQL databases
import mysql.connector

# Define a function to establish and return a connection to the MySQL database
def get_db_connection():
    # Use the mysql.connector.connect() function to create a connection object
    # This function requires several parameters to be passed:
    return mysql.connector.connect(
        host="localhost",      # The hostname or IP address where the MySQL server is running. 'localhost' means it's on the same machine as the code.
        user="root",           # The username to log into the MySQL server. 'root' is the default administrative account in MySQL.
        password="root",       # The password for the MySQL 'root' user account. This should be replaced with your actual password.
        database="MusicLibrary" # The name of the specific database within MySQL to connect to. In this case, it's 'MusicLibrary'.
    )
    # The function returns the connection object, which can be used to interact with the database.

