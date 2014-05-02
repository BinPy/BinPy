from BinPy.Sequential import *
from BinPy.Sequential.registers import *


class Counter(object):

    """
    Base class for all counters
    """

    def __init__(self, bits, clock_connector, data, preset, clear):

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
        self.set_once = False
        self.reset_once = False
        self.bits_fixed = False
        self.ripple_type = True
        self.preset = preset
        self.clear = clear

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

        if self.clear.state == 1 and self.preset.state == 0:
            self.setCounter()
        elif self.preset.state == 1 and self.clear.state == 0:
            self.resetCounter()

        return self.state()

    def __call__(self):
        self.trigger()

    def setCounter(self):
        inset = self.clear.state
        if self.bits_fixed:
            self.__init__(self.clk, 1, self.preset, self.clear)
        else:
            self.__init__(self.bits, self.clk, 1, self.preset, self.clear)
        if not self.set_once:
            self.clear.state = inset

    def resetCounter(self):
        reset = self.preset.state
        if self.bits_fixed:
            self.__init__(self.clk, 0, self.preset, self.clear)
        else:
            self.__init__(self.bits, self.clk, 0, self.preset, self.clear)
        if not self.reset_once:
            self.preset.state = reset

    def enable(self):
        # Enables counting on trigger
        self.enable.state = 1

    def disable(self):
        # Disables counter
        self.enable.state = 0

    def state(self):
        # MSB is at the Right Most position
        # To print with MSB at the Left Most position

        return [self.out[i].state for i in range(self.bits)]


class BinaryCounter(Counter):

    """
    An N-Bit Binary Counter
    Output connectors can be referenced by --> BinaryCounter_instance_name.out

    Examples
    ========

    >>> From BinPy import *
    >>> clock = Clock(0, 100)  #A clock with leading edge = 0 and frequency = 100Hz
    >>> clock.start()
    >>> clk_conn = clock.A
    >>> b = BinaryCounter(2, clk_conn)
    >>> for i in range(0, 5):
    >>>     b.trigger()
    >>>     print(b.state)
    [0, 1]
    [1, 0]
    [1, 1]
    [0, 0]
    [0, 1]
    """

    def __init__(self, bits, clk, data=0,
                 preset=Connector(1), clear=Connector(1)):
        Counter.__init__(self, bits, clk, data, preset, clear)

        # Calling the super class constructor
        self.ff[self.bits - 1] = TFlipFlop(
            self.t,
            self.enable,
            self.clk,
            self.preset,
            self.clear,
            self.out[self.bits - 1],
            self.outinv[self.bits - 1])
        for i in range(self.bits - 2, -1, -1):
            self.ff[i] = TFlipFlop(
                self.t,
                self.enable,
                self.out[i + 1],
                self.preset,
                self.clear,
                self.out[i],
                self.outinv[i])

        # <self.bit> nos of TFlipFlop instances are appended in the ff array
        # output of previous stage becomes the input clock for next flip flop


class NBitRippleCounter(Counter):

    """
    An N-Bit Ripple Counter

    Examples
    ========

    >>> From BinPy import *
    >>> clock = Clock(0, 100)  #A clock with leading edge = 0 and frequency = 100Hz
    >>> clock.start()
    >>> clk_conn = clock.A
    >>> counter = NBitRippleCounter(4, clk_conn)
    >>> for i in range(0, 8):
    >>>     counter.trigger()
    >>>     print(counter.state)
    [0, 0, 0, 1]
    [0, 0, 1, 0]
    [0, 0, 1, 1]
    [0, 1, 0, 0]
    [0, 1, 0, 1]
    [0, 1, 1, 0]
    [0, 1, 1, 1]
    [1, 0, 0, 0]
    [1, 0, 0, 1]
    [1, 0, 1, 0]
    [1, 0, 1, 1]
    [1, 1, 0, 0]
    [1, 1, 0, 1]
    [1, 1, 1, 0]
    [1, 1, 1, 1]
    [0, 0, 0, 0]
    """

    def __init__(
            self,
            bits,
            clock_connector,
            data=0,
            preset=Connector(1),
            clear=Connector(1)):

        # All the output bits are initialized to this data bit

        Counter.__init__(self, bits, clock_connector, data,
                         preset, clear)
        # Calling the super class constructor

        self.ff[
            self.bits -
            1] = TFlipFlop(
            self.t,
            self.enable,
            self.clk,
            self.preset,
            self.clear,
            self.out[
                self.bits -
                1],
            self.outinv[
                self.bits -
                1])

        for i in range(self.bits - 1):
            self.ff[i] = TFlipFlop(
                self.t,
                self.enable,
                self.out[
                    i + 1],
                self.preset,
                self.clear,
                self.out[i],
                self.outinv[i])


