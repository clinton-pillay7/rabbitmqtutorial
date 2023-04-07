
## import my modules
from flask import Flask, render_template, request
import pika


# creating a new flask instance
app = Flask(__name__)


# creation of a route for the home page, which renders the html page, which contains the main message text entry. 
@app.route("/")
def home():
	return render_template("home.html")


## creation of the text entry confirmation page, as well as the rabbitmq producer code. 
@app.route("/textinput", methods = ["POST", "GET"])
def textinput():
	if request.method == "POST":
		text_data = request.form["text"]

		# rabbitmq code
		connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))	# creates a new connection
		channel = connection.channel()								# creates anew instance of a channel. 
		channel.queue_declare(queue='hello')							# creates a new queue - called hello
		channel.basic_publish(exchange='', routing_key='hello', body=text_data)			# publishes the message, note the "body", which contains the actual message
		connection.close()									# closes the connection
		return render_template("result.html", text_data= text_data)				# renders a html template to show confirmation of what was entered

# runs the flask app
if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = 5000)
