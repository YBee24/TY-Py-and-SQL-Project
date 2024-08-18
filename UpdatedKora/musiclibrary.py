# Import necessary libraries
import pandas as pd  # Pandas is a powerful data manipulation library in Python
import mysql.connector  # mysql.connector is a library for connecting to and interacting with a MySQL database

# Define the file path to the Excel file
# This is the path where your Excel file is located on your computer
file_path = r'D:\TYPython&SQLProject.xlsx'

# Load the Excel file using Pandas
# pd.ExcelFile() loads the entire Excel workbook, allowing you to access individual sheets
excel_data = pd.ExcelFile(file_path)

# Parse the data from 'Sheet1'
# The parse() method reads the data from the specified sheet in the Excel file into a DataFrame
full_df = excel_data.parse('Sheet1')

# Create a DataFrame with the specific columns you want to work with
# The columns 'ID', 'Genre', 'Artist', 'Track_Name', 'Mood', 'Year _of _Release', and 'YouTube_Link' are selected
# from the Excel sheet to create a new DataFrame called 'songs_df'
songs_df = full_df[['ID', 'Genre', 'Artist', 'Track_Name', 'Mood', 'Year _of _Release', 'YouTube_Link']]

# Check for missing values in the DataFrame
# isna() checks for missing values (NaN) in each column, and sum() adds up the number of missing values per column
print("Missing values before handling:")
print(songs_df.isna().sum())  # This prints the count of missing values in each column before handling

# Handle missing values by dropping rows with any missing data
# dropna() removes any rows that contain NaN (missing) values
songs_df = songs_df.dropna()

# Check for missing values again after handling them
# This ensures that there are no missing values left in the DataFrame
print("Missing values after handling:")
print(songs_df.isna().sum())  # This prints the count of missing values in each column after handling

# Connect to your MySQL database
# mysql.connector.connect() establishes a connection to the MySQL database using the provided credentials
db_connection = mysql.connector.connect(
    host="localhost",  # The address of the database server (localhost means your own computer)
    user="root",  # The username to connect to the database (default is 'root')
    password="root",  # The password for the database user (set to 'root' here, but this can vary)
    database="MusicLibrary"  # The name of the database you want to connect to (replace with your database name)
)

# Create a cursor object to interact with the database
# A cursor is an interface for executing SQL commands and fetching data from the database
cursor = db_connection.cursor()

# Loop through each row in the DataFrame 'songs_df'
# iterrows() generates an iterator that yields index, row pairs
for _, row in songs_df.iterrows():
    # Execute an SQL REPLACE command to insert the song data into the 'Songs' table
    # REPLACE works like an INSERT, but if a record with the same primary key exists, it deletes it first
    # and then inserts the new record (effectively an update operation)
    cursor.execute("""
    REPLACE INTO Songs (SongID, Genre, Artist, Track_Name, Mood, Year_of_Release, YouTube_Link)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (row['ID'], row['Genre'], row['Artist'], row['Track_Name'], row['Mood'], row['Year _of _Release'], row['YouTube_Link']))

# Commit the transaction to save all the changes to the database
# This makes sure that all the insertions are finalized in the database
db_connection.commit()

# Verify that the data was inserted correctly by selecting and printing all records from the 'Songs' table
cursor.execute("SELECT * FROM Songs")
for row in cursor.fetchall():
    print(row)  # Print each row of the result to the console

# Close the cursor to free up resources
cursor.close()

# Close the database connection to free up resources
db_connection.close()
