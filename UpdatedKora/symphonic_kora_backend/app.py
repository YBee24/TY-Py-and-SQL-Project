from flask import Flask, request, redirect, url_for, render_template_string, flash
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
from youtube_search import search_youtube_for_artist

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Home page route
@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Symphonic Kora Library</title>
        <style>
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
                    <a href="{{ url_for('get_all_songs') }}">View All Songs</a>
                    <a href="{{ url_for('add_new_song') }}">Add New Song</a>
                    <a href="{{ url_for('search_song') }}">Search Song</a>
                </div>
            </div>
            <div class="section">
                <h2>Playlists</h2>
                <div class="button-group">
                    <a href="{{ url_for('get_all_playlists') }}">View All Playlists</a>
                    <a href="{{ url_for('add_new_playlist') }}">Add New Playlist</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    ''')

# Song routes
@app.route('/songs', methods=['GET'])
def get_all_songs():
    return render_all_songs()

@app.route('/songs/add', methods=['GET', 'POST'])
def add_new_song():
    if request.method == 'POST':
        handle_add_song(request.form)
        return redirect(url_for('get_all_songs'))
    return render_add_song_form()

@app.route('/songs/update/<int:song_id>', methods=['GET', 'POST'])
def update_existing_song(song_id):
    if request.method == 'POST':
        handle_update_song(song_id, request.form)
        return redirect(url_for('get_all_songs'))
    return render_update_song_form(song_id)

@app.route('/songs/delete/<int:song_id>', methods=['GET', 'POST'])
def delete_existing_song(song_id):
    if request.method == 'POST':
        handle_delete_song(song_id)
        return redirect(url_for('get_all_songs'))
    return render_delete_song_form(song_id)

@app.route('/songs/search', methods=['GET', 'POST'])
def search_song():
    if request.method == 'POST':
        return handle_song_search(request.form)
    return '''
    <form method="post">
        Song Name: <input type="text" name="song_name"><br>
        Song ID: <input type="number" name="song_id"><br>
        Artist: <input type="text" name="artist"><br>
        <input type="submit" value="Search">
    </form>
    '''

@app.route('/songs/<int:song_id>', methods=['GET'])
def get_song(song_id):
    return render_song_details(song_id)

# Playlist routes
@app.route('/playlists', methods=['GET'])
def get_all_playlists():
    return render_all_playlists()

@app.route('/playlists/add', methods=['GET', 'POST'])
def add_new_playlist():
    if request.method == 'POST':
        handle_add_playlist(request.form)
        return redirect(url_for('get_all_playlists'))
    return render_add_playlist_form()

@app.route('/playlists/update/<int:playlist_id>', methods=['GET', 'POST'])
def update_existing_playlist(playlist_id):
    if request.method == 'POST':
        handle_update_playlist(playlist_id, request.form)
        return redirect(url_for('get_all_playlists'))
    return render_update_playlist_form(playlist_id)

@app.route('/playlists/delete/<int:playlist_id>', methods=['GET', 'POST'])
def delete_existing_playlist(playlist_id):
    if request.method == 'POST':
        handle_delete_playlist(playlist_id)
        return redirect(url_for('get_all_playlists'))
    return render_delete_playlist_form(playlist_id)

@app.route('/playlists/<int:playlist_id>', methods=['GET'])
def get_single_playlist(playlist_id):
    return render_playlist_details(playlist_id)

@app.route('/playlists/<int:playlist_id>/add_song', methods=['GET', 'POST'])
def add_song_to_playlist(playlist_id):
    if request.method == 'POST':
        handle_add_song_to_playlist(playlist_id, request.form)
        return redirect(url_for('get_single_playlist', playlist_id=playlist_id))
    return render_add_song_to_playlist_form(playlist_id)

@app.route('/playlists/<int:playlist_id>/remove_song/<int:song_id>', methods=['POST'])
def remove_song_from_playlist(playlist_id, song_id):
    return handle_remove_song_from_playlist(playlist_id, song_id)

# Add YouTube Song route
@app.route('/songs/add_youtube', methods=['POST'])
def add_youtube_song_route():
    title = request.form['title']
    artist = request.form['artist']
    video_id = request.form['video_id']
    add_youtube_song(artist, title, video_id)
    return redirect(url_for('get_all_songs'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
