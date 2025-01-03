from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Package(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(120), nullable=False)
    destination = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(50), default="pending")