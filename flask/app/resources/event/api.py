import re
from flask_restful import Resource, marshal_with, abort, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import db
from app.resources.event.model import Event
from app.resources.event_participations.model import EventParticipation
from app.resources.event.args import post_args, update_args
from app.resources.event.fields import resource_fields
from uuid import uuid4
import datetime

class EventAPI(Resource):
    @marshal_with(resource_fields)
    def post(self):

        #Get arguments
        args = post_args.parse_args()

        #Create unique ID
        id = str(uuid4())
            

        #Create event object
        event = Event(
            eventId = id,
            name = args['name'],
            #image = args['image'],
            description = args['description'],
            org_Id = args['org_id'],
            fee = args['fee'],
            date = args['date'],
            time_starter = args['time_starter'],
            time_main = args['time_main'],
            time_dessert = args['time_dessert'],
            city = args['city'],
            zip_code = args['zip_code'],
            isPublic = args['isPublic'],
            max_participants = args['max_participants'],
            registration_deadline = datetime.datetime.strptime(args['registration_deadline'], '%d-%m-%Y'),
            #datetime_created = args['datetime_created'],
            #datetime_updated = args['datetime_updated']
        )

        #Model integration
        #event.hash_password()

        #Add user to database
        db.session.add(event)
        db.session.commit()

        #Select created event
        event_created = Event.query.filter_by(eventId=id).first()

        #Return recently created event
        return event_created, 201

class getActiveEvents(Resource):

    @jwt_required()
    @marshal_with(resource_fields)
    def get(self, id=None):

        userId = get_jwt_identity()
        #Get all active events 
        active_events = db.session.query(Event).filter(datetime.datetime.now() < Event.registration_deadline).all()
        print(active_events)
        # Events bei dem User registriert ist
        user_registrated = db.session.query(EventParticipation).filter((EventParticipation.userId == userId) | (EventParticipation.partner_userId == userId) ).all()
        print(user_registrated)

        registEvents = [event.eventId for event in user_registrated]
        allEvents = [event for event in active_events if event.eventId not in registEvents]

        return allEvents
    


