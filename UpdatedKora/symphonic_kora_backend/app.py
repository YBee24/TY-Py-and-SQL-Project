# Import necessary libraries
# Flask is a web framework for building web applications in Python
# request is used to handle incoming HTTP requests and extract data from them
# jsonify is used to convert Python data structures into JSON format
from flask import Flask, request, jsonify

# mysql.connector is a library for connecting to and interacting with a MySQL database
import mysql.connector

# googleapiclient.discovery is a module for accessing Google APIs, in this case, the YouTube Data API
from googleapiclient.discovery import build

# Create an instance of the Flask class for your web application.
# This instance will be used to route HTTP requests and define how the application should respond to them.
app = Flask(__name__)


# Define a function to establish a connection to the MySQL database
# This function will return a connection object that allows us to interact with the database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  # The address of the database server (localhost means your own computer)
        user="root",  # The username to connect to the database (default is 'root')
        password="root",  # The password for the database user (set to 'root' here, but this can vary)
        database="MusicLibrary"  # The name of the database you want to connect to (replace with your database name)
    )


# Define a function to search YouTube for a song
# This function will use the YouTube Data API to search for videos matching the given song name
def search_youtube(song_name):
    api_key = 'AIzaSyC33vQ1bcNeRoCYsL1Rocr3AvMjyNHPFNU'  # Replace with your actual API key
    # 'build' is used to create a service object for the YouTube API
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Create a request to search YouTube using the API
    # part='snippet' specifies that we want basic details about the video (title, description, etc.)
    # q=song_name is the query string (i.e., the name of the song we're searching for)
    # maxResults=1 limits the search results to the first video found
    request = youtube.search().list(
        part='snippet',
        q=song_name,
        maxResults=1
    )

    # Execute the request to YouTube and get the response
    response = request.execute()

    # Check if any items (videos) were found in the response
    if response['items']:
        # If a video was found, extract the video ID and title
        video_id = response['items'][0]['id']['videoId']
        video_title = response['items'][0]['snippet']['title']
        # Construct the full URL of the video using the video ID
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        # Return the video title and URL
        return video_title, video_url
    else:
        # If no videos were found, return None for both the title and URL
        return None, None


# Define a route for the search functionality
# When a GET request is made to /songs/search, this function will handle it
@app.route('/songs/search', methods=['GET'])
def search_songs():
    # Extract the 'Artist' and 'SongName' parameters from the request's query string
    artist = request.args.get('Artist')
    song_name = request.args.get('SongName')

    # Establish a connection to the MySQL database
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)  # Create a cursor object to interact with the database

    # Construct an SQL query to check if the song already exists in the database
    # We use placeholders (%s) to avoid SQL injection attacks
    query = "SELECT * FROM Songs WHERE Artist = %s AND SongName = %s"
    cursor.execute(query, (artist, song_name))
    song = cursor.fetchone()  # Fetch the first result (if any)

    # If the song is found in the database, return it as a JSON response with a 200 (OK) status code
    if song:
        return jsonify(song), 200
    else:
        # If the song is not found in the database, search for it on YouTube
        full_name = f"{artist} {song_name}"  # Combine the artist's name and song title for the search query
        video_title, video_url = search_youtube(full_name)

        if video_title and video_url:
            # If a matching video is found on YouTube, insert the song details into the database
            cursor.execute("""
                INSERT INTO Songs (Artist, SongName, YouTubeURL)
                VALUES (%s, %s, %s)
            """, (artist, song_name, video_url))
            db.commit()  # Commit the transaction to save the changes in the database

            # Fetch the newly added song from the database to return it
            cursor.execute(query, (artist, song_name))
            new_song = cursor.fetchone()

            cursor.close()  # Close the cursor to free up resources
            db.close()  # Close the database connection to free up resources

            # Return the newly added song as a JSON response with a 200 (OK) status code
            return jsonify(new_song), 200
        else:
            # If no matching video is found on YouTube, return a 404 (Not Found) status code
            cursor.close()
            db.close()
            return jsonify({'message': 'No songs found matching the criteria on YouTube'}), 404


# The following code will only run if this script is executed directly (not imported as a module)
if __name__ == '__main__':
    # Start the Flask web server in debug mode on port 5001
    # Debug mode allows for automatic reloading and error messages to be displayed
    app.run(debug=True, port=5001)
