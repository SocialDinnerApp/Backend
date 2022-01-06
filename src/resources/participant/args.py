from flask_restful import reqparse

post_args = reqparse.RequestParser()
post_args.add_argument("email", type=str, help="email of the user is required", required=True)
post_args.add_argument("username", type=str, help="name of the user is required", required=True)
post_args.add_argument("password", type=str, help="password of the user is required", required=True)
post_args.add_argument("val_key", type=str, help="val_key is required", required=True)


update_args = reqparse.RequestParser()
update_args.add_argument("email", type=str, help="email of the user is required")
update_args.add_argument("username", type=str, help="name of the user is required")
update_args.add_argument("password", type=str, help="password of the user is required")

login_args = reqparse.RequestParser()
login_args.add_argument("username", type=str, help="username of the user is required", required=True)
login_args.add_argument("password", type=str, help="password of the user is required", required=True)
