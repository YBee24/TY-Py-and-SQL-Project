from config import get_db_connection
from flask import redirect, url_for, render_template_string

def handle_update_playlist(playlist_id, form_data):
    playlist_name = form_data.get('playlist_name')
    description = form_data.get('description')

    # Database connection and update operation
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute(
        "UPDATE Playlists SET PlaylistName = %s, Description = %s WHERE PlaylistID = %s",
        (playlist_name, description, playlist_id)
    )
    db_conn.commit()
    cursor.close()
    db_conn.close()

    # Redirect to the "All Playlists" page after updating the playlist
    return redirect(url_for('get_all_playlists'))

def render_update_playlist_form(playlist_id):
    # Fetching the existing playlist details from the database
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Playlists WHERE PlaylistID = %s", (playlist_id,))
    playlist = cursor.fetchone()
    cursor.close()
    db_conn.close()

    # HTML form pre-filled with the current playlist details
    return render_template_string('''
        <html>
        <head>
            <title>Update Playlist</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    padding: 20px;
                }
                .container {
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    width: 50%;
                    margin: 0 auto;
                }
                input[type="text"] {
                    width: 100%;
                    padding: 10px;
                    margin: 10px 0;
                    border-radius: 5px;
                    border: 1px solid #ccc;
                }
                input[type="submit"] {
                    background-color: #007BFF;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #0056b3;
                }
                a {
                    display: block;
                    margin-top: 20px;
                    text-align: center;
                    text-decoration: none;
                    color: #007BFF;
                }
                a:hover {
                    color: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Update Playlist</h1>
                <form method="post">
                    <label for="playlist_name">Playlist Name:</label>
                    <input type="text" id="playlist_name" name="playlist_name" value="{{ playlist['PlaylistName'] }}" required>
                    <label for="description">Description:</label>
                    <input type="text" id="description" name="description" value="{{ playlist['Description'] }}">
                    <input type="submit" value="Update Playlist">
                </form>
                <a href="{{ url_for('get_all_playlists') }}">Back to All Playlists</a>
            </div>
        </body>
        </html>
    ''', playlist=playlist)
