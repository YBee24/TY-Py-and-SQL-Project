from config import *

def delete_song(song_id):
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute("DELETE FROM Songs WHERE SongID = %s", (song_id,))
    db_conn.commit()
    cursor.close()
    db_conn.close()

    html_content = """
    <html>
    <head>
        <title>Song Deleted</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f4; }
            .container { width: 80%; margin: auto; text-align: center; padding: 20px; }
            .message { font-size: 24px; color: #333; }
        </style>
    </head>
    <body>
        <div class="container">
            <p class="message">Song deleted successfully.</p>
        </div>
    </body>
    </html>
    """
    return html_content, 200
