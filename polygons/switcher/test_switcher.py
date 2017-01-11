import subprocess
from unittest import TestCase

class TestService(TestCase):

    def _start_worker():
        command_body = 'celery worker -A switcher --loglevel=info'
        proc = subprocess.Popen(command_body.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    def test_start_service():
        #given
        #when
        self._start_worker()
        #then
        
        
