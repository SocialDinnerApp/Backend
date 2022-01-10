from src.resources.event.model import Event
from src.resources.visualization.revenue.args import post_args
from flask_restful import Resource, marshal_with, abort, request
from src.resources.visualization.revenue.fields import resource_fields


class MontlyRevenueAPI(Resource):

    # @jwt_required()
    # @marshal_with(resource_fields)
    def get(self):

        #Get arguments
        args = post_args.parse_args()

        events = Event.query.filter_by(org_Id=args['organizerId']).all()

        print(events)





        