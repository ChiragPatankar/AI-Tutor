# app/ai_components/recommendation_engine.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.cosine_similarity import cosine_similarity
import numpy as np
from app.models.content import Content
from app.models.progress import Progress


class RecommendationEngine:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def get_personalized_recommendations(self, user, n_recommendations=10):
        # Get user's content history
        completed_content = Progress.query.filter_by(
            user_id=user.id,
            status='completed'
        ).all()

        if not completed_content:
            return self._get_default_recommendations(user.subject, user.learning_level)

        # Build user profile
        user_profile = self._build_user_profile(completed_content)

        # Find similar content
        all_content = Content.query.filter_by(
            subject=user.subject,
            level=user.learning_level
        ).all()

        # Calculate similarities
        content_vectors = self.vectorizer.fit_transform(
            [c.description for c in all_content]
        )
        similarities = cosine_similarity(user_profile, content_vectors)

        # Get top recommendations
        content_scores = list(zip(all_content, similarities[0]))
        recommendations = sorted(content_scores, key=lambda x: x[1], reverse=True)

        return [content for content, score in recommendations[:n_recommendations]]

    def _build_user_profile(self, completed_content):
        content_texts = [c.content.description for c in completed_content]
        content_vectors = self.vectorizer.fit_transform(content_texts)
        return np.mean(content_vectors.toarray(), axis=0).reshape(1, -1)

    def _get_default_recommendations(self, subject, level):
        return Content.query.filter_by(
            subject=subject,
            level=level
        ).order_by(Content.rating.desc()).limit(10).all()