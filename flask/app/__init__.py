from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLAlchemy_DATABASE_URI'] = 'sqllite:///data/database.db'
db = SQLAlchemy(app)
db.create_all()
