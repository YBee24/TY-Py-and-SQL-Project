from config import get_db_connection
from flask import redirect, url_for, render_template_string, flash

def render_add_song_to_playlist_form(playlist_id):
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)

    # Fetch playlist details
    cursor.execute("SELECT * FROM Playlists WHERE PlaylistID = %s", (playlist_id,))
    playlist = cursor.fetchone()

    if not playlist:
        cursor.close()
        db_conn.close()
        return render_template_string('<p>Playlist not found.</p>')

    # Fetch all songs
    cursor.execute("SELECT * FROM Songs")
    all_songs = cursor.fetchall()

    # Fetch songs already in the playlist
    cursor.execute("SELECT SongID FROM PlaylistOperations WHERE PlaylistID = %s", (playlist_id,))
    existing_songs = [song['SongID'] for song in cursor.fetchall()]

    # Filter songs not already in the playlist
    available_songs = [song for song in all_songs if song['SongID'] not in existing_songs]

    cursor.close()
    db_conn.close()

    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Add Song to {{ playlist['PlaylistName'] }}</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    padding: 20px;
                }
                h1 {
                    color: #333;
                }
                form {
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    width: 50%;
                    margin: 0 auto;
                }
                label {
                    display: block;
                    margin-bottom: 10px;
                    font-weight: bold;
                }
                select {
                    width: 100%;
                    padding: 10px;
                    margin-bottom: 20px;
                    border-radius: 5px;
                    border: 1px solid #ccc;
                }
                input[type="submit"] {
                    background-color: #28a745;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #218838;
                }
                .links {
                    text-align: center;
                    margin-top: 20px;
                }
                .links a {
                    margin: 0 10px;
                    text-decoration: none;
                    color: #007BFF;
                }
                .links a:hover {
                    color: #0056b3;
                }
            </style>
        </head>
        <body>
            <h1>Add Song to "{{ playlist['PlaylistName'] }}"</h1>
            {% if available_songs %}
            <form method="post">
                <label for="song">Select Song:</label>
                <select name="song_id" required>
                    {% for song in available_songs %}
                        <option value="{{ song['SongID'] }}">{{ song['SongName'] }} by {{ song['Artist'] }}</option>
                    {% endfor %}
                </select>
                <input type="submit" value="Add Song">
            </form>
            {% else %}
                <p>All available songs are already added to this playlist.</p>
            {% endif %}
            <div class="links">
                <a href="{{ url_for('get_single_playlist', playlist_id=playlist['PlaylistID']) }}">Back to Playlist Details</a>
                <a href="{{ url_for('get_all_playlists') }}">Back to All Playlists</a>
            </div>
        </body>
        </html>
    ''', available_songs=available_songs, playlist=playlist)


def handle_add_song_to_playlist(playlist_id, form_data):
    song_id = form_data.get('song_id')

    if not song_id:
        flash('No song selected.', 'error')
        return redirect(url_for('add_song_to_playlist', playlist_id=playlist_id))

    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO PlaylistOperations (PlaylistID, SongID) VALUES (%s, %s)",
            (playlist_id, song_id)
        )
        db_conn.commit()
        flash('Song added to playlist successfully!', 'success')
    except Exception as e:
        db_conn.rollback()
        flash('An error occurred while adding the song to the playlist.', 'error')
        print(f"Error: {e}")
    finally:
        cursor.close()
        db_conn.close()

    return redirect(url_for('get_single_playlist', playlist_id=playlist_id))


def handle_remove_song_from_playlist(playlist_id, song_id):
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM PlaylistOperations WHERE PlaylistID = %s AND SongID = %s",
            (playlist_id, song_id)
        )
        db_conn.commit()
        flash('Song removed from playlist successfully!', 'success')
    except Exception as e:
        db_conn.rollback()
        flash('An error occurred while removing the song from the playlist.', 'error')
        print(f"Error: {e}")
    finally:
        cursor.close()
        db_conn.close()

    return redirect(url_for('get_single_playlist', playlist_id=playlist_id))
