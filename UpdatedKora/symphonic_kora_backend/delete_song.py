from config import get_db_connection
from flask import render_template_string, redirect, url_for

def handle_delete_song(song_id):
    # Database connection and delete operation
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute("DELETE FROM Songs WHERE SongID = %s", (song_id,))
    db_conn.commit()
    cursor.close()
    db_conn.close()

    # Redirect to the "All Songs" page after deleting the song
    return redirect(url_for('get_all_songs'))

def render_delete_song_form(song_id):
    # Fetching the song details for confirmation before deletion
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Songs WHERE SongID = %s", (song_id,))
    song = cursor.fetchone()
    cursor.close()
    db_conn.close()

    # HTML form pre-filled with the current song details for confirmation
    return render_template_string('''
        <html>
        <head>
            <title>Delete Song</title>
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
                p {
                    font-size: 18px;
                    margin-bottom: 20px;
                }
                input[type="submit"], .cancel-button {
                    background-color: #007BFF;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    text-decoration: none;
                }
                input[type="submit"]:hover, .cancel-button:hover {
                    background-color: #0056b3;
                }
                a.cancel-button {
                    background-color: #e7e7e7;
                    color: #333;
                    display: inline-block;
                    margin-left: 10px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Delete Song</h1>
                <p>Are you sure you want to delete the song "{{ song['SongName'] }}" by {{ song['Artist'] }}?</p>
                <form method="post">
                    <input type="submit" value="Delete Song">
                    <a href="{{ url_for('get_all_songs') }}" class="cancel-button">Cancel</a>
                </form>
            </div>
        </body>
        </html>
    ''', song=song)
