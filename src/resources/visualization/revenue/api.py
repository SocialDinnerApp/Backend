from math import e
from src.resources.event.model import Event
from src.resources.event_participations.model import EventParticipation
from src.resources.visualization.revenue.args import post_args
from flask_restful import Resource, marshal_with, abort, request
from src.resources.visualization.revenue.fields import resource_fields
from sqlalchemy import extract
from flask import jsonify
import datetime
from src import db


class MontlyRevenueAPI(Resource):

    # @jwt_required()
    #@marshal_with(resource_fields)
    def get(self):

        #Get arguments
        args = post_args.parse_args()

        # Rein machen !!!!
        #organizer_id = get_jwt_identity()

        event_this_month = db.session.query(Event).filter((datetime.datetime.now().month == extract('month', Event.registration_deadline)) and (Event.org_Id == args['organizerId'])).all()
        
        count_revenu = 0
        for event in event_this_month:
            sum_of_participants = 0
            eventId = event.eventId
            participants = db.session.query(EventParticipation).filter(EventParticipation.eventId == eventId).all()
            for participant in participants:
                sum_of_participants += 1
            event_revenue = 0
            event_revenue = event_revenue + sum_of_participants * event.fee
            count_revenu = count_revenu + sum_of_participants * event.fee
            print(f'Sum of participants: for {event}:', sum_of_participants)
            print(f'Revenue:', event_revenue)

        print(f'Overall revenue:', count_revenu)


        return jsonify(revenue=count_revenu)




        