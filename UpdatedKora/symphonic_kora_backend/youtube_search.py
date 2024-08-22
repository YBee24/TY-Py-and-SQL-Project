from googleapiclient.discovery import build

def search_youtube_for_artist(artist_name):
    api_key = 'AIzaSyDVSCTmYSc2VjHVGdXagQK5scyJalAG9io'  # Replace with your YouTube API key
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        q=artist_name,
        part='snippet',
        type='video',
        maxResults=5
    )
    response = request.execute()

    results = [
        {
            'title': item['snippet']['title'],
            'video_id': item['id']['videoId'],
            'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        }
        for item in response['items']
    ]

    return results
