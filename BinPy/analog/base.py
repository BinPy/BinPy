from BinPy import *


class Resistor:

    """
    This Class implements the Resistor, having the following parameters:
    '+' : Resistor end at positive potential
    '-' : Resistor end at negative potential
    'r' : Resistance value
    'i' : Current flowing through the resistor

    Example:
        >>> from BinPy import *
        >>> params = {'r':5}
        >>> r = Resistor(params)
        >>> r.getParams()
        {'i': 0, '+': 0, 'r': 5, '-': 0}
        >>> r.setVoltage(Connector(5), Connector(0))
        {'i': 1.0, '+': 5, 'r': 5, '-': 0}
        >>> r.setCurrent(10)
        {'i': 10, '+': 50, 'r': 5, '-': 0}
        >>> r.setResistance(10)
        {'i': 5.0, '+': 50, 'r': 10, '-': 0}

    """

    def __init__(self, params):
        self.params = {'+': Connector(0), '-': Connector(0), 'i': 0, 'r':
                       0}
        for i in params:
            self.params[i] = params[i]

    def setResistance(self, value):
        self.params['r'] = value
        self.params['i'] = (
            self.params['+'].state - self.params['-'].state) / self.params['r']
        return self.params

    def getParams(self):
        return self.params

    def setCurrent(self, value):
        self.params['i'] = value
        self.params['+'].state = self.params['-'].state + \
            (self.params['i'] * self.params['r'])
        return self.params

    def setVoltage(self, val1, val2):
        if not(isinstance(val1, Connector) and isinstance(val2, Connector)):
            raise Exception(
                "Invalid Voltage Values, Expecting a Connector Class Object")
        self.params['+'] = val1
        self.params['-'] = val2
        self.params['i'] = (
            self.params['+'].state - self.params['-'].state) / self.params['r']
        return self.params

    def __repr__(self):
        return str(self.params['r'])
