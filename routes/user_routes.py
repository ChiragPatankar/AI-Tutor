from flask import Blueprint, render_template, request, redirect, url_for
from app.models.user import User  # Importing the User model
from app.models.progress import Progress  # Importing the Progress model (if applicable)
from app import db  # Assuming you're using SQLAlchemy

# Create a blueprint for user-related routes
user_bp = Blueprint('user', __name__)

# Route for displaying the user's profile
@user_bp.route('/profile')
def profile():
    # Get the current user (this could be done via session, token, or database query)
    user = User.query.first()  # Example query; update as needed for actual user retrieval
    return render_template('dashboard/profile.html', user=user)

# Route for displaying and updating user progress
@user_bp.route('/progress', methods=['GET', 'POST'])
def progress():
    user = User.query.first()  # Example query for user
    progress = Progress.query.filter_by(user_id=user.id).first()  # Retrieve progress from the database

    if request.method == 'POST':
        # Example of updating progress (modify as needed for your app)
        progress.completed_lessons = request.form['completed_lessons']
        db.session.commit()
        return redirect(url_for('user.progress'))

    return render_template('dashboard/progress.html', user=user, progress=progress)
