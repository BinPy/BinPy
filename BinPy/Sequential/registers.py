from BinPy.Sequential.sequential import *
from BinPy.tools import *


class Register(object):

    """
    Base class for all registers
    """

    def __init__(self, inputs, clock, clear):
        self.inputs = inputs
        if not isinstance(clock, Clock):
            raise Exception("Error: Invalid Clock Input")
        self.clock = clock
        self.clear = clear
        self.result = None
        self.outputType = {}
        self.outputConnector = {}
        self._updateConnections(self.inputs)

    def _updateConnections(self, inputs):
        for i in inputs:
            if isinstance(i, Connector):
                i.tap(self, 'input')

    def setInputs(self, *inputs):
        if len(list(inputs)) < len(self.inputs):
            raise Exception("Error: Invalid Arguments")
        else:
            self.inputs = list(inputs)
            self._updateConnections(self.inputs)

    def setInput(self, index, value):
        if index >= len(self.inputs):
            self.inputs.append(value)
        else:
            self.inputs[index] = value
        if isinstance(value, Connector):
            value.tap(self, 'input')

    def setClock(self, clk):
        if not isinstance(clk, Clock):
            raise Exception("Error: Invalid Clock")
        self.clock = clk

    def setClear(self, clr):
        self.clear = clr

    def getInputStates(self):
        input_states = []
        for i in self.inputs:
            if isinstance(i, Connector):
                input_states.append(i.state)
            else:
                input_states.append(i)
        return input_states

    def _updateResult(self, value):
        self.result = value
        for i in self.outputType:
            if self.outputType[i] == 1:
                self.outputConnector[i].state = self.result[i]
                self.outputConnector[i].trigger()

    def setOutput(self, index, value):
        if not isinstance(value, Connector):
            raise Exception("Error: Expecting a Connector Class Object")
        self.outputType[index] = 1
        self.outputConnector[index] = value
        value.tap(self, 'output')
        self._updateResult(self.result)

    def output(self):
        self.trigger()
        return self.result


class FourBitRegister(Register):

    """
    Four Bit Register
    Inputs: A0, A1, A2, A3
    Clock: clock
    Clear: clear

    Example:
        >>> from BinPy import *
        >>> c = Clock(1, 500)
        >>> c.start()
        >>> fr = FourBitRegister(1, 0, 1, 1, c, 1)
        >>> fr.output()
        [1, 0, 1, 1]

    """

    def __init__(self, A0, A1, A2, A3, clock, clear):
        Register.__init__(self, [A0, A1, A2, A3], clock, clear)

    def trigger(self):
        out = []
        for i in range(0, 4):
            ff1 = DFlipFlop(self.inputs[i], Connector(1), self.clock.A,
                            clear=self.clear)

            while True:
                if self.clock.A.state == 1:
                    ff1.trigger()
                    break
            while True:
                if self.clock.A.state == 0:
                    ff1.trigger()
                    break
            out.append(ff1.state()[0])

        self._updateResult(out)


class FourBitLoadRegister(Register):

    """
    Four Bit Register with Load
    Inputs: A0, A1, A2, A3
    Clock: clock
    Clear: clear
    Load: load
    Methods: setLoad()

    Example:
        >>> from BinPy import *
        >>> c = Clock(1, 500)
        >>> c.start()
        >>> fr = FourBitLoadRegister(1, 0, 1, 1, c, 1, 1)
        >>> fr.output()
        [1, 0, 1, 0]

    """

    def __init__(self, A0, A1, A2, A3, clock, clear, load):
        self.old = [0, 0, 0, 0]             # Clear State
        self.load = load
        Register.__init__(self, [A0, A1, A2, A3], clock, clear)

    def setLoad(self, load):
        self.load = load

    def trigger(self):
        out = []
        for i in range(0, 4):
            ff1 = DFlipFlop(self.inputs[i], Connector(1), self.clock.A,
                            clear=self.clear)
            if self.load == 0:
                ff1.setInputs(d=self.old[i])
            while True:
                if self.clock.A.state == 1:
                    ff1.trigger()
                    break
            while True:
                if self.clock.A.state == 0:
                    ff1.trigger()
                    break
            out.append(ff1.state()[0])
        self.old = out
        self._updateResult(out)


class ShiftRegister(Register):

    """
    Shift Register
    Inputs: [A0, A1, A2, A3]
    Clock: clock

    Example:
        >>> from BinPy import *
        >>> c = Clock(1, 500)
        >>> c.start()
        >>> fr = ShiftRegister([1, 0, 0, 0], c)
        >>> fr.output()
        [1, 1, 0, 0]
        >>> fr.output()
        [1, 1, 1, 0]
        >>> fr.output()
        [1, 1, 1, 1]

    """

    def __init__(self, inputs, clock, clear=Connector(1), circular=0):
        self.circular = circular
        Register.__init__(self, inputs, clock, clear)

    def trigger(self):
        a0 = self.inputs[0]
        for i in range(0, len(self.inputs)):
            ff1 = DFlipFlop(self.inputs[i], Connector(1), self.clock.A,
                            clear=self.clear)
            if self.circular and i == 0:
                self.inputs[i] = self.inputs[len(self.inputs) - 1]
            else:
                self.inputs[i] = a0
            while True:
                if self.clock.A.state == 1:
                    ff1.trigger()
                    break
            while True:
                if self.clock.A.state == 0:
                    ff1.trigger()
                    break
            a0 = ff1.state()[0]
        out = self.inputs
        self._updateResult(out)
