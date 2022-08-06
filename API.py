#!/usr/bin/python3
# using flask_restful
from flask import Flask, jsonify
from flask_restful import Resource, Api

from predict import get_prediction

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

class API(Resource):
	def get(self, domain):
		prob, pred = get_prediction(domain)
		return jsonify({"domain": "isDGA", domain: 1 if float(prob) >= 0.5 else 0})
		# return jsonify(f"domain,isDGA\n{domain},{1 if float(prob)>= 0.5 else 0}")

# adding the defined resources along with their corresponding urls
api.add_resource(API, "/<domain>")

# driver function
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug = True)
