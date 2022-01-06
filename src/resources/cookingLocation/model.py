from enum import unique
from sqlalchemy.orm import backref
from src import db
from datetime import date, datetime

from src.resources import event_participations

class CookingLocation(db.Model):
    cookinglocationId = db.Column(db.String(36), primary_key = True)
    zip_code = db.Column(db.Integer, nullable = False)
    city = db.Column(db.String(36), nullable = False)
    street = db.Column(db.String, nullable = False)
    housenumber = db.Column(db.Integer, nullable = False)
    floor = db.Column(db.Integer, nullable = False)
    hints = db.Column(db.String(100), nullable = False)
    #Beziehung
    event_participation = db.relationship('EventParticipation', backref='cookingLocation', lazy=True)

