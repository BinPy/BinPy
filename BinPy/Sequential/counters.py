from BinPy.Sequential.sequential import *


class Counter(object):

    """
    Base class for all counters
    """

    def __init__(self, bits, clock_connector, set, reset, data):

        self.bits = bits
        self.out = []
        for i in range(self.bits):
            self.out.append(Connector(data))
        self.outinv = []
        for i in range(self.bits):
            self.outinv.append(Connector(NOT(data).output()))

        self.outold = self.out[:]
        self.outoldinv = self.outinv[:]
        self.ff = [None] * self.bits
        self.enable = Connector(1)
        self.t = Connector(1)
        self.clk = clock_connector
        self.set = set
        self.reset = reset
        self.set_once = False
        self.reset_once = False
        self.bits_fixed = False
        self.ripple_type = True

    def setInput(self, t, enable):
        if isinstance(t, Connector):
            self.t = t
        else:
            self.t.state = int(t)
        if isinstance(enable, Connector):
            self.enable = enable
        else:
            self.enable.state = int(enable)

    def trigger(self, ffnumber=None):

        self.outold = self.out[:]
        if ffnumber is None:
            ffnumber = self.bits - 1

        # Sending a negative edge to ff
        while True:
            if self.clk.state == 0:
                # Falling edge will trigger the FF
                if self.ripple_type:
                    self.ff[ffnumber].trigger()
                else:
                    for i in range(self.bits):
                        self.ff[i].trigger()
                break
        # Sending a positive edge to ff
        while True:
            if self.clk.state == 1:
                if self.ripple_type:
                    self.ff[ffnumber].trigger()
                else:
                    for i in range(self.bits):
                        self.ff[i].trigger()
                break
        # This completes one full pulse.

        if self.set.state == 1:
            self.setCounter()
        elif self.reset.state == 1:
            self.resetCounter()

        return self.state()

    def __call__(self):
        self.trigger()

    def setCounter(self):
        set = self.set.state
        if self.bits_fixed:
            self.__init__(self.clk, self.set, self.reset, 1)
        else:
            self.__init__(self.bits, self.clk, self.set, self.reset, 1)
        if not self.set_once:
            self.set.state = set

    def resetCounter(self):
        reset = self.reset.state
        if self.bits_fixed:
            self.__init__(self.clk, self.set, self.reset, 0)
        else:
            self.__init__(self.bits, self.clk, self.set, self.reset, 0)
        if not self.reset_once:
            self.reset.state = reset

    def Enable(self):
        # Enables counting on trigger
        self.enable.state = 1

    def Disable(self):
        # Disables counter
        self.enable.state = 0

    def state(self):
        # MSB is at the Right Most position
        # To print with MSB at the Left Most position

        return [self.out[i].state for i in range(self.bits)]


class BinaryCounter(Counter):

    """
    A 2 Bit Binary Counter
    Output connectors can be referenced by --> BinaryCounter_instance_name.out
    """

    def __init__(self, clk, set=Connector(0), reset=Connector(0), data=0):

        Counter.__init__(self, 2, clk, set, reset, data)
        # Calling the super class constructor

        self.ff[1] = TFlipFlop(
            self.t,
            self.enable,
            self.clk,
            self.out[1],
            self.outinv[1],
            self.set,
            self.reset)
        self.ff[0] = TFlipFlop(
            self.t,
            self.enable,
            self.out[1],
            self.out[0],
            self.outinv[0],
            self.set,
            self.reset)

        #<self.bit> nos of TFlipFlop instances are appended in the ff array
        # output of previous stage becomes the input clock for next flip flop
        self.bits_fixed = True


class NBitRippleCounter(Counter):

    """
    An N-Bit Ripple Counter
    """

    def __init__(
            self,
            bits,
            clock_connector,
            set=Connector(0),
            reset=Connector(0),
            data=0):

        # All the output bits are initialized to this data bit

        Counter.__init__(self, bits, clock_connector, set, reset, data)
        # Calling the super class constructor

        self.ff[
            self.bits -
            1] = TFlipFlop(
            self.t,
            self.enable,
            self.clk,
            self.out[
                self.bits -
                1],
            self.outinv[
                self.bits -
                1],
            self.set,
            self.reset)

        for i in range(self.bits - 1):
            self.ff[i] = TFlipFlop(
                self.t,
                self.enable,
                self.out[
                    i + 1],
                self.out[i],
                self.outinv[i],
                self.set,
                self.reset)


class NBitDownCounter(Counter):

    """
    An N-Bit Down Counter
    """

    def __init__(
            self,
            bits,
            clock_connector,
            set=Connector(0),
            reset=Connector(0),
            data=0):

        # All the output bits are initialized to this data bit
        Counter.__init__(self, bits, clock_connector, set, reset, data)
        # Calling the super class constructor

        self.ff[
            self.bits -
            1] = TFlipFlop(
            self.t,
            self.enable,
            self.clk,
            self.out[
                self.bits -
                1],
            self.outinv[
                self.bits -
                1],
            self.set,
            self.reset)

        for i in range(self.bits - 1):
            self.ff[i] = TFlipFlop(
                self.t,
                self.enable,
                self.outinv[
                    i + 1],
                self.out[i],
                self.outinv[i],
                self.set,
                self.reset)


