from config import get_db_connection
from flask import url_for, render_template_string

def render_all_songs():
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)

    # Fetching all songs from the database
    cursor.execute("SELECT * FROM Songs")
    songs = cursor.fetchall()

    cursor.close()
    db_conn.close()

    # Generate HTML for the song list
    html_rows = ''.join(
        f"<tr>"
        f"<td>{song['SongID']}</td>"
        f"<td>{song['SongName']}</td>"
        f"<td>{song['Artist']}</td>"
        f"<td>{song['Genre']}</td>"
        f"<td>"
        f"<a href='{url_for('get_song', song_id=song['SongID'])}' class='btn btn-primary'>View Details</a>"
        f"<a href='{url_for('update_existing_song', song_id=song['SongID'])}' class='btn btn-secondary'>Update</a>"
        f"<form action='{url_for('delete_existing_song', song_id=song['SongID'])}' method='post' style='display:inline;'><button type='submit' class='btn btn-danger'>Delete</button></form>"
        f"</td>"
        f"</tr>"
        for song in songs
    )

    # Return HTML with all songs
    return render_template_string(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>All Songs</title>
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
                a.btn {{
                    text-decoration: none;
                    color: white;
                    padding: 5px 10px;
                    border-radius: 5px;
                    margin-right: 5px;
                    display: inline-block;
                }}
                .btn-primary {{
                    background-color: #007BFF;
                }}
                .btn-primary:hover {{
                    background-color: #0056b3;
                }}
                .btn-secondary {{
                    background-color: #6c757d;
                }}
                .btn-secondary:hover {{
                    background-color: #5a6268;
                }}
                .btn-danger {{
                    background-color: #dc3545;
                    color: white;
                    border: none;
                    cursor: pointer;
                }}
                .btn-danger:hover {{
                    background-color: #c82333;
                }}
                .action-buttons {{
                    display: flex;
                    gap: 5px;
                }}
            </style>
        </head>
        <body>
            <h1>All Songs</h1>
            <table border="1">
                <tr>
                    <th>Song ID</th>
                    <th>Song Name</th>
                    <th>Artist</th>
                    <th>Genre</th>
                    <th>Actions</th>
                </tr>
                {html_rows}
            </table>
        </body>
        </html>
    """)
