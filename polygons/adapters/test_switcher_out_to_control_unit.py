from unittest import TestCase
from switcher_out_to_control_unit import SwitcherOutToControlUnit
from Warmy.polygons.switcher.port_out import PortOut as PortFromSwitcher

class can_communicate_with_control_unit(TestCase):

    def setUp(self):
        self.adapter = SwitcherOutToControlUnit()
        self.switcher_out = PortFromSwitcher()

    def test_can_read_port_in(self):
        self.switcher_out.set_on() #implementation_specific
        self.assertTrue(self.adapter.read_port_in() == 1)

    def test_can_write_port_out(self):
        self.adapter.set_port_out(1)
        self.assertTrue(self.adapter.read_port_out() == 1)
