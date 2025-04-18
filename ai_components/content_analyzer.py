# app/ai_components/content_analyzer.py
from transformers import pipeline
from textblob import TextBlob
import requests
from bs4 import BeautifulSoup


class ContentAnalyzer:
    def __init__(self):
        self.sentiment_analyzer = pipeline('sentiment-analysis')
        self.summarizer = pipeline('summarization')

    def analyze_content(self, content_url):
        # Fetch content
        response = requests.get(content_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract main content
        main_text = ' '.join([p.text for p in soup.find_all('p')])

        # Generate summary
        summary = self.summarizer(main_text[:1024],
                                  max_length=150,
                                  min_length=50)[0]['summary_text']

        # Analyze sentiment
        sentiment = self.sentiment_analyzer(summary)[0]

        # Calculate readability
        blob = TextBlob(main_text)
        readability_score = self._calculate_readability(blob)

        return {
            'summary': summary,
            'sentiment': sentiment['label'],
            'sentiment_score': sentiment['score'],
            'readability_score': readability_score,
            'language': blob.detect_language()
        }

    def _calculate_readability(self, blob):
        words = len(blob.words)
        sentences = len(blob.sentences)
        syllables = sum(self._count_syllables(word) for word in blob.words)

        if sentences == 0:
            return 0

        return 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)

    def _count_syllables(self, word):
        count = 0
        vowels = 'aeiouy'
        word = word.lower()
        if word[0] in vowels:
            count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith('e'):
            count -= 1
        if count == 0:
            count += 1
        return count