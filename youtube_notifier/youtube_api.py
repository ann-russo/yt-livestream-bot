import os
import logging
import socket
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

API_KEY = os.getenv("YOUTUBE_API_KEY")
LOFIGIRL_ID = 'UCSJ4gkVC6NrvII8umztf0Ow'
FIGHTINCOWBOY_ID = 'UC9N0DmacOi4iWKQyygX89OQ'


def check_live_stream():
    try:
        socket.create_connection(("www.google.com", 80), timeout=10)
    except OSError:
        logging.error("No internet connection.")
        return []
    try:
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        request = youtube.search().list(
            part='snippet',
            channelId=FIGHTINCOWBOY_ID,
            eventType='live',
            type='video'
        )
        response = request.execute()
        logging.info("YouTube API request succeeded.")
        return response.get('items', [])
    except HttpError as e:
        logging.error(f"YouTube API request failed. Details: {e}")
        return []
    except Exception as e:
        logging.error(f"Unexpected error occurred. Details: {e}")
        return []
