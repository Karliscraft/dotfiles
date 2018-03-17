#!/usr/bin/env python3

import subprocess
import panelconfig

from time import sleep

while True:
    with open(panelconfig.configdir + '/ipc/wifi', 'w') as f:
        f.write(subprocess.getoutput('nmcli -m tabular -t  device show ' + panelconfig.wifi).split('\n')[5])
    sleep(5)