class DecadeCounter(Counter):

    """
    A 4-Bit Decade Counter
    """

    def __init__(
            self,
            clock_connector,
            set=Connector(0),
            reset=Connector(0),
            data=0):

        # All the output bits are initialized to this data bit

        Counter.__init__(self, 4, clock_connector, set, reset, data)
        # Calling the super class constructor

        self.ff = [None] * 4

        self.ff[3] = TFlipFlop(
            self.t,
            self.enable,
            self.clk,
            self.out[3],
            self.outinv[3],
            self.set,
            self.reset)
        self.ff[2] = TFlipFlop(
            self.t,
            self.enable,
            self.out[3],
            self.out[2],
            self.outinv[2],
            self.set,
            self.reset)
        self.ff[1] = TFlipFlop(
            self.t,
            self.enable,
            self.out[2],
            self.out[1],
            self.outinv[1],
            self.set,
            self.reset)
        self.ff[0] = TFlipFlop(
            self.t,
            self.enable,
            self.out[1],
            self.out[0],
            self.outinv[0],
            self.set,
            self.reset)

        self.g1 = AND(self.out[0], self.out[2])
        self.g1.setOutput(self.reset)

        self.bits_fixed = True
        self.reset_once = True


class RingCounter(object):

    """
    An N-bit Ring Counter
    """

    def __init__(
            self,
            bits,
            clock_connector,
            reset=Connector(0)):

        self.bits = bits
        self.clk = clock_connector
        self.enable = Connector(1)
        self.reset = reset
        # Initializing list of connectors  for flip flops
        self.connectors = [Connector(0) if i > 0 else Connector(1)
                           for i in range(self.bits)]
        # Initializing list of flip flops
        self.ffs = [DFlipFlop(self.connectors[i],
                    self.enable,
                    self.clk,
                    Connector(0),
                    Connector(1))
                    for i in range(self.bits)]
        # Initializing state of the counter
        self.initialState = [0 if i > 0 else 1 for i in range(self.bits)]
        self.counterState = self.initialState

    def _updateState(self):
        """ Updates current state of the counter """
        for i in range(self.bits):
            self.counterState[i] = self.ffs[i].state()[0]

    def resetCounter(self):
        self.counterState = self.initialState

    def trigger(self):

        # Update the connectors states by the current state before triggering
        for i in range(self.bits):
            self.connectors[i].state = self.counterState[i-1]
            # Connects each flip flop with output of preceding one

        # Sending a negative edge to ff
        while True:
            if self.clk.state == 0:
                for i in range(self.bits):
                    self.ffs[i-1].trigger()
                break
        # Sending a positive edge to ff
        while True:
            if self.clk.state == 1:
                for i in range(self.bits):
                    self.ffs[i].trigger()
                break
        # This completes one full pulse.

        # Update state after triggering
        self._updateState()

        if self.reset.state == 1:
            self.resetCounter()

    def state(self):
        """ Returns state of the counter """
        return self.counterState

    def __call__(self):
        self.trigger()


class JohnsonCounter(object):

    """
    An N-bit Johnson Counter
    """

    def __init__(
            self,
            bits,
            clock_connector,
            reset=Connector(0)):

        self.bits = bits
        self.clk = clock_connector
        self.enable = Connector(1)
        self.reset = reset
        # Initializing list of connectors  for flip flops
        self.connectors = [Connector(0) for i in range(self.bits)]
        # Initializing list of flip flops
        self.ffs = [DFlipFlop(self.connectors[i],
                    self.enable,
                    self.clk,
                    Connector(0),
                    Connector(1))
                    for i in range(self.bits)]
        # Initializing state of the counter
        self.initialState = [0 for i in range(self.bits)]
        self.counterState = self.initialState

    def _updateState(self):
        """ Updates current state of the counter """
        for i in range(self.bits):
            self.counterState[i] = self.ffs[i].state()[0]

    def resetCounter(self):
        self.counterState = self.initialState

    def trigger(self):

        # Update the connectors states by the current state before triggering
        for i in range(self.bits):
            if i == 0:
                self.connectors[i].state = NOT(self.counterState[i-1]).output()
            else:
                self.connectors[i].state = self.counterState[i-1]
            # Connects each flip flop with output of preceding one
            # except the first one is connected to complement of last one

        # Sending a negative edge to ff
        while True:
            if self.clk.state == 0:
                for i in range(self.bits):
                    self.ffs[i-1].trigger()
                break
        # Sending a positive edge to ff
        while True:
            if self.clk.state == 1:
                for i in range(self.bits):
                    self.ffs[i].trigger()
                break
        # This completes one full pulse.

        # Update state after triggering
        self._updateState()

        if self.reset.state == 1:
            self.resetCounter()

    def state(self):
        """ Returns state of the counter """
        return self.counterState

    def __call__(self):
        self.trigger()
