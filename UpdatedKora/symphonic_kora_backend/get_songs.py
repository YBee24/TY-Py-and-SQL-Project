from config import *

def get_songs():
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Songs")
    songs = cursor.fetchall()
    cursor.close()
    db_conn.close()

    if songs:
        html_table_rows = ''.join(
            f"<tr><td>{song['SongID']}</td><td>{song['SongName']}</td><td>{song['Artist']}</td></tr>"
            for song in songs
        )
        html_content = f"""
        <html>
        <head>
            <title>All Songs</title>
            <style>
                body {{ font-family: Arial, sans-serif; background-color: #f4f4f4; }}
                .container {{ width: 80%; margin: auto; padding: 20px; }}
                table {{ width: 100%; border-collapse: collapse; margin: 20px 0; background: #fff; }}
                table th, table td {{ padding: 12px; text-align: left; border: 1px solid #ddd; }}
                table th {{ background: #333; color: #fff; }}
                table tr:nth-child(even) {{ background: #f2f2f2; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>All Songs</h1>
                <table>
                    <tr>
                        <th>Song ID</th>
                        <th>Song Name</th>
                        <th>Artist</th>
                    </tr>
                    {html_table_rows}
                </table>
            </div>
        </body>
        </html>
        """
        return html_content, 200
    else:
        html_content = """
        <html>
        <head>
            <title>No Songs Found</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #f4f4f4; }
                .container { width: 80%; margin: auto; text-align: center; padding: 20px; }
                .message { font-size: 24px; color: #333; }
            </style>
        </head>
        <body>
            <div class="container">
                <p class="message">No songs found in the database.</p>
            </div>
        </body>
        </html>
        """
        return html_content, 404
