class PortBoolean(object):

    def __init__(self, status_file = None):
        self._status = 0
        self._status_file = status_file
        self.set_off()

    def check_status(self):
        if self._status not in (0, 1):
            raise ValueError('Non-boolean value detected for port')
        return self._status    
    
    def read(self):
        with open(self._status_file, "r") as f:
            self._status = int(f.read())
        return self.check_status()

    def set_on(self):
        with open(self._status_file, "w") as f:
            self._status = f.write("1")

    def set_off(self):
        with open(self._status_file, "w") as f:
            self._status = f.write("0")
