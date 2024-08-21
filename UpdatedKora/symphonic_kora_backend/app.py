from flask import Flask, request
from get_songs import get_songs
from add_song import add_song
from songSearchbyid import *
from update_song import *
from delete_song import *
from get_playlists import *
from get_playlist import *
from add_playlist import *
from update_playlist import *
from delete_playlist import *

app = Flask(__name__)

# Song routes
@app.route('/songs', methods=['GET'])
def get_all_songs():
    return get_songs()

@app.route('/songs/<int:song_id>', methods=['GET'])
def get_song(song_id):
        return get_song_details(song_id)

@app.route('/songs', methods=['POST'])
def add_new_song():
    data = request.json
    return add_song(data)

@app.route('/songs/<int:song_id>', methods=['PUT'])
def update_existing_song(song_id):
    data = request.json
    return update_song(song_id, data)

@app.route('/songs/<int:song_id>', methods=['DELETE'])
def delete_existing_song(song_id):
    return delete_song(song_id)

# Playlist routes
@app.route('/playlists', methods=['GET'])
def get_all_playlists():
    return get_playlists()

@app.route('/playlists/<int:playlist_id>', methods=['GET'])
def get_single_playlist(playlist_id):
    return get_playlist(playlist_id)

@app.route('/playlists', methods=['POST'])
def add_new_playlist():
    data = request.json
    return add_playlist(data)

@app.route('/playlists/<int:playlist_id>', methods=['PUT'])
def update_existing_playlist(playlist_id):
    data = request.json
    return update_playlist(playlist_id, data)

@app.route('/playlists/<int:playlist_id>', methods=['DELETE'])
def delete_existing_playlist(playlist_id):
    return delete_playlist(playlist_id)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
