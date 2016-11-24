from port_in import port_in 
from port_out import port_out 
class Core(object):

    def __init__(self):
        self.port_in = port_in()
        self.port_out = port_out()
