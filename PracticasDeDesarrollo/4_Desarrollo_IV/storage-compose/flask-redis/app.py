#!/usr/bin/env python3
import os
from flask import Flask, jsonify
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route("/")
def hello():
	try:
		visits = cache.incr("counter")
	except redis.RedisError:
		print('Cant connect to Redis')
		visits = "NaN"

	return jsonify(message=f"Hello! I'm inside a container. You have called me {visits} times. ")

if __name__ == '__main__':    
    app.run(host='0.0.0.0', debug=True)