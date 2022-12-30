"""
a very funny logging module created by me cuz im too lazy to learn how to use the built in logging module :clown:
format: tlog(flags, phr)
.i.e: tlog('console init', 'Hello world') -> [dd-mm-YYYY hh:mm:ss] [console] [init] Hello world
khoi1908vn#0100
"""
import datetime, pytz
def tlog(tags, phr):
    logtime = datetime.datetime.now(pytz.timezone("Asia/Bangkok")).strftime("%d-%m-%Y %H:%M:%S")
    if tags == '':
        print(f'[{logtime}] ' + phr)
    else:
        tags = tags.split()
        outtags = ''
        for i in tags:
            outtags = outtags + f'[{i}] '
        print(f'[{logtime}] ' + outtags + phr)