from enum import unique
from sqlalchemy.orm import backref
from app import db
from datetime import date, datetime

#Klassenamen wird genutzt für Tabellennamen
class eventTeamMatching(db.Model):
    matchingId = db.Column(db.String(36), primary_key = True)
    teamId = db.Column(db.String(36), db.ForeignKey('event_participation.teamId'))
    eventId = db.Column(db.String(36), db.ForeignKey('event.eventId'))
    starterTeamId = db.Column(db.String(36), db.ForeignKey('event_participation.teamId'))
    mainTeamId = db.Column(db.String(36), db.ForeignKey('event_participation.teamId'))
    dessertTeamId = db.Column(db.String(36), db.ForeignKey('event_participation.teamId'))
    datetime_created = db.Column(db.DateTime, default=datetime.utcnow)  
    datetime_updated = db.Column(db.DateTime, default=datetime.utcnow)