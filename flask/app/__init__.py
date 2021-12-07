from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/database.db'
db = SQLAlchemy(app)

from app.resources.organizer.model import Organizer
from app.resources.participant.model import Participant
from app.resources.event.model import Event
from app.resources.cookingLocation.model import CookingLocation