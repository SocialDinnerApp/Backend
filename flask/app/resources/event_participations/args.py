from flask_restful import reqparse

#Was muss für ein bestimmten Request übergeben
post_args = reqparse.RequestParser()
post_args.add_argument("userId", type=str, help="userId of the event is required", required=True)
post_args.add_argument("partner_userId", type=str, help="partner_userId of the event is required", required=True)
post_args.add_argument("eventId", type=str, help="eventId of the event is required", required=True)
post_args.add_argument("cooking_locationId", type=str, help="cooking_locationId of the event is required", required=True)

update_args = reqparse.RequestParser()
update_args.add_argument("userId", type=str, help="userId of the event is required")
update_args.add_argument("partner_userId", type=str, help="partner_userId of the event is required")
update_args.add_argument("eventId", type=str, help="eventId of the event is required")
update_args.add_argument("cooking_locationId", type=str, help="cooking_locationId of the event is required")
