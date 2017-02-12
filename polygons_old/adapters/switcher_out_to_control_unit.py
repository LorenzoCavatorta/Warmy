from Warmy.polygons.switcher.port_out import PortOut as PortIn
import serial
from time import sleep

class SwitcherOutToControlUnit(object):

    def __init__(self):
        self.port_in = PortIn()
        self.cu = ControlUnitConnector()
        
    def read_port_in(self):
        return self.port_in.read()
        
    def read_port_out(self):
        attempts = 10
        read = self.cu.read_from_serial()
        for i in range(attempts):
            new_read = self.cu.read_from_serial()
            if new_read != read:
                return new_read
        return new_read


    def set_port_out(self,port_status):
        self.cu.write_to_serial('6')

class ControlUnitConnector(object):

    def __init__(self):
        self.port_name = '/dev/ttyACM0'
        self.freq = 9600
        self.connection = serial.Serial(self.port_name, self.freq)
        self.write_to_serial('0')
        sleep(2)

    def write_to_serial(self,v):
        self.connection.write(v.encode())

    def read_from_serial(self):
        raw_read = self.connection.readline()
        return raw_read.decode()[0]
        
'''import serial
from test_switcher_out_to_control_unit import  SwitcherOutToControlUnit
ser = serial.Serial('/dev/ttyACM1', 9600)
'''
