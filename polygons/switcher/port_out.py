class port(object):

    def __init__(self):
        self._status = None

    def read(self):
        return self.check_valid_status()

    def set_on(self):
        self._status = 1

    def set_off(self):
        self._status = 0

    def check_valid_status(self):
        if self._status not in (0, 1):
            raise ValueError('nooooo')
        return self._status
