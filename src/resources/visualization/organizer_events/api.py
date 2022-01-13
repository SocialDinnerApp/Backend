from math import e, nan
from src.resources.event.model import Event
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from src.resources.event_participations.model import EventParticipation
from flask_restful import Resource, marshal_with, abort, request
from src.resources.visualization.organizer_events.fields import resource_fields
from sqlalchemy import extract
from flask import jsonify
import datetime
from src import db


class Last_Seven_Events(Resource):

    @jwt_required()
    #@marshal_with(resource_fields)
    def get(self):

        #Get arguments
        organizer_id = get_jwt_identity()

        events = db.session.query(Event).filter(Event.org_Id == organizer_id).order_by(Event.datetime_created.desc()).all()

        if len(events) >= 8:
            events = events[:7]

        event_informations = []
        for event in events:
            participants = db.session.query(EventParticipation).filter(EventParticipation.eventId == event.eventId).all()
            count = len(participants)
            event_info = {'date': event.date, 'name': event.name, 'Anzahl': count}
            event_informations.append(dict(event_info))

        return event_informations
