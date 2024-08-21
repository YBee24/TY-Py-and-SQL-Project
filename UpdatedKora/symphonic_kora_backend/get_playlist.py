from config import *

def get_playlist(playlist_id):
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Playlists WHERE PlaylistID = %s", (playlist_id,))
    playlist = cursor.fetchone()
    cursor.close()
    db_conn.close()

    if playlist:
        html_table_rows = ''.join(
            f"<tr><td>{key}</td><td>{value}</td></tr>" for key, value in playlist.items()
        )
        html_content = f"""
        <html>
        <head>
            <title>Playlist Details</title>
            <style>
                body {{ font-family: Arial, sans-serif; background-color: #f4f4f4; }}
                .container {{ width: 80%; margin: auto; padding: 20px; }}
                table {{ width: 100%; border-collapse: collapse; margin: 20px 0; background: #fff; }}
                table th, table td {{ padding: 12px; text-align: left; border: 1px solid #ddd; }}
                table th {{ background: #333; color: #fff; }}
                table tr:nth-child(even) {{ background: #f2f2f2; }}
                header {{ background-color: #333; color: white; padding: 10px 0; text-align: center; }}
                h1 {{ margin: 0; font-size: 24px; }}
            </style>
        </head>
        <body>
            <header>
                <h1>Playlist Details</h1>
            </header>
            <div class="container">
                <table>
                    <tr>
                        <th>Field</th>
                        <th>Value</th>
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
            <title>Playlist Not Found</title>
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
                <h1>Playlist Not Found</h1>
            </header>
            <div class="container">
                <p class="message">The playlist you are looking for does not exist.</p>
            </div>
        </body>
        </html>
        """
        return html_content, 404
