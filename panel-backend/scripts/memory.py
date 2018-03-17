#!/usr/bin/env python3
from time import sleep

import psutil
import panelconfig

while True:
    with open(panelconfig.configdir + '/ipc/memory', 'w') as f:
        f.write(str(round(psutil.virtual_memory().used / 1000000)) + 'M')
    sleep(5)
