"""
main.py, the place i use to create threads and start/stop them
khoi1908vn#0100
"""
from server import _server_
from console import _console_
from threading import Thread
import time
from tlog import tlog
t1 = Thread(target=_server_)
t2 = Thread(target=_console_)
def start_server():
    tlog('server init', 'Server starting...')
    els = time.time()
    t1.start()
    el = str(round(time.time() - els, 3))
    tlog('server init', f'Server started in {el}s')

def start_console():
    tlog('console init', 'Console starting...')
    els = time.time()
    t2.start()
    el = str(round(time.time() - els, 3))
    tlog('console init', f'Console started in {el}s')


start_console()
start_server()