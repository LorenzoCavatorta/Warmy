from port_in import PortIn
from port_out import PortOut
class Core(object):

    
    def __init__(self):
        def patching_port_in_set_on():
            self.port_in._status = 1
            self.send_on_to_out()

        self.port_in = PortIn()
#        import pdb; pdb.set_trace()
        self.port_in.set_on = patching_port_in_set_on
        self.port_out = PortOut()



        
        
