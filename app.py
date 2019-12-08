from flask import Flask
from flask import request
import time

app = Flask(__name__)

@app.route('/current_time')
def current_time():
	return str(int(time.time()))