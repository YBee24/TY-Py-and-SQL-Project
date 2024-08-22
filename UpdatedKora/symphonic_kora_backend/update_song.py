from config import get_db_connection
from flask import render_template_string, redirect, url_for

def handle_update_song(song_id, form_data):
    song_name = form_data.get('song_name')
    artist = form_data.get('artist')
    genre = form_data.get('genre')
    mood = form_data.get('mood')
    year_of_release = form_data.get('year_of_release')
    youtube_url = form_data.get('youtube_url')

    # Database connection and update operation
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute(
        "UPDATE Songs SET SongName = %s, Artist = %s, Genre = %s, Mood = %s, Year_of_Release = %s, YouTubeURL = %s WHERE SongID = %s",
        (song_name, artist, genre, mood, year_of_release, youtube_url, song_id)
    )
    db_conn.commit()
    cursor.close()
    db_conn.close()

    # Redirect to the "All Songs" page after updating the song
    return redirect(url_for('get_all_songs'))

def render_update_song_form(song_id):
    # Fetching the existing song details from the database
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Songs WHERE SongID = %s", (song_id,))
    song = cursor.fetchone()
    cursor.close()
    db_conn.close()

    # HTML form pre-filled with the current song details
    return render_template_string('''
        <html>
        <head>
            <title>Update Song</title>
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
                <form method="post">
                    Song Name: <input type="text" name="song_name" value="{{ song['SongName'] }}" required><br>
                    Artist: <input type="text" name="artist" value="{{ song['Artist'] }}" required><br>
                    Genre: <input type="text" name="genre" value="{{ song['Genre'] }}" required><br>
                    Mood: <input type="text" name="mood" value="{{ song['Mood'] }}" required><br>
                    Year of Release: <input type="number" name="year_of_release" value="{{ song['Year_of_Release'] }}" required><br>
                    YouTube URL: <input type="text" name="youtube_url" value="{{ song['YouTubeURL'] }}" required><br>
                    <input type="submit" value="Update Song">
                </form>
                <a href="{{ url_for('get_all_songs') }}">Back to All Songs</a>
            </div>
        </body>
        </html>
    ''', song=song)