class NBitDownCounter(Counter):

    """
    An N-Bit Down Counter

    Examples
    ========

    >>> From BinPy import *
    >>> clock = Clock(0, 100)  #A clock with leading edge = 0 and frequency = 100Hz
    >>> clock.start()
    >>> clk_conn = clock.A
    >>> counter = NBitDownCounter(4, clk_conn)
    >>> for i in range(0, 8):
    >>>     counter.trigger()
    >>>     print(counter.state)
    [1, 1, 1, 1]
    [1, 1, 1, 0]
    [1, 1, 0, 1]
    [1, 1, 0, 0]
    [1, 0, 1, 1]
    [1, 0, 1, 0]
    [1, 0, 0, 1]
    [1, 0, 0, 0]
    [0, 1, 1, 1]
    [0, 1, 1, 0]
    [0, 1, 0, 1]
    [0, 1, 0, 0]
    [0, 0, 1, 1]
    [0, 0, 1, 0]
    [0, 0, 0, 1]
    [0, 0, 0, 0]
    [1, 1, 1, 1]
    """

    def __init__(
            self,
            bits,
            clock_connector,
            data=0,
            preset=Connector(1),
            clear=Connector(1)):

        # All the output bits are initialized to this data bit
        Counter.__init__(self, bits, clock_connector, data,
                         preset, clear)
        # Calling the super class constructor

        self.ff[
            self.bits -
            1] = TFlipFlop(
            self.t,
            self.enable,
            self.clk,
            self.preset,
            self.clear,
            self.out[
                self.bits -
                1],
            self.outinv[
                self.bits -
                1])

        for i in range(self.bits - 1):
            self.ff[i] = TFlipFlop(
                self.t,
                self.enable,
                self.outinv[
                    i + 1],
                self.preset,
                self.clear,
                self.out[i],
                self.outinv[i])


class DecadeCounter(Counter):

    """
    A 4-Bit Decade Counter
    """

    def __init__(
            self,
            clock_connector,
            data=0,
            preset=Connector(1),
            clear=Connector(1)):

        # All the output bits are initialized to this data bit

        Counter.__init__(self, 4, clock_connector, data, preset,
                         clear)
        # Calling the super class constructor

        self.ff = [None] * 4

        self.ff[3] = TFlipFlop(
            self.t,
            self.enable,
            self.clk,
            self.preset,
            self.clear,
            self.out[3],
            self.outinv[3])
        self.ff[2] = TFlipFlop(
            self.t,
            self.enable,
            self.out[3],
            self.preset,
            self.clear,
            self.out[2],
            self.outinv[2])
        self.ff[1] = TFlipFlop(
            self.t,
            self.enable,
            self.out[2],
            self.preset,
            self.clear,
            self.out[1],
            self.outinv[1])
        self.ff[0] = TFlipFlop(
            self.t,
            self.enable,
            self.out[1],
            self.preset,
            self.clear,
            self.out[0],
            self.outinv[0])

        self.g1 = NAND(self.out[0], self.out[2])
        self.g1.setOutput(self.clear)

        self.bits_fixed = True
        self.reset_once = True


