import unittest
import numpy as np
from app.ai_components.recommendation_engine import RecommendationEngine


class RecommendationEngineTestCase(unittest.TestCase):
    def setUp(self):
        self.engine = RecommendationEngine()

    def test_content_similarity(self):
        content1 = "Machine learning basics"
        content2 = "Introduction to machine learning"

        vec1 = self.engine.vectorizer.fit_transform([content1])
        vec2 = self.engine.vectorizer.transform([content2])

        similarity = np.dot(vec1.toarray(), vec2.toarray().T)[0][0]
        self.assertGreater(similarity, 0.5)