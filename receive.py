# import my modules
import pika, sys, os


def main():                   																
	credentials = pika.PlainCredentials('root', 'rootpassword')								# create variable for authentication
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672,'/',credentials))			# create connection
	channel = connection.channel()												# create new channel
	channel.queue_declare(queue='hello')											# create new queue


	def callback(ch, method, properties, body):										# create function for displaying the message received
		print(" [x] Received %r" % body)

#	channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)  					# setting parameters to receive the message 
	channel.basic_consume(queue='hello', consumer_callback=callback)  					# setting parameters to receive the message 

	print(' [*] Waiting for messages. To exit press CTRL+C')								# receiving the actual message
	channel.start_consuming()

if __name__ == '__main__':													# flask code to run the app, and also to terminate the app. 
	try:
		main()
	except KeyboardInterrupt:
		print('Interrupted')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
