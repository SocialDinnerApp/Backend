from flask_restful import Resource, marshal_with, abort, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from src import db
from src.resources import event_participations, participant
from src.resources.cookingLocation import model
from src.resources.event_participations.model import EventParticipation
from src.resources.event.model import Event
from src.resources.event_team_matching.model import eventTeamMatching
from src.resources.participant.model import Participant
from src.resources.cookingLocation.model import CookingLocation
from src.resources.event_participations.args import post_args, update_args
from src.resources.event_participations.fields import resource_fields
from uuid import uuid4
from flask import json, jsonify
import datetime

class Event_ParticipationsAPI(Resource):
    @jwt_required()
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

    @jwt_required()
    @marshal_with(resource_fields)
    def get(self, id=None):
        event_participations = EventParticipation.query.filter_by(teamId=id).first_or_404()
        teamId = event_participations.teamId

        if teamId:
            return event_participations, 200
        else:
            abort(400, message='Error')

class Get_event_detailsAPI(Resource):

    @jwt_required()
    #@marshal_with(resource_fields)
    def get(self, eventId=None):

        userId = get_jwt_identity()

        #Event information
        event_information = db.session.query(Event).filter(Event.eventId == eventId).all()
        event_eventId = event_information[0].eventId
        event_description = event_information[0].description
        event_date = event_information[0].date
        event_starter_time = event_information[0].time_starter
        event_main_time= event_information[0].time_main
        event_dessert_time = event_information[0].time_dessert

        # Participation information for special Event 
        event_participation = db.session.query(EventParticipation).filter((EventParticipation.userId == userId) | (EventParticipation.partner_userId == userId)).filter(EventParticipation.eventId == event_eventId).all()
        teamId = event_participation[0].teamId

        # Team_MatchingId
        event_team_matchingId = db.session.query(eventTeamMatching).filter(eventTeamMatching.teamId == teamId).first()
        if event_team_matchingId:
            starter_id = event_team_matchingId.starterTeamId
            main_id = event_team_matchingId.mainTeamId
            dessert_id = event_team_matchingId.dessertTeamId

            teamId_starter = db.session.query(EventParticipation).filter(EventParticipation.teamId == starter_id).first()
            starter_name = db.session.query(Participant).filter(Participant.userid == teamId_starter.userId).first()
            starter_name = starter_name.username

            teamId_main = db.session.query(EventParticipation).filter(EventParticipation.teamId == main_id).first()
            main_name = db.session.query(Participant).filter(Participant.userid == teamId_main.userId).first()
            main_name = main_name.username


            teamId_dessert = db.session.query(EventParticipation).filter(EventParticipation.teamId == dessert_id).first()
            dessert_name = db.session.query(Participant).filter(Participant.userid == teamId_dessert.userId).first()
            dessert_name = dessert_name.username

            #Get location information for starter
            cooking_location_starter = db.session.query(CookingLocation).filter(CookingLocation.cookinglocationId == teamId_starter.cooking_locationId).all()
            starter_zipcode = cooking_location_starter[0].zip_code
            starter_city = cooking_location_starter[0].city
            starter_street = cooking_location_starter[0].street
            starter_housenumber = cooking_location_starter[0].housenumber
            starter_hints = cooking_location_starter[0].hints
            starter_floor = cooking_location_starter[0].floor

            #Get location information for main
            cooking_location_main = db.session.query(CookingLocation).filter(CookingLocation.cookinglocationId == teamId_main.cooking_locationId).all()
            main_zipcode = cooking_location_main[0].zip_code
            main_city = cooking_location_main[0].city
            main_street = cooking_location_main[0].street
            main_housenumber = cooking_location_main[0].housenumber
            main_hints = cooking_location_main[0].hints
            main_floor = cooking_location_main[0].floor

            #Get location information for dessert
            cooking_location_dessert = db.session.query(CookingLocation).filter(CookingLocation.cookinglocationId == teamId_dessert.cooking_locationId).all()
            dessert_zipcode = cooking_location_dessert[0].zip_code
            dessert_city = cooking_location_dessert[0].city
            dessert_street = cooking_location_dessert[0].street
            dessert_housenumber = cooking_location_dessert[0].housenumber
            dessert_hints = cooking_location_dessert[0].hints
            dessert_floor = cooking_location_dessert[0].floor


            event_information_dict = {'event_information': 
                    {'event_name': event_information[0].name,
                    'event_date': event_date,
                    'event_starter_time': event_starter_time,
                    'event_main_time': event_main_time,
                    'event_dessert_time': event_dessert_time,
                    'event_description': event_description},
                    'starter':{
                        'starter_name': starter_name,
                        'starter_zipcode':  starter_zipcode,
                        'starter_city': starter_city, 
                        'starter_street': starter_street,
                        'starter_housenumber':starter_housenumber,
                        'starter_hints': starter_hints, 
                        'starter_floor': starter_floor},
                    'main':{
                        'main_name': main_name,
                        'main_zipcode':  main_zipcode,
                        'main_city': main_city, 
                        'main_street': main_street,
                        'main_housenumber': main_housenumber,
                        'main_hints': main_hints,
                        'main_floor': main_floor},
                    'dessert': {
                        'dessert_name': dessert_name,
                        'dessert_zipcode': dessert_zipcode,
                        'dessert_city': dessert_city,
                        'dessert_street': dessert_street,
                        'dessert_housenumber': dessert_housenumber,
                        'dessert_hints': dessert_hints,
                        'dessert_floor': dessert_floor
                        }}
        else:
            event_information_dict = {'event_information': 
                    {'event_name': event_information[0].name,
                    'event_date': event_date,
                    'event_starter_time': event_starter_time,
                    'event_main_time': event_main_time,
                    'event_dessert_time': event_dessert_time,
                    'event_description': event_description},
                    'starter':{
                        'starter_name': "Ausstehend",
                        'starter_zipcode':  "Ausstehend",
                        'starter_city': "Ausstehend", 
                        'starter_street': "Ausstehend",
                        'starter_housenumber':"Ausstehend",
                        'starter_hints': "Ausstehend", 
                        'starter_floor': "Ausstehend"},
                    'main':{
                        'main_name': "Ausstehend",
                        'main_zipcode':  "Ausstehend",
                        'main_city': "Ausstehend", 
                        'main_street': "Ausstehend",
                        'main_housenumber': "Ausstehend",
                        'main_hints': "Ausstehend",
                        'main_floor': "Ausstehend"},
                    'dessert': {
                        'dessert_name': "Ausstehend",
                        'dessert_zipcode': "Ausstehend",
                        'dessert_city': "Ausstehend",
                        'dessert_street': "Ausstehend",
                        'dessert_housenumber': "Ausstehend",
                        'dessert_hints': "Ausstehend",
                        'dessert_floor': "Ausstehend"
                        }}

            

        return event_information_dict