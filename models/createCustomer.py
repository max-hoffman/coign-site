from flask import request, json, jsonify
from flask_restful import Resource, abort, Api
import stripe

stripe.api_key = "sk_test_fqD4n0Wm1j1gPIYlH7R4NQhS"

class CreateCustomer(Resource):

	def post(self):

		args = json.loads(request.data)
		new = args['new']
		userID = args['userID']

		if userID is not None:
			if new:
				try:
					return stripe.Customer.create(description = userID)
					#customer = stripe.Customer.create(description = userID)
					customerObject = json.loads(customer)
					return jsonify(customerObject), 200
				except:
					return 'Failed to create customer', 402
			else:
				return 'Need to specify whether to create new customer or not', 402
		else:
			return 'No user ID provided ', 402