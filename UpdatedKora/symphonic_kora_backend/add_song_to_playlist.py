# Importing the get_db_connection function from the config module
# This function is used to establish a connection to the database
from config import get_db_connection

# Importing necessary functions from the Flask module
# render_template_string: Renders a template from a string
# redirect: Redirects the user to a different URL
# url_for: Generates a URL for a given endpoint
# flash: Allows flashing messages to the user
from flask import redirect, url_for, render_template_string, flash

# Function to render a form for adding a song to a specific playlist
def render_add_song_to_playlist_form(playlist_id):
    # Establishing the database connection
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)  # Creating a cursor object to execute SQL queries, with results returned as dictionaries

    # Fetch playlist details
    cursor.execute("SELECT * FROM Playlists WHERE PlaylistID = %s", (playlist_id,))
    playlist = cursor.fetchone()  # Fetching the playlist details

    # If the playlist does not exist, close the connection and return a message
    if not playlist:
        cursor.close()
        db_conn.close()
        return render_template_string('<p>Playlist not found.</p>')

    # Fetch all songs from the database
    cursor.execute("SELECT * FROM Songs")
    all_songs = cursor.fetchall()  # Fetching all songs

    # Fetch songs already in the playlist
    cursor.execute("SELECT SongID FROM PlaylistOperations WHERE PlaylistID = %s", (playlist_id,))
    existing_songs = [song['SongID'] for song in cursor.fetchall()]  # Fetching song IDs already in the playlist

    # Filter songs that are not already in the playlist
    available_songs = [song for song in all_songs if song['SongID'] not in existing_songs]

    # Closing the cursor and database connection
    cursor.close()
    db_conn.close()

    # Returning the HTML form for adding a song to the playlist
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Add Song to {{ playlist['PlaylistName'] }}</title>
            <style>
                /* Basic styling for the form */
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
    ''', available_songs=available_songs, playlist=playlist)  # Passing the available songs and playlist details to the template

# Function to handle adding a song to a specific playlist
def handle_add_song_to_playlist(playlist_id, form_data):
    # Extract the song ID from the form data
    song_id = form_data.get('song_id')

    # If no song is selected, flash an error message and redirect to the add song form
    if not song_id:
        flash('No song selected.', 'error')
        return redirect(url_for('add_song_to_playlist', playlist_id=playlist_id))

    # Establishing the database connection
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    try:
        # Insert the song into the PlaylistOperations table
        cursor.execute(
            "INSERT INTO PlaylistOperations (PlaylistID, SongID) VALUES (%s, %s)",
            (playlist_id, song_id)
        )
        db_conn.commit()  # Commit the transaction
        flash('Song added to playlist successfully!', 'success')
    except Exception as e:
        db_conn.rollback()  # Rollback the transaction in case of error
        flash('An error occurred while adding the song to the playlist.', 'error')
        print(f"Error: {e}")  # Print the error for debugging purposes
    finally:
        cursor.close()
        db_conn.close()  # Close the database connection

    # Redirect to the playlist details page after adding the song
    return redirect(url_for('get_single_playlist', playlist_id=playlist_id))

# Function to handle removing a song from a specific playlist
def handle_remove_song_from_playlist(playlist_id, song_id):
    # Establishing the database connection
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    try:
        # Delete the song from the PlaylistOperations table
        cursor.execute(
            "DELETE FROM PlaylistOperations WHERE PlaylistID = %s AND SongID = %s",
            (playlist_id, song_id)
        )
        db_conn.commit()  # Commit the transaction
        flash('Song removed from playlist successfully!', 'success')
    except Exception as e:
        db_conn.rollback()  # Rollback the transaction in case of error
        flash('An error occurred while removing the song from the playlist.', 'error')
        print(f"Error: {e}")  # Print the error for debugging purposes
    finally:
        cursor.close()
        db_conn.close()  # Close the database connection

    # Redirect to the playlist details page after removing the song
    return redirect(url_for('get_single_playlist', playlist_id=playlist_id))
