from flask_restful import Resource, marshal_with, abort, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import db
from app.resources.participant.model import Participant
from app.resources.participant.args import post_args, update_args, login_args
from app.resources.participant.fields import resource_fields

from uuid import uuid4
import datetime

class ParticipantAPI(Resource):
    @marshal_with(resource_fields)
    def post(self):
        
        #Get arguments
        args = post_args.parse_args()

        #Create unique ID
        id = str(uuid4())

        #Create participant object
        participant = Participant(
            userid = id,
            username = args['username'],
            email = args['email'],
            password = args['password'],
        )
        #Model integration   
        participant.hash_password()

        #Add user to database
        db.session.add(participant)
        db.session.commit()

        #Select created participant
        participant_created = Participant.query.filter_by(userid=id).first()

        #Return recently created participant
        return participant_created, 201        
        