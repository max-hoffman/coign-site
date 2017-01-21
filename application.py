from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from firebase import firebase
from twilio.rest import TwilioRestClient
import stripe


application = Flask(__name__)
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

# stripe endpoints

#new user
@application.route('/createNewUser', methods = ['POST'])
def createNewUser():

	stripe.api_key = "sk_test_fqD4n0Wm1j1gPIYlH7R4NQhS"
	name = request.get('name')
	userID = request.get('userID')

	print(name + " : " + userID)
	customer = stripe.Customer.create(
	  description="Customer for" + name,
	)

	return customer

# show a post
def getPost(postID):
	result = fb.get('/posts', postID)
	print(result) 
	return result


if __name__ == "__main__":
	application.run(debug = True)