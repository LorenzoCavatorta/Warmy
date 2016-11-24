from unittest import TestCase
from core import Core
class TestCore(TestCase):

    def setUp(self):
        self.switcher = Core()

    def test_read_port_in(self):
        self.switcher.port_in._status = 1
        self.assertTrue(self.switcher.port_in.read() == 1)

    def test_port_in_non_boolean(self):
        self.switcher.port_in.status = 7
        with self.assertRaises(ValueError):
            self.switcher.port_in.read()


    def test_set_port_in(self):
        self.switcher.port_in.set_on()
        self.assertTrue(self.switcher.port_in.read() == 1)


