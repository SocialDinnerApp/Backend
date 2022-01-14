from src.resources.event.model import Event
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.resources.event_participations.model import EventParticipation
from flask_restful import Resource, abort
from sqlalchemy import extract
import datetime
from src import db


class ParticipantHistory(Resource):

    @jwt_required()
    def get(self):

        # Get arguments
        organizer_id = get_jwt_identity()

        events = db.session.query(Event).filter(
            Event.org_Id == organizer_id).order_by(Event.datetime_created.desc()).all()

        if len(events) >= 8:
            events = events[:7]

        event_informations = []
        for event in events:
            participants = db.session.query(EventParticipation).filter(
                EventParticipation.eventId == event.eventId).all()
            hist_values, hist_dates = self.getPartHist(participants)
            event_info = {
                'eventDate': event.date,
                'eventName': event.name,
                'values': hist_values,
                'dates': hist_dates,
            }
            event_informations.append(event_info)

        return event_informations

    def getPartHist(self, participants):
        hist_values = []
        hist_dates = []

        # How many splits you want to have
        daySteps = 5
        fromDay = 30
        fromDate = datetime.datetime.now() - datetime.timedelta(days=fromDay)
        toDay = 25

        for _ in range(daySteps + 1):
            toDate = datetime.datetime.now() - datetime.timedelta(days=toDay)
            hist_dates.append(toDate.strftime('%d-%m-%Y'))
            hist_values.append(len(
                [part for part in participants if fromDate <= part.datetime_created < toDate]))

            toDay -= daySteps

        return hist_values, hist_dates
