import subprocess
from unittest import TestCase
from .switcher.service import ServiceHelper as SwitcherService

class TestService(TestCase):

    def _start_worker():
        switcher = SwitcherService('switcher')
        switcher.start()
        return switcher

    def test_start_service():
        #given
        #when
        self._start_worker()
        #then
        self._check_worker()
