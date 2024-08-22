# Importing the get_db_connection function from the config module
# This function is used to establish a connection to the database
from config import get_db_connection

# Importing necessary functions from the Flask module
# url_for: Generates a URL for a given endpoint
# render_template_string: Renders a template from a string
from flask import url_for, render_template_string

# Function to render all songs in the database
def render_all_songs():
    # Establishing the database connection
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)  # Creating a cursor object to execute SQL queries, with results returned as dictionaries

    # Fetching all songs from the Songs table
    cursor.execute("SELECT * FROM Songs")
    songs = cursor.fetchall()  # Fetching all songs

    # Closing the cursor and database connection
    cursor.close()
    db_conn.close()

    # Generating HTML for the list of songs
    html_rows = ''.join(
        f"<tr>"
        f"<td>{song['SongID']}</td>"  # Displaying the SongID
        f"<td>{song['SongName']}</td>"  # Displaying the SongName
        f"<td>{song['Artist']}</td>"  # Displaying the Artist
        f"<td>{song['Genre']}</td>"  # Displaying the Genre
        f"<td class='action-buttons'>"  # Adding action buttons for each song
        f"<a href='{url_for('get_song', song_id=song['SongID'])}' class='btn btn-primary'>View Details</a>"  # Link to view song details
        f"<a href='{url_for('update_existing_song', song_id=song['SongID'])}' class='btn btn-secondary'>Update</a>"  # Link to update the song
        f"<form action='{url_for('delete_existing_song', song_id=song['SongID'])}' method='post' style='display:inline;'>"
        f"<button type='submit' class='btn btn-danger'>Delete</button></form>"  # Button to delete the song
        f"</td>"
        f"</tr>"
        for song in songs
    )

    # Returning HTML that displays all songs
    return render_template_string(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>All Songs</title>
            <style>
                /* Basic styling for the page */
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    padding: 20px;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }}
                th, td {{
                    padding: 10px;
                    text-align: left;
                    border-bottom: 1px solid #ddd;
                }}
                th {{
                    background-color: #007BFF;
                    color: white;
                }}
                tr:hover {{
                    background-color: #f1f1f1;
                }}
                a.btn {{
                    text-decoration: none;
                    color: white;
                    padding: 5px 10px;
                    border-radius: 5px;
                    margin-right: 5px;
                    display: inline-block;
                }}
                .btn-primary {{
                    background-color: #007BFF;
                }}
                .btn-primary:hover {{
                    background-color: #0056b3;
                }}
                .btn-secondary {{
                    background-color: #6c757d;
                }}
                .btn-secondary:hover {{
                    background-color: #5a6268;
                }}
                .btn-danger {{
                    background-color: #dc3545;
                    color: white;
                    border: none;
                    cursor: pointer;
                }}
                .btn-danger:hover {{
                    background-color: #c82333;
                }}
                .action-buttons {{
                    display: flex;
                    gap: 5px;
                }}
            </style>
        </head>
        <body>
            <h1>All Songs</h1>
            <table border="1">
                <tr>
                    <th>Song ID</th>
                    <th>Song Name</th>
                    <th>Artist</th>
                    <th>Genre</th>
                    <th>Actions</th>
                </tr>
                {html_rows}
            </table>
        </body>
        </html>
    """)
