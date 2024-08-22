# Importing the get_db_connection function from the config module
# This function is used to establish a connection to the database
from config import get_db_connection

# Importing necessary functions from the Flask module
# redirect: Redirects the user to a different URL
# url_for: Generates a URL for a given endpoint
# render_template_string: Renders a template from a string
from flask import redirect, url_for, render_template_string

# Function to handle the addition of a new playlist to the database
def handle_add_playlist(form_data):
    # Extracting data submitted from the form
    playlist_name = form_data.get('playlist_name')  # Get the playlist name from the form data
    description = form_data.get('description')      # Get the description of the playlist from the form data

    # Establishing a connection to the database
    db_conn = get_db_connection()
    cursor = db_conn.cursor()  # Creating a cursor object to execute SQL queries

    # Executing an SQL query to insert the new playlist into the Playlists table
    cursor.execute(
        "INSERT INTO Playlists (PlaylistName, Description) VALUES (%s, %s)",
        (playlist_name, description)
    )

    # Committing the transaction to save changes to the database
    db_conn.commit()

    # Closing the cursor and database connection
    cursor.close()
    db_conn.close()

    # Redirecting the user to the "All Playlists" page after the playlist is added
    return redirect(url_for('get_all_playlists'))

# Function to render a form for adding a new playlist
def render_add_playlist_form():
    # HTML form for adding a new playlist to the database
    html_form = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Add New Playlist</title>
        <style>
            /* Basic styling for the form */
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                padding: 20px;
            }
            .container {
                max-width: 600px;
                margin: auto;
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                font-size: 24px;
                color: #333;
            }
            form {
                display: flex;
                flex-direction: column;
            }
            label, input, textarea {
                margin-bottom: 10px;
            }
            input[type="text"], textarea {
                padding: 10px;
                font-size: 16px;
                border-radius: 5px;
                border: 1px solid #ccc;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                color: #fff;
                background-color: #007BFF;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Add New Playlist</h1>
            <!-- The form where users input details about the playlist -->
            <form method="post">
                <label for="playlist_name">Playlist Name:</label>
                <input type="text" id="playlist_name" name="playlist_name" required>

                <label for="description">Description:</label>
                <textarea id="description" name="description"></textarea>

                <button type="submit">Add Playlist</button>
            </form>
            <!-- Link to navigate back to the home page -->
            <a href="{{ url_for('home') }}">Back to Home</a>
        </div>
    </body>
    </html>
    """
    # Rendering the HTML form as a string and returning it
    return render_template_string(html_form)
