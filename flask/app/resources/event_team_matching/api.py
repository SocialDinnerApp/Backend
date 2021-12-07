from flask_restful import Resource, marshal_with, abort, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import db
from app.resources import event_participations
from app.resources.event_team_matching.model import eventTeamMatching
from app.resources.event_team_matching.args import post_args, update_args
from uuid import uuid4
import datetime
from app.resources.event_team_matching.fields import resource_fields


class Event_Team_MatchingAPI(Resource):
    @marshal_with(resource_fields)
    def post(self):

        #Get arguments
        args = post_args.parse_args()

        #Create unique ID
        id = str(uuid4())

        event_Team_Matching = eventTeamMatching(
            matchingId = id,
            teamId = args['teamId'],
            eventId = args['eventId'],
            starterTeamId = args['starterTeamId'],
            mainTeamId = args['mainTeamId'],
            dessertTeamId = args['dessertTeamId']
        )

        #Add event_Team_Matching to database
        db.session.add(event_Team_Matching)
        db.session.commit()

        #Select created event_Team_Matching
        event_Team_Matching_created = eventTeamMatching.query.filter_by(matchingId=id).first()

        #Return recently created event_Team_MatchingAPI
        return event_Team_Matching_created, 201