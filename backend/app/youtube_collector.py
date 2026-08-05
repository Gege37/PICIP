"""
PICIP YouTube Collector

Phase 3.4.2

Official YouTube Channel Collector.
"""

from services.youtube_client import get_latest_videos


def collect_youtube(channel_id):
    """
    Collect the latest videos from an official YouTube channel.
    """

    print(f"Collecting YouTube channel: {channel_id}")

    return get_latest_videos(channel_id)
