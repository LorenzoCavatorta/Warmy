from unittest import TestCase
from core import Core
class TestCore(TestCase):

    def setUp(self):
        self.switcher = Core()

    def test_port_in_non_boolean(self):
        #todo: let down gracefully and default to 0
        with open(self.switcher.port_in._status_file,'w') as f:
            f.write('-20')
        with self.assertRaises(ValueError):
            self.switcher.port_in.read()

    def test_set_port_in_on(self):
        self.switcher.port_in.set_on()
        self.assertTrue(self.switcher.port_in.read() == 1)

    def test_set_port_in_off(self):
        self.switcher.port_in.set_off()
        self.assertTrue(self.switcher.port_in.read() == 0)

    def test_set_port_out_on(self):
        self.switcher.port_out.set_on()
        self.assertTrue(self.switcher.port_out.read() == 1)

    def test_set_port_out_off(self):
        self.switcher.port_out.set_off()
        self.assertTrue(self.switcher.port_out.read() == 0)

    def test_port_out_non_boolean(self):
        #todo: let down gracefully and default to 0
        with open(self.switcher.port_out._status_file,'w') as f:
            f.write('2.5')
        with self.assertRaises(ValueError):
            self.switcher.port_out.read()

    def test_on_from_port_in_to_port_out(self):
        #todo: move this test to a service version where you don't have to invoke the in_to_out method
        self.switcher.port_in.set_on()
        self.switcher.process_in_on()
        on_signal_is_out_and_in_port_is_reset = self.switcher.port_out.read() == 1 and self.switcher.port_in.read() == 0
        self.assertTrue(on_signal_is_out_and_in_port_is_reset)

