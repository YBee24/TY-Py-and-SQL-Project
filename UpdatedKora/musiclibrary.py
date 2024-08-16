import pandas as pd  # Import the pandas library, which is used for handling data in tabular form
import mysql.connector  # Import MySQL connector to interact with the MySQL database

# Load the Excel file
file_path = r'D:\TYPython&SQLProject.xlsx'  # Define the path to the Excel file that contains your data
excel_data = pd.ExcelFile(file_path)  # Load the entire Excel file into a variable

# Read the information from 'Sheet1' (since it contains all the data)
full_df = excel_data.parse('Sheet1')  # Parse (read) the data from the first sheet named 'Sheet1' into a DataFrame

# Adjust the DataFrame creation to use the correct columns
songs_df = full_df[['ID', 'Track_Name']]  # Create a new DataFrame with only the 'ID' and 'Track_Name' columns

# Check for missing values in the DataFrame
print("Missing values before handling:")
print(songs_df.isna().sum())  # Print the number of missing values (NaNs) in each column of the DataFrame

# Handle missing values by dropping rows that contain them
songs_df = songs_df.dropna()  # Remove any rows from the DataFrame that have missing values

# After handling missing values, print the number of missing values again to confirm they are gone
print("Missing values after handling:")
print(songs_df.isna().sum())  # Should show 0 missing values in each column

# Connect to your MySQL database
db_connection = mysql.connector.connect(
    host="localhost",  # The server hosting the MySQL database (localhost means your own computer)
    user="root",  # The username to connect to the MySQL database (default is usually 'root')
    password="root",  # The password for the MySQL database user (set to 'root' here, but it could be different)
    database="MusicLibrary"  # The name of the database you want to connect to
)

cursor = db_connection.cursor()  # Create a cursor object, which is used to execute SQL commands

# Step 4: Create a table for storing songs in your digital library if it doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS Songs (
    SongID INT PRIMARY KEY,  # Define the SongID column as an integer and the primary key (unique identifier)
    SongName VARCHAR(100)  # Define the SongName column as a string with a maximum of 100 characters
)
""")

db_connection.commit()  # Save the changes made to the database (in this case, the creation of the table)

# Step 5: Fill the digital library with your songs from the DataFrame
for _, row in songs_df.iterrows():  # Iterate over each row in the DataFrame
    cursor.execute("""
    INSERT INTO Songs (SongID, SongName)
    VALUES (%s, %s)
    """, (row['ID'], row['Track_Name']))  # Insert the SongID and SongName into the Songs table

db_connection.commit()  # Save the changes made to the database (in this case, the insertion of data)

# Step 6: Check that everything worked by retrieving and printing all records from the Songs table
cursor.execute("SELECT * FROM Songs")  # Execute an SQL command to select all records from the Songs table
for row in cursor.fetchall():  # Fetch all the rows from the result of the query
    print(row)  # Print each row to verify that the data was inserted correctly

# Step 7: Close the connection to your digital library
cursor.close()  # Close the cursor to free up resources
db_connection.close()  # Close the database connection to free up resources
