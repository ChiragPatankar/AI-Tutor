# app/routes/content_routes.py
from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.ai_components.content_aggregator import ContentAggregator
from app.ai_components.recommendation_engine import RecommendationEngine
from app.models.content import Content
from app import db

content_routes = Blueprint('content', __name__)
aggregator = ContentAggregator()
recommender = RecommendationEngine()


@content_routes.route('/api/content/fetch', methods=['GET'])
@login_required
def fetch_content():
    query = request.args.get('query', '')
    subject = request.args.get('subject', '')
    level = request.args.get('level', current_user.learning_level)

    content = aggregator.get_best_content(query, subject, level)
    return jsonify(content)


@content_routes.route('/api/content/recommend', methods=['GET'])
@login_required
def get_recommendations():
    recommendations = recommender.get_personalized_recommendations(current_user)
    return jsonify(recommendations)


@content_routes.route('/api/content/track', methods=['POST'])
@login_required
def track_progress():
    data = request.json
    content_id = data.get('content_id')
    progress = data.get('progress')

    # Update user progress
    user_progress = Progress(
        user_id=current_user.id,
        content_id=content_id,
        status='completed' if progress == 100 else 'in_progress',
        progress=progress
    )
    db.session.add(user_progress)
    db.session.commit()

    return jsonify({'status': 'success'})