"""
Contains
========

* GATES(Base class for all the gates)
* AND
* OR
* NOT
* XOR
* XNOR
* NAND
* NOR
"""


from BinPy.connectors.connector import *


class GATES:

    '''
    Base Class implementing all common functions used by Logic Gates
    '''

    def __init__(self, inputs):

        # Clean Connections before updating new connections
        self.history_active = 0  # Ignore history for first computation
        self.output_type = 0  # 1->output goes to a connector class
        self.result = None  # To store the result
        self.output_connector = None  # Valid only if output_type = 1
        self.inputs = inputs[:]  # Set the inputs
        self.history_inputs = []  # Save a copy of the inputs
        self._update_connections()
        self._update_history()
        self.trigger()
        # Any change in the input will trigger change in the
        # output

    def _update_connections(self):
        for i in self.inputs:
            if isinstance(i, Connector):
                i.tap(self, 'input')

    def set_inputs(self, *inputs):
        """
        This method sets multiple inputs of the gate at a time.
        You can also use set_input() multiple times with different index
        to add multiple inputs to the gate.
        """

        # Clean Connections before updating new connections
        if len(inputs) < 2:
            raise Exception("ERROR: Too few inputs given")
        else:
            self.history_active = 1  # Use history before computing
            self.inputs = list(inputs)[:]  # Set the inputs
            self._update_connections()
        self.trigger()
        # Any change in the input will trigger change in the
        # output

    def set_input(self, index, value):
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
            self._update_history()
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

    def get_input_states(self):
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

    def _update_result(self, value):
        if value is None:
            self.result = None
        else:
            self.result = int(value)  # Set True or False
        if self.output_type == 1:
            self.output_connector.state = self.result

    def _update_history(self):
        for i in range(len(self.inputs)):
            if isinstance(self.inputs[i], Connector):
                val1 = self.inputs[i].state
            else:
                val1 = self.inputs[i]
            if len(self.history_inputs) <= i:
                self.history_inputs.append(val1)
            else:
                self.history_inputs[i] = val1

    def set_output(self, connector):
        """
        This method sets the output of the gate. It connects
        the passed connector to its output.
        """

        if not isinstance(connector, Connector):
            raise Exception("ERROR: Expecting a Connector Class Object")
        connector.tap(self, 'output')
        self.output_type = 1
        self.output_connector = connector
        self.history_active = 0
        self.trigger()

    def reset_output(self):
        """
        The method resets the output of the gate. The output of the gate is not
        directed to any Connector Object
        """

        self.output_connector.untap(self, 'output')
        self.output_type = 0
        self.output_connector = None

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

    def build_str(self, gate_name):
        '''
        Returns a string representation of a gate, where gate_name is the class
        name For example, for an AND gate with two inputs the resulting string
        would be: 'AND Gate; Output: 0; Inputs: [0, 1];'
        '''

        return gate_name + " Gate; Output: " + \
            str(self.output()) + "; Inputs: " + \
            str(self.get_input_states()) + ";"

    def _compare_history(self):
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

    def add_input(self, value):
        """
        This method adds an input to an existing gate
        """

        self.history_active = 0  # Don't use history after adding an input
        self.inputs.append(value)
        self._update_connections()
        self._update_history()

    def remove_input(self, index):
        """
        This method removes an input whose index is passed
        """

        if len(self.inputs) - 1 < 2:
            raise Exception("ERROR: Too few inputs left after removing")

        if index > len(self.inputs):
            raise Exception("ERROR: Index value out of range")

        self.history_active = 0
        self.inputs.pop(index)
        self._update_connections()
        self._update_history()


class AND(MIGATES):

    """
    This class implements AND gate

    Examples
    ========

    >>> from BinPy import *
    >>> gate = AND(0, 1)
    >>> gate.output()
    0
    >>> gate.set_inputs(1, 1, 1, 1)
    >>> gate.output()
    1
    >>> conn = Connector()
    >>> gate.set_output(conn)
    >>> gate2 = AND(conn, 1)
    >>> gate2.output()
    1
    """

    def __init__(self, *inputs):
        MIGATES.__init__(self, *inputs)

    def trigger(self):
        if self._compare_history():
            self.history_active = 1
            self._update_result(True)
            self._update_history()  # Update the inputs after a computation
            val = True
            for i in self.inputs:
                if (isinstance(i, Connector)):
                    val = val and i.state
                elif (isinstance(i, GATES)):
                    val = val and i.output()
                else:
                    val = val and i

            self._update_result(val)
            if self.output_type:
                self.output_connector.trigger()

    def __str__(self):
        return self.build_str("AND")


