def create_tables(connection):
    cursor = connection.cursor()

    # Create the box to store users
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL
    );
    """)

    # Create the box to store playlists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS playlists (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        name VARCHAR(255) NOT NULL,
        description TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    """)

    # Create the box to store tracks (songs)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tracks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        playlist_id INT,
        title VARCHAR(255) NOT NULL,
        artist VARCHAR(255) NOT NULL,
        youtube_link VARCHAR(255),
        FOREIGN KEY (playlist_id) REFERENCES playlists(id)
    );
    """)

    connection.commit()
    cursor.close()
