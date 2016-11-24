from unittest import TestCase
from core import Core
class TestCore(TestCase):

    def test_read_port_in(self):
        switcher = Core()
        switcher.port_in.status = 1
        self.assertTrue(switcher.port_in.read() == 1)
        
    def test_set_port_in(self):
        switcher = Core()
        switcher.port_in.set_on()
        self.assertTrue(switcher.port_in.read() == 1)
