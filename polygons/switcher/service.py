import subprocess

class ServiceHelper():

    def __init__(self, name, loglevel='info'):
        self.name = name
        self.loglevel = loglevel

    def start(self):
        command_body = 'celery worker -A {0} --loglevel={1}'.format(self.name, self.loglevel)
        import pdb;pdb.set_trace()
        proc = subprocess.Popen(
            command_body.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True)
