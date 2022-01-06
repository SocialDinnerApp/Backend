from enum import unique
from sqlalchemy.orm import backref
from src import db
from datetime import date, datetime

class Event(db.Model):
    eventId = db.Column(db.String(36), primary_key = True)
    #image = db.Column(db.Text, nullable=False)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(300), nullable=False)
    org_Id = db.Column(db.String(36), db.ForeignKey('organizer.organizerId'))
    fee = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String, nullable=False)
    time_starter = db.Column(db.String, nullable=False)
    time_main = db.Column(db.String, nullable=False)
    time_dessert = db.Column(db.String, nullable=False)
    city = db.Column(db.String(36), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    isPublic = db.Column(db.Boolean, nullable=False)
    max_participants = db.Column(db.Integer, nullable=False)
    registration_deadline = db.Column(db.DateTime, nullable=False)
    datetime_created = db.Column(db.DateTime, default=datetime.utcnow)
    datetime_updated = db.Column(db.DateTime, default=datetime.utcnow)