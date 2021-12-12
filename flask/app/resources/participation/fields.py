from flask_restful import fields

#Rückgabe Format
resource_fields = {
    'cookinglocationId': fields.String,
    'zip_code': fields.Integer,
    'city': fields.String,
    'street': fields.String,
    'housenumber': fields.Integer,
    'floor': fields.Integer,
    'hints': fields.String,
    'username_partner': fields.String,
    'userId': fields.String,
    'eventId': fields.String    
}