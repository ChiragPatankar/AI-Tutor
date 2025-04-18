import PyPDF2
import requests
from io import BytesIO
from app.utils.cache_manager import cache
import textract


class PDFService:
    def __init__(self):
        self.supported_extensions = ['.pdf', '.txt', '.docx']

    def extract_text(self, file_path_or_url):
        try:
            if file_path_or_url.startswith('http'):
                return self._extract_from_url(file_path_or_url)
            return self._extract_from_file(file_path_or_url)
        except Exception as e:
            print(f"Error extracting text: {str(e)}")
            return None

    def _extract_from_url(self, url):
        # Check cache first
        cached_content = cache.get(url)
        if cached_content:
            return cached_content

        response = requests.get(url)
        pdf_file = BytesIO(response.content)

        text = self._extract_from_pdf(pdf_file)
        cache.set(url, text)
        return text

    def _extract_from_file(self, file_path):
        file_extension = file_path.lower().split('.')[-1]

        if file_extension == 'pdf':
            with open(file_path, 'rb') as file:
                return self._extract_from_pdf(file)
        else:
            return textract.process(file_path).decode()

    def _extract_from_pdf(self, file_obj):
        pdf_reader = PyPDF2.PdfReader(file_obj)
        text = []
        for page in pdf_reader.pages:
            text.append(page.extract_text())
        return '\n'.join(text)
