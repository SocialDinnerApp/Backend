from flask_restful import fields

# #Rückgabe Format
resource_fields = {
    'date': fields.Integer,
    'name': fields.String,
    'value': fields.Integer
}