from sqlalchemy.orm import backref
from app import db
from datetime import date, datetime
from flask_bcrypt import generate_password_hash, check_password_hash

class Participant(db.Model):
    userid = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    datetime_created = db.Column(db.DateTime, default=datetime.utcnow)
    #datetime_updated = db.Column(db.DateTime, default=datetime.utcnow))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)