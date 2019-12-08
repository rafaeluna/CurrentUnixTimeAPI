from flask import Flask
from flask import request
import time

app = Flask(__name__)

@app.route('/')
def home():
	return '''
	<!DOCTYPE html>
	<html>
	<head>
		<title>Current UNIX Time API</title>
	</head>
	<body>
		<h1>Current UNIX time API</h1>
		<p>A simple API that returns the number of seconds that have passed since January 1st, 1970, also known as a UNIX Time</p>
		<h2>Usage</h2>
		<p>Simply make a GET request to <a href="https://current-unix-time-api.herokuapp.com/current_time">current-unix-time-api.herokuapp.com/current_time</a></p>
		<h2>Future</h2>
		<p>More features to come!</p>
		<p><a href="mailto:rafaelunag@hotmail.com">You can send me feature ideas via email</a></p>
	</body>
	</html>
	'''

@app.route('/current_time')
def current_time():
	return str(int(time.time()))