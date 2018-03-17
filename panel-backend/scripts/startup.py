import os
import threading
import sys

def run(fname):
    with open('fname', 'r') as f:
        exec(f.read())
threads = []

with open('startup.conf', 'r') as f:
    for i in f.readlines():
        threads.append(threading.Thread(target=run, args=(i)))

print(threads)
while sys.stdin.read(9) != 'aqwsderfg':
    pass
