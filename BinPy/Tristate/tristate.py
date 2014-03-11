from BinPy.Gates import *

class Buffer(Gate):
    def __init__(self, c, b, a):
        Gate.__init__(self, c, b, a)

    def calc_output(self, in_states):
        if self.inputs[0] == 0:
            return 2
        elif self.inputs[0] == 1:
            return self.inputs[1]
        else:
            return 0

# Useful to implement output enable in ICs
class Bus(object):
    pass



