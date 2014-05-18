from BinPy.Gates.gates import *
import math


class HalfAdder():

    """This Class implements Half Adder, Arithmetic sum of two bits and return its
    Sum and Carry
    Output: [CARRY, SUM]
    Example:
        >>> from BinPy import *
        >>> ha = HalfAdder(0, 1)
        >>> ha.output()
        [0, 1]

    """

    def __init__(self, *inputs):

        if len(inputs) is not 2:
            raise Exception("ERROR: Number of arguments not consistent")

        self.inputs = list(inputs[:])
        self.S = XOR(self.inputs[0], self.inputs[1])
        self.C = AND(self.inputs[0], self.inputs[1])

    def set_input(self, index, value):
        if index > 1 or index < 0:
            raise Exception("ERROR: Not a valid index value")
        self.inputs[index] = value
        if index == 0:
            self.S.setInput(0, self.inputs[0])
            self.C.setInput(0, self.inputs[0])
        elif index == 1:
            self.S.setInput(1, self.inputs[1])
            self.C.setInput(1, self.inputs[1])

    def set_inputs(self, *inputs):
        self.inputs = list(inputs)[:]
        self.S.setInputs(*inputs)
        self.C.setInputs(*inputs)

    def set_output(self, index, value):
        if not isinstance(value, Connector):
            raise Exception("ERROR: Expecting a Connector Class Object")
        if index == 0:
            self.C.setOutput(value)
        elif index == 1:
            self.S.setOutput(value)

    def output(self):
        return [self.C.output(), self.S.output()]


class FullAdder():

    """This Class implements Full Adder, Arithmetic sum of three bits and
    return its Sum and Carry
    Output: [CARRY, SUM]
    Example:
        >>> from BinPy import *
        >>> fa = FullAdder(0, 1, 1)
        >>> fa.output()
        [1, 0]
    """

    def __init__(self, *inputs):
        if len(inputs) is not 3:
            raise Exception("ERROR: Number of arguments are inconsistent")

        self.inputs = list(inputs)[:]
        # Connector Object to connect the two half adders
        self.con1 = Connector()
        self.ha1 = HalfAdder(self.inputs[0], self.inputs[1])
        self.ha1.set_output(1, self.con1)
        self.ha2 = HalfAdder(self.con1, self.inputs[2])
        self.con2 = Connector()
        self.con3 = Connector()
        self.ha1.set_output(0, self.con2)
        self.ha2.set_output(0, self.con3)
        self.or1 = OR(self.con2, self.con3)

    def set_input(self, index, value):
        if index > 3 or index < 0:
            raise Exception("ERROR: Not a valid index number")
        self.inputs[index] = value
        if index == 0:
            self.ha1.set_input(0, self.inputs[0])
        elif index == 1:
            self.ha1.set_input(1, self.inputs[1])
        elif index == 2:
            self.ha2.set_input(1, self.inputs[2])

    def set_inputs(self, *inputs):
        if len(inputs) is not 3:
            raise Exception("ERROR: Number of arguments are inconsistent")
        self.inputs = list(inputs)[:]
        self.ha1.set_inputs(self.inputs[0], self.inputs[1])
        self.ha2.set_input(1, self.inputs[2])

    def set_output(self, index, value):
        if not isinstance(value, Connector):
            raise Exception("ERROR: Expecting a Connector Class Object")

        if index == 0:
            self.or1.setOutput(value)
        elif index == 1:
            self.ha2.set_output(1, value)
        else:
            raise Exception("ERROR: Invalid index passed")

    def output(self):
        return [self.or1.output(), self.ha2.output()[1]]


