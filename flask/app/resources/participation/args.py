from flask_restful import reqparse

#Was muss für ein bestimmten Request übergeben
post_args = reqparse.RequestParser()
post_args.add_argument("zip_code", type=str, help="zip_code of the cookinglocation is required", required=True)
post_args.add_argument("city", type=str, help="city of the cookinglocation is required", required=True)
post_args.add_argument("street", type=str, help="street of the cookinglocation is required", required=True)
post_args.add_argument("housenumber", type=str, help="housenumber of the cookinglocation is required", required=True)
post_args.add_argument("floor", type=str, help="floor of the cookinglocation is required", required=True)
post_args.add_argument("hints", type=str, help="hints of the cookinglocation is required")
post_args.add_argument("username_partner", type=str, help="username_partner of the cookinglocation is required", required=True)
post_args.add_argument("userId", type=str, help="username_partner of the cookinglocation is required", required=True)
post_args.add_argument("eventId", type=str, help="username_partner of the cookinglocation is required", required=True)