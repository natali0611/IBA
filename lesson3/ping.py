#!/usr/bin/env python3

'''делать ping google.com. Если сервер отвечает, то выводить - success, если нет - doesn't work. '''

import subprocess

def ping(host):
    result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE)
    return 'success' if result.returncode == 0 else "doesn't work"

print(ping('google.com'))
