# Importing the get_db_connection function from the config module
# This function is used to establish a connection to the database
from config import get_db_connection

# Importing necessary functions from the Flask module
# url_for: Generates a URL for a given endpoint
# render_template_string: Renders a template from a string
from flask import url_for, render_template_string

# Function to render the details of a specific playlist
def render_playlist_details(playlist_id):
    # Establishing the database connection
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)  # Creating a cursor object to execute SQL queries, with results returned as dictionaries

    # Fetching playlist details from the Playlists table
    cursor.execute("SELECT * FROM Playlists WHERE PlaylistID = %s", (playlist_id,))
    playlist = cursor.fetchone()  # Fetching the playlist details

    # If the playlist does not exist, close the connection and return a message
    if not playlist:
        cursor.close()
        db_conn.close()
        return render_template_string('<p>Playlist not found.</p>')

    # Fetching songs in the playlist by joining PlaylistOperations and Songs tables
    cursor.execute("""
        SELECT s.SongID, s.SongName, s.Artist
        FROM PlaylistOperations po
        JOIN Songs s ON po.SongID = s.SongID
        WHERE po.PlaylistID = %s
    """, (playlist_id,))
    songs_in_playlist = cursor.fetchall()  # Fetching all songs in the playlist

    # Closing the cursor and database connection
    cursor.close()
    db_conn.close()

    # Generating HTML for each song in the playlist
    songs_html = ''.join(
        f"<li>{song['SongName']} by {song['Artist']} - "
        f"<a href='{url_for('get_song', song_id=song['SongID'])}'>View Song</a> | "
        f"<form action='{url_for('remove_song_from_playlist', playlist_id=playlist_id, song_id=song['SongID'])}' method='post' style='display:inline;'><button type='submit'>Remove</button></form>"
        f"</li>"
        for song in songs_in_playlist
    )

    # Returning HTML that includes the playlist details and the list of songs
    return render_template_string(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Playlist Details</title>
            <style>
                /* Basic styling for the page */
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    padding: 20px;
                }}
                h1 {{
                    color: #333;
                }}
                ul {{
                    list-style-type: none;
                    padding: 0;
                }}
                li {{
                    background-color: #fff;
                    margin: 5px 0;
                    padding: 10px;
                    border-radius: 5px;
                    box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
                }}
                a {{
                    text-decoration: none;
                    color: #007BFF;
                }}
                a:hover {{
                    color: #0056b3;
                }}
                .back-link {{
                    display: block;
                    margin-top: 20px;
                    text-align: center;
                    text-decoration: none;
                    color: #007BFF;
                }}
                .back-link:hover {{
                    color: #0056b3;
                }}
            </style>
        </head>
        <body>
            <h1>{{{{ playlist['PlaylistName'] }}}}</h1>
            <p>{{{{ playlist['Description'] }}}}</p>
            <h2>Songs in Playlist:</h2>
            <ul>
                {songs_html}
            </ul>
            <!-- Link to add a song to the playlist -->
            <a href="{{{{ url_for('add_song_to_playlist', playlist_id=playlist['PlaylistID']) }}}}">Add Song to Playlist</a>
            <!-- Link to go back to all playlists -->
            <a href="{{{{ url_for('get_all_playlists') }}}}" class="back-link">Back to All Playlists</a>
        </body>
        </html>
    """, playlist=playlist)  # Passing the playlist details to the template
