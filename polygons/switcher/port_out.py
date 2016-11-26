from .port import PortBoolean as Port

class PortOut(Port):

    def __init__(self):
        self.file_location = '/tmp/port_out.status'
        super().__init__(self.file_location)

    
