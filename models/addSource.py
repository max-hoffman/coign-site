from flask import request, json
from flask_restful import Resource, abort, Api
import stripe

stripe.api_key = "sk_test_fqD4n0Wm1j1gPIYlH7R4NQhS"

class AddSource(Resource):

	def post(self):
		args = json.loads(request.data)

		try:
		    stripeID = args['stripeID']
			source = args['source']
		    customer = stripe.Customer.retrieve(stripeID)
		    customer.sources.create(source=source)
		    return 'Success', 200
		  except stripe.error.StripeError as e:
		    return 'Error adding source'. 402