'''
class BCDAdder(GATES):

    """This Class implements 4 bit BCD Adder,
    and return its BCD Sum and Carry
    Output: [SUM, CARRY]
    Example:
        >>> from BinPy import *
        >>> ba = BCDAdder([0, 1, 1, 0], [1, 0, 1, 0], 0)
        >>> ba.output()
        [0, 0, 0, 0, 1]
    """

    def __init__(self, input1, input2, carry):
        self.carry = carry
        self.size = max(len(input1), len(input2))
        self.input1 = input1
        self.input2 = input2
        input3 = self.fill(self.input1, self.size)
        input4 = self.fill(self.input2, self.size)
        GATES.__init__(self, [input3, input4])
        self.outputType = [0] * (self.size + 1)
        self.outputConnector = [None] * (self.size + 1)
        self.trigger()

    def fill(self, arr, size):
        arr = list(map(str, arr))
        arr = "".join(arr)
        arr = str.zfill(arr, size)
        arr = list(arr)
        arr = list(map(int, arr))
        return arr

    def trigger(self):
        if isinstance(self.outputType, int):
            return
        result = BinaryAdder(self.input1, self.input2, self.carry).output()
        temp = AND(result[1], result[2]).output()
        temp1 = AND(result[1], result[3]).output()
        temp = OR(temp1, temp).output()
        temp = OR(result[0], temp).output()
        self.input1[0] = 0
        self.input1[1] = temp
        self.input1[2] = temp
        self.input1[3] = 0
        self.input2[0] = result[1]
        self.input2[1] = result[2]
        self.input2[2] = result[3]
        self.input2[3] = result[4]
        self.carry = result[0]
        result = BinaryAdder(self.input1, self.input2, self.carry).output()
        self._updateResult(result)

    def setOutput(self, index, value):
        if not isinstance(value, Connector):
            raise Exception("ERROR: Expecting a Connector Class Object")
        value.tap(self, 'output')
        self.outputType[index] = 1
        self.outputConnector[index] = value
        self.trigger()

    def _updateResult(self, value):
        self.result = value
        for i in range(len(value)):
            if self.outputType[i] == 1:
                self.outputConnector[i].state = value[i]
'''


class HalfSubtractor():

    """This Class implements Half Subtractor, Arithmetic difference of two bits and return its
    Difference and Borrow output
    Output: [BORROW, DIFFERENCE]
    Example:
        >>> from BinPy import *
        >>> hs = HalfSubtractor(0, 1)
        >>> hs.output()
        [1, 1]

    """

    def __init__(self, *inputs):
        if len(inputs) is not 2:
            raise Exception("Number of arguments are inconsistent")
        self.inputs = list(inputs)[:]
        self.D = XOR(self.inputs[0], self.inputs[1])
        self.N = NOT(self.inputs[0])
        self.con = Connector()
        self.N.setOutput(self.con)
        self.B = AND(self.con, self.inputs[1])

    def set_input(self, index, value):
        if index > 3 or index < 0:
            raise Exception("ERROR: Invalid Index passed")
        self.inputs[index] = value
        if index == 0:
            self.D.setInput(0, self.inputs[0])
            self.N.setInput(self.inputs[0])
        elif index == 1:
            self.D.setInput(1, self.inputs[1])
            self.B.setInput(1, self.inputs[1])

    def set_inputs(self, *inputs):
        if len(inputs) is not 2:
            raise Exception("Number of arguments are inconsistent")
        self.inputs = list(inputs)[:]
        self.D.setInputs(self.inputs[0], self.inputs[1])
        self.N.setInput(self.inputs[0])
        self.B.setInputs(self.con, self.inputs[1])

    def set_output(self, index, value):
        if not isinstance(value, Connector):
            raise Exception("ERROR: Expecting a Connector Class Object")
        if index == 0:
            self.B.setOutput(value)
        elif index == 1:
            self.D.setOutput(value)
        else:
            raise Exception("ERROR: Invalid Index passed")

    def output(self):
        return [self.B.output(), self.D.output()]


