class port(object):

    def __init__(self):
        self._status = None

    def check_status(self):
        if self._status not in (0, 1):
            raise ValueError('Non-boolean value detected for port')
        return self._status
        

    def read(self):
        return self.check_status()

    def set_on(self):
        self._status = 1

    def set_off(self):
        self._status = 0
