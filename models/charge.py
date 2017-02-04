from flask import request, json
from flask_restful import Resource, abort, Api
import stripe

stripe.api_key = "sk_test_fqD4n0Wm1j1gPIYlH7R4NQhS"

class Charge(Resource):

	def post(self):
		args = json.loads(request.data)
		source = args["source"]
		userID = args["userID"]
		customerID = args["customerID"]

		if source is not None:
			try:
				charge = stripe.Charge.create(
				  amount = 100,
				  currency = "usd",
				  description = "Donation from {0}".format(userID),
				  customer = customerID,
				  source = source,
				  statement_descriptor = "Donation to Coign"
				)
				return 'Payment success', 200
			except stripe.error.CardError, e:
				return {"result" : e}, 500
			except Exception as e:
				print(e)
			return {"result" : e}, 500
		else:
			return 'No token provided', 402