# Importing the get_db_connection function from the config module
# This function is used to establish a connection to the database
from config import get_db_connection

# Importing necessary functions from the Flask module
# render_template_string: Renders a template from a string
# redirect: Redirects the user to a different URL
# url_for: Generates a URL for a given endpoint
from flask import render_template_string, redirect, url_for

# Function to handle the deletion of an existing song in the database
def handle_delete_song(song_id):
    # Establishing a connection to the database
    db_conn = get_db_connection()
    cursor = db_conn.cursor()  # Creating a cursor object to execute SQL queries

    # Executing an SQL query to delete the song from the Songs table
    cursor.execute("DELETE FROM Songs WHERE SongID = %s", (song_id,))

    # Committing the transaction to save changes to the database
    db_conn.commit()

    # Closing the cursor and database connection
    cursor.close()
    db_conn.close()

    # Redirecting the user to the "All Songs" page after the song is deleted
    return redirect(url_for('get_all_songs'))

# Function to render a form for confirming the deletion of a song
def render_delete_song_form(song_id):
    # Establishing a connection to the database
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)  # Creating a cursor object to execute SQL queries, with results returned as dictionaries

    # Executing an SQL query to fetch the details of the song to be deleted
    cursor.execute("SELECT * FROM Songs WHERE SongID = %s", (song_id,))
    song = cursor.fetchone()  # Fetching the first (and only) result from the query

    # Closing the cursor and database connection
    cursor.close()
    db_conn.close()

    # HTML form pre-filled with the current song details for confirmation
    return render_template_string('''
        <html>
        <head>
            <title>Delete Song</title>
            <style>
                /* Basic styling for the form */
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    padding: 20px;
                }
                .container {
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    width: 50%;
                    margin: 0 auto;
                }
                p {
                    font-size: 18px;
                    margin-bottom: 20px;
                }
                input[type="submit"], .cancel-button {
                    background-color: #007BFF;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    text-decoration: none;
                }
                input[type="submit"]:hover, .cancel-button:hover {
                    background-color: #0056b3;
                }
                a.cancel-button {
                    background-color: #e7e7e7;
                    color: #333;
                    display: inline-block;
                    margin-left: 10px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Delete Song</h1>
                <p>Are you sure you want to delete the song "{{ song['SongName'] }}" by {{ song['Artist'] }}?</p>
                <form method="post">
                    <!-- Button to confirm deletion of the song -->
                    <input type="submit" value="Delete Song">
                    <!-- Link to cancel the deletion and return to the "All Songs" page -->
                    <a href="{{ url_for('get_all_songs') }}" class="cancel-button">Cancel</a>
                </form>
            </div>
        </body>
        </html>
    ''', song=song)  # Passing the song details to the template
