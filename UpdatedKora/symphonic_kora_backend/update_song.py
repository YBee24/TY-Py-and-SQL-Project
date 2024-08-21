from config import *

def update_song(song_id, data):
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute("""
        UPDATE Songs
        SET SongName = %s, Genre = %s, Artist = %s, Mood = %s, Year_of_Release = %s, YouTubeURL = %s
        WHERE SongID = %s
    """, (data['SongName'], data['Genre'], data['Artist'], data['Mood'], data['Year_of_Release'], data['YouTubeURL'], song_id))
    db_conn.commit()
    cursor.close()
    db_conn.close()

    html_content = """
    <html>
    <head>
        <title>Song Updated</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f4; }
            .container { width: 80%; margin: auto; text-align: center; padding: 20px; }
            .message { font-size: 24px; color: #333; }
        </style>
    </head>
    <body>
        <div class="container">
            <p class="message">Song updated successfully.</p>
        </div>
    </body>
    </html>
    """
    return html_content, 200
