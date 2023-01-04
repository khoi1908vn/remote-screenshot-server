from server import start_server
from console import _console_
from threading import Thread
import time
from tlog import tlog

t2 = Thread(target=_console_)
def start_console():
    tlog('console init', 'Console starting...')
    t2.start()

if __name__ == '__main__':
    start_server()
    time.sleep(1)
    start_console()