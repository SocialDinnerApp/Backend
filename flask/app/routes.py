from app import api
from app.resources.organizer.api import OrganizerAPI
from app.resources.organizer.model import Organizer 


from app.resources.participant.api import ParticipantAPI, LoginApi, MyEventsAPI
from app.resources.participant.model import Participant


from app.resources.event.api import EventAPI
from app.resources.event.api import getActiveEvents
from app.resources.event.model import Event

from app.resources.cookingLocation.api import CookingLocationAPI
from app.resources.cookingLocation.model import CookingLocation

from app.resources.event_participations.api import Event_ParticipationsAPI, Get_event_detailsAPI
from app.resources.event_participations.model import EventParticipation

from app.resources.event_team_matching.api import Event_Team_MatchingAPI
from app.resources.event_team_matching.model import eventTeamMatching

from app.resources.participation.api import ParticipationAPI


#Participant API
api.add_resource(ParticipantAPI, '/api/participant', '/api/participant/<string:id>')
api.add_resource(LoginApi, '/api/participant/login')
api.add_resource(MyEventsAPI, '/api/participant/myEvents')

#Participation API
api.add_resource(ParticipationAPI, '/api/participation')


#Organizer API
api.add_resource(OrganizerAPI, '/api/organizer', '/api/organizer/<string:id>')
#api.add_resource(LoginApi, '/api/organizer/login')

#Event API
api.add_resource(EventAPI, '/api/event', '/api/event/<string:id>')
api.add_resource(getActiveEvents, '/api/event/getActiveEvents')

#CookingLocation API
api.add_resource(CookingLocationAPI, '/api/cookingLocation', '/api/cookingLocation/<string:id>')

#Event_Paticipations API
api.add_resource(Event_ParticipationsAPI, '/api/eventParticipation', '/api/eventParticipation/<string:id>')
api.add_resource(Get_event_detailsAPI, '/api/eventParticipation/event_details', '/api/eventParticipation/event_details/<string:eventId>')

#Event_Team_Matching API
api.add_resource(Event_Team_MatchingAPI, '/api/eventTeamMatching', '/api/eventTeamMatching/<string:id>')