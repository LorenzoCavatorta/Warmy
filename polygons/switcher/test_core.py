from unittest import TestCase
from core import Core
class TestCore(TestCase):

    def test_read_port_in(self):
        switcher = Core()
        switcher.port_in.read()

