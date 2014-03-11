from BinPy.Gates.connector import *


class Gate(object):

    """
    Base Class implementing all common functions used by Logic gates
    """

    def __init__(self, output, *inputs):
        is_connector(*(list(inputs) + [output]))
        self.output = output
        self.inputs = []
        self.in_states = []
        self.connect(output, *inputs)

    def trigger(self):
        self.in_states = [i.state for i in self.inputs]
        out_state = self.calc_output(self.in_states)
        if out_state != self.output.state:
            self.output.set(out_state)

    def connect(self, output, *inputs):
        inputs = list(inputs)
        if output in inputs:
            raise Exception("Feedback not allowed")
        if isinstance(self, NOT):
            if len(inputs) != 1:
                raise Exception("NOT Gate take only one input")
        else:
            if len(inputs) < 2:
                raise Exception("At least 2 inputs expected")
        self.disconnect()
        self.inputs = inputs
        self.output = output
        output.tap(self, 'output')
        for i in inputs:
            i.tap(self, 'input')
        self.trigger()

    def disconnect(self):
        if self in self.output.connections['output']:
            self.output.connections['output'].remove(self)
        if self in self.output.connections['input']:
            self.output.connections['input'].remove(self)
        for i in range(len(self.inputs)):
            if self in self.inputs[i].connections['input']:
                self.inputs[i].connections['input'].remove(self)
            if self in self.inputs[i].connections['output']:
                self.inputs[i].connections['output'].remove(self)

    def getStates(self):
        return {'inputs': self.in_states, 'output': self.output()}

    def getConns(self):
        return {'output': self.output.name,
                'inputs': [i.name for i in self.inputs]}



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


class AND(Gate):
    def __init__(self, output, *inputs):
        Gate.__init__(self, output, *inputs)

    def calc_output(self, in_states):
        return and_alg(in_states)


class OR(Gate):
    def __init__(self, output, *inputs):
        Gate.__init__(self, output, *inputs)

    def calc_output(self, in_states):
        return or_alg(in_states)


class NOT(Gate):
    def __init__(self, output, *inputs):
        Gate.__init__(self, output, *inputs)

    def calc_output(self, in_states):
        return abs(in_states[0]-1) if in_states[0] in (0,1) else in_states[0]


class NAND(Gate):
    def __init__(self, output, *inputs):
        Gate.__init__(self, output, *inputs)

    def calc_output(self, in_states):
        temp = and_alg(in_states)
        return abs(temp-1) if temp in (0,1) else temp


class NOR(Gate):
    def __init__(self, output, *inputs):
        Gate.__init__(self, output, *inputs)

    def calc_output(self, in_states):
        temp = or_alg(in_states)
        return abs(temp-1) if temp in (0,1) else temp


class XOR(Gate):
    def __init__(self, output, *inputs):
        Gate.__init__(self, output, *inputs)

    def calc_output(self, in_states):
        return xor_alg(in_states)


class XNOR(Gate):
    def __init__(self, output, *inputs):
        Gate.__init__(self, output, *inputs)

    def calc_output(self, in_states):
        temp = xor_alg(in_states)
        return abs(temp-1) if temp in (0,1) else temp