from config import get_db_connection
from flask import redirect, url_for, render_template_string

def handle_add_song(form_data):
    # Extracting form data
    song_name = form_data.get('song_name')
    artist = form_data.get('artist')
    genre = form_data.get('genre')
    mood = form_data.get('mood')
    year_of_release = form_data.get('year_of_release')
    youtube_url = form_data.get('youtube_url')

    # Database connection and insertion
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute(
        "INSERT INTO Songs (SongName, Artist, Genre, Mood, Year_of_Release, YouTubeURL) VALUES (%s, %s, %s, %s, %s, %s)",
        (song_name, artist, genre, mood, year_of_release, youtube_url)
    )
    db_conn.commit()
    cursor.close()
    db_conn.close()

    # Redirect to the "All Songs" page after adding the song
    return redirect(url_for('get_all_songs'))


def add_youtube_song(artist, title, video_id):
    db_conn = get_db_connection()
    cursor = db_conn.cursor()

    # Define the insert query
    query = """
        INSERT INTO Songs (SongName, Artist, Genre, Mood, Year_of_Release, YouTubeURL)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    # Since this is from YouTube, some fields will be left as placeholders
    cursor.execute(query, (title, artist, 'Unknown', 'Unknown', 2023, f'https://www.youtube.com/watch?v={video_id}'))

    db_conn.commit()
    cursor.close()
    db_conn.close()

    return redirect(url_for('get_all_songs'))

def render_add_youtube_song_form(video):
    html_content = f"""
    <html>
    <head>
        <title>Add YouTube Song</title>
    </head>
    <body>
        <h1>Add Song: {video['title']}</h1>
        <form method="POST">
            <input type="hidden" name="title" value="{video['title']}">
            <input type="hidden" name="artist" value="{video['artist']}">
            <input type="hidden" name="video_id" value="{video['video_id']}">
            <input type="submit" value="Add Song">
        </form>
        <a href="{{ url_for('home') }}">Back to Home</a>
    </body>
    </html>
    """
    return render_template_string(html_content)

from flask import render_template_string

def render_add_song_form():
    html_form = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Add New Song</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                padding: 20px;
            }
            .container {
                max-width: 600px;
                margin: auto;
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                font-size: 24px;
                color: #333;
            }
            form {
                display: flex;
                flex-direction: column;
            }
            label, input, textarea {
                margin-bottom: 10px;
            }
            input[type="text"], textarea {
                padding: 10px;
                font-size: 16px;
                border-radius: 5px;
                border: 1px solid #ccc;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                color: #fff;
                background-color: #007BFF;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Add New Song</h1>
            <form method="post">
                <label for="song_name">Song Name:</label>
                <input type="text" id="song_name" name="song_name" required>

                <label for="artist">Artist:</label>
                <input type="text" id="artist" name="artist" required>

                <label for="genre">Genre:</label>
                <input type="text" id="genre" name="genre">

                <label for="mood">Mood:</label>
                <input type="text" id="mood" name="mood">

                <label for="youtube_url">YouTube URL:</label>
                <input type="text" id="youtube_url" name="youtube_url">

                <button type="submit">Add Song</button>
            </form>
            <a href="{{ url_for('home') }}">Back to Home</a>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_form)
