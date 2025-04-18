# app/services/youtube_service.py
from googleapiclient.discovery import build
from app.models.content import Content
from app import db
import os


class YouTubeService:
    def __init__(self):
        self.api_key = os.getenv('YOUTUBE_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def search_educational_videos(self, query, max_results=10):
        try:
            search_response = self.youtube.search().list(
                q=query,
                part='snippet',
                type='video',
                videoCategory='27',  # Education category
                maxResults=max_results,
                relevanceLanguage='en',
                safeSearch='strict'
            ).execute()

            videos = []
            for item in search_response['items']:
                video_id = item['id']['videoId']
                # Get video statistics
                stats = self.get_video_stats(video_id)

                video = {
                    'title': item['snippet']['title'],
                    'description': item['snippet']['description'],
                    'url': f'https://www.youtube.com/watch?v={video_id}',
                    'thumbnail': item['snippet']['thumbnails']['high']['url'],
                    'channel': item['snippet']['channelTitle'],
                    'stats': stats
                }
                videos.append(video)

            return videos

        except Exception as e:
            print(f"Error in YouTube API: {str(e)}")
            return []

    def get_video_stats(self, video_id):
        stats_response = self.youtube.videos().list(
            part='statistics',
            id=video_id
        ).execute()

        if stats_response['items']:
            stats = stats_response['items'][0]['statistics']
            return {
                'views': int(stats.get('viewCount', 0)),
                'likes': int(stats.get('likeCount', 0)),
                'comments': int(stats.get('commentCount', 0))
            }
        return None
