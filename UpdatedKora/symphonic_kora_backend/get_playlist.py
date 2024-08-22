# Importing the get_db_connection function from the config module
# This function is used to establish a connection to the database
from config import get_db_connection

# Importing necessary functions from the Flask module
# render_template_string: Renders a template from a string
# url_for: Generates a URL for a given endpoint
from flask import render_template_string, url_for

# Function to render all playlists from the database
def render_all_playlists():
    # Establishing the database connection
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)  # Creating a cursor object to execute SQL queries, with results returned as dictionaries

    # Executing an SQL query to fetch all playlists from the Playlists table
    cursor.execute("SELECT * FROM Playlists")
    playlists = cursor.fetchall()  # Fetching all results from the query

    # Closing the cursor and database connection
    cursor.close()
    db_conn.close()

    # Returning an HTML page that lists all playlists
    return render_template_string('''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>All Playlists</title>
                <style>
                    /* Basic styling for the page */
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        padding: 20px;
                    }
                    .container {
                        width: 80%;
                        max-width: 1200px;
                        margin: 0 auto;
                        background-color: #fff;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    }
                    h1 {
                        font-size: 36px;
                        margin-bottom: 20px;
                    }
                    table {
                        width: 100%;
                        border-collapse: collapse;
                        margin-bottom: 20px;
                    }
                    th, td {
                        padding: 10px;
                        text-align: left;
                        border-bottom: 1px solid #ddd;
                    }
                    th {
                        background-color: #007BFF;
                        color: white;
                    }
                    tr:hover {
                        background-color: #f1f1f1;
                    }
                    a {
                        text-decoration: none;
                        color: #007BFF;
                    }
                    a:hover {
                        text-decoration: underline;
                    }
                    .button-group {
                        margin-top: 20px;
                    }
                    .button-group a {
                        text-decoration: none;
                        color: #fff;
                        background-color: #007BFF;
                        padding: 10px 20px;
                        border-radius: 5px;
                        margin-right: 10px;
                    }
                    .button-group a:hover {
                        background-color: #0056b3;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>All Playlists</h1>
                    <table border="1">
                        <tr>
                            <th>Playlist ID</th>
                            <th>Playlist Name</th>
                            <th>Description</th>
                            <th>Actions</th>
                        </tr>
                        <!-- Loop through each playlist in the playlists list -->
                        {% for playlist in playlists %}
                        <tr>
                            <td>{{ playlist['PlaylistID'] }}</td>
                            <td>{{ playlist['PlaylistName'] }}</td>
                            <td>{{ playlist['Description'] }}</td>
                            <td>
                                <!-- Links to view, update, or delete each playlist -->
                                <a href="{{ url_for('get_single_playlist', playlist_id=playlist['PlaylistID']) }}">View Details</a> |
                                <a href="{{ url_for('update_existing_playlist', playlist_id=playlist['PlaylistID']) }}">Update</a> |
                                <a href="{{ url_for('delete_existing_playlist', playlist_id=playlist['PlaylistID']) }}">Delete</a>
                            </td>
                        </tr>
                        {% endfor %}
                    </table>
                    <div class="button-group">
                        <!-- Links to return to the home page or add a new playlist -->
                        <a href="{{ url_for('home') }}">Home</a>
                        <a href="{{ url_for('add_new_playlist') }}">Add New Playlist</a>
                    </div>
                </div>
            </body>
            </html>
        ''', playlists=playlists)  # Passing the playlists data to the template
