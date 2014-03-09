from connector import *


class GATES:

    '''
    Takes in as input connectors or the values 0,1 or None.
    The inputs of the class will be the inputs to the gate.
    Base Class implementing all common functions used by Logic Gates
    '''

    def __init__(self, inputs):

        # Clean Connections before updating new connections
        self.history_active = 0  # Ignore history for first computation
        self.outputType = 0  # 1->output goes to a connector class
        self.result = None  # To store the result
        self.outputConnector = None  # Valid only if outputType = 1
        self.inputs = inputs[:]  # Set the inputs
        self.history_inputs = []  # Save a copy of the inputs
        self._updateConnections(self.inputs)
        self._updateHistory()
        self.trigger()  # Any change in the input will trigger change in the
                        # output

    def _updateConnections(self, inputs):
        for i in inputs:
            if isinstance(i, Connector):
                i.tap(self, 'input')

    def setInputs(self, *inputs):
        # Clean Connections before updating new connections
        if len(inputs) != len(self.inputs):
            raise Exception('''ERROR: Given number of inputs does not match
with the number of inputs of the gate''')

        self.history_active = 1  # Use history before computing
        for index in range(len(inputs)):
            if inputs[index] == '~':
                pass
            else:
                if isinstance(self.inputs[index], Connector):
                    if len(self.inputs[index].connections["output"]) != 0:
                        raise Exception(''''ERROR: Tried to assign a value to
an output connector of a logic object''')
                    self.history_inputs[index] = self.inputs[index].state
                    self.inputs[index].state = inputs[index]
                    self.inputs[index].trigger()
                else:
                    self.history_inputs[index] = self.inputs[index]
                    self.inputs[index] = inputs[index]
                    self.trigger()  # Any change in the input will trigger
                                    # change in the output

    def setInput(self, index, value):
        if index >= len(self.inputs) or index < 0:
            raise Exception('''ERROR: Index value greater than number of
inputs to the gate''')
        self.history_active = 1  # Use history before computing
        if isinstance(self.inputs[index], Connector):
            if len(self.inputs[index].connections["output"]) != 0:
                raise Exception('''ERROR: Tried to assign a value to an output
connector of a logic object''')
            self.history_inputs[index] = self.inputs[index].state
            self.inputs[index].state = value
            self.inputs[index].trigger()
        else:
            self.history_inputs[index] = self.inputs[
                index]  # Modify the history
            self.inputs[index] = value
            self.trigger()

    def getInputStates(self):
        input_states = []
        for i in self.inputs:
            if isinstance(i, Connector):
                input_states.append(i.state)
            else:
                input_states.append(i)
        return input_states

    def _updateResult(self):
        if self.outputType == 1:
            #updates owner during first update
            if (len(self.outputConnector.connections["output"]) == 1):
                self.outputConnector.owner = self
            # if the current object is not the owner and there is an owner
            # and the connector is not having a value of None,
            # there is a contention
            else:
                if (self.outputConnector.owner != self and
                    self.outputConnector.owner is not None
                    and self.result is not None):
                    print('WARNING: Logic Contention detected')
                #the owner is not updated if the connector has a value of None
                if (self.outputConnector.owner != self and self.result is None):
                    return
            # if connector value is None, there is no owner
            if (self.outputConnector.state is None):
                self.outputConnector.owner = None
            self.outputConnector.state = self.result  # updates the connector
            self.outputConnector.trigger()

    def _updateHistory(self):
        for i in range(len(self.inputs)):
            if isinstance(self.inputs[i], Connector):
                val1 = self.inputs[i].state
            else:
                val1 = self.inputs[i]
            if len(self.history_inputs) <= i:
                self.history_inputs.append(val1)
            else:
                self.history_inputs[i] = val1

    def setOutput(self, connector):
        if not isinstance(connector, Connector):
            raise Exception("ERROR: Expecting a Connector Class Object")
        connector.tap(self, "output")
        self.outputType = 1
        self.outputConnector = connector
        self.history_active = 0
        self.trigger()

    def output(self):
        self.trigger()
        return self.result

    def _compareHistory(self):
        if self.history_active == 1:  # Only check history if it is active
            for i in range(len(self.inputs)):
                if isinstance(self.inputs[i], Connector):
                    val1 = self.inputs[i].state
                else:
                    val1 = self.inputs[i]
                if (i >= len(self.history_inputs) or
                   self.history_inputs[i] != val1):
                    return True
            return False
        return True


class MIGATES(GATES):

    def __init__(self, *inputs):
        if len(inputs) < 2:
            raise Exception(
                "ERROR: Too few inputs given. Needs at least 2 or more inputs.")

        GATES.__init__(self, list(inputs))


