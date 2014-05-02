"""
Contains
========

* GATES(Base class for all the gates)
* MIGATES(Base class for multiple input gates inherits GATES)
* AND
* OR
* NOT
* XOR
* XNOR
* NAND
* NOR
"""


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
        """
        This method sets multiple inputs of the gate at a time.
        You can also use setInput() multiple times with different index
        to add multiple inputs to the gate.
        """

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
        """
        This method is used to add input to a gate.
        It requires an index and a value/connector object to add
        an input to the gate.
        """

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
        """
        This method returns the input states of the gate
        """

        input_states = []
        for i in self.inputs:
            if isinstance(i, Connector):
                input_states.append(i.state)
            else:
                input_states.append(i)
        return input_states

    def _updateResult(self, value):
        if value is None:
            self.result = None
        else:
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
        """
        This method sets the output of the gate. It connects
        the passed connector to its output.
        """

        if not isinstance(connector, Connector):
            raise Exception("ERROR: Expecting a Connector Class Object")
        connector.tap(self, 'output')
        self.outputType = 1
        self.outputConnector = connector
        self.history_active = 0
        self.trigger()

    def output(self):
        """
        This methods returns the output of the gate.
        """

        self.trigger()
        return self.result

    def __repr__(self):
        '''
        Simple way to do 'print g', where g would be an instance of any gate
        class. Functions returns the result of self.output() as a string.
        '''

        return str(self.output())

    def buildStr(self, gate_name):
        '''
        Returns a string representation of a gate, where gate_name is the class
        name For example, for an AND gate with two inputs the resulting string
        would be: 'AND Gate; Output: 0; Inputs: [0, 1];'
        '''

        return gate_name + " Gate; Output: " + \
            str(self.output()) + "; Inputs: " + \
            str(self.getInputStates()) + ";"

    def _compareHistory(self):
        if self.history_active == 1:  # Only check history if it is active
            for i in range(len(self.inputs)):
                if isinstance(self.inputs[i], Connector):
                    val1 = self.inputs[i].state
                else:
                    val1 = self.inputs[i]
                if i >= len(self.history_inputs) or self.history_inputs[i]\
                        != val1:
                    return True
            return False
        return True


class MIGATES(GATES):

    """
    This class makes GATES compatible with multiple inputs.
    """

    def __init__(self, *inputs):
        if len(inputs) < 2:
            raise Exception(
                "ERROR: Too few inputs given. Needs at least 2 or\
                 more inputs.")

        GATES.__init__(self, list(inputs))


class AND(MIGATES):

    """
    This class implements AND gate

    Examples
    ========

    >>> from BinPy import *
    >>> gate = AND(0, 1)
    >>> gate.output()
    0
    >>> gate.setInputs(1, 1, 1, 1)
    >>> gate.output()
    1
    >>> conn = Connector()
    >>> gate.setOutput(conn)
    >>> gate2 = AND(conn, 1)
    >>> gate2.output()
    1
    """

    def __init__(self, *inputs):
        MIGATES.__init__(self, *inputs)

    def trigger(self):
        if self._compareHistory():
            self.history_active = 1
            self._updateResult(True)
            self._updateHistory()  # Update the inputs after a computation
            val = True
            for i in self.inputs:
                if (isinstance(i, Connector)):
                    val = val and i.state
                elif (isinstance(i, GATES)):
                    val = val and i.output()
                else:
                    val = val and i

            self._updateResult(val)
            if self.outputType:
                self.outputConnector.trigger()

    def __str__(self):
        return self.buildStr("AND")


class OR(MIGATES):

    """
    This class implements OR gate

    Examples
    ========

    >>> from BinPy import *
    >>> gate = OR(0, 1)
    >>> gate.output()
    1
    >>> gate.setInputs(0, 0, 0, 0)
    >>> gate.output()
    0
    >>> conn = Connector()
    >>> gate.setOutput(conn)
    >>> gate2 = AND(conn, 1)
    >>> gate2.output()
    0
    """

    def __init__(self, *inputs):
        MIGATES.__init__(self, *inputs)

    def trigger(self):
        if self._compareHistory():
            self.history_active = 1
            self._updateResult(False)
            self._updateHistory()  # Update the inputs after a computation
            val = False
            for i in self.inputs:
                if (isinstance(i, Connector)):
                    val = val or i.state
                elif (isinstance(i, GATES)):
                    val = val or i.output()
                else:
                    val = val or i

            self._updateResult(val)
            if self.outputType:
                self.outputConnector.trigger()

    def __str__(self):
        return self.buildStr("OR")


