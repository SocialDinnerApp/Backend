from app import api 
from app.resources.participant.api import ParticipantAPI

# Participant API
api.add_resource(ParticipantAPI, '/api/participant', '/api/participant/<string:id>')