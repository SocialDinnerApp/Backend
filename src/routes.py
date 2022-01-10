from src import api
from src.resources.organizer.api import OrganizerAPI
from src.resources.organizer.model import Organizer 


from src.resources.participant.api import ParticipantAPI, LoginApi, MyEventsAPI
from src.resources.participant.model import Participant


from src.resources.event.api import EventAPI
from src.resources.event.api import getActiveEvents
from src.resources.event.model import Event

from src.resources.cookingLocation.api import CookingLocationAPI
from src.resources.cookingLocation.model import CookingLocation

from src.resources.event_participations.api import Event_ParticipationsAPI, Get_event_detailsAPI
from src.resources.event_participations.model import EventParticipation

from src.resources.event_team_matching.api import Event_Team_MatchingAPI
from src.resources.matching.api import TeamMatchingAlgorithmus
from src.resources.event_team_matching.model import eventTeamMatching

from src.resources.participation.api import ParticipationAPI

from src.resources.helper.api import EmailExistenceAPI, UsernameExistenceAPI, MatchingUsernamesAPI


from src.resources.visualization.revenue.api import MontlyRevenueAPI


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
api.add_resource(TeamMatchingAlgorithmus, '/api/eventTeamMatching/run', '/api/eventTeamMatching/run/<string:id>')

#Helpers
api.add_resource(EmailExistenceAPI, '/api/emailexistence')
api.add_resource(UsernameExistenceAPI, '/api/usernameexistence')
api.add_resource(MatchingUsernamesAPI, '/api/matchingusernames')

api.add_resource(MontlyRevenueAPI, '/api/monthlyrevenue')

