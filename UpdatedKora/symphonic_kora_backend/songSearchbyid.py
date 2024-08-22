from youtube_search import search_youtube_for_artist
from config import get_db_connection
from flask import url_for, render_template_string

def render_song_list(songs):
    html_rows = ''.join(
        f"<tr><td>{song['SongName']}</td>"
        f"<td>{song['Artist']}</td>"
        f"<td>{song['Genre']}</td>"
        f"<td>{song['Mood']}</td>"
        f"<td><a href='/songs/{song['SongID']}'>View Details</a></td></tr>"
        for song in songs
    )
    return render_template_string(f"""
    <html>
    <head>
        <title>Song List</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                padding: 20px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}
            th, td {{
                padding: 10px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }}
            th {{
                background-color: #007BFF;
                color: white;
            }}
            tr:hover {{
                background-color: #f1f1f1;
            }}
            a {{
                text-decoration: none;
                color: #007BFF;
                padding: 10px 15px;
                border-radius: 5px;
                background-color: #e7e7e7;
            }}
            a:hover {{
                background-color: #0056b3;
                color: white;
            }}
        </style>
    </head>
    <body>
        <h1>Song List</h1>
        <table border="1">
            <tr><th>Song Name</th><th>Artist</th><th>Genre</th><th>Mood</th><th>Action</th></tr>
            {html_rows}
        </table>
        <a href="{{ url_for('home') }}">Back to Home</a>
    </body>
    </html>
    """)

def handle_song_search(form_data):
    song_id = form_data.get('song_id')
    song_name = form_data.get('song_name')
    artist = form_data.get('artist')

    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)

    if song_id:
        cursor.execute("SELECT * FROM Songs WHERE SongID = %s", (song_id,))
    elif song_name:
        cursor.execute("SELECT * FROM Songs WHERE SongName LIKE %s", ("%" + song_name + "%",))
    elif artist:
        cursor.execute("SELECT * FROM Songs WHERE Artist LIKE %s", ("%" + artist + "%",))

    songs = cursor.fetchall()
    cursor.close()
    db_conn.close()

    if songs:
        return render_song_list(songs)
    else:
        if artist:
            youtube_results = search_youtube_for_artist(artist)
            if youtube_results:
                return render_youtube_song_list(youtube_results, artist)
        return "<p>No songs found for the specified artist.</p>"

def render_song_details(song_id):
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Songs WHERE SongID = %s", (song_id,))
    song = cursor.fetchone()
    cursor.close()
    db_conn.close()

    if song:
        return render_template_string(f"""
        <html>
        <head>
            <title>{song['SongName']} - Details</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    padding: 20px;
                }}
                .container {{
                    max-width: 600px;
                    margin: auto;
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                }}
                h1 {{
                    font-size: 24px;
                    color: #333;
                }}
                p {{
                    font-size: 18px;
                    color: #666;
                }}
                a {{
                    text-decoration: none;
                    color: #007BFF;
                    background-color: #e7e7e7;
                    padding: 10px 15px;
                    border-radius: 5px;
                }}
                a:hover {{
                    background-color: #0056b3;
                    color: white;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>{song['SongName']}</h1>
                <p><strong>Artist:</strong> {song['Artist']}</p>
                <p><strong>Genre:</strong> {song['Genre']}</p>
                <p><strong>Mood:</strong> {song['Mood']}</p>
                <p><strong>Year of Release:</strong> {song['Year_of_Release']}</p>
                <p><a href="{song['YouTubeURL']}" target="_blank">Watch on YouTube</a></p>
                <a href="{{ url_for('get_all_songs') }}">Back to All Songs</a>
            </div>
        </body>
        </html>
        """)
    else:
        return render_template_string(f"""
        <html>
        <head>
            <title>Song Not Found</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    padding: 20px;
                    text-align: center;
                }}
                h1 {{
                    font-size: 24px;
                    color: #F44336;
                }}
                a {{
                    text-decoration: none;
                    color: #007BFF;
                    background-color: #e7e7e7;
                    padding: 10px 15px;
                    border-radius: 5px;
                }}
                a:hover {{
                    background-color: #0056b3;
                    color: white;
                }}
            </style>
        </head>
        <body>
            <h1>Song Not Found</h1>
            <p>The song you are looking for does not exist.</p>
            <a href="{{ url_for('get_all_songs') }}">Back to All Songs</a>
        </body>
        </html>
        """)

def render_youtube_song_list(youtube_results, artist):
    html_rows = ''.join(
        f"""
        <tr>
            <td>{video['title']}</td>
            <td>{artist}</td>
            <td><a href='https://www.youtube.com/watch?v={video['video_id']}' target='_blank'>Watch on YouTube</a></td>
            <td>
                <form action="{{{{ url_for('add_youtube_song_route') }}}}" method="post">
                    <input type="hidden" name="title" value="{video['title']}">
                    <input type="hidden" name="artist" value="{artist}">
                    <input type="hidden" name="video_id" value="{video['video_id']}">
                    <input type="submit" value="Add to Library">
                </form>
            </td>
        </tr>
        """ for video in youtube_results
    )

    return render_template_string(f"""
    <html>
    <head>
        <title>YouTube Results for {artist}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                padding: 20px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}
            th, td {{
                padding: 10px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }}
            th {{
                background-color: #007BFF;
                color: white;
            }}
            tr:hover {{
                background-color: #f1f1f1;
            }}
            a {{
                text-decoration: none;
                color: #007BFF;
                padding: 10px 15px;
                border-radius: 5px;
                background-color: #e7e7e7;
            }}
            a:hover {{
                background-color: #0056b3;
                color: white;
            }}
            input[type="submit"] {{
                background-color: #28a745;
                color: white;
                padding: 5px 10px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}
            input[type="submit"]:hover {{
                background-color: #218838;
            }}
        </style>
    </head>
    <body>
        <h1>YouTube Results for {artist}</h1>
        <table border="1">
            <tr><th>Title</th><th>Artist</th><th>Video</th><th>Action</th></tr>
            {html_rows}
        </table>
        <a href="{{{{ url_for('home') }}}}">Back to Home</a>
    </body>
    </html>
    """)
