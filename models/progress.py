from datetime import datetime
import db


class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content_id = db.Column(db.Integer, db.ForeignKey('content.id'))
    status = db.Column(db.String(20))  # 'started', 'completed', 'in_progress'
    score = db.Column(db.Float)
    time_spent = db.Column(db.Integer)  # in seconds
    last_accessed = db.Column(db.DateTime, default=datetime.utcnow)
    completion_date = db.Column(db.DateTime)