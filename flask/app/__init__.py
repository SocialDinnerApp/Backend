from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/database.db'
CORS(app)
db = SQLAlchemy(app)

from app.resources.organizer.model import Organizer
from app.resources.participant.model import Participant
from app.resources.event.model import Event
from app.resources.cookingLocation.model import CookingLocation