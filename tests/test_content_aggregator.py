import unittest
from unittest.mock import patch
from app.ai_components.content_aggregator import ContentAggregator


class ContentAggregatorTestCase(unittest.TestCase):
    def setUp(self):
        self.aggregator = ContentAggregator()

    @patch('app.services.youtube_service.YouTubeService.search_educational_videos')
    def test_fetch_videos(self, mock_youtube):
        mock_youtube.return_value = [{
            'title': 'Test Video',
            'url': 'https://youtube.com/test'
        }]

        content = self.aggregator.get_best_content(
            query='machine learning',
            subject='AI',
            level='beginner'
        )

        self.assertTrue(len(content['videos']) > 0)
        self.assertEqual(content['videos'][0]['title'], 'Test Video')