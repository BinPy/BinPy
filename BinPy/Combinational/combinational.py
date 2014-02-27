from BinPy import *
import math

class MUX(GATES):
    """
    This class can be used to create MUX in your circuit.
    It takes 2^n inputs and has n select lines, which are used to select which input line to send to the output.
    """
    def __init__(self, *inputs):
        if not (len(inputs) > 1 and (len(inputs) & (len(inputs) - 1) == 0)):
            raise Exception("ERROR: Number inputs should be a power of 2")
        self.selects = []
        GATES.__init__(self, list(inputs))

    def selectLines(self, *select):
        if not (pow(2, len(select)) == len(self.inputs)):
            raise Exception("ERROR: No. of Select lines are inconsistent with the inputs")
        self.selects = list(select)
        self._updateConnections(self.selects)
        self.trigger()

    def selectLine(self, index, value):
        if index >= len(self.selects):
            self.selects.append(value) 
        else:
            self.selects[index] = value
        if isinstance(value, Connector):
            value.tap(self, 'input')
            self.trigger()

    def setInput(self, index, value):
        if index >= len(self.inputs):
            self.inputs.append(value)
        else:
            self.inputs[index] = value
        if isinstance(value, Connector):
            value.tap(self, 'input')
            self.trigger()

    def trigger(self):
        if len(self.selects) == 0:
            return
        if not (len(self.inputs) > 1 and (len(self.inputs) & (len(self.inputs) - 1) == 0)):
            raise Exception("ERROR: Number of inputs should be a power of 2")
        bstr = ''
        for i in self.selects:
            if isinstance(i, Connector):
                bstr = bstr + str(i.state)
            else:
                bstr = bstr + str(i)
        try:        
            if isinstance(self.inputs[int(bstr, 2)], Connector):
                self._updateResult(self.inputs[int(bstr, 2)].state)
            else:
                self._updateResult(self.inputs[int(bstr, 2)])
        except IndexError:
            raise Exception("Error: Select lines are inconsistent with Input lines")
        if self.outputType:
            self.outputConnector.trigger()

class DEMUX(GATES):
    """
    This class can be used to create de-multiplexer in your circuit.
    It has one input, n select lines and return one of many data-output-lines, 
    which is connected to the single input. In case of high input,
    it works as decoder.
    """
    def __init__(self, *inputs):
        if not (len(inputs) == 1):
            raise Exception("ERROR: Input should be 0/1")
        self.selects = []
        GATES.__init__(self, list(inputs))
        self.outputType = []
        self.outputConnector = []

    def selectLines(self, *select):
        if not (len(select) != 0):
            raise Exception("ERROR: Number of select lines should be greater than zero")
        self.selects = list(select)
        for i in range(pow(2, len(select))):
            self.outputType.append(0)
            self.outputConnector.append(None)
        self._updateConnections(self.selects)
        self.trigger()

    def selectLine(self, index, value):
        if index >= len(self.selects):
            self.selects.append(value)
            for i in range(len(self.outputType), pow(2, len(self.selects))):
                self.outputType.append(0)
                self.outputConnector.append(None)
        else:
            self.selects[index] = value
        if isinstance(value, Connector):
            value.tap(self, 'input')
            self.trigger()

    def setInput(self, index, value):
        if not (index == 0):
            raise Exception("ERROR: There should be a single input")
        self.inputs[index] = value
        if isinstance(value, Connector):
            value.tap(self, 'input')
            self.trigger()

    def trigger(self):
        if len(self.selects) == 0:
            return
        out = []
        for i in range(pow(2, len(self.selects))):
            out.append(0)
            bstr = ''
        for i in self.selects:
            if isinstance(i, Connector):
                bstr = bstr + str(i.state)
            else:
                bstr = bstr + str(i)
        if isinstance(self.inputs[0], Connector):
            out[int(bstr, 2)] = self.inputs[0].state
            self._updateResult(out)
        else:
            out[int(bstr, 2)] = self.inputs[0]
            self._updateResult(out)

    def setInputs(self, *inputs):
        if not (len(inputs) == 1):
            raise Exception("ERROR: There should be a single Input")
        self.inputs = list(inputs)
        self._updateConnections(self.inputs)
        self.trigger()

    def setOutput(self, index, value):
        if not isinstance(value, Connector):
            raise Exception("ERROR: Expecting a Connector Class Object")
        value.tap(self,'output')
        self.outputType[index] = 1
        self.outputConnector[index] = value
        self.trigger()

    def _updateResult(self, value):
        self.result = value
        for i in range(len(value)):
            if self.outputType[i] == 1:
                self.outputConnector[i].state = value[i]

