# Importing the get_db_connection function from the config module
# This function is used to establish a connection to the database
from config import get_db_connection

# Importing necessary functions from the Flask module
# redirect: Redirects the user to a different URL
# url_for: Generates a URL for a given endpoint
# render_template_string: Renders a template from a string
from flask import redirect, url_for, render_template_string

# Function to handle the deletion of an existing playlist in the database
def handle_delete_playlist(playlist_id):
    # Establishing a connection to the database
    db_conn = get_db_connection()
    cursor = db_conn.cursor()  # Creating a cursor object to execute SQL queries

    # Executing an SQL query to delete the playlist from the Playlists table
    cursor.execute("DELETE FROM Playlists WHERE PlaylistID = %s", (playlist_id,))

    # Committing the transaction to save changes to the database
    db_conn.commit()

    # Closing the cursor and database connection
    cursor.close()
    db_conn.close()

    # Redirecting the user to the "All Playlists" page after the playlist is deleted
    return redirect(url_for('get_all_playlists'))

# Function to render a form for confirming the deletion of a playlist
def render_delete_playlist_form(playlist_id):
    # Establishing a connection to the database
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)  # Creating a cursor object to execute SQL queries, with results returned as dictionaries

    # Executing an SQL query to fetch the details of the playlist to be deleted
    cursor.execute("SELECT * FROM Playlists WHERE PlaylistID = %s", (playlist_id,))
    playlist = cursor.fetchone()  # Fetching the first (and only) result from the query

    # Closing the cursor and database connection
    cursor.close()
    db_conn.close()

    # HTML form to confirm deletion of the playlist
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Delete Playlist</title>
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
                    text-align: center;
                }
                input[type="submit"] {
                    background-color: #d9534f;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #c9302c;
                }
                a {
                    display: block;
                    margin-top: 20px;
                    text-decoration: none;
                    color: #007BFF;
                }
                a:hover {
                    color: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Delete Playlist</h1>
                <p>Are you sure you want to delete the playlist "<strong>{{ playlist['PlaylistName'] }}</strong>"?</p>
                <form method="post">
                    <!-- Button to confirm deletion of the playlist -->
                    <input type="submit" value="Confirm Delete">
                </form>
                <!-- Link to cancel deletion and return to the "All Playlists" page -->
                <a href="{{ url_for('get_all_playlists') }}">Back to All Playlists</a>
            </div>
        </body>
        </html>
    ''', playlist=playlist)  # Passing the playlist details to the template
