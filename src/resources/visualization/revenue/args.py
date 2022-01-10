from flask_restful import reqparse

#Was muss für ein bestimmten Request übergeben
post_args = reqparse.RequestParser()
post_args.add_argument("organizerId", type=str, help="organizerId of the organizer is required", required=True)
