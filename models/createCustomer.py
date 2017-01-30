from flask import request, json, jsonify
from flask_restful import Resource, abort, Api
import stripe

stripe.api_key = "sk_test_fqD4n0Wm1j1gPIYlH7R4NQhS"

class CreateCustomer(Resource):

	def post(self):

		customerString = "{\"account_balance\": 0, \"created\": 1485723158, \"currency\": null, \"default_source\": null, \"delinquent\": false, \"description\": \"123456\", \"discount\": null, \"email\": null, \"id\": \"cus_A1Sagqm1XX9tOU\", \"livemode\": false, \"metadata\": {}, \"object\": \"customer\", \"shipping\": null, \"sources\": {\"data\": [], \"has_more\": false, \"object\": \"list\", \"total_count\": 0, \"url\": \"/v1/customers/cus_A1Sagqm1XX9tOU/sources\"}, \"subscriptions\": {\"data\": [], \"has_more\": false, \"object\": \"list\", \"total_count\": 0, \"url\": \"/v1/customers/cus_A1Sagqm1XX9tOU/subscriptions\"}}"
		customerObject = json.loads(customerString)
		return jsonify(customerObject)

		args = json.loads(request.data)
		new = args['new']
		userID = args['userID']

		if userID is not None:
			if new:
				try:
					customer = stripe.Customer.create(description = userID)
					customerObject = json.loads(customer)
					return jsonify(customerObject), 200
				except:
					return 'Failed to create customer', 402
			else:
				return 'Need to specify whether to create new customer or not', 402
		else:
			return 'No user ID provided ', 402