class FullSubtractor(GATES):

    """This Class implements Full Subtractor, Arithmetic difference of three bits and
    return its Difference and Borrow
    Output: [BORROW, DIFFERENCE]
    Example:
        >>> from BinPy import *
        >>> fs = FullSubtractor(0, 1, 1)
        >>> fs.output()
        [0, 1]
    """

    def __init__(self, *inputs):
        if len(inputs) is not 3:
            raise Exception("ERROR: Number of arguments inconsistent")
        self.inputs = list(inputs)[:]
        self.hs1 = HalfSubtractor(self.inputs[0], self.inputs[1])
        self.con1 = Connector()
        self.hs1.set_output(1, self.con1)
        self.hs2 = HalfSubtractor(self.con1, self.inputs[2])
        self.con2 = Connector()
        self.con3 = Connector()
        self.hs1.set_output(0, self.con1)
        self.hs2.set_output(0, self.con2)
        self.or1 = OR(self.con1, self.con2)

    def set_input(self, index, value):
        if index > 3 or index < 0:
            raise Exception("ERROR: Invalid Index passed")
        self.inputs[index] = value  
        if index == 0:
            self.hs1.set_input(0, self.inputs[0])
        elif index == 1:
            self.hs1.set_input(1, self.inputs[1])
        elif index == 2:
            self.hs2.set_input(1, self.inputs[2])

    def set_inputs(self, *inputs):
        if len(inputs) is not 3:
            raise Exception("ERROR: Number of arguments inconsistent")
        self.inputs = list(inputs)[:]
        self.hs1.set_inputs(self.inputs[0], self.inputs[1])
        self.hs2.set_input(1, self.inputs[2])

    def set_output(self, index, value):
        if not isinstance(value, Connector):
            raise Exception("ERROR: Expecting a Connector Class Object")
        if index == 0:
            self.or1.setOutput(value)
        elif index == 1:
            self.hs2.set_output(1, value)
        else:
            raise Exception("ERROR: Invalid Index passed")

    def output(self):
        return [self.or1.output(), self.hs2.output()[1]]


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
            raise Exception(
                "ERROR: No. of Select lines are inconsistent with the inputs")
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
            raise Exception(
                "Error: Select lines are inconsistent with Input lines")
        if self.outputType:
            self.outputConnector.trigger()

    def __str__(self):
        return self.buildStr("MUX")


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
            raise Exception(
                "ERROR: Number of select lines should be greater than zero")
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
        value.tap(self, 'output')
        self.outputType[index] = 1
        self.outputConnector[index] = value
        self.trigger()

    def _updateResult(self, value):
        self.result = value
        for i in range(len(value)):
            if self.outputType[i] == 1:
                self.outputConnector[i].state = value[i]

    def __str__(self):
        return self.buildStr("DEMUX")


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
        if isinstance(self.outputType, int):
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
        value.tap(self, 'output')
        self.outputType[index] = 1
        self.outputConnector[index] = value
        self.trigger()

    def _updateResult(self, value):
        self.result = value
        for i in range(len(value)):
            if self.outputType[i] == 1:
                self.outputConnector[i].state = value[i]

    def __str__(self):
        return self.buildStr("Decoder")


class Encoder(GATES):

    """
    This class can be used to create encoder in your circuit.
    It converts the input BCD form to binary output.
    It works as the inverse of the decoder
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
                                             filter(lambda i: isinstance(i, Connector), inputs)).count(1) == 1):
            raise Exception("Invalid Input")
        GATES.__init__(self, list(inputs))
        self.outputType = []
        self.outputConnector = []
        for i in range(int(math.log(len(self.inputs), 2))):
            self.outputType.append(0)
            self.outputConnector.append(None)

    def trigger(self):
        if isinstance(self.outputType, int):
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
                                             filter(lambda i: isinstance(i, Connector), inputs)).count(1) == 1):
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
                                               filter(lambda i: isinstance(i, Connector), temp)).count(1) == 1):
                raise Exception("ERROR: Invalid Input")
                self.inputs.append(value)
            for i in range(len(self.outputType), int(math.log(len(self.inputs), 2))):
                self.outputType.append(0)
                self.outputConnector.append(None)
        else:
            temp[index] = value
            if not (temp.count(1) == 1 or list(x.state for x in
                                               filter(lambda i: isinstance(i, Connector), temp)).count(1) == 1):
                raise Exception("ERROR: Invalid Input")
                self.inputs[index] = value

        if isinstance(value, Connector):
            value.tap(self, 'input')
            self.trigger()

    def setOutput(self, index, value):
        if not isinstance(value, Connector):
            raise Exception("ERROR: Expecting a Connector Class Object")
        value.tap(self, 'output')
        self.outputType[index] = 1
        self.outputConnector[index] = value
        self.trigger()

    def _updateResult(self, value):
        self.result = value
        for i in range(len(value)):
            if self.outputType[i] == 1:
                self.outputConnector[i].state = value[i]

    def __str__(self):
        return self.buildStr("Encoder")
