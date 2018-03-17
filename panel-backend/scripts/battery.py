"""Decides on which battery icon to show."""
import panelconfig
import subprocess

from time import sleep

def pba_run():
    while True:
        batterylvl = int(subprocess.getoutput('acpi --battery').split(',')[1].replace('%', '').strip())

        open(panelconfig.configdir, 'w').write('' if batterylvl < 25 else '' if batterylvl < 50 else '' if batterylvl < 75 else '' if batterylvl < 100 else '')
        open(panelconfig.configdir, 'w').write('{}%'.format(str(batterylvl)))
        sleep(5)

if __name__=='__main__':
    pba_run()
