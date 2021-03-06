from flask_restful import Resource, marshal_with, abort, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from src import db
from src.resources.organizer.model import Organizer
from src.resources.organizer.args import post_args, update_args, login_args
from src.resources.organizer.fields import resource_fields
from authorization import val_key
from uuid import uuid4
import datetime

class OrganizerAPI(Resource):
    @marshal_with(resource_fields)
    def post(self):
        
        #Get arguments
        args = post_args.parse_args()

        if args["val_key"] != val_key:
            abort(401, message='You are not allowed')
        

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

class OrganizerLoginApi(Resource):
    def post(self):
        #Get passed arguments from the user
        args = login_args.parse_args()

        #get user object
        organizer = Organizer.query.filter_by(username=args['username']).first_or_404()

        #check if password is correct
        authorized = organizer.check_password(args['password'])
        if not authorized:
            abort(401, message="username or password is invalid")

        #Set expiration
        expires = datetime.timedelta(days=7)

        #Create access token, which the user uses for further requests
        access_token = create_access_token(identity=str(organizer.organizerId), expires_delta=expires)

        #Get expiration date
        expiresAt = datetime.datetime.utcnow() + expires
        expiresAt_str = expiresAt.strftime("%Y-%m-%d %H:%M:%S")

        #Return relevant information
        print(access_token)
        return {
            'token': access_token,
            'expiresAt': expiresAt_str,
            'userId': organizer.organizerId,
            'username': organizer.username,
            'email': organizer.email,
            }, 200