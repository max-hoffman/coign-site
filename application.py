from flask import Flask, render_template
from flask_bootstrap import Bootstrap


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

if __name__ == "__main__":
	application.run(debug = True)