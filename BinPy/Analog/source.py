from math import *
from BinPy import *


class Source:

    "This class represents a base class for the signal source"

    def __init__(self, equation, params):
        self.params = params
        self.equation = equation

    def setParam(self, param, value):
        if not isinstance(self.params[param], type(value)):
            raise Exception("Invalid Value")
        self.params[param] = value
        self.trigger()

    def setParams(self, params):
        for i in params:
            self.setParam(i, params[i])

    def getParams(self):
        self.trigger()
        return self.params

    def setEquation(self, equation):
        self.equation = equation
        self.trigger()

    def evaluate(self):
        for i in self.params:
            exec("%s=%f" % (i, self.params[i]))
        self.val = eval(self.equation)
        return self.val


class VoltageSource(Source):

    def __init__(self, equation, params):
        Source.__init__(self, equation, params)
        self.params.update({'H': Connector(0), 'L': Connector(0)})
        self.trigger()

    def trigger(self):
        self.params['H'].state = self.evaluate() + self.params['L'].state

    def setOutput(self, param, value):
        if not isinstance(value, Connector):
            raise Exception("Expecting a Connector Class Object")
        self.params[param] = value


class CurrentSource(Source):

    def __init__(self, equation, params):
        Source.__init__(self, equation, params)
        self.params.update({'H': Connector(0), 'L': Connector(0)})
        self.trigger()

    def trigger(self):
        self.params['i'] = self.evaluate()

    def setoutput(self, param, value):
        if not isinstance(value, Connector):
            raise Exception("Expecting a Connector Class Object")
        self.params[param] = value


class SinWaveVoltageSource(VoltageSource):

    def __init__(self, amplitude=0, frequency=0, time=0, epoch=0):

        equation = 'V*round(sin(radians((w*t)+e)), 2)'
        params = {'V': amplitude, 'w': frequency, 't': time, 'e': epoch}
        VoltageSource.__init__(self, equation, params)


class CosWaveVoltageSource(VoltageSource):

    def __init__(self, amplitude=0, frequency=0, time=0, epoch=0):

        equation = 'V*round(cos(radians((w*t)+e)), 2)'
        params = {'V': amplitude, 'w': frequency, 't': time, 'e': epoch}
        VoltageSource.__init__(self, equation, params)


class SinWaveCurrentSource(CurrentSource):

    def __init__(self, amplitude=0, frequency=0, time=0, epoch=0):

        equation = 'I*round(sin(radians((w*t)+e)), 2)'
        params = {'I': amplitude, 'w': frequency, 't': time, 'e': epoch}
        CurrentSource.__init__(self, equation, params)


class CosWaveCurrentSource(CurrentSource):

    def __init__(self, amplitude=0, frequency=0, time=0, epoch=0):

        equation = 'I*round(cos(radians((w*t)+e)), 2)'
        params = {'I': amplitude, 'w': frequency, 't': time, 'e': epoch}
        CurrentSource.__init__(self, equation, params)
