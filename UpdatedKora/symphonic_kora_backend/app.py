from flask import Flask, request, jsonify  # Import necessary modules from Flask
import mysql.connector  # Import MySQL connector to interact with the MySQL database

app = Flask(__name__)  # Create a new Flask web application

# Function to establish a connection to the MySQL database
def get_db_connection():
    # This function returns a connection object to the MySQL database
    return mysql.connector.connect(
        host="localhost",  # The server hosting the MySQL database (localhost means your own computer)
        user="root",  # The username to connect to the MySQL database (default is usually 'root')
        password="root",  # The password for the MySQL database user (set to 'root' here, but it could be different)
        database="MusicLibrary"  # The name of the database you want to connect to
    )


# Route to create a new playlist (C in CRUD: Create)
@app.route('/playlists', methods=['POST'])
def add_playlist():
    data = request.json  # Get the data sent in the request body as JSON format

    db = get_db_connection()  # Establish a connection to the database using the function defined above
    cursor = db.cursor()  # Create a cursor object, which is used to execute SQL commands

    # Insert a new record into the Playlists table in the database
    cursor.execute("""
        INSERT INTO Playlists (PlaylistID, PlaylistName, Description)
        VALUES (%s, %s, %s)
    """, (data['PlaylistID'], data['PlaylistName'], data.get('Description', '')))
    # The above command inserts values into PlaylistID, PlaylistName, and Description columns
    # It uses placeholders (%s) to insert the values provided in the data dictionary.
    # The get('Description', '') method retrieves the Description or uses an empty string if none is provided.

    db.commit()  # Save the changes made to the database
    cursor.close()  # Close the cursor to free up resources
    db.close()  # Close the database connection to free up resources

    # Return a success message in JSON format with a status code of 201 (Created)
    return jsonify({'message': 'Playlist added successfully'}), 201


# Route to read (retrieve) all playlists (R in CRUD: Read)
@app.route('/playlists', methods=['GET'])
def get_playlists():
    db = get_db_connection()  # Establish a connection to the database
    cursor = db.cursor(dictionary=True)  # Create a cursor that returns rows as dictionaries

    # Select all records from the Playlists table
    cursor.execute("SELECT * FROM Playlists")  # This SQL command fetches all data from the Playlists table
    playlists = cursor.fetchall()  # Fetch all the rows returned by the query and store them in the playlists variable

    cursor.close()  # Close the cursor to free up resources
    db.close()  # Close the database connection to free up resources

    # Return the list of playlists as a JSON response
    return jsonify(playlists)


# Route to read (retrieve) a specific playlist by its ID
@app.route('/playlists/<int:playlist_id>', methods=['GET'])
def get_playlist(playlist_id):
    db = get_db_connection()  # Establish a connection to the database
    cursor = db.cursor(dictionary=True)  # Create a cursor that returns rows as dictionaries

    # Select a specific playlist by its ID
    cursor.execute(
        "SELECT PlaylistID, PlaylistName, IFNULL(Description, '') AS Description FROM Playlists WHERE PlaylistID = %s",
        (playlist_id,))
    # The SQL command retrieves a playlist with the specified PlaylistID
    # IFNULL(Description, '') ensures that if the Description is NULL, an empty string is returned instead

    playlist = cursor.fetchone()  # Fetch the single row returned by the query

    cursor.close()  # Close the cursor to free up resources
    db.close()  # Close the database connection to free up resources

    if playlist:
        # If the playlist is found, return it as a JSON response with a status code of 200 (OK)
        return jsonify(playlist), 200
    else:
        # If the playlist is not found, return an error message with a status code of 404 (Not Found)
        return jsonify({'message': 'Playlist not found'}), 404


# Route to update (U in CRUD: Update) an existing playlist
@app.route('/playlists/<int:playlist_id>', methods=['PUT'])
def update_playlist(playlist_id):
    data = request.json  # Get the data sent in the request body as JSON format
    db = get_db_connection()  # Establish a connection to the database
    cursor = db.cursor()  # Create a cursor object to execute SQL commands

    # Update the playlist details in the Playlists table
    cursor.execute("""
        UPDATE Playlists SET PlaylistName = %s, Description = %s WHERE PlaylistID = %s
    """, (data['PlaylistName'], data.get('Description', ''), playlist_id))
    # This command updates the PlaylistName and Description of the playlist with the specified PlaylistID

    db.commit()  # Save the changes made to the database
    cursor.close()  # Close the cursor to free up resources
    db.close()  # Close the database connection to free up resources

    # Return a success message in JSON format
    return jsonify({'message': 'Playlist updated successfully'})


# Route to delete (D in CRUD: Delete) a playlist by its ID
@app.route('/playlists/<int:playlist_id>', methods=['DELETE'])
def delete_playlist(playlist_id):
    db = get_db_connection()  # Establish a connection to the database
    cursor = db.cursor()  # Create a cursor object to execute SQL commands

    # Delete the playlist from the Playlists table
    cursor.execute("DELETE FROM Playlists WHERE PlaylistID = %s", (playlist_id,))
    # This command deletes the playlist with the specified PlaylistID from the table

    db.commit()  # Save the changes made to the database
    cursor.close()  # Close the cursor to free up resources
    db.close()  # Close the database connection to free up resources

    # Return a success message in JSON format
    return jsonify({'message': 'Playlist deleted successfully'})


# Start the Flask development server
if __name__ == '__main__':
    app.run(debug=True)  # Start the server in debug mode, which provides detailed error messages
