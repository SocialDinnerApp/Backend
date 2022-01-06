from flask_restful import reqparse

#Was muss für ein bestimmten Request übergeben
post_args = reqparse.RequestParser()
post_args.add_argument("name", type=str, help="name of the event is required", required=True)
#post_args.add_argument("image", type=str, help="base64 of the image is required", required=True)
post_args.add_argument("description", type=str, help="description of the event is required", required=True)
post_args.add_argument("fee", type=int, help="fee of the event is required", required=True)
post_args.add_argument("date", type=str, help="date of the event is required", required=True)
post_args.add_argument("time_starter", type=str, help="time_starter of the event is required", required=True)
post_args.add_argument("time_main", type=str, help="time_main of the event is required", required=True)
post_args.add_argument("time_dessert", type=str, help="time_dessert of the event is required", required=True)
post_args.add_argument("org_id", type=str, help="name of the event is required", required=True)
post_args.add_argument("city", type=str, help="city of the event is required", required=True)
post_args.add_argument("zip_code", type=int, help="zip_code of the event is required", required=True)
post_args.add_argument("isPublic", type=bool, help="isPublic of the event is required", required=True)
post_args.add_argument("max_participants", type=int, help="max_participants of the event is required", required=True)
post_args.add_argument("registration_deadline", type=str, help="registration_deadline of the event is required", required=True)


update_args = reqparse.RequestParser()
update_args.add_argument("name", type=str, help="name of the event is required")
update_args.add_argument("description", type=str, help="description of the event is required")
update_args.add_argument("fee", type=int, help="fee of the event is required")
update_args.add_argument("date", type=str, help="date of the event is required")
update_args.add_argument("time_starter", type=str, help="time_starter of the event is required")
update_args.add_argument("time_main", type=str, help="time_main of the event is required")
update_args.add_argument("time_dessert", type=str, help="time_dessert of the event is required")
update_args.add_argument("org_id", type=str, help="name of the event is required")
update_args.add_argument("city", type=str, help="city of the event is required")
update_args.add_argument("zip_code", type=int, help="zip_code of the event is required")
update_args.add_argument("isPublic", type=bool, help="isPublic of the event is required")
update_args.add_argument("max_participants", type=int, help="max_participants of the event is required")
update_args.add_argument("registration_deadline", type=str, help="registration_deadline of the event is required")