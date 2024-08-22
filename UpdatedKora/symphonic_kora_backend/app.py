# Importing necessary modules and functions from Flask and other custom files
from flask import Flask, request, redirect, url_for, render_template_string
from songSearchbyid import handle_song_search, render_song_details
from get_songs import render_all_songs
from add_song import render_add_song_form, handle_add_song, add_youtube_song
from update_song import render_update_song_form, handle_update_song
from delete_song import render_delete_song_form, handle_delete_song
from get_playlist import render_all_playlists
from add_playlist import render_add_playlist_form, handle_add_playlist
from update_playlist import render_update_playlist_form, handle_update_playlist
from delete_playlist import render_delete_playlist_form, handle_delete_playlist
from get_playlistID import render_playlist_details
from add_song_to_playlist import render_add_song_to_playlist_form, handle_add_song_to_playlist, handle_remove_song_from_playlist

# Create an instance of the Flask class
app = Flask(__name__)

# Set a secret key, which is necessary for managing sessions, flash messages, etc.
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Define the route for the home page ('/')
@app.route('/')
def home():
    # Render the home page using an inline HTML template
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Symphonic Kora Library</title>
        <style>
            /* Basic styling for the web page */
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
                text-align: center;
                padding: 20px;
                margin: 0;
            }
            .container {
                width: 80%;
                max-width: 1200px;
                margin: 0 auto;
                background-color: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                font-size: 36px;
                margin-bottom: 20px;
            }
            h2 {
                font-size: 24px;
                margin-bottom: 20px;
            }
            .section {
                margin-bottom: 40px;
            }
            .button-group {
                display: flex;
                justify-content: space-around;
                margin-top: 20px;
            }
            .button-group a {
                text-decoration: none;
                color: #fff;
                background-color: #007BFF;
                padding: 10px 20px;
                border-radius: 5px;
                transition: background-color 0.3s;
            }
            .button-group a:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Symphonic Kora Library</h1>
            <h2>Welcome to the ultimate music library experience</h2>
            <div class="section">
                <h2>Songs</h2>
                <div class="button-group">
                    <!-- Links to different song management actions -->
                    <a href="{{ url_for('get_all_songs') }}">View All Songs</a>
                    <a href="{{ url_for('add_new_song') }}">Add New Song</a>
                    <a href="{{ url_for('search_song') }}">Search Song</a>
                </div>
            </div>
            <div class="section">
                <h2>Playlists</h2>
                <div class="button-group">
                    <!-- Links to different playlist management actions -->
                    <a href="{{ url_for('get_all_playlists') }}">View All Playlists</a>
                    <a href="{{ url_for('add_new_playlist') }}">Add New Playlist</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    ''')

# Define the route to view all songs
@app.route('/songs', methods=['GET'])
def get_all_songs():
    # Calls the function to render and display all songs
    return render_all_songs()

# Define the route to add a new song
@app.route('/songs/add', methods=['GET', 'POST'])
def add_new_song():
    # If the request is a POST request (i.e., form submission), add the new song
    if request.method == 'POST':
        handle_add_song(request.form)
        # Redirect to the page that displays all songs
        return redirect(url_for('get_all_songs'))
    # If it's a GET request, render the form to add a new song
    return render_add_song_form()

# Define the route to update an existing song
@app.route('/songs/update/<int:song_id>', methods=['GET', 'POST'])
def update_existing_song(song_id):
    # If the request is a POST request, update the song details
    if request.method == 'POST':
        handle_update_song(song_id, request.form)
        # Redirect to the page that displays all songs
        return redirect(url_for('get_all_songs'))
    # If it's a GET request, render the form to update the song
    return render_update_song_form(song_id)

# Define the route to delete an existing song
@app.route('/songs/delete/<int:song_id>', methods=['GET', 'POST'])
def delete_existing_song(song_id):
    # If the request is a POST request, delete the song
    if request.method == 'POST':
        handle_delete_song(song_id)
        # Redirect to the page that displays all songs
        return redirect(url_for('get_all_songs'))
    # If it's a GET request, render the form to confirm deletion
    return render_delete_song_form(song_id)

# Define the route to search for songs
@app.route('/songs/search', methods=['GET', 'POST'])
def search_song():
    # If the request is a POST request, process the search
    if request.method == 'POST':
        return handle_song_search(request.form)
    # If it's a GET request, render the search form
    return '''
    <form method="post">
        Song Name: <input type="text" name="song_name"><br>
        Song ID: <input type="number" name="song_id"><br>
        Artist: <input type="text" name="artist"><br>
        <input type="submit" value="Search">
    </form>
    '''

# Define the route to get details of a specific song
@app.route('/songs/<int:song_id>', methods=['GET'])
def get_song(song_id):
    # Calls the function to render and display details of the specified song
    return render_song_details(song_id)

# Define the route to view all playlists
@app.route('/playlists', methods=['GET'])
def get_all_playlists():
    # Calls the function to render and display all playlists
    return render_all_playlists()

# Define the route to add a new playlist
@app.route('/playlists/add', methods=['GET', 'POST'])
def add_new_playlist():
    # If the request is a POST request, add the new playlist
    if request.method == 'POST':
        handle_add_playlist(request.form)
        # Redirect to the page that displays all playlists
        return redirect(url_for('get_all_playlists'))
    # If it's a GET request, render the form to add a new playlist
    return render_add_playlist_form()

# Define the route to update an existing playlist
@app.route('/playlists/update/<int:playlist_id>', methods=['GET', 'POST'])
def update_existing_playlist(playlist_id):
    # If the request is a POST request, update the playlist details
    if request.method == 'POST':
        handle_update_playlist(playlist_id, request.form)
        # Redirect to the page that displays all playlists
        return redirect(url_for('get_all_playlists'))
    # If it's a GET request, render the form to update the playlist
    return render_update_playlist_form(playlist_id)

# Define the route to delete an existing playlist
@app.route('/playlists/delete/<int:playlist_id>', methods=['GET', 'POST'])
def delete_existing_playlist(playlist_id):
    # If the request is a POST request, delete the playlist
    if request.method == 'POST':
        handle_delete_playlist(playlist_id)
        # Redirect to the page that displays all playlists
        return redirect(url_for('get_all_playlists'))
    # If it's a GET request, render the form to confirm deletion
    return render_delete_playlist_form(playlist_id)

# Define the route to get details of a specific playlist
@app.route('/playlists/<int:playlist_id>', methods=['GET'])
def get_single_playlist(playlist_id):
    # Calls the function to render and display details of the specified playlist
    return render_playlist_details(playlist_id)

# Define the route to add a song to a specific playlist
@app.route('/playlists/<int:playlist_id>/add_song', methods=['GET', 'POST'])
def add_song_to_playlist(playlist_id):
    # If the request is a POST request, add the song to the playlist
    if request.method == 'POST':
        handle_add_song_to_playlist(playlist_id, request.form)
        # Redirect to the page that displays details of the specific playlist
        return redirect(url_for('get_single_playlist', playlist_id=playlist_id))
    # If it's a GET request, render the form to add a song to the playlist
    return render_add_song_to_playlist_form(playlist_id)

# Define the route to remove a song from a specific playlist
@app.route('/playlists/<int:playlist_id>/remove_song/<int:song_id>', methods=['POST'])
def remove_song_from_playlist(playlist_id, song_id):
    # Calls the function to remove the song from the playlist
    return handle_remove_song_from_playlist(playlist_id, song_id)

# Define the route to add a song from YouTube
@app.route('/songs/add_youtube', methods=['POST'])
def add_youtube_song_route():
    # Extract the title, artist, and video ID from the submitted form data
    title = request.form['title']
    artist = request.form['artist']
    video_id = request.form['video_id']
    # Calls the function to add the YouTube song to the library
    add_youtube_song(artist, title, video_id)
    # Redirect to the page that displays all songs
    return redirect(url_for('get_all_songs'))

# Check if the script is being run directly (not imported)
if __name__ == '__main__':
    # Run the Flask application on port 5001 with debug mode enabled
    app.run(debug=True, port=5001)
