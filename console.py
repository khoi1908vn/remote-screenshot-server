"""
here's the code of the internal console, which allow you to get/update the database and start/stop the server
without using the api endpoints
khoi1908vn#0100
"""
from tlog import tlog
from database import *
import requests
helpcommand = """Commands:
help    :   Show this help
get     :   Get the required data from the database
update  :   Update the required data in the database
server  :   Start/stop the server
exit    :   Stop everything
"""
"""
get/update:
- status
- webhook
"""
def _console_():
    while True:
        inp1 = input('> ')
        inp = inp1.split()
        if len(inp) != 0:
            if inp[0] == 'help':
                tlog('console help', helpcommand)
            elif inp[0] == 'get':
                if len(inp) == 1:
                    tlog('console help', 'get     :   Get the required data from the database')
                elif len(inp) == 2:
                    if inp[1] == 'status':
                        tlog('console info', 'current status: ' + getstatus())
                    elif inp[1] == 'webhook':
                        tlog('console info', 'current webhook: ' + getwebhook())
                    else:
                        tlog('console error', 'Invalid syntax')
                elif len(inp) > 2:
                    tlog('console error', 'Invalid syntax')
            elif inp[0] == 'update':
                if len(inp) == 1:
                    tlog('console help', 'update  :   Update the required data in the database')
                elif len(inp) == 3:
                    if inp[1] == 'status':
                        if inp[2] not in ['0', '1']:
                            tlog('console error', 'Invalid syntax')
                        else:
                            updatestatus(inp[2])
                            tlog('console info', f'successfully updated the status to {inp[2]}')
                    elif inp[1] == 'webhook':
                        if 'https://discord.com/api/webhooks/' not in inp[2]:
                            tlog('console error', 'Invalid syntax')
                        elif requests.get(inp[2]).status_code != 200:
                            tlog('console error', 'Invalid webhook')
                        else:
                            updatewebhook(inp[2])
                            tlog('console info', f'successfully updated the webhook to {inp[2]}')
                else:
                    tlog('console error', 'Invalid syntax')
            elif inp[0] == 'exit':
                raise KeyboardInterrupt('User intentionally exited')
            else:
                tlog('console error', 'Unkwown command')
                
if __name__ == '__main__':
    try:
        _console_()
    except KeyboardInterrupt:
        tlog('console init', 'Exiting...')