class AND(MIGATES):

    def __init__(self, *inputs):
        MIGATES.__init__(self, *inputs)

    def trigger(self):
        if self._compareHistory() is True:
            self.history_active = 1
            self._updateHistory()  # Update the inputs before a computation
            self.result = int(True)
            for i in self.inputs:
                if ((isinstance(i, Connector) and
                    not i.state and i.state is not None) or
                    (not isinstance(i, Connector) and not i and i is not None)):
                    self.result = int(False)
                    break
            self._updateResult()


class OR(MIGATES):

    def __init__(self, *inputs):
        MIGATES.__init__(self, *inputs)

    def trigger(self):
        if self._compareHistory() is True:
            self.history_active = 1
            self._updateHistory()  # Update the inputs before a computation
            self.result = int(False)
            for i in self.inputs:
                if ((isinstance(i, Connector) and
                    (i.state or i.state is None)) or
                    (i or i is None)):
                    self.result = int(True)
                    break
            self._updateResult()


class NOT(GATES):

    def __init__(self, *inputs):
        if len(inputs) != 1:
            raise Exception("ERROR: NOT Gates takes only one input")
        else:
            GATES.__init__(self, list(inputs))

    def setInputs(self, *inputs):
        # Clean Connections before updating new connections
        if len(inputs) != 1:
            raise Exception("ERROR: NOT Gates takes only one input")
        else:
            val = inputs[0]
            self.history_active = 1  # Use history before computing
            if isinstance(self.inputs[0], Connector):
                self.inputs[0].state = val  # Set the inputs
                self.inputs[0].trigger()
            else:
                self.inputs[0] = val
        self.trigger()  # Any change in the input will trigger change in the
                        # output

    def setInput(self, value):
        self.setInputs(value)

    def trigger(self):
        if self._compareHistory() is True:
            self.history_active = 1
            self._updateHistory()  # Update the inputs after a computation
            if (isinstance(self.inputs[0], Connector)):
                self.result = ((not self.inputs[0].state) and
                              (self.inputs[0].state is not None))
            else:
                self.result = ((not self.inputs[0]) and
                              (self.inputs[0] is not None))
            self._updateResult()


class XOR(MIGATES):

    def __init__(self, *inputs):
        MIGATES.__init__(self, *inputs)

    def trigger(self):
        if self._compareHistory() is True:
            self.history_active = 1
            self._updateHistory()  # Update the inputs before a computation
            temp = 1
            for i in self.inputs:
                if isinstance(i, Connector):
                    val = (i.state or i.state is None)
                else:
                    val = (i or i is None)
                temp = temp ^ val
            temp = temp ^ 1
            self.result = int(temp)
            self._updateResult()


class XNOR(MIGATES):

    def __init__(self, *inputs):
        MIGATES.__init__(self, *inputs)

    def trigger(self):
        if self._compareHistory() is True:
            self.history_active = 1
            self._updateHistory()  # Update the inputs before a computation
            temp = 1
            for i in self.inputs:
                if (isinstance(i, Connector)):
                    val = i.state
                else:
                    val = i
                temp = temp ^ val
            temp = temp ^ 1
            self.result = int(not temp)
            self._updateResult()


class NAND(MIGATES):

    def __init__(self, *inputs):
        MIGATES.__init__(self, *inputs)

    def trigger(self):
        if self._compareHistory() is True:
            self.history_active = 1
            self.result = int(False)
            self._updateHistory()  # Update the inputs before a computation
            for i in self.inputs:
                if ((isinstance(i, Connector) and
                    not i.state and i.state is not None) or
                    (not isinstance(i, Connector) and not i and i is not None)):
                    self.result = int(True)
                    break
            self._updateResult()


class NOR(MIGATES):

    def __init__(self, *inputs):
        MIGATES.__init__(self, *inputs)

    def trigger(self):
        if self._compareHistory() is True:
            self.history_active = 1
            self.result = int(True)
            self._updateHistory()  # Update the inputs before a computation
            for i in self.inputs:
                if ((isinstance(i, Connector) and
                    (i.state or i.state is None)) or
                    (i or i is None)):
                    self.result = int(False)
            self._updateResult()


class BUFFER(GATES):
    '''A single input Buffer Gate object
    Assumes that the first argument is an input to the gate and the second one
    is the enable input of the buffer.
    Input values can be 0, 1 or None.'''
    def __init__(self, *inputs):
        if len(inputs) != 2:
            raise Exception('''ERROR: BUFFER Gates take only two inputs -
Input and Enable''')
        else:
            GATES.__init__(self, list(inputs))

    def trigger(self):
        if self._compareHistory() is True:
            self.history_active = 1
            self.result = None
            self._updateHistory()  # Update the inputs after a computation
            if ((isinstance(self.inputs[1], Connector) and
                self.inputs[1].state == 1)):
                self.result = not not self.inputs[0].state
            elif (not isinstance(self.inputs[1], Connector) and self.inputs[1]):
                self.result = not not self.inputs[0]
            self._updateResult()
