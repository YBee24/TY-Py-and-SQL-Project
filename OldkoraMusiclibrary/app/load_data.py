import pandas as pd
import mysql.connector
from .config import create_connection

# Load the Excel file
excel_file_path = '"C:\Users\natur\Documents\New folder\TY Python & SQL Project.xlsx"'  # Replace with the actual path to the Excel file
data = pd.read_excel(excel_file_path)

# Connect to the MySQL database
conn = create_connection()
cursor = conn.cursor()

# Iterate through the rows in the Excel file
for index, row in data.iterrows():
    # Insert playlist data into the playlists table
    cursor.execute(
        "INSERT INTO playlists (user_id, name, description) VALUES (%s, %s, %s)",
        (1, row['Playlist Name'], row['Description'])  # Assuming user_id=1 for now
    )
    playlist_id = cursor.lastrowid  # Get the ID of the newly created playlist

    # Insert track data into the tracks table
    cursor.execute(
        "INSERT INTO tracks (playlist_id, title, artist, youtube_link) VALUES (%s, %s, %s, %s)",
        (playlist_id, row['Track Name'], row['Artist'], row['YouTube Link'])
    )

conn.commit()  # Save all the changes to the database
cursor.close()
conn.close()
