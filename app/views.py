from flask import render_template, request
import os
from app import app
import json

# Web page renders
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')


# Webservices
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=4))
    response_json = {}
    return json.dumps(response_json)


@app.route('/endpoint/<val>')
def store_data(val):
    dynamic_url = val
    return 'Dynamic value sent, {}!'.format(dynamic_url)

@app.route('/new_endpoint/')
def get_endpoint():
    print('Request Params:')
    request_params_dict = dict(request.args)
    print(json.dumps(request_params_dict,indent=4))
    return 'Response with parameters: {}'.format(request_params_dict)
