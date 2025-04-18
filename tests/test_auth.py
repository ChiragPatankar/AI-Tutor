import unittest
from app import create_app, db
from app.models.user import User


class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register(self):
        response = self.client.post('/register', data={
            'email': 'test@example.com',
            'password': 'test123',
            'name': 'Test User',
            'level': 'beginner',
            'subject': 'Machine Learning'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        user = User.query.filter_by(email='test@example.com').first()
        self.assertIsNotNone(user)


