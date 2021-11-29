from flask_restful import Resource, marshal_with, abort, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import db
from app.resources.participant.model import Participant
from app.resources.participant.args import post_args, update_args, login_args