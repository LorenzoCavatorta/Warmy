from Warmy.polygons.switcher.port_out import PortOut as PortIn
import serial

class SwitcherOutToControlUnit(object):

    def __init__(self):
        self.port_in = PortIn()
        
    def read_port_in(self):
        return self.port_in.read()
        
    def read_port_out(self):
        pass

    def set_port_out(self,port_status):
        self.ser = serial.Serial('/dev/ttyACM1', 9600)
        self.ser.write(b'6')
        self.ser.write(b'6')

'''import serial
from test_switcher_out_to_control_unit import  SwitcherOutToControlUnit
ser = serial.Serial('/dev/ttyACM1', 9600)
'''
