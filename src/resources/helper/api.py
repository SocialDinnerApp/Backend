import re
from flask_restful import Resource, marshal_with, abort, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from authorization import val_key
from src import db
from src.resources.helper.args import post_args_emailexistence, post_args_usernameexistence, post_args_matchingusernames
from src.resources.participant.model import Participant
from src.resources.event_participations.model import EventParticipation


from uuid import uuid4
import datetime

class EmailExistenceAPI(Resource):
    def get(self):

        #Get arguments
        args = post_args_emailexistence.parse_args()

        if args["val_key"] != val_key:
            abort(401, message='You are not allowed')

        mailexists = Participant.query.filter_by(email=args['email']).first()
        if mailexists:
            return {'exists' : 'true'}, 200
        else:
            return {'exists' : 'false'}, 200

class UsernameExistenceAPI(Resource):
    def get(self):

        #Get arguments
        args = post_args_usernameexistence.parse_args()

        if args["val_key"] != val_key:
            abort(401, message='You are not allowed')

        usernameexists = Participant.query.filter_by(username=args['username']).first()
        if usernameexists:
            return {'exists' : 'true'}, 200
        else:
            return {'exists' : 'false'}, 200

class MatchingUsernamesAPI(Resource):
    @jwt_required()
    def get(self):

        #Get arguments
        args = post_args_matchingusernames.parse_args()
        userId = get_jwt_identity()

        if args["val_key"] != val_key:
            abort(401, message='You are not allowed')
        if not args["username"]:
            return {'usernames' : []}, 200

        allUsers = Participant.query.all()
        matchingUsers = [user.userid for user in allUsers if user.username.startswith(args['username']) and user.userid != userId]
        print('All User')
        print(matchingUsers)

        #Subtract user, which are already in registered for this event
        allParticipations = EventParticipation.query.filter_by(eventId=args['eventId']).all()
        part_userids = [parts.partner_userId for parts in allParticipations] + [parts.userId for parts in allParticipations]
        print('Alle user, die bereits für dieses Event angemeldet sind')
        print(part_userids)

        matchingUsers = [matchu for matchu in matchingUsers if matchu not in part_userids]
        print('All Users abzüglich')
        print(matchingUsers)
        matchingUsers = db.session.query(Participant.username).filter(Participant.userid.in_(matchingUsers)).all()
        # print(type(matchingUsers))
        #Unpack tuple
        matchingUsers = [matchu[0] for matchu in matchingUsers]
        print(matchingUsers)
        return {'usernames' : matchingUsers}, 200