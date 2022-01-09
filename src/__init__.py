import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

# Set environment variables
#os.environ['ENV_FILE_LOCATION'] = './.env'
app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'super-secret' # must be changed
jwt = JWTManager(app)

#app.config.from_envvar('ENV_FILE_LOCATION')
api = Api(app)


database_uri = os.environ['DATABASE_URI']


app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
CORS(app)
db = SQLAlchemy(app)


from src.resources.organizer.model import Organizer
from src.resources.participant.model import Participant
from src.resources.event.model import Event
from src.resources.cookingLocation.model import CookingLocation
from src.resources.event_participations.model import EventParticipation
from src.resources.event_team_matching.model import eventTeamMatching