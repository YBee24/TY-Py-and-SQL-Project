# Importing the get_db_connection function from the config module
# This function is used to establish a connection to the database
from config import get_db_connection

# Importing necessary functions from the Flask module
# redirect: Redirects the user to a different URL
# url_for: Generates a URL for a given endpoint
# render_template_string: Renders a template from a string
from flask import redirect, url_for, render_template_string

# Function to handle the addition of a new song to the database
def handle_add_song(form_data):
    # Extracting data submitted from the form
    song_name = form_data.get('song_name')  # Get the song name from the form data
    artist = form_data.get('artist')        # Get the artist's name from the form data
    genre = form_data.get('genre')          # Get the genre from the form data
    mood = form_data.get('mood')            # Get the mood from the form data
    year_of_release = form_data.get('year_of_release')  # Get the year of release from the form data
    youtube_url = form_data.get('youtube_url')          # Get the YouTube URL from the form data

    # Establishing a connection to the database
    db_conn = get_db_connection()
    cursor = db_conn.cursor()  # Creating a cursor object to execute SQL queries

    # Executing an SQL query to insert the new song into the Songs table
    cursor.execute(
        "INSERT INTO Songs (SongName, Artist, Genre, Mood, Year_of_Release, YouTubeURL) VALUES (%s, %s, %s, %s, %s, %s)",
        (song_name, artist, genre, mood, year_of_release, youtube_url)
    )

    # Committing the transaction to save changes to the database
    db_conn.commit()

    # Closing the cursor and database connection
    cursor.close()
    db_conn.close()

    # Redirecting the user to the "All Songs" page after the song is added
    return redirect(url_for('get_all_songs'))

# Function to add a song from YouTube to the database
def add_youtube_song(artist, title, video_id):
    # Establishing a connection to the database
    db_conn = get_db_connection()
    cursor = db_conn.cursor()  # Creating a cursor object to execute SQL queries

    # Defining the SQL query to insert the YouTube song into the Songs table
    query = """
        INSERT INTO Songs (SongName, Artist, Genre, Mood, Year_of_Release, YouTubeURL)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    # Executing the query with placeholders for the song details
    # Since this is from YouTube, some fields are set as 'Unknown' or use default values
    cursor.execute(query, (title, artist, 'Unknown', 'Unknown', 2023, f'https://www.youtube.com/watch?v={video_id}'))

    # Committing the transaction to save changes to the database
    db_conn.commit()

    # Closing the cursor and database connection
    cursor.close()
    db_conn.close()

    # Redirecting the user to the "All Songs" page after the song is added
    return redirect(url_for('get_all_songs'))

# Function to render a form to add a YouTube song
def render_add_youtube_song_form(video):
    # HTML content for the form, which is dynamically generated based on the video's details
    html_content = f"""
    <html>
    <head>
        <title>Add YouTube Song</title>
    </head>
    <body>
        <h1>Add Song: {video['title']}</h1>
        <form method="POST">
            <!-- Hidden inputs to store the video's details that will be submitted with the form -->
            <input type="hidden" name="title" value="{video['title']}">
            <input type="hidden" name="artist" value="{video['artist']}">
            <input type="hidden" name="video_id" value="{video['video_id']}">
            <input type="submit" value="Add Song">
        </form>
        <!-- Link to navigate back to the home page -->
        <a href="{{ url_for('home') }}">Back to Home</a>
    </body>
    </html>
    """
    # Rendering the HTML content as a string and returning it
    return render_template_string(html_content)

# Function to render a form for adding a new song
def render_add_song_form():
    # HTML form for adding a new song to the database
    html_form = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Add New Song</title>
        <style>
            /* Basic styling for the form */
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
            <!-- The form where users input details about the song -->
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
            <!-- Link to navigate back to the home page -->
            <a href="{{ url_for('home') }}">Back to Home</a>
        </div>
    </body>
    </html>
    """
    # Rendering the HTML form as a string and returning it
    return render_template_string(html_form)
