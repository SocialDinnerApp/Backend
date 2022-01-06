from flask_restful import reqparse

#Was muss für ein bestimmten Request übergeben
post_args = reqparse.RequestParser()
post_args.add_argument("teamId", type=str, help="teamId is required", required=True)
post_args.add_argument("eventId", type=str, help="eventId is required", required=True)
post_args.add_argument("starterTeamId", type=str, help="starterTeamId  is required", required=True)
post_args.add_argument("mainTeamId", type=str, help="mainTeamId is required", required=True)
post_args.add_argument("dessertTeamId", type=str, help="dessertTeamId  is required", required=True)

update_args = reqparse.RequestParser()
update_args.add_argument("teamId", type=str, help="teamId is required")
update_args.add_argument("eventId", type=str, help="eventId is required")
update_args.add_argument("starterTeamId", type=str, help="starterTeamId is required")
update_args.add_argument("mainTeamId", type=str, help="mainTeamId  is required")
update_args.add_argument("dessertTeamId", type=str, help="dessertTeamId is required")