class OctalCounter(Counter):

    """
    A 4-Bit Octal Counter
    """

    def __init__(
            self,
            clock_connector,
            data=0,
            preset=Connector(1),
            clear=Connector(1)):

        # All the output bits are initialized to this data bit

        Counter.__init__(self, 4, clock_connector, data, preset,
                         clear)
        # Calling the super class constructor

        self.ff = [None] * 4

        self.ff[3] = TFlipFlop(
            self.t,
            self.enable,
            self.clk,
            self.preset,
            self.clear,
            self.out[3],
            self.outinv[3])
        self.ff[2] = TFlipFlop(
            self.t,
            self.enable,
            self.out[3],
            self.preset,
            self.clear,
            self.out[2],
            self.outinv[2])
        self.ff[1] = TFlipFlop(
            self.t,
            self.enable,
            self.out[2],
            self.preset,
            self.clear,
            self.out[1],
            self.outinv[1])
        self.ff[0] = TFlipFlop(
            self.t,
            self.enable,
            self.out[1],
            self.preset,
            self.clear,
            self.out[0],
            self.outinv[0])

        self.g1 = NOT(self.out[0])
        self.g1.setOutput(self.clear)

        self.bits_fixed = True
        self.reset_once = True


class Stage14Counter(Counter):

    """
    A 14-Bit Counter
    """

    def __init__(
            self,
            clock_connector,
            data=0,
            preset=Connector(1),
            clear=Connector(1)):

        # All the output bits are initialized to this data bit

        Counter.__init__(self, 4, clock_connector, data, preset,
                         clear)
        # Calling the super class constructor

        self.ff = [None] * 4

        self.ff[3] = TFlipFlop(
            self.t,
            self.enable,
            self.clk,
            self.preset,
            self.clear,
            self.out[3],
            self.outinv[3])
        self.ff[2] = TFlipFlop(
            self.t,
            self.enable,
            self.out[3],
            self.preset,
            self.clear,
            self.out[2],
            self.outinv[2])
        self.ff[1] = TFlipFlop(
            self.t,
            self.enable,
            self.out[2],
            self.preset,
            self.clear,
            self.out[1],
            self.outinv[1])
        self.ff[0] = TFlipFlop(
            self.t,
            self.enable,
            self.out[1],
            self.preset,
            self.clear,
            self.out[0],
            self.outinv[0])

        self.g1 = NAND(self.out[0], self.out[1], self.out[2])
        self.g1.setOutput(self.clear)

        self.bits_fixed = True
        self.reset_once = True


class RingCounter(Counter):

    """
    An N-bit Ring Counter
    """

    def __init__(
            self,
            bits,
            clock_connector,
            preset=Connector(1),
            clear=Connector(1)):

        Counter.__init__(self, bits, clock_connector, data=None, preset=preset,
                         clear=clear)
        arr = [0] * bits
        arr[0] = 1
        self.sr = ShiftRegister(arr, clock_connector, circular=1)
        self.out = []

    def trigger(self):
        self.out = self.sr.output()
        return self.out

    def state(self):
        return self.out

    def reset(self):
        self.__init__(self.bits, clock_connector, clear=Connector(0))

    def set(self):
        self.__init__(self.bits, clock_connector, preset=Connector(0))


class JohnsonCounter(Counter):

    """
    An N-bit Johnson Counter
    """

    def __init__(
            self,
            bits,
            clock_connector,
            preset=Connector(1),
            clear=Connector(1)):

        Counter.__init__(self, bits, clock_connector, data=None, preset=preset,
                         clear=clear)
        arr = [0] * bits
        arr[0] = 1
        self.sr = ShiftRegister(arr, clock_connector, circular=1)
        self.out = []
        self.tail = 1

    def trigger(self):
        self.out = self.sr.output()
        self.out[0] = self.tail
        self.tail = NOT(self.out[self.bits - 1]).output()
        return self.out

    def state(self):
        return self.out

    def reset(self):
        self.__init__(self.bits, clock_connector, clear=Connector(0))

    def set(self):
        self.__init__(self.bits, clock_connector, preset=Connector(0))
