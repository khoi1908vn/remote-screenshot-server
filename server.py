"""
the server's code, which use flask to host 4 endpoints
you can upgrade the code to use multiple userKey and clientKey (im too lazy)
khoi1908vn#0100

SERVER SOURCE
---start index---
    */
    status/
            get/
            update/
    webhook/
            get/
            update/
---end index---
"""
from flask import Flask, request
import json, logging, requests
from database import getstatus as gs, getwebhook as gwh, updatestatus as us, updatewebhook as uwh

with open('./databases/config.json', 'r') as f:
    config = json.load(f)
    _client = config['clientKey']
    _user = config['userKey']
setlog = logging.getLogger('werkzeug').setLevel(logging.ERROR)
app = Flask('')
@app.route('/',methods=["GET"])
def home():
    return "Hello, this is a project-remote-screenshot server, please refer to /status/ and /webhook/ for more information\nMade by khoi1908vn#0100"
@app.route('/status/',methods=["GET"])
def status_info():
    return "This is the place where you update and get your agent status. If you want your agent to send screenshot to your /webhook/get/ please use /status/update/<your status, please use 0 or 1> and also include the userKey in the header.\nAlternately, you can make your own controller or use our controller"
@app.route('/webhook/',methods=["GET"])
def webhook_info():
    return "You update and get your Discord webhook here. \nTo update your webhook use /webhook/update/<new webhook with https://> and make sure to include your userKey in the request header.\nTo get your current webhook use /webhook/get/ and make sure to include your clientKey in the request header."
@app.route('/status/get/',methods=["GET"])
def status_get():
    if 'clientKey' not in request.headers:
        return "Missing clientKey", 401
    elif request.headers['clientKey'] != _client:
        return "Incorrect clientKey", 403
    else:
        return gs()

@app.route('/webhook/get/',methods=["GET"])
def webhook_get():
    if 'clientKey' not in request.headers:
        return "Missing clientKey", 401
    elif request.headers['clientKey'] != _client:
        return "Incorrect clientKey", 403
    else:
        return gwh()

@app.route('/status/update/<newstatus>',methods=["GET"])
def status_update(newstatus):
    if 'userKey' not in request.headers:
        return "Missing userKey", 401
    elif request.headers['userKey'] != _user:
        return "Incorrect userKey", 403
    else:
        us(newstatus)
        return 'success'

@app.route('/webhook/update/<newwebhook>',methods=["GET"])
def webhook_update(newwebhook):
    if 'userKey' not in request.headers:
        return "Missing userKey", 401
    elif request.headers['userKey'] != _user:
        return "Incorrect userKey", 403
    elif requests.get(newwebhook).status_code != 200:
        return "Invalid webhook", 400
    else:
        uwh(newwebhook)
        return 'success'
def _server_():
  app.run(host='0.0.0.0',port=8080)