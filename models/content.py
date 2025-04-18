import db


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    content_type = db.Column(db.String(50))
    url = db.Column(db.String(500))
    source = db.Column(db.String(100))
    subject = db.Column(db.String(100))
    level = db.Column(db.String(50))
    rating = db.Column(db.Float, default=0.0)
    votes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)
    metadata = db.Column(db.JSON)