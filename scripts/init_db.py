from app import create_app, db
from app.models.user import User
from app.models.content import Content
from app.models.progress import Progress


def init_db():
    app = create_app()
    with app.app_context():
        # Create all tables
        db.create_all()

        # Create admin user
        if not User.query.filter_by(email='admin@aitutor.com').first():
            admin = User(
                email='admin@aitutor.com',
                name='Admin',
                learning_level='advanced',
                subject='all'
            )
            admin.set_password('admin123')
            db.session.add(admin)

        # Add some initial content
        initial_content = [
            {
                'title': 'Introduction to Machine Learning',
                'description': 'Basic concepts of ML',
                'content_type': 'video',
                'url': 'https://youtube.com/watch?v=example1',
                'subject': 'Machine Learning',
                'level': 'beginner'
            },
            {
                'title': 'Deep Learning Fundamentals',
                'description': 'Neural Networks explained',
                'content_type': 'pdf',
                'url': 'https://example.com/dl-basics.pdf',
                'subject': 'Deep Learning',
                'level': 'intermediate'
            }
        ]

        for content_data in initial_content:
            if not Content.query.filter_by(url=content_data['url']).first():
                content = Content(**content_data)
                db.session.add(content)

        db.session.commit()


if __name__ == '__main__':
    init_db()
