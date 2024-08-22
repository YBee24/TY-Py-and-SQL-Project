from config import get_db_connection
from flask import redirect, url_for, render_template_string

def handle_add_playlist(form_data):
    playlist_name = form_data.get('playlist_name')
    description = form_data.get('description')

    # Database connection and insertion
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute(
        "INSERT INTO Playlists (PlaylistName, Description) VALUES (%s, %s)",
        (playlist_name, description)
    )
    db_conn.commit()
    cursor.close()
    db_conn.close()

    # Redirect to the "All Playlists" page after adding the playlist
    return redirect(url_for('get_all_playlists'))

def render_add_playlist_form():
    html_form = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Add New Playlist</title>
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
            <h1>Add New Playlist</h1>
            <form method="post">
                <label for="playlist_name">Playlist Name:</label>
                <input type="text" id="playlist_name" name="playlist_name" required>

                <label for="description">Description:</label>
                <textarea id="description" name="description"></textarea>

                <button type="submit">Add Playlist</button>
            </form>
            <a href="{{ url_for('home') }}">Back to Home</a>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_form)
