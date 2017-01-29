from flask import request, json
from flask_restful import Resource, abort, Api
import stripe

stripe.api_key = "sk_test_fqD4n0Wm1j1gPIYlH7R4NQhS"

class Charge(Resource):

	def post(self):
		args = json.loads(request.data)
		token = args["token"]
		userID = args["userID"]

		if token is not None:
			try:
				charge = stripe.Charge.create(
				  amount=1000,
				  currency="usd",
				  description="Donation from  {0}".format(userID),
				  source=token,
				)
				return 'Payment success', 200
			except:
				return 'Invalid token provided', 402
		else:
			return 'No token provided', 402