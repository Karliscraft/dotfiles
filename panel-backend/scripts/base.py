import threading
import panelconfig
import shlex


class Config(object):
    def __init__(self, *, filename = None, filelike = None, body = None):
        self.parsetree = self.parse(filename = filename, filelike = filelike, body = body)

    def parse(self, *, filename, filelike, body):
        parsetree = []
        conftype = [x for x in ('filename', 'filelike', 'body') if locals()[x] is not None]
        if len(conftype) > 1:
            raise Exception("You may not pass more than one paramater")
        conftype = conftype[0]
        elif conftype == 'filename':
            with open(filename, 'r') as f:
                contents = f.readlines()
        elif conftype == 'filelike':
            contents = filelike.readlines()
        elif conftype == 'body':
            contents = body.split('\n')
        context = []
        for line in contents:
            argv = shlex.split(line)
            cmd = argv[0]
            params = argv[1::]
            if argv[-1].endswith(':'):
                context.append(argv)


class IPC(object):
    def __init__(self, filename):
        self.filename = filename
    def write(self, ipc, text):
        with open('
