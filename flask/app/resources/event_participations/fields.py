from flask_restful import fields

resource_fields = {
    'teamId': fields.String,
    'userId': fields.String,
    'partner_userId': fields.String,
    'eventId': fields.String,
    'cooking_locationId': fields.String,
    }