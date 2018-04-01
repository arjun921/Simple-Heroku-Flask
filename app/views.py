from flask import render_template
import os
from app import app


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
    res = makeWebhookResult(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


@app.route('/storeBalance/<bal>')
def storeData(bal):
    fopen = open('balance','w')
    fopen.write(bal)
    fopen.close()
    return 'Balance Updated, {}!'.format(bal)
