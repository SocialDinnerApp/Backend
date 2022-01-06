from enum import unique
from sqlalchemy.orm import backref
from src import db
from datetime import date, datetime

#Klassenamen wird genutzt für Tabellennamen
class EventParticipation(db.Model):
    #__tablename__ = 'users'
    teamId = db.Column(db.String(36), primary_key = True)
    userId = db.Column(db.String(36), db.ForeignKey('participant.userid'))
    partner_userId = db.Column(db.String(36), db.ForeignKey('participant.userid'))
    cooking_locationId = db.Column(db.String(36), db.ForeignKey('cooking_location.cookinglocationId'))
    eventId = db.Column(db.String(36), db.ForeignKey('event.eventId'))
    datetime_created = db.Column(db.DateTime, default=datetime.utcnow)  
    datetime_updated = db.Column(db.DateTime, default=datetime.utcnow)
    #eventTeamMatching = db.relationship('eventTeamMatching', backref='EventParticipation', lazy=True)
