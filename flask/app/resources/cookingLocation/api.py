import re
from flask_restful import Resource, marshal_with, abort, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import db
from app.resources import cookingLocation
from app.resources.cookingLocation.model import CookingLocation
from app.resources.cookingLocation.args import post_args, update_args
from app.resources.cookingLocation.fields import resource_fields

from uuid import uuid4
import datetime

class CookingLocationAPI(Resource):
    @marshal_with(resource_fields)
    def post(self):

        #Get arguments
        args = post_args.parse_args()

        #Create unique ID
        id = str(uuid4())

        #Create cookingLocation object
        cookingLocation = CookingLocation(
            cookinglocationId = id,
            zip_code = args['zip_code'],
            city = args['city'],
            street = args['street'],
            housenumber = args['housenumber'],
            floor = args['floor'],
            hints = args['hints'],
        )

        #Model integration   
        #cookingLocation.hash_password()

        #Add cookingLocation to database
        db.session.add(cookingLocation)
        db.session.commit()

        #Select created cookingLocation
        cookingLocation_created = CookingLocation.query.filter_by(cookinglocationId=id).first()

        #Return recently created cookingLocation
        return cookingLocation_created, 201