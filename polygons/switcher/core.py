from port_in import PortIn
from port_out import PortOut
class Core(object):

    
    def __init__(self):

        def patching_port_in_set_on():
            self.port_in._status = 1
            self.process_in_on()

        self.port_in = PortIn()
        self.port_in.set_on = patching_port_in_set_on
        self.port_out = PortOut()

    def process_in_on(self):
        self.port_out.set_on()
        self.port_in.set_off()
        

        
        
