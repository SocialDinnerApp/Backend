from flask_restful import fields


resource_fields = {
    'userid': fields.String,
    'username': fields.String,
    'email': fields.String,
    # 'password': fields.String,
    'datetime_created': fields.String
}


resource_fields2 = {
    'eventId': fields.String,
    'name': fields.String,
    'description': fields.String,
    'org_Id': fields.String,
    'fee': fields.Integer,
    'date': fields.String,
    'time_starter': fields.String,
    'time_main': fields.String,
    'time_dessert': fields.String,
    'city': fields.String,
    'zip_code': fields.Integer,
    'isPublic': fields.Boolean,
    'max_participants': fields.Integer,
    'registration_deadline': fields.String,
    'datetime_created': fields.String,
    'datetime_updated': fields.String
}