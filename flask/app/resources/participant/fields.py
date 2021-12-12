from flask_restful import fields


resource_fields = {
    'userid': fields.String,
    'username': fields.String,
    'email': fields.String,
    # 'password': fields.String,
    'datetime_created': fields.String
}
