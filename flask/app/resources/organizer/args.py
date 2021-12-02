from flask_restful import reqparse

#Was muss für ein bestimmten Request übergeben
post_args = reqparse.RequestParser()
post_args.add_argument("username", type=str, help="name of the organizer is required", required=True)
post_args.add_argument("email", type=str, help="email of the organizer is required", required=True)
post_args.add_argument("password", type=str, help="password of the organizer is required", required=True)
post_args.add_argument("university", type=str, help="university of the organizer is required", required=True)
post_args.add_argument("city", type=str, help="city of the organizer is required", required=True)
post_args.add_argument("faculty", type=str, help="faculty of the organizer is required", required=True)


update_args = reqparse.RequestParser()
update_args.add_argument("username", type=str, help="name of the organizer is required", required=True)
update_args.add_argument("email", type=str, help="email of the organizer is required", required=True)
update_args.add_argument("password", type=str, help="password of the organizer is required", required=True)
update_args.add_argument("university", type=str, help="university of the organizer is required", required=True)
update_args.add_argument("city", type=str, help="city of the organizer is required", required=True)
update_args.add_argument("faculty", type=str, help="faculty of the organizer is required", required=True)

login_args = reqparse.RequestParser()
login_args.add_argument("email", type=str, help="email of the organizer is required", required=True)
login_args.add_argument("password", type=str, help="password of the organizer is required", required=True)
