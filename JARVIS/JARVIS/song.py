import os
import webbrowser
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up the YouTube Data API client
api_key = "AIzaSyByc8KfJya-y95xpMMgmXW4Guq2JTv-b-0"
youtube = build('youtube', 'v3', developerKey=api_key)

def search_and_play_song(query):
    try:
        # Call the YouTube Data API to search for videos matching the query
        search_response = youtube.search().list(
            q=query,
            type='video',
            part='id,snippet',
            maxResults=1
        ).execute()

        # Extract the video ID from the search response
        video_id = search_response['items'][0]['id']['videoId']

        # Construct the YouTube URL for the video
        youtube_url = f"https://www.youtube.com/watch?v={video_id}"

        # Open the YouTube URL in the user's default web browser
        webbrowser.open(youtube_url)

        return f"Now playing {query} on YouTube!"

    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred:\n{e.content}")
        return "Sorry, I couldn't find that song on YouTube."

# Test the function
# search_and_play_song("Shape of You")
