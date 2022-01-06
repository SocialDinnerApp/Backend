from src import app
from src import routes

#from flask import Flask
#from flask_restful import Api, Resource

#app = Flask(__name__)
#api = Api(app)

#names = {"tim": {"age": 19, "gender": "male"},


#class HelloWorld(Resource):
#    def get(self, name):
#        #return {"name": name, "test": test, }
#        return names[name]

#    def post(self):
#        return {"data": "posted"}

# Endpoint to find the resource
#api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)