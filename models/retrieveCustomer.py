from flask import request, json, jsonify
from flask_restful import Resource, abort, Api
import stripe

stripe.api_key = "sk_test_fqD4n0Wm1j1gPIYlH7R4NQhS"

class RetrieveCustomer(Resource):

	def post(self):
		args = json.loads(request.data)
		customerID = args['stripeID']
		
		if customerID is not None:
			try:
				#return stripe.Customer.retrieve(customerID), 200
				customer = stripe.Customer.retrieve(customerID)
				customerObject = json.loads(customer)
				return jsonify(customerObject), 200
			except Exception as e: 
				return str(e) 
		else:
			return 'Did not provide customer ID', 402