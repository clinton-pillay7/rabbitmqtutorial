from flask import Flask, render_template, request
import pika


app = Flask(__name__)


@app.route("/")
def home():
	return render_template("home.html")

@app.route("/textinput", methods = ["POST", "GET"])
def textinput():
	if request.method == "POST":
		text_data = request.form["text"]

		connection = pika.BlockingConnection(
		pika.ConnectionParameters(host='localhost'))
		channel = connection.channel()
		channel.queue_declare(queue='hello')
		channel.basic_publish(exchange='', routing_key='hello', body=text_data)
		connection.close()
		return render_template("result.html", text_data= text_data)

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = 5000)
