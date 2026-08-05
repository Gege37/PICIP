"""
PICIP YouTube Client

Phase 3.4.1

Reusable client for the YouTube Data API.
"""

from googleapiclient.discovery import build

from config.settings import YOUTUBE_API_KEY


def get_latest_videos(channel_id, limit=10):
    """
    Return the latest videos published by a YouTube channel.
    """

    if not YOUTUBE_API_KEY:
        print("YouTube API key not configured.")
        return []

    try:

        youtube = build(
            "youtube",
            "v3",
            developerKey=YOUTUBE_API_KEY
        )

        response = youtube.search().list(
            part="snippet",
            channelId=channel_id,
            order="date",
            type="video",
            maxResults=limit
        ).execute()

        videos = []

        for item in response.get("items", []):

            snippet = item["snippet"]

            videos.append({

                "title": snippet["title"],

                "content": snippet["description"],

                "url":
                    "https://www.youtube.com/watch?v="
                    + item["id"]["videoId"]

            })

        print(f"YouTube: collected {len(videos)} videos.")

        return videos

    except Exception as e:

        print(f"YouTube API error: {e}")

        return []
