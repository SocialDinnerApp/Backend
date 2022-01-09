from flask_restful import reqparse


post_args = reqparse.RequestParser()
post_args.add_argument("eventId", type=str, help="teamId is required", required=True)