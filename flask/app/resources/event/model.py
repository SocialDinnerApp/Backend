from enum import unique
from sqlalchemy.orm import backref
from app import db
from datetime import date, datetime
from flask_bcrypt import generate_password_hash, check_password_hash

class Event(db.Model):
    eventId = db.Column(db.String(36), primary_key = True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text(300), nullable=False)
    org_Id = db.Column(db.String(36), db.ForeignKey('organizer.organizerId'))
    fee = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time_starter = db.Column(db.DateTime, nullable=False)
    time_main = db.Column(db.DateTime, nullable=False)
    time_dessert = db.Column(db.DateTime, nullable=False)
    city = db.Column(db.String(36), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    isPublic = db.Column(db.Boolean, nullable=False)
    max_participants = db.Column(db.Integer, nullable=False)
    registration_deadline = db.Column(db.DateTime, nullable=False)
    datetime_created = db.Column(db.DateTime, default=datetime.utcnow)
    datetime_updated = db.Column(db.DateTime, default=datetime.utcnow)