class OR(MIGATES):

    """
    This class implements OR gate

    Examples
    ========

    >>> from BinPy import *
    >>> gate = OR(0, 1)
    >>> gate.output()
    1
    >>> gate.set_inputs(0, 0, 0, 0)
    >>> gate.output()
    0
    >>> conn = Connector()
    >>> gate.set_output(conn)
    >>> gate2 = AND(conn, 1)
    >>> gate2.output()
    0
    """

    def __init__(self, *inputs):
        MIGATES.__init__(self, *inputs)

    def trigger(self):
        if self._compare_history():
            self.history_active = 1
            self._update_result(False)
            self._update_history()  # Update the inputs after a computation
            val = False
            for i in self.inputs:
                if (isinstance(i, Connector)):
                    val = val or i.state
                elif (isinstance(i, GATES)):
                    val = val or i.output()
                else:
                    val = val or i

            self._update_result(val)
            if self.output_type:
                self.output_connector.trigger()

    def __str__(self):
        return self.build_str("OR")


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
    >>> gate.set_output(conn)
    >>> gate2 = AND(conn, 1)
    >>> gate2.output()
    1
    """

    def __init__(self, *inputs):
        if len(inputs) != 1:
            raise Exception("ERROR: NOT Gates takes only one input")
        else:
            GATES.__init__(self, list(inputs))

    def set_inputs(self, *inputs):
        # Clean Connections before updating new connections
        if len(inputs) != 1:
            raise Exception("ERROR: NOT Gates takes only one input")
        else:
            self.history_active = 1  # Use history before computing
            self.inputs = list(inputs)[:]  # Set the inputs
            self._update_connections()
        self.trigger()
        # Any change in the input will trigger change in the
        # output

    def set_input(self, value):
        self.set_inputs(value)

    def trigger(self):
        if self._compare_history():
            self.history_active = 1
            self._update_history()  # Update the inputs after a computation
            if (isinstance(self.inputs[0], Connector)):
                self._update_result(not self.inputs[0].state)
            elif (isinstance(self.inputs[0], GATES)):
                self._update_result(not self.inputs[0].output())
            else:
                self._update_result(not self.inputs[0])
            if self.output_type == 1:
                self.output_connector.trigger()

    def __str__(self):
        return self.build_str("NOT")


class XOR(MIGATES):

    """
    This class implements XOR gate

    Examples
    ========

    >>> from BinPy import *
    >>> gate = XOR(0, 1)
    >>> gate.output()
    1
    >>> gate.set_inputs(1, 0, 1, 0)
    >>> gate.output()
    0
    >>> conn = Connector()
    >>> gate.set_output(conn)
    >>> gate2 = AND(conn, 1)
    >>> gate2.output()
    0
    """

    def __init__(self, *inputs):
        MIGATES.__init__(self, *inputs)

    def trigger(self):
        if self._compare_history():
            self.history_active = 1
            self._update_result(True)
            self._update_history()  # Update the inputs after a computation
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
            self._update_result(temp)
            if self.output_type:
                self.output_connector.trigger()

    def __str__(self):
        return self.build_str("XOR")


class XNOR(MIGATES):

    """
    This class implements XNOR gate

    Examples
    ========

    >>> from BinPy import *
    >>> gate = XNOR(0, 1)
    >>> gate.output()
    0
    >>> gate.set_inputs(1, 0, 1, 0)
    >>> gate.output()
    1
    >>> conn = Connector()
    >>> gate.set_output(conn)
    >>> gate2 = AND(conn, 1)
    >>> gate2.output()
    1
    """

    def __init__(self, *inputs):
        MIGATES.__init__(self, *inputs)

    def trigger(self):
        if self._compare_history():
            self.history_active = 1
            self._update_result(True)
            self._update_history()  # Update the inputs after a computation
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
            self._update_result(not temp)
            if self.output_type:
                self.output_connector.trigger()

    def __str__(self):
        return self.build_str("XNOR")


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
        if self._compare_history():
            self.history_active = 1
            self._update_result(False)
            self._update_history()  # Update the inputs after a computation
            val = True
            for i in self.inputs:
                if (isinstance(i, Connector)):
                    val = val and i.state

                elif (isinstance(i, GATES)):
                    val = val and i.output()
                else:
                    val = val and i

            self._update_result(not val)
            if self.output_type:
                self.output_connector.trigger()

    def __str__(self):
        return self.build_str("NAND")


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
        if self._compare_history():
            self.history_active = 1
            self._update_result(True)
            self._update_history()  # Update the inputs after a computation
            val = False
            for i in self.inputs:
                if (isinstance(i, Connector)):
                    val = val or i.state
                elif (isinstance(i, GATES)):
                    val = val or i.output()
                else:
                    val = val or i

            self._update_result(not val)

            if self.output_type:
                self.output_connector.trigger()

    def __str__(self):
        return self.build_str("NOR")