class Decoder(GATES):
    """
    This class can be used to create decoder in your circuit.
    Input is taken as Binary String and returns the 2^n output.
    """
    def __init__(self, *inputs):
        if not (len(inputs) != 0):
            raise Exception("ERROR: Input Length should be greater than zero")
        GATES.__init__(self, list(inputs))
        self.outputType = []
        self.outputConnector = []
        for i in range(pow(2, len(inputs))):
            self.outputType.append(0)
            self.outputConnector.append(None)

    def trigger(self):
        if type(self.outputType) == int:
            return
        out = []
        for i in range(pow(2, len(self.inputs))):
            out.append(0)
            bstr = ''
        for i in self.inputs:
            if isinstance(i, Connector):
                bstr = bstr + str(i.state)
            else:
                bstr = bstr + str(i)
        out[int(bstr, 2)] = 1
        self._updateResult(out)

    def setInputs(self, *inputs):
        if not (len(inputs) != 0):
            raise Exception("ERROR: Input length must be greater than zero")
        self.inputs = list(inputs)
        for i in range(len(self.outputType), pow(2, len(self.inputs))):
            self.outputType.append(0)
            self.outputConnector.append(None)
        self._updateConnections(self.inputs)
        self.trigger()

    def setInput(self, index, value):
        if index >= len(self.inputs):
            self.inputs.append(value)
            for i in range(len(self.outputType), pow(2, len(self.inputs))):
                self.outputType.append(0)
                self.outputConnector.append(None) 
        else:
            self.inputs[index] = value    
        if isinstance(value, Connector):
            value.tap(self, 'input')
            self.trigger()

    def setOutput(self, index, value):
        if not isinstance(value, Connector):
            raise Exception("ERROR: Expecting a Connector Class Object")
        value.tap(self,'output')
        self.outputType[index] = 1
        self.outputConnector[index] = value
        self.trigger()

    def _updateResult(self, value):
        self.result = value
        for i in range(len(value)):
            if self.outputType[i] == 1:
                self.outputConnector[i].state = value[i]

class Encoder(GATES):
    """
    This class can be used to create encoder in your circuit.
    Input is taken as an array and returns the binary coded output.
    """
    def __init__(self, *inputs):
        if not (len(inputs) > 1 and (len(inputs) & (len(inputs) - 1) == 0)):
            raise Exception("ERROR: Number of inputs should be a power of 2")
        if not (inputs.count(1) == 1 or list(x.state for x in 
             filter(lambda i : isinstance(i, Connector), inputs)).count(1) == 1):
            raise Exception("Invalid Input")
        GATES.__init__(self, list(inputs))
        self.outputType = []
        self.outputConnector = []
        for i in range(int(math.log(len(self.inputs), 2))):
            self.outputType.append(0)
            self.outputConnector.append(None)

    def trigger(self):
        if type(self.outputType) == int:
            return
        if not (len(self.inputs) > 1 and (len(self.inputs) & (len(self.inputs) - 1) == 0)):
            raise Exception("ERROR: Number of inputs should be a power of 2")
        temp = self.inputs[:]
        for i in range(len(temp)):
            if isinstance(temp[i], Connector):
                temp[i] = temp[i].state
        bstr = bin(temp.index(1))[2:]
        while len(bstr) < math.log(len(self.inputs), 2):
            bstr = '0' + bstr
        out = list(bstr)
        out = map(int, out)
        self._updateResult(out)

    def setInputs(self, *inputs):
        if not (len(inputs) > 1 and (len(inputs) & (len(inputs) - 1) == 0)):
            raise Exception("ERROR: Number of inputs should be a power of 2")
        if not (inputs.count(1) == 1 or list(x.state for x in 
            filter(lambda i : isinstance(i, Connector), inputs)).count(1) == 1):
            raise Exception("ERROR: Invalid Input")
        self.inputs = list(inputs)
        for i in range(len(self.outputType), int(math.log(len(self.inputs), 2))):
            self.outputType.append(0)
            self.outputConnector.append(None)
            self._updateConnections(self.inputs)
            self.trigger()

    def setInput(self, index, value):
        temp = self.inputs[:]
        if index >= len(temp):        
            temp.append(value)
            if not (temp.count(1) == 1 or list(x.state for x in 
                    filter(lambda i : isinstance(i,Connector), temp)).count(1) == 1):
                raise Exception("ERROR: Invalid Input")
                self.inputs.append(value)
            for i in range(len(self.outputType), int(math.log(len(self.inputs), 2))):
                self.outputType.append(0)
                self.outputConnector.append(None)
        else:
            temp[index] = value
            if not (temp.count(1) == 1 or list(x.state for x in 
                    filter(lambda i : isinstance(i,Connector), temp)).count(1) == 1):
                raise Exception("ERROR: Invalid Input")
                self.inputs[index] = value

        if isinstance(value, Connector):
            value.tap(self, 'input')
            self.trigger()

    def setOutput(self, index, value):
        if not isinstance(value, Connector):
            raise Exception("ERROR: Expecting a Connector Class Object")
        value.tap(self,'output')
        self.outputType[index] = 1
        self.outputConnector[index] = value
        self.trigger()

    def _updateResult(self, value):
        self.result = value
        for i in range(len(value)):
            if self.outputType[i] == 1:
                self.outputConnector[i].state = value[i]
