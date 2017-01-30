from flask import request, json, jsonify
from flask_restful import Resource, abort, Api
import stripe

stripe.api_key = "sk_test_fqD4n0Wm1j1gPIYlH7R4NQhS"

class RetrieveCustomer(Resource):

	def post(self):
		args = json.loads(request.data)
		customerID = args['stripeID']

		if StripeID is not None:
			try:
				customer = stripe.Customer.retrieve(customerID)
				customerObject = json.loads(customer)
				return jsonify(customer), 200
			except:
				return 'Failed to find customer', 402
		else:
			return 'Did not provide customer ID', 402