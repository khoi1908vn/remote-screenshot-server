"""
here is the code used to control the database, you need to create config.json and db.json before using this
khoi1908vn#0100
"""
# gs gwh us uwh
import json
def getstatus():
    with open('./databases/db.json', 'r') as f:
        db = json.load(f)
        status = db['status']
    return status
def getwebhook():
    with open('./databases/db.json', 'r') as f:
        db = json.load(f)
        webhook = db['webhook']
    return webhook
def updatestatus(ns):
    with open('./databases/db.json','r') as f:
        db = json.load(f)
    db['status'] = ns
    with open('./databases/db.json','w') as f:
        json.dump(db, f)
def updatewebhook(nwh):
    with open('./databases/db.json','r') as f:
        db = json.load(f)
    db['webhook'] = nwh
    with open('./databases/db.json','w') as f:
        json.dump(db, f)
def updateclient(nc):
    with open('./databases/config.json', 'r') as f:
        config = json.load(f)
    config['clientKey'] = nc
    with open('./databases/config.json', 'r') as f:
        json.dump(config, f)
def updateuser(nc):
    with open('./databases/config.json', 'r') as f:
        config = json.load(f)
    config['userKey'] = nc
    with open('./databases/config.json', 'r') as f:
        json.dump(config, f)
