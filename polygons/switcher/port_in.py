class port(object):

    def __init__(self):
        self.status = None

    def read(self):
        return self.status

    def set_on(self):
        self.status = 1
