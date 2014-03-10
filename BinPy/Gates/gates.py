from BinPy.Gates.connector import *


class GATES:

    """
    Base Class implementing all common functions used by Logic Gates
    """

    def __init__(self, output, *inputs):
        for i in list(inputs) + [output]:
            if not isinstance(i, Connector):
                raise Exception("Connector Class instance/s expected")
        if isinstance(self, NOT):
            if len(inputs) != 1:
                raise Exception("NOT Gates take only one input")
            self.in_state = 2
        else:
            self.in_states = []
            if len(inputs) < 2:
                raise Exception("At least 2 inputs expected.")
        
        self.output = output
        self.inputs = list(inputs)
        self._connect(self.output, self.inputs)
        self.trigger()

    def trigger(self):
        self.in_states = [i.state for i in self.inputs]
        out_state = self.calc_output(self.in_states)
        if out_state != self.output.state:
            self.output.state = out_state
            self.output.trigger()

    def _connect(self, output, inputs):
        output.tap(self, 'output')
        for i in inputs:
            i.tap(self, 'input')

    def getStates(self):
        input_states = []
        for i in self.inputs:
            input_states.append(i.state)
        return {'inputs': input_states, 'output': self.output()}

    def setInput(self, index, input):
        if not isinstance(input, Connector):
                raise Exception("Connector Class instance/s expected")
        innum = len(self.inputs)
        if index < innum <= index:
            raise Exception("input index out of range.")
        self.inputs[index] = input  # Remove from connector too
        input.tap(self, 'input')
        self.trigger()

    def setOutput(self, output):
        if not isinstance(output, Connector):
            raise Exception("Connector Class instance/s expected")
        output.tap(self, 'output')
        self.trigger()

# GATE ALGORITHMS

def and_alg(inputs):
    if 0 in inputs: return 0
    elif inputs.count(1) == len(inputs): return 1
    else: return 3

def or_alg(inputs):
    if 1 in inputs: return 1
    elif inputs.count(0) == len(inputs): return 0
    else: return 3

def xor_alg(inputs):
    if 2 in inputs or 3 in inputs: return 3
    else:
        return 1 if inputs.count(1) % 2 else 0


class AND(GATES):
    def __init__(self, output, *inputs):
        GATES.__init__(self, output, *inputs)

    def calc_output(self, in_states):
        return and_alg(in_states)


class OR(GATES):
    def __init__(self, output, *inputs):
        GATES.__init__(self, output, *inputs)

    def calc_output(self, in_states):
        return or_alg(in_states)


class NOT(GATES):
    def __init__(self, output, *inputs):
        GATES.__init__(self, output, *inputs)

    def calc_output(self, in_state):
        return abs(in_state-1) if in_state in (0,1) else in_state


class NAND(GATES):
    def __init__(self, output, *inputs):
        GATES.__init__(self, output, *inputs)

    def calc_output(self, in_states):
        temp = and_alg(in_states)
        return abs(temp-1) if temp in (0,1) else temp


class NOR(GATES):
    def __init__(self, output, *inputs):
        GATES.__init__(self, output, *inputs)

    def calc_output(self, in_states):
        temp = or_alg(in_states)
        return abs(temp-1) if temp in (0,1) else temp


class XOR(GATES):
    def __init__(self, output, *inputs):
        GATES.__init__(self, output, *inputs)

    def calc_output(self, in_states):
        return xor_alg(in_states)


class NXOR(GATES):
    def __init__(self, output, *inputs):
        GATES.__init__(self, output, *inputs)

    def calc_output(self, in_states):
        temp = xor_alg(in_states)
        return abs(temp-1) if temp in (0,1) else temp