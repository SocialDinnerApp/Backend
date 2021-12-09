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

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/database.db'
CORS(app)
db = SQLAlchemy(app)


from app.resources.organizer.model import Organizer
from app.resources.participant.model import Participant
from app.resources.event.model import Event
from app.resources.cookingLocation.model import CookingLocation
from app.resources.event_participations.model import EventParticipation
from app.resources.event_team_matching.model import eventTeamMatching