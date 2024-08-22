# Importing the get_db_connection function from the config module
# This function is used to establish a connection to the database
from config import get_db_connection

# Importing necessary functions from the Flask module
# redirect: Redirects the user to a different URL
# url_for: Generates a URL for a given endpoint
# render_template_string: Renders a template from a string
from flask import redirect, url_for, render_template_string

# Function to handle the updating of an existing playlist in the database
def handle_update_playlist(playlist_id, form_data):
    # Extracting the updated playlist details from the form data
    playlist_name = form_data.get('playlist_name')  # Get the updated playlist name
    description = form_data.get('description')      # Get the updated description

    # Establishing a connection to the database
    db_conn = get_db_connection()
    cursor = db_conn.cursor()  # Creating a cursor object to execute SQL queries

    # Executing an SQL query to update the playlist in the Playlists table
    cursor.execute(
        "UPDATE Playlists SET PlaylistName = %s, Description = %s WHERE PlaylistID = %s",
        (playlist_name, description, playlist_id)
    )

    # Committing the transaction to save changes to the database
    db_conn.commit()

    # Closing the cursor and database connection
    cursor.close()
    db_conn.close()

    # Redirecting the user to the "All Playlists" page after the playlist is updated
    return redirect(url_for('get_all_playlists'))

# Function to render a form for updating an existing playlist
def render_update_playlist_form(playlist_id):
    # Establishing a connection to the database
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)  # Creating a cursor object to execute SQL queries, with results returned as dictionaries

    # Executing an SQL query to fetch the details of the playlist to be updated
    cursor.execute("SELECT * FROM Playlists WHERE PlaylistID = %s", (playlist_id,))
    playlist = cursor.fetchone()  # Fetching the first (and only) result from the query

    # Closing the cursor and database connection
    cursor.close()
    db_conn.close()

    # HTML form pre-filled with the current playlist details
    return render_template_string('''
        <html>
        <head>
            <title>Update Playlist</title>
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
                input[type="text"] {
                    width: 100%;
                    padding: 10px;
                    margin: 10px 0;
                    border-radius: 5px;
                    border: 1px solid #ccc;
                }
                input[type="submit"] {
                    background-color: #007BFF;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #0056b3;
                }
                a {
                    display: block;
                    margin-top: 20px;
                    text-align: center;
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
                <h1>Update Playlist</h1>
                <!-- The form is pre-filled with the current playlist details -->
                <form method="post">
                    <label for="playlist_name">Playlist Name:</label>
                    <input type="text" id="playlist_name" name="playlist_name" value="{{ playlist['PlaylistName'] }}" required>
                    <label for="description">Description:</label>
                    <input type="text" id="description" name="description" value="{{ playlist['Description'] }}">
                    <input type="submit" value="Update Playlist">
                </form>
                <!-- Link to navigate back to the "All Playlists" page -->
                <a href="{{ url_for('get_all_playlists') }}">Back to All Playlists</a>
            </div>
        </body>
        </html>
    ''', playlist=playlist)  # Passing the playlist details to the template
