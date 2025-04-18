# app/services/web_scraper.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import trafilatura
from app.utils.cache_manager import cache


class WebScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def scrape_educational_content(self, url):
        # Check cache
        cached_content = cache.get(url)
        if cached_content:
            return cached_content

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()

            # Use trafilatura for main content extraction
            content = trafilatura.extract(response.text)

            if not content:
                # Fallback to BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')
                content = self._extract_main_content(soup)

            # Extract metadata
            metadata = self._extract_metadata(soup)

            result = {
                'content': content,
                'metadata': metadata
            }

            # Cache the result
            cache.set(url, result)
            return result

        except Exception as e:
            print(f"Error scraping {url}: {str(e)}")
            return None

    def _extract_main_content(self, soup):
        # Try common content containers
        content_tags = [
            soup.find('article'),
            soup.find('main'),
            soup.find(class_=['content', 'main-content', 'article-content'])
        ]

        for tag in content_tags:
            if tag:
                return tag.get_text(strip=True)

        # Fallback to paragraph extraction
        paragraphs = soup.find_all('p')
        return '\n'.join(p.get_text() for p in paragraphs)

    def _extract_metadata(self, soup):
        return {
            'title': soup.title.string if soup.title else None,
            'meta_description': soup.find('meta', {'name': 'description'})['content'] if soup.find('meta', {
                'name': 'description'}) else None,
            'meta_keywords': soup.find('meta', {'name': 'keywords'})['content'] if soup.find('meta', {
                'name': 'keywords'}) else None
        }