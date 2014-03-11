from BinPy.Gates.connector import *

class buffer(object):
    def __init__(self, a, b, c):
        is_connector(a, b, c)
        self.a, self.b, self.c = a, b, c

    def trigger(self):
        if self.b == 0:
            self.c.set(2)
        elif self.b.state == 1:
            self.c.set(self.a.state)
        else:
            self.c.set(3)


class bus(object):
    pass



