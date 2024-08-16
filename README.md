Music Library Management System
This project is a simple Music Library Management System built using Python, pandas, and MySQL. The system reads song data from an Excel file, cleans it, and stores it in a MySQL database. The data can then be managed (CRUD operations) using a Flask web application.

Features
Data Import: Load and clean song data from an Excel file.
Database Management: Store, retrieve, update, and delete song data in a MySQL database.
API: A Flask web application that provides endpoints for creating, reading, updating, and deleting playlists in the database.
Requirements
Python 3.x
MySQL Server
Python Libraries:
pandas
mysql-connector-python
Flask
Setup
1. Clone the Repository
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/music-library-management.git
2. Install Python Dependencies
Navigate to the project directory and install the required Python packages:

bash
Copy code
cd music-library-management
pip install pandas mysql-connector-python Flask
3. Set Up MySQL Database
Ensure MySQL is installed and running on your machine.
Create a new database called MusicLibrary.
Create the required tables in the database by running the Python script (explained below).
4. Load and Store Data
Run the musiclibrary.py script to load the song data from the Excel file and store it in the MySQL database:

bash
Copy code
python musiclibrary.py
This script will:
Load the song data from the specified Excel file.
Clean the data by removing any rows with missing values.
Store the cleaned data in the Songs table of the MusicLibrary database.
5. Running the Flask Application
To start the Flask web application that allows you to manage playlists:

bash
Copy code
python app.py
This will start a local web server. You can access the API at http://127.0.0.1:5000/.
6. API Endpoints
Create a Playlist

POST /playlists
JSON Body:
json
Copy code
{
    "PlaylistID": 1,
    "PlaylistName": "Chill Vibes",
    "Description": "A playlist for relaxing and unwinding."
}
Get All Playlists

GET /playlists
Get a Playlist by ID

GET /playlists/<playlist_id>
Update a Playlist

PUT /playlists/<playlist_id>
JSON Body:
json
Copy code
{
    "PlaylistName": "Updated Playlist Name",
    "Description": "Updated description."
}
Delete a Playlist

DELETE /playlists/<playlist_id>
Troubleshooting
Common Issues
MySQL Connection Errors:

Ensure MySQL is running on your machine.
Double-check the database name, username, and password in the get_db_connection function.
File Paths:

Ensure the path to the Excel file is correct. Adjust file_path in musiclibrary.py if necessary.
Missing Dependencies:

Make sure all required Python packages are installed by running pip install -r requirements.txt.
