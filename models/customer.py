from flask import request, json
from flask_restful import Resource, reqparse, abort, Api
import stripe

stripe.api_key = "sk_test_fqD4n0Wm1j1gPIYlH7R4NQhS"

class Customer(Resource):

	def post(self):
		args = json.loads(request.data)
		new = args['new']
		
		return args
		if new:
			customer = stripe.Customer.create(description = "test")
			return (json.dumps(customer), 200)
		else:
			try:
				stripeID = args['stripeID']
				customer = stripe.Customer.retrieve(stripeID)
				return (json.dumps(customer), 200)
			except stripe.error.StripeError as e:
				return 'There exists no customer with the given ID', 402