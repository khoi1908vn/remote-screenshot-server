from server import start_server
from console import _console_
from multiprocessing import Process
from threading import Thread
import time
from tlog import tlog

t2 = Thread(target=_console_)
def start_console():
    tlog('console init', 'Console starting...')
    t2.start()

if __name__ == '__main__':
    start_server()
    time.sleep(0.5)
    start_console()