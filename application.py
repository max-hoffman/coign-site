from flask import Flask, render_template
from flask_bootstrap import Bootstrap


application = Flask(__name__)
Bootstrap(application)

@application.route("/")
def index():
	return render_template("index.html")


if __name__ == "__main__":
	application.run(debug = True)