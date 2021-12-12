from flask_restful import Resource, marshal_with, abort, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.datastructures import auth_property
from app import db
from app.resources.event.model import Event
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
        event_created = Event.query.filter_by(evendId=id).first()

        #Return recently created event
        return event_created, 201

class getActiveEvents(Resource):

    #@jwt_required()
    @marshal_with(resource_fields)
    def get(self, id=None):
        active_events = db.session.query(Event).filter(datetime.datetime.now() < Event.registration_deadline).all()
        return active_events


        #result = test.registration_deadline
        #return test

        #Event.query.
        #registration_deadline


