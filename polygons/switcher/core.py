from port_in import PortIn
from port_out import PortOut
class Core(object):

    
    def __init__(self):
        self.port_in = PortIn()
        self.port_out = PortOut()

    def process_in_on(self):
        if self.port_in.read() == 1:
            self.port_out.set_on()
            self.port_in.set_off()
        
        

        
        
