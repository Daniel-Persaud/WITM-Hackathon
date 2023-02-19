from datetime import datetime
from safeto import db

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    date_reported = db.Column(db.DateTime, nullable=False, default=datetime.now)
    location = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Report('{self.category}', '{self.date_reported}')"