from flask_restful import fields

resource_fields = {
    'matchingId': fields.String,
    'teamId': fields.String,
    'eventId': fields.String,
    'starterTeamId': fields.String,
    'mainTeamId': fields.String,
    'dessertTeamId': fields.String
    }