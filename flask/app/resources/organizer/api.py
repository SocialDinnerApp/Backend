from flask_restful import Resource, marshal_with, abort, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import db
from app.resources.organizer.model import Organizer
from app.resources.organizer.args import post_args, update_args, login_args
from app.resources.organizer.fields import resource_fields
from uuid import uuid4
import datetime

class OrganizerAPI(Resource):
    @marshal_with(resource_fields)
    def post(self):
        
        #Get arguments
        args = post_args.parse_args()

        #Create unique ID
        id = str(uuid4())

        #Create organizer object
        organizer = Organizer(
            organizerId = id,
            username = args['username'],
            email = args['email'],
            password = args['password'],
            university = args['university'],
            city = args['city'],
            faculty = args['faculty'],
        )

        #Model integration
        organizer.hash_password()

        #Add user to database
        db.session.add(organizer)
        db.session.commit()

        #Select created organizer
        organizer_created = Organizer.query.filter_by(organizerId=id).first()

        #Return recently created organizer
        return organizer_created, 201


    @jwt_required()
    @marshal_with(resource_fields)
    def get(self, id=None):
        #Get organizerId
        #organizer_key = get_jwt_identity()
        organizer = Organizer.query.filter_by(organizerId=id).first_or_404()
        username = organizer.username

        if username:
            return organizer, 200
        else:
            abort(400, message='Error')