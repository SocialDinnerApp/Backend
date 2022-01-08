from flask_restful import reqparse

#Was muss für ein bestimmten Request übergeben
post_args_emailexistence = reqparse.RequestParser()
post_args_emailexistence.add_argument("email", type=str, help="email is required", required=True)
post_args_emailexistence.add_argument("val_key", type=str, help="val key is required", required=True)

post_args_usernameexistence = reqparse.RequestParser()
post_args_usernameexistence.add_argument("username", type=str, help="username is required", required=True)
post_args_usernameexistence.add_argument("val_key", type=str, help="val key is required", required=True)

post_args_matchingusernames = reqparse.RequestParser()
post_args_matchingusernames.add_argument("username", type=str, help="username is required", required=True)
post_args_matchingusernames.add_argument("val_key", type=str, help="val key is required", required=True)
post_args_matchingusernames.add_argument("eventId", type=str, help="eventId is required", required=True)