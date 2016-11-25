from port import PortBoolean as Port

class PortIn(Port):

    def __init__(self):
        self.file_location = '/tmp/port_in.status'
        super().__init__(self.file_location)

    
