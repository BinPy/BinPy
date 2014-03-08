from BinPy.Sequential.sequential import *


class Counter(object):

    """
    Base class for all counters
    """

    def __init__(self, bits, clock_connector):

        self.bits = bits
        self.out = []
        for i in range(self.bits):
            self.out.append(Connector(0))
        self.outold = self.out[:]
        self.ff = []
        self.enable = Connector(1)
        self.t = Connector(1)
        self.clk = clock_connector

    def setInput(self, t, enable):
        if isinstance(t, Connector):
            self.t = t
        else:
            self.t.state = int(t)
        if isinstance(enable, Connector):
            self.enable = enable
        else:
            self.enable.state = int(enable)

    def __call__(self):
        self.trigger()

    def Enable(self):
        # Enables counting on trigger
        self.enable.state = 1

    def Disable(self):
        # Disables counter
        self.enable.state = 0

    def reset(self):
        # Resets the counter to 0
        for i in range(self.bits):
            self.out[i].state = 0
        self.enable.state = 1

    def state(self):
        # MSB is at the Right Most position
        # To print with MSB at the Left Most position

        return [self.out[i].state for i in range(self.bits - 1, -1, -1)]


class BinaryCounter(Counter):

    """
    A 2 Bit Binary Counter
    Output connectors can be referenced by --> BinaryCounter_instance_name.out
    """

    def __init__(self, clk):

        Counter.__init__(self, 2, clk)
        # Calling the super class constructor

        self.ff = [TFlipFlop(self.t, self.enable, self.clk, self.out[0]),
                   TFlipFlop(self.t, self.enable, self.out[0], self.out[1])]
        #<self.bit> nos of TFlipFlop instances are appended in the ff array

        # output of previous stage becomes the input clock for next flip flop

    def trigger(self):
        # Sending a negative edge to ff
        while True:
            if self.clk.state == 0:
                # Falling edge will trigger the FF
                self.ff[0].trigger()
                break
        # Sending a positive edge to ff
        while True:
            if self.clk.state == 1:
                self.ff[0].trigger()
                break

        # This completes one full pulse.

        # To print with MSB at the Left Most position
        return [i.state for i in self.out[::-1]]


class NBitRippleCounter(Counter):

    """
    An N-Bit Ripple Counter
    """

    def __init__(self, bits, clock_connector):

        Counter.__init__(self, bits, clock_connector)
        # Calling the super class constructor

        self.ff = [TFlipFlop(self.t, self.enable, self.clk, self.out[0])]

        for i in range(1, bits):
            self.ff.append(
                TFlipFlop(self.t, self.enable, self.out[i - 1], self.out[i]))

    def trigger(self):
         # Sending a negative edge to ff
        while True:
            if self.clk.state == 0:
                # Falling edge will trigger the FF
                self.ff[0].trigger()
                break
        # Sending a positive edge to ff
        while True:
            if self.clk.state == 1:
                self.ff[0].trigger()
                break

        # This completes one full pulse.

        # To print with MSB at the Left Most position
        return [i.state for i in self.out[::-1]]
