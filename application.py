from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from firebase import firebase


application = Flask(__name__)
Bootstrap(application)


@application.route("/")
def index():
	return render_template("index.html")

@application.route("/mission")
def mission():
	return render_template("mission.html")

@application.route("/contact")
def contact():
	return render_template("contact.html")

@application.route("/posts/<path>")
def post(path):
	postData = getPost(path)
	return render_template("post.html", data = postData)

#fb = firebase.firebaseApplication("https://coign-dev.firebaseio.com/", None)
##firebase data retrieval
def getPost(postID):
	#result = firebase.get('/users', postID)
	result = postID
	print(result) 
	return result

if __name__ == "__main__":
	application.run(debug = True)