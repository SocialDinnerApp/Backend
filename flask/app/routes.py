from app import api
from app.resources.organizer.api import OrganizerAPI
from app.resources.organizer.model import Organizer 
from app.resources.participant.api import ParticipantAPI
from app.resources.event.api import EventAPI

#Participant API
api.add_resource(ParticipantAPI, '/api/participant', '/api/participant/<string:id>')

#Organizer API
api.add_resource(OrganizerAPI, '/api/organizer', '/api/organizer/<string:id>')

#Event API
api.add_resource(EventAPI, '/api/event', '/api/event/<string:id>')