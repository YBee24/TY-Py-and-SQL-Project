from config import get_db_connection
from flask import url_for, render_template_string

def render_playlist_details(playlist_id):
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)

    # Fetching playlist details
    cursor.execute("SELECT * FROM Playlists WHERE PlaylistID = %s", (playlist_id,))
    playlist = cursor.fetchone()

    if not playlist:
        cursor.close()
        db_conn.close()
        return render_template_string('<p>Playlist not found.</p>')

    # Fetching songs in the playlist
    cursor.execute("""
        SELECT s.SongID, s.SongName, s.Artist
        FROM PlaylistOperations po
        JOIN Songs s ON po.SongID = s.SongID
        WHERE po.PlaylistID = %s
    """, (playlist_id,))
    songs_in_playlist = cursor.fetchall()

    cursor.close()
    db_conn.close()

    # Generate HTML for songs in the playlist
    songs_html = ''.join(
        f"<li>{song['SongName']} by {song['Artist']} - "
        f"<a href='{url_for('get_song', song_id=song['SongID'])}'>View Song</a> | "
        f"<form action='{url_for('remove_song_from_playlist', playlist_id=playlist_id, song_id=song['SongID'])}' method='post' style='display:inline;'><button type='submit'>Remove</button></form>"
        f"</li>"
        for song in songs_in_playlist
    )

    # Return HTML with playlist details and songs
    return render_template_string(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Playlist Details</title>
            <style>
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
            <a href="{{{{ url_for('add_song_to_playlist', playlist_id=playlist['PlaylistID']) }}}}">Add Song to Playlist</a>
            <a href="{{{{ url_for('get_all_playlists') }}}}" class="back-link">Back to All Playlists</a>
        </body>
        </html>
    """, playlist=playlist)
