from flask import Flask, request
import json, logging, requests
from database import getstatus as gs, getwebhook as gwh, updatestatus as us, updatewebhook as uwh
from tlog import tlog
import time
from multiprocessing import Process

with open('./databases/config.json', 'r') as f:
    config = json.load(f)
    _client = config['clientKey']
    _user = config['userKey']
logging.getLogger('werkzeug').setLevel(logging.ERROR)

app = Flask('')
"""
indexing:
/
    update/
        webhook/
        status/
    get/
to use any update feature please include the userKey configured in /databases/config.json
to use any get feature please include the userKey/clientKey configured in /databases/config.json
"""

@app.route('/')
def home():
    return 'Hello this is a beta remote-screenshot server for individual usage. ( 1 client - 1 user )'
@app.get('/get/')
def get():
    if request.headers.get('clientKey') == _client or request.headers.get('userKey') == _user:
        status_code = 200
        error_desp = 'None'
        return_webhook = gwh()
        return_status = gs()
    elif any(i in ['userKey', 'clientKey'] for i in request.headers):
        status_code = 403
        error_desp = 'Invalid userKey/clientKey'
        return_webhook = 'none'
        return_status = 'none'
    else:
        status_code = 401
        error_desp = 'Missing a authorization key'
        return_webhook = 'none'
        return_status = 'none'
    
    return_dict = {
        "status_code": status_code,
        "error": error_desp,
        "webhook": return_webhook,
        "status": return_status
    }
    return return_dict, status_code

def user_check(_userKey):
    global _client
    if _userKey == None:
        sc = 401
        err = 'Missing userKey'
        acp = False
    elif _userKey == _user:
        sc = 200
        err = 'none'
        acp = True
    else:
        sc = 403
        err = 'Invalid userKey'
        acp = False

@app.post('/update/webhook/')
def webhook_update():
    status_code, error, bol = user_check(request.headers.get('userKey'))
    newwebhook = str(request.form.get('webhook'))
    if bol:
        if newwebhook == None or 'https://discord.com/api/webhooks/' not in newwebhook or requests.get(newwebhook).status_code != 200:
            status_code = 403
            error = 'Invalid webhook'
            bol = False
    else:
        uwh(newwebhook)
    return_dict = {
        "status_code": status_code,
        "error": error,
        "success_state": bol
    }
    return return_dict, status_code

@app.post('/update/status/')
def status_update():
    status_code, error, bol = user_check(request.headers.get('userKey'))
    newstatus = str(request.form.get('status'))
    if bol:
        if newstatus not in ['0', '1']:
            status_code = 403
            error = 'Invalid status, must be 0 or 1'
            bol = False
        else:
            us(newstatus)
    return_dict = {
        "status_code": status_code,
        "error": error,
        "success_state": bol
    }
    return return_dict, status_code

def _server_():
    app.run(host='0.0.0.0',port=8080)
t1 = Process(target=_server_, daemon=True)
def start_server():
    if not t1.is_alive():
        tlog('server init', 'Server starting...')
        els = time.time()
        t1.start()
        el = str(round(time.time() - els, 3))
        tlog('server init', f'Server started in {el}s')
    else:
        tlog('server init', f'Server already started!')
def stop_server():
    if t1.is_alive():
        tlog('server init', 'Server stopping...')
        els = time.time()
        t1.terminate()
        el = str(round(time.time() - els, 3))
        tlog('server init', f'Server stopped in {el}s')
    else:
        tlog('server init', f'Server already stopped!')
