from flask_restful import Resource, marshal_with, abort, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import db
from app.resources import event_participations
from app.resources.event_participations.model import EventParticipation
from app.resources.event_participations.args import post_args, update_args
from app.resources.event_participations.fields import resource_fields
from uuid import uuid4
import datetime

class Event_ParticipationsAPI(Resource):
    @marshal_with(resource_fields)
    def post(self):

        #Get arguments
        args = post_args.parse_args()

        #Create unique ID
        id = str(uuid4())

        event_participations = EventParticipation(
            teamId = id,
            userId = args['userId'],
            partner_userId = args['partner_userId'],
            eventId = args['eventId'],
            cooking_locationId = args['cooking_locationId']
        )

        #Add event_participations to database
        db.session.add(event_participations)
        db.session.commit()

        #Select created event_participations
        event_participations_created = EventParticipation.query.filter_by(teamId=id).first()

        #Return recently created event
        return event_participations_created, 201