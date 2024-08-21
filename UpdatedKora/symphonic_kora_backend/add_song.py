from config import get_db_connection

def add_song(data):
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute("""
        INSERT INTO Songs (SongName, Genre, Artist, Mood, Year_of_Release, YouTubeURL)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (data['SongName'], data['Genre'], data['Artist'], data['Mood'], data['Year_of_Release'], data['YouTubeURL']))
    db_conn.commit()
    cursor.close()
    db_conn.close()

    html_content = """
    <html>
    <head>
        <title>Song Added</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f4; }
            .container { width: 80%; margin: auto; text-align: center; padding: 20px; }
            .message { font-size: 24px; color: #333; }
        </style>
    </head>
    <body>
        <div class="container">
            <p class="message">Song added successfully.</p>
        </div>
    </body>
    </html>
    """
    return html_content, 201
