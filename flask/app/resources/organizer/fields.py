from flask_restful import fields

#Rückgabe Format

resource_fields = {
    'organizerId': fields.String,
    'username': fields.String,
    'email': fields.String,
    'password': fields.String,
    'university': fields.String,
    'city': fields.String,
    'faculty': fields.String,
    'datetime_created': fields.String,
    'datetime_updated': fields.String
}