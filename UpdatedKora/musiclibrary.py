import pandas as pd
import mysql.connector
 
# Define the file path to the CSV file
file_path = r'C:\Users\M3Trainee\Downloads\SKL_Data.csv'
 
# Load the CSV file using Pandas with a specified encoding
songs_df = pd.read_csv(file_path, encoding='ISO-8859-1')
 
# Check for missing values in the DataFrame
print("Missing values before handling:")
print(songs_df.isna().sum())
 
# Handle missing values by dropping rows with any missing data
songs_df = songs_df.dropna()
 
# Check for missing values again after handling them
print("Missing values after handling:")
print(songs_df.isna().sum())
 
# Connect to your MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="MusicLibrary"
)
 
# Create a cursor object to interact with the database
cursor = db_connection.cursor()
 
# Loop through each row in the DataFrame 'songs_df'
for _, row in songs_df.iterrows():
    cursor.execute("""
    REPLACE INTO Songs (SongID, Genre, Artist, SongName, Mood, Year_of_Release, YouTubeURL)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (row['ID'], row['Genre'], row['Artist'], row['SongName'], row['Mood'], row['Year_of_Release'], row['YouTubeURL']))
 
# Commit the transaction to save all the changes to the database
db_connection.commit()
 
# Verify that the data was inserted correctly
cursor.execute("SELECT * FROM Songs")
for row in cursor.fetchall():
    print(row)
 
# Close the cursor and the database connection
cursor.close()
db_connection.close()
