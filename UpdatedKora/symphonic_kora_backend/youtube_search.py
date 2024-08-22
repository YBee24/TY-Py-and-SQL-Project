# Import the build function from the googleapiclient.discovery module
# This function is used to construct a service object for interacting with the YouTube API
from googleapiclient.discovery import build

# Define a function that searches YouTube for videos related to a specific artist
def search_youtube_for_artist(artist_name):
    # Specify your YouTube API key. This key is needed to authenticate requests to the YouTube Data API.
    api_key = 'AIzaSyDVSCTmYSc2VjHVGdXagQK5scyJalAG9io'  # Replace with your YouTube API key

    # Use the build function to create a service object for the YouTube API
    # The 'youtube' parameter specifies the service to be used, and 'v3' is the version of the API
    # The developerKey parameter is where you pass your API key
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Create a request to search for videos on YouTube
    # The search().list() method allows us to specify various search parameters
    request = youtube.search().list(
        q=artist_name,         # The query string, which in this case is the artist's name
        part='snippet',        # The part parameter specifies a comma-separated list of resource properties that the API response will include; 'snippet' provides details like the video title and description
        type='video',          # Restrict the search results to videos only
        maxResults=5           # Limit the number of search results returned to 5
    )

    # Execute the API request and store the response
    response = request.execute()

    # Process the response to extract relevant information about each video
    # This loop creates a list of dictionaries, where each dictionary contains:
    # - 'title': The title of the video
    # - 'video_id': The unique identifier for the video on YouTube
    # - 'url': The full URL to watch the video on YouTube
    results = [
        {
            'title': item['snippet']['title'],                  # Extract the video title
            'video_id': item['id']['videoId'],                  # Extract the video ID
            'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}"  # Construct the full URL for the video
        }
        for item in response['items']  # Iterate over each item in the API response
    ]

    # Return the list of video results
    return results

