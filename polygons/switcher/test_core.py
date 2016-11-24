from unittest import TestCase
from core import Core
class TestCore(TestCase):

    def setUp(self):
        self.switcher = Core()

    def test_read_port_in(self):
        self.switcher.port_in._status = 1
        self.assertTrue(self.switcher.port_in.read() == 1)

    def test_port_in_non_boolean(self):
        #todo: let down gracefully and default to 0
        self.switcher.port_in._status = 7
        with self.assertRaises(ValueError):
            self.switcher.port_in.read()

#    def test_set_port_in_on(self):
#        self.switcher.port_in.set_on()
#        self.assertTrue(self.switcher.port_in.read() == 1)

    def test_set_port_in_off(self):
        self.switcher.port_in.set_off()
        self.assertTrue(self.switcher.port_in.read() == 0)

    def test_read_port_out(self):
        self.switcher.port_out._status = 1
        self.assertTrue(self.switcher.port_out.read() == 1)
        
    def test_set_port_out_on(self):
        self.switcher.port_out.set_on()
        self.assertTrue(self.switcher.port_out.read() == 1)

    def test_set_port_out_off(self):
        self.switcher.port_out.set_off()
        self.assertTrue(self.switcher.port_out.read() == 0)

    def test_port_out_non_boolean(self):
        #todo: let down gracefully and default to 0
        self.switcher.port_out._status = 2.5
        with self.assertRaises(ValueError):
            self.switcher.port_out.read()

    def test_on_from_port_in_to_port_out(self):
        self.switcher.port_in.set_on()
        on_signal_is_out_and_in_port_is_reset = self.switcher.port_out.read() == 1 and self.switcher.port_in.read() == 0
        self.assertTrue(on_signal_is_out_and_in_port_is_reset)

