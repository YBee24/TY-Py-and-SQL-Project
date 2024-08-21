from config import *

def update_playlist(playlist_id, data):
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute("""
        UPDATE Playlists
        SET PlaylistName = %s, Description = %s
        WHERE PlaylistID = %s
    """, (data['PlaylistName'], data['Description'], playlist_id))
    db_conn.commit()
    cursor.close()
    db_conn.close()

    html_content = """
    <html>
    <head>
        <title>Playlist Updated</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f4; }
            .container { width: 80%; margin: auto; text-align: center; padding: 20px; }
            .message { font-size: 24px; color: #333; }
            header { background-color: #333; color: white; padding: 10px 0; text-align: center; }
            h1 { margin: 0; font-size: 24px; }
        </style>
    </head>
    <body>
        <header>
            <h1>Playlist Updated</h1>
        </header>
        <div class="container">
            <p class="message">Playlist updated successfully.</p>
        </div>
    </body>
    </html>
    """
    return html_content, 200
