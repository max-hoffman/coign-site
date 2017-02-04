from flask import Flask, render_template, request, jsonify, json
from flask_restful import Resource, abort, Api
from flask_restful.representations.json import output_json
import logging
from flask_bootstrap import Bootstrap
from firebase import firebase
from twilio.rest import TwilioRestClient
import stripe
from models.createCustomer import CreateCustomer
from models.retrieveCustomer import RetrieveCustomer
from models.charge import Charge
from models.changeDefaultSource import ChangeDefaultSource
from models.addSource import AddSource

application = Flask(__name__)
api = Api(application)

Bootstrap(application)
fb = firebase.FirebaseApplication('https://coign-dev.firebaseio.com/', None)

# web pages
@application.route("/")
def index():
	return render_template("index.html")

@application.route("/mission")
def mission():
	return render_template("mission.html")

@application.route("/contact")
def contact():
	return render_template("contact.html")

@application.route("/terms")
def terms():
	return render_template("terms.html")

@application.route("/ppolicy")
def ppolicy():
	return render_template("ppolicy.html")

#should this be a GET?
@application.route("/posts/<path>")
def post(path):
	postData = getPost(path)
	return render_template("post.html", data = postData)

# send text
@application.route('/text', methods=['POST'])
def text():

	#get the phone number
	phone_number = request.form.get('phoneNumber')
	if phone_number is not None:
	
		# Find these values at https://twilio.com/user/account
		account_sid = "AC64bff1796402535465c9bebe442d1f18"
		auth_token = "73e624975dec2ef220940fea6467ce9e"
	                                     
		#twilio_client=TwilioRestClient(app.config['TWILIO_ACCOUNT_SID'],app.config['TWILIO_AUTH_TOKEN'])
		twilio_client = TwilioRestClient(account_sid, auth_token)
		try:
			message = twilio_client.messages.create(to=phone_number, from_="+14142929862 ", body="test message")
		except:
			print()

	return render_template("index.html")


###### API #########

api.add_resource(CreateCustomer, '/api/create-customer')
api.add_resource(RetrieveCustomer, '/api/retrieve-customer')
api.add_resource(Charge, '/api/charge')
api.add_resource(AddSource, '/api/add-source')
api.add_resource(ChangeDefaultSource, '/api/change-default-source')

# Logging

class Service(Api):
    def handle_error(self, e):
        # Attach the exception to itself so Flask-Restful's error handler
        # tries to render it.
        if not hasattr(e, 'data'):
            e.data = e

        return super(Service, self).handle_error(e)

api = Service(application)

@api.representation('application/json')
def output_json_exception(data, code, *args, **kwargs):
    """Render exceptions as JSON documents with the exception's message."""
    if isinstance(data, Exception):
        data = {'status': code, 'message': str(data)}

    return output_json(data, code, *args, **kwargs)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
application.logger.addHandler(handler)

# show a post
def getPost(postID):
	result = fb.get('/posts', postID)
	print(result) 
	return result

if __name__ == "__main__":
	application.run(debug = True)