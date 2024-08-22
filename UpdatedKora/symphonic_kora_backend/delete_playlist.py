from config import get_db_connection
from flask import redirect, url_for, render_template_string

def handle_delete_playlist(playlist_id):
    # Database connection and delete operation
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute("DELETE FROM Playlists WHERE PlaylistID = %s", (playlist_id,))
    db_conn.commit()
    cursor.close()
    db_conn.close()

    # Redirect to the "All Playlists" page after deleting the playlist
    return redirect(url_for('get_all_playlists'))

def render_delete_playlist_form(playlist_id):
    # Fetching the playlist details to confirm deletion
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Playlists WHERE PlaylistID = %s", (playlist_id,))
    playlist = cursor.fetchone()
    cursor.close()
    db_conn.close()

    # HTML form to confirm deletion
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Delete Playlist</title>
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
                    text-align: center;
                }
                input[type="submit"] {
                    background-color: #d9534f;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #c9302c;
                }
                a {
                    display: block;
                    margin-top: 20px;
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
                <h1>Delete Playlist</h1>
                <p>Are you sure you want to delete the playlist "<strong>{{ playlist['PlaylistName'] }}</strong>"?</p>
                <form method="post">
                    <input type="submit" value="Confirm Delete">
                </form>
                <a href="{{ url_for('get_all_playlists') }}">Back to All Playlists</a>
            </div>
        </body>
        </html>
    ''', playlist=playlist)
