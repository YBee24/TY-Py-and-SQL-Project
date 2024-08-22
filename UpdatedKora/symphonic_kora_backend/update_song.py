# Importing the get_db_connection function from the config module
# This function is used to establish a connection to the database
from config import get_db_connection

# Importing necessary functions from the Flask module
# render_template_string: Renders a template from a string
# redirect: Redirects the user to a different URL
# url_for: Generates a URL for a given endpoint
from flask import render_template_string, redirect, url_for

# Function to handle the updating of an existing song in the database
def handle_update_song(song_id, form_data):
    # Extracting the updated song details from the form data
    song_name = form_data.get('song_name')          # Get the updated song name
    artist = form_data.get('artist')                # Get the updated artist name
    genre = form_data.get('genre')                  # Get the updated genre
    mood = form_data.get('mood')                    # Get the updated mood
    year_of_release = form_data.get('year_of_release')  # Get the updated year of release
    youtube_url = form_data.get('youtube_url')      # Get the updated YouTube URL

    # Establishing a connection to the database
    db_conn = get_db_connection()
    cursor = db_conn.cursor()  # Creating a cursor object to execute SQL queries

    # Executing an SQL query to update the song in the Songs table
    cursor.execute(
        "UPDATE Songs SET SongName = %s, Artist = %s, Genre = %s, Mood = %s, Year_of_Release = %s, YouTubeURL = %s WHERE SongID = %s",
        (song_name, artist, genre, mood, year_of_release, youtube_url, song_id)
    )

    # Committing the transaction to save changes to the database
    db_conn.commit()

    # Closing the cursor and database connection
    cursor.close()
    db_conn.close()

    # Redirecting the user to the "All Songs" page after the song is updated
    return redirect(url_for('get_all_songs'))

# Function to render a form for updating an existing song
def render_update_song_form(song_id):
    # Establishing a connection to the database
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)  # Creating a cursor object to execute SQL queries, with results returned as dictionaries

    # Executing an SQL query to fetch the details of the song to be updated
    cursor.execute("SELECT * FROM Songs WHERE SongID = %s", (song_id,))
    song = cursor.fetchone()  # Fetching the first (and only) result from the query

    # Closing the cursor and database connection
    cursor.close()
    db_conn.close()

    # HTML form pre-filled with the current song details
    return render_template_string('''
        <html>
        <head>
            <title>Update Song</title>
            <style>
                /* Basic styling for the form */
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
                input[type="text"], input[type="number"] {
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
                <h1>Update Song</h1>
                <!-- The form is pre-filled with the current song details -->
                <form method="post">
                    Song Name: <input type="text" name="song_name" value="{{ song['SongName'] }}" required><br>
                    Artist: <input type="text" name="artist" value="{{ song['Artist'] }}" required><br>
                    Genre: <input type="text" name="genre" value="{{ song['Genre'] }}" required><br>
                    Mood: <input type="text" name="mood" value="{{ song['Mood'] }}" required><br>
                    Year of Release: <input type="number" name="year_of_release" value="{{ song['Year_of_Release'] }}" required><br>
                    YouTube URL: <input type="text" name="youtube_url" value="{{ song['YouTubeURL'] }}" required><br>
                    <input type="submit" value="Update Song">
                </form>
                <!-- Link to navigate back to the "All Songs" page -->
                <a href="{{ url_for('get_all_songs') }}">Back to All Songs</a>
            </div>
        </body>
        </html>
    ''', song=song)  # Passing the song details to the template
