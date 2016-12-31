from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from firebase import firebase
from twilio.rest import TwilioRestClient


application = Flask(__name__)
Bootstrap(application)
firebase = firebase.FirebaseApplication('https://coign-dev.firebaseio.com/', None)

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

@application.route("/posts/<path>")
def post(path):
	postData = getPost(path)
	return render_template("post.html", data = postData)

# @application.route('/text', methods=['POST'])
# def text():
# 	#get the phone number
# 	phone_number=request.form.get('phoneNumber', None)

# 	# Find these values at https://twilio.com/user/account
# 	account_sid = "AC64bff1796402535465c9bebe442d1f18"
# 	auth_token = "73e624975dec2ef220940fea6467ce9e"
                                     
# 	try:
# 		# twilio_client=TwilioRestClient(app.config['TWILIO_ACCOUNT_SID'],app.config['TWILIO_AUTH_TOKEN'])
# 		twilio_client = TwilioRestClient(account_sid, auth_token)
# 		message = client.messages.create(to=phone_number, from_="+15555555555",
#                                      body="Download Coign at www....")

##firebase data retrieval
def getPost(postID):
	result = firebase.get('/posts', postID)
	print(result) 
	return result

if __name__ == "__main__":
	application.run(debug = True)