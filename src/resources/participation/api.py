import re
from flask_restful import Resource, marshal_with, abort, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from src import db
from src.resources import cookingLocation
from src.resources.cookingLocation.model import CookingLocation
from src.resources.event_participations.model import EventParticipation
from src.resources.participation.args import post_args
from src.resources.participation.fields import resource_fields
from src.resources.participant.model import Participant
from uuid import uuid4
import datetime

class ParticipationAPI(Resource):
    @jwt_required()
    @marshal_with(resource_fields)
    def post(self):

        #Get arguments
        args = post_args.parse_args()

        #Create unique ID
        cookingLocation_id = str(uuid4())
        event_participations_id = str(uuid4())


        #Create cookingLocation object
        cookingLocation = CookingLocation(
            cookinglocationId = cookingLocation_id,
            zip_code = args['zip_code'],
            city = args['city'],
            street = args['street'],
            housenumber = args['housenumber'],
            floor = args['floor'],
            hints = args['hints'],
        )

        teammate = Participant.query.filter_by(username=args['username_partner']).first()

        event_participations = EventParticipation(
            teamId = event_participations_id,
            userId = args['userId'],
            partner_userId = teammate.userid,
            eventId = args['eventId'],
            cooking_locationId = cookingLocation_id
        )

        #Add cookingLocation to database
        db.session.add(cookingLocation)
        db.session.add(event_participations)
        db.session.commit()

        #Return recently created cookingLocation
        return {'success': 'True'}, 201