class NOT(GATES):

    """
    This class implements NOT gate

    Examples
    ========

    >>> from BinPy import *
    >>> gate = NOT(0)
    >>> gate.output()
    1
    >>> conn = Connector()
    >>> gate.setOutput(conn)
    >>> gate2 = AND(conn, 1)
    >>> gate2.output()
    1
    """

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
            elif (isinstance(self.inputs[0], GATES)):
                self._updateResult(not self.inputs[0].output())
            else:
                self._updateResult(not self.inputs[0])
            if self.outputType == 1:
                self.outputConnector.trigger()

    def __str__(self):
        return self.buildStr("NOT")


class XOR(MIGATES):

    """
    This class implements XOR gate

    Examples
    ========

    >>> from BinPy import *
    >>> gate = XOR(0, 1)
    >>> gate.output()
    1
    >>> gate.setInputs(1, 0, 1, 0)
    >>> gate.output()
    0
    >>> conn = Connector()
    >>> gate.setOutput(conn)
    >>> gate2 = AND(conn, 1)
    >>> gate2.output()
    0
    """

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
                elif isinstance(i, GATES):
                    val = i.output()
                else:
                    val = i
                temp = (temp and not val) or (not temp and val)
            temp = (temp and not 1) or (not temp and 1)
            self._updateResult(temp)
            if self.outputType:
                self.outputConnector.trigger()

    def __str__(self):
        return self.buildStr("XOR")


class XNOR(MIGATES):

    """
    This class implements XNOR gate

    Examples
    ========

    >>> from BinPy import *
    >>> gate = XNOR(0, 1)
    >>> gate.output()
    0
    >>> gate.setInputs(1, 0, 1, 0)
    >>> gate.output()
    1
    >>> conn = Connector()
    >>> gate.setOutput(conn)
    >>> gate2 = AND(conn, 1)
    >>> gate2.output()
    1
    """

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
                elif isinstance(i, GATES):
                    val = i.output()
                else:
                    val = i
                temp = (temp and not val) or (not temp and val)
            temp = (temp and not 1) or (not temp and 1)
            self._updateResult(not temp)
            if self.outputType:
                self.outputConnector.trigger()

    def __str__(self):
        return self.buildStr("XNOR")


class NAND(MIGATES):

    """
    This class implements NAND gate

    Examples
    ========

    >>> from BinPy import *
    >>> gate = NAND(0, 1)
    >>> gate.output()
    1
    """

    def __init__(self, *inputs):
        MIGATES.__init__(self, *inputs)

    def trigger(self):
        if self._compareHistory():
            self.history_active = 1
            self._updateResult(False)
            self._updateHistory()  # Update the inputs after a computation
            val = True
            for i in self.inputs:
                if (isinstance(i, Connector)):
                    val = val and i.state

                elif (isinstance(i, GATES)):
                    val = val and i.output()
                else:
                    val = val and i

            self._updateResult(not val)
            if self.outputType:
                self.outputConnector.trigger()

    def __str__(self):
        return self.buildStr("NAND")


class NOR(MIGATES):

    """
    This class implements NOR gate

    Examples
    ========

    >>> from BinPy import *
    >>> gate = NOR(0, 1)
    >>> gate.output()
    0
    """

    def __init__(self, *inputs):
        MIGATES.__init__(self, *inputs)

    def trigger(self):
        if self._compareHistory():
            self.history_active = 1
            self._updateResult(True)
            self._updateHistory()  # Update the inputs after a computation
            val = False
            for i in self.inputs:
                if (isinstance(i, Connector)):
                    val = val or i.state
                elif (isinstance(i, GATES)):
                    val = val or i.output()
                else:
                    val = val or i

            self._updateResult(not val)

            if self.outputType:
                self.outputConnector.trigger()

    def __str__(self):
        return self.buildStr("NOR")
