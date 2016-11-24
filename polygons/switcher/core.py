from port_in import port as port_in
from port_out import port as port_out
class Core(object):

    def __init__(self):
        self.port_in = port_in()
        self.port_out = port_out()
