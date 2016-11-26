from unittest import TestCase
from switcher_out_to_control_unit import SwitcherOutToControlUnit

class can_communicate_with_control_unit(TestCase):

    def test_can_read_port_in(self):
        adapter = SwitcherOutToControlUnit()
        adapter.port_in.set_on()
        self.assertTrue(adapter.port_in.read() == 1)

    
