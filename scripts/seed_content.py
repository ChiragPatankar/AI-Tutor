import json
import random
from app import create_app, db
from app.models.content import Content
from app.services.youtube_service import YouTubeService
from app.services.pdf_service import PDFService


def seed_content():
    app = create_app()
    youtube_service = YouTubeService()

    subjects = ['Machine Learning', 'Deep Learning', 'Data Science', 'AI Ethics']
    levels = ['beginner', 'intermediate', 'advanced']

    with app.app_context():
        for subject in subjects:
            for level in levels:
                # Fetch YouTube videos
                videos = youtube_service.search_educational_videos(
                    f"{subject} {level} tutorial",
                    max_results=5
                )

                for video in videos:
                    content = Content(
                        title=video['title'],
                        description=video['description'],
                        content_type='video',
                        url=video['url'],
                        subject=subject,
                        level=level,
                        metadata=json.dumps(video['stats'])
                    )
                    db.session.add(content)

        db.session.commit()


if __name__ == '__main__':
    seed_content()