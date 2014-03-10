from BinPy.Gates.connector import *


class GATES:

    '''
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
        self.trigger()
                     # Any change in the input will trigger change in the
                     # output

    def _updateConnections(self, inputs):
        for i in inputs:
            if isinstance(i, Connector):
                i.tap(self, 'input')

    def setInputs(self, *inputs):
        # Clean Connections before updating new connections
        if len(inputs) < 2:
            raise Exception("ERROR: Too few inputs given")
        else:
            self.history_active = 1  # Use history before computing
            self.inputs = list(inputs)[:]  # Set the inputs
            self._updateConnections(self.inputs)
        self.trigger()
                     # Any change in the input will trigger change in the
                     # output

    def setInput(self, index, value):
        if index >= len(self.inputs):
            # If the index is more than the length then append to the list
            self.inputs.append(value)
            # Dont use history after a new input is added
            self.history_active = 0
            self._updateHistory()
                                # because history_active is set to 0 trigger
                                # will get called irrespective of the history.

        else:
            self.history_active = 1  # Use history before computing
            if isinstance(self.inputs[index], Connector):
                self.history_inputs[index] = self.inputs[index].state
            else:
                self.history_inputs[index] = self.inputs[
                    index]  # Modify the history
            self.inputs[index] = value
        if isinstance(value, Connector):
            value.tap(self, 'input')
        self.trigger()

    def getInputStates(self):
        input_states = []
        for i in self.inputs:
            if isinstance(i, Connector):
                input_states.append(i.state)
            else:
                input_states.append(i)
        return input_states

    def _updateResult(self, value):
        self.result = int(value)  # Set True or False
        if self.outputType == 1:
            self.outputConnector.state = self.result

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
        connector.tap(self, 'output')
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
                if i >= len(self.history_inputs) or self.history_inputs[i] != val1:
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
        if self._compareHistory():
            self.history_active = 1
            self._updateResult(True)
            self._updateHistory()  # Update the inputs after a computation
            for i in self.inputs:
                if (isinstance(i, Connector) and i.state == False) or (isinstance(i, GATES) and i.output() == False) or i == False:
                    self._updateResult(False)
                    break
            if self.outputType:
                self.outputConnector.trigger()


class OR(MIGATES):

    def __init__(self, *inputs):
        MIGATES.__init__(self, *inputs)

    def trigger(self):
        if self._compareHistory():
            self.history_active = 1
            self._updateResult(False)
            self._updateHistory()  # Update the inputs after a computation

            for i in self.inputs:
                if (isinstance(i, Connector) and i.state) or i:
                    self._updateResult(True)
                    break
            if self.outputType:
                self.outputConnector.trigger()


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
            self.history_active = 1  # Use history before computing
            self.inputs = list(inputs)[:]  # Set the inputs
            self._updateConnections(self.inputs)
        self.trigger()
                     # Any change in the input will trigger change in the
                     # output

    def setInput(self, value):
        self.setInputs(value)

    def trigger(self):
        if self._compareHistory():
            self.history_active = 1
            self._updateHistory()  # Update the inputs after a computation
            if (isinstance(self.inputs[0], Connector)):
                self._updateResult(not self.inputs[0].state)
            else:
                self._updateResult(not self.inputs[0])
            if self.outputType == 1:
                self.outputConnector.trigger()


class XOR(MIGATES):

    def __init__(self, *inputs):
        MIGATES.__init__(self, *inputs)

    def trigger(self):
        if self._compareHistory():
            self.history_active = 1
            self._updateResult(True)
            self._updateHistory()  # Update the inputs after a computation
            temp = 1
            for i in self.inputs:
                if isinstance(i, Connector):
                    val = i.state
                else:
                    val = i
                temp = temp ^ val
            temp = temp ^ 1
            self._updateResult(temp)
            if self.outputType:
                self.outputConnector.trigger()


class XNOR(MIGATES):

    def __init__(self, *inputs):
        MIGATES.__init__(self, *inputs)

    def trigger(self):
        if self._compareHistory():
            self.history_active = 1
            self._updateResult(True)
            self._updateHistory()  # Update the inputs after a computation
            temp = 1
            for i in self.inputs:
                if (isinstance(i, Connector)):
                    val = i.state
                else:
                    val = i
                temp = temp ^ val
            temp = temp ^ 1
            self._updateResult(not temp)
            if self.outputType:
                self.outputConnector.trigger()


class NAND(MIGATES):

    def __init__(self, *inputs):
        MIGATES.__init__(self, *inputs)

    def trigger(self):
        if self._compareHistory():
            self.history_active = 1
            self._updateResult(False)
            self._updateHistory()  # Update the inputs after a computation
            for i in self.inputs:
                if (isinstance(i, Connector) and i.state == False) or i == False:
                    self._updateResult(True)
                    break
            if self.outputType:
                self.outputConnector.trigger()


class NOR(MIGATES):

    def __init__(self, *inputs):
        MIGATES.__init__(self, *inputs)

    def trigger(self):
        if self._compareHistory():
            self.history_active = 1
            self._updateResult(True)
            self._updateHistory()  # Update the inputs after a computation
            for i in self.inputs:
                if (isinstance(i, Connector) and i.state) or i:
                    self._updateResult(False)

            if self.outputType:
                self.outputConnector.trigger()
