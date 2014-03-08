from BinPy.Gates.gates import *
import math

class MUX(GATES):
    """
    This class can be used to create MUX in your circuit. MUX is used to select
    a single output line out of many inputs. This class can be used as any 2^n X
    n Multiplexer where n is the number of select lines used to select the input
    out of 2^n input lines.
    INPUT:          nth index has nth input value, input should be power of 2
    OUTPUT:         single output, 1 or 0
    SELECT LINES:   In binary form, select line for 4 will be 1 0 0

    Example:
        >>> from BinPy import *
        >>> mux = MUX(0, 1)            "MUX takes its 2^n inputs (digital or Connector)"
        >>> mux.selectLines(0)         "Put select Line"
        >>> mux.output()
        0
        >>> mux.selectLine(0, 1)       "Select line at index 0 is changed to 1"
        >>> mux.output()
        1
        >>> mux.setInput(1, 0)         "Input line at index 1 is changed to 0"
        >>> mux.output()
        0

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
    This class can be used to create DEMUX in your circuit. DEMUX is used to select
    It takes single input and n select lines and decode the select lines into BCD form
    base upon the input. In case of high input, it works as a decoder.
    INPUT:          Single Input, 1 or 0
    OUTPUT:         BCD form of select lines in case of high input, else low output
    SELECT LINES:   nth select line at nth index

    Example:
        >>> from BinPy import *
        >>> demux = DEMUX(0)             "DEMUX takes 1 input (digital or Connector)"
        >>> demux.selectLines(0)         "Put select Lines"
        >>> demux.output()
        [0, 0]
        >>> demux.selectLine(0, 1)       "Select line at index 0 is changed to 1"
        >>> demux.output()
        [0, 1]
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
    Input is taken as Binary String and returns the equivalent BCD form.
    INPUT:      n Binary inputs, nth input ant the nth index
    OUTPUT:     Gives equivalent BCD form

    Example:
        >>> decoder = Decoder(0)            "Decoder with 1 input, 0"
        >>> decoder.output()
        [1, 0]
        >>> decoder.setInputs(0, 1)         "sets the new inputs to the decoder"
        [0, 1, 0, 1]

    """
    def __init__(self, *inputs):
        if len(inputs) == 0:
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
        if len(inputs) == 0:
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
    This class can be used to create encoder in your circuit. It converts the input BCD form to binary output. It works as the inverse of the decoder
    INPUT:      Input in BCD form, length of input must me in power of 2
    OUTPUT:     Encoded Binary Form

    Example:
        >>> encoder = Encoder(0, 1)             "Encoder with BCD input 01 "
        >>> encoder.output()                    "Binary Form"
        [1]
        >>> encoder.setInputs(0, 0, 0, 1)       "Sets the new inputs"
        [1 , 1]
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
        self._updateResult(list(out))

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
