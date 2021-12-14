from flask_restful import Resource, marshal_with, abort, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import db
from app.resources.event_participations.model import EventParticipation
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

    @jwt_required()
    @marshal_with(resource_fields)
    def get(self, id=None):
        #Get participantId
        participant_key = get_jwt_identity()
        participant = Participant.query.filter_by(userid=participant_key).first_or_404()
        username = participant.username

        if username:
            return participant, 200
        else:
            abort(400, message='Error')

class MyEvents(Resource):
    def get(self):

        userId = Participant.query.filter_by(userid=args['userId']).first()
        my_events = []
        my_events.append(EventParticipation.query.filter_by(userId=userId))
        
        myEvent = MyEvents(
            username = ['username'],

        )
            
        
class LoginApi(Resource):
    def post(self):
        #Get passed arguments from the user
        args = login_args.parse_args()

        #get user object
        participant = Participant.query.filter_by(username=args['username']).first_or_404()

        #check if password is correct
        authorized = participant.check_password(args['password'])
        if not authorized:
            abort(401, message="Email or password is invalid")

        #Set expiration
        expires = datetime.timedelta(days=7)

        #Create access token, which the user uses for further requests
        access_token = create_access_token(identity=str(participant.userid), expires_delta=expires)

        #Get expiration date
        expiresAt = datetime.datetime.utcnow() + expires
        expiresAt_str = expiresAt.strftime("%Y-%m-%d %H:%M:%S")

        #Return relevant information
        print(access_token)
        return {
            'token': access_token,
            'expiresAt': expiresAt_str,
            'userId': participant.userid,
            'username': participant.username,
            'email': participant.email,
            }, 200

            