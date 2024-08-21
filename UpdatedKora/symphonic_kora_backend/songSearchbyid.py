
from config import *
def get_song_details(song_id):
    db_conn = get_db_connection()  # Establish database connection

    cursor = db_conn.cursor(dictionary=True)  # Create a cursor object

    cursor.execute("SELECT * FROM Songs WHERE SongID = %s", (song_id,))  # Execute SQL query to fetch the song

    song = cursor.fetchone()  # Fetch the result

    cursor.close()  # Close the cursor

    db_conn.close()  # Close the database connection

    if song:

        # Create an HTML table with the song details

        html_table_rows = ''.join(f"<tr><td>{key}</td><td>{value}</td></tr>" for key, value in song.items())

        html_content = f"""

        <html>

        <head>

            <title>Song Details</title>

            <style>

                body {{

                    font-family: Arial, sans-serif;

                    margin: 0;

                    padding: 0;

                    background-color: #f4f4f4;

                }}

                .container {{

                    width: 80%;

                    margin: auto;

                    overflow: hidden;

                }}

                header {{

                    background: #333;

                    color: #fff;

                    padding: 10px 0;

                    text-align: center;

                }}

                table {{

                    width: 100%;

                    border-collapse: collapse;

                    margin: 20px 0;

                    background: #fff;

                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);

                }}

                table th, table td {{

                    padding: 12px;

                    text-align: left;

                }}

                table th {{

                    background: #333;

                    color: #fff;

                }}

                table tr:nth-child(even) {{

                    background: #f2f2f2;

                }}

                .message {{

                    text-align: center;

                    margin-top: 50px;

                }}

            </style>

        </head>

        <body>

            <header>

                <h1>Song Details</h1>

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

        return html_content, 200  # Return the HTML content with 200 status

    else:

        html_content = """

        <html>

        <head>

            <title>Song Not Found</title>

            <style>

                body {{

                    font-family: Arial, sans-serif;

                    margin: 0;

                    padding: 0;

                    background-color: #f4f4f4;

                }}

                .container {{

                    width: 80%;

                    margin: auto;

                    text-align: center;

                    padding: 20px;

                }}

                .message {{

                    font-size: 24px;

                    color: #333;

                }}

                header {{

                    background: #333;

                    color: #fff;

                    padding: 10px 0;

                    text-align: center;

                }}

            </style>

        </head>

        <body>

            <header>

                <h1>Song Not Found</h1>

            </header>

            <div class="container">

                <p class="message">The song you are looking for does not exist.</p>

            </div>

        </body>

        </html>

        """

        return html_content, 404  # Return 404 status with not found HTML
