from connector import *


class GATES:
        '''
        Takes in as input the connectors/values 0,1 or None of the inputs to the gate.
        Base Class implementing all common functions used by Logic Gates
        '''

        def __init__(self, inputs):

                #Clean Connections before updating new connections
                self.history_active = 0  # Ignore history for first computation
                self.outputType = 0  # 1->output goes to a connector class
                self.result = None  # To store the result
                self.outputConnector = None  # Valid only if outputType = 1
                self.inputs = inputs[:]  # Set the inputs
                self.history_inputs = []  # Save a copy of the inputs
                self._updateConnections(self.inputs)
                self._updateHistory()
                self.trigger()  # Any change in the input triggers change in the output

        def _updateConnections(self, inputs):
                ''' Called when a gate is created, it updates the connector's input_to list'''

                for i in inputs:
                        if isinstance(i, Connector):
                                i.tap(self, 'input')

        def setInput(self, index, value):
                '''Sets the value of an input at the specified index if the input.

                index - Starting from 0, the index of the input whose value is to be set
                value - The value to be assigned (can be 0,1 or None)
                Exception is raised if an input which is not present is tried to be set.
                Exception is raised if the output of a logic object is tried to be set
                '''

                if index >= len(self.inputs) or index < 0:
                        raise Exception("ERROR: Index value greater than number of inputs to the gate")
                if isinstance(self.inputs[index], Connector):
                        if len(self.inputs[index].output_of) != 0:
                                raise Exception("ERROR: Tried to assign a value to a connector class")
                        self.inputs[index].state = value
                        self.inputs[index].trigger()
                else:
                        self.inputs[index] = value
                        self.trigger()

        def setInputs(self, *inputs_list):
                ''' Take in as argument ALL the input values in the same order as input connections of a Gate.
                An exception is raised if the lengths of the list does not agree with the number of inputs to the Gate.
                The value of 0, 1 or None can be assigned to an input connection if it is not an output of any other logic object.
                If it is an output of any logic object, one HAS to provide the corresponding element in the list as '~'
                Else an exception will be raised.
                '~' can also be used if one does not want to change value of an input.
                Eg. of valid list input: ['~',1,0,'~',0,'~'] if 0th, 3rd and 5th inputs cannot/should not be changed.'''
                
                if len(inputs_list) != len(self.inputs):
                        raise Exception("ERROR: Given number of inputs does not match with the number of inputs of the gate")

                self.history_active = 1  # Use history before computing
                for index in range(len(inputs_list)):
                        if inputs_list[index] == '~':
                                pass
                        else:
                                if isinstance(self.inputs[index], Connector):
                                        if len(self.inputs[index].output_of) != 0:
                                                raise Exception("ERROR: Tried to assign a value to a connector class")
                                        self.inputs[index].state = inputs_list[index]
                                        self.inputs[index].trigger()
                                else:
                                        self.inputs[index] = inputs_list[index]
                                        self.trigger()

        def getInputStates(self):
                '''Returns a list of the current input values of the gate.'''
                input_states = []
                for index in range(len(self.inputs)):
                        if isinstance(self.inputs[index], Connector):
                                input_states.append(self.inputs[index].state)
                        else:
                                input_states.append(self.inputs[index])
                return input_states

        def _updateResult(self):
                '''Updates the output connector and checks for Logic Contention.
                Displays a warning if there is a contention but still updates the wire.'''

                if self.outputType == 1:
                        if (len(self.outputConnector.output_of) == 1):
                                self.outputConnector.owner = self #updates owner during first update
                        else:
                                # if the current object is not the owner and there is an owner
                                #and the connector is not having a value of None, there is a contention
                                if (self.outputConnector.owner != self and\
                                    self.outputConnector.owner is not None\
                                    and self.result is not None):
                                        print('WARNING: Logic Contention detected')
                                #the owner is not updated if the connector has a value of None
                                if (self.outputConnector.owner != self and self.result is None):
                                        return
                        # if connector value is None, there is no owner
                        if (self.outputConnector.state is None):
                                self.outputConnector.owner = None
                        self.outputConnector.state = self.result  # updates the connector

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
                ''' Takes in a connector as a input and assigns it as the output of a gate.'''

                if not isinstance(connector, Connector):
                        raise Exception("ERROR: Expecting a Connector Class Object")
                        return None
                connector.tap(self, 'output')
                self.outputType = 1
                self.outputConnector = connector
                self.history_active = 0
                self.trigger()

        def output(self):
                '''Returns the output of the gate.'''

                self.trigger()
                return self.result

        def _compareHistory(self):

                if self.history_active == 1:  # Only check history if it is active
                        for i in range(len(self.inputs)):
                                if isinstance(self.inputs[i], Connector):
                                        val1 = self.inputs[i].state
                                else:
                                        val1 = self.inputs[i]

                                if self.history_inputs[i] != val1:
                                        return True
                        return False
                return True


class AND(GATES):
        '''A n-input AND Gate object. (n > 2)
        Input values can be 0, 1 or None.'''

        def __init__(self, *inputs):

                if len(inputs) < 2:
                        raise Exception("ERROR: Too few inputs given")
                        return None

                else:
                        GATES.__init__(self, list(inputs))

        def trigger(self):

                if self._compareHistory() is True:
                        self.history_active = 1
                        self.result = True

                        for i in self.inputs:
                                if (isinstance(i, Connector) and (not i.state and i.state != None)) or (not i and i != None):
                                        self.result = False
                                        break
                        self._updateHistory()  # Update the inputs after a computation
                        self._updateResult()

                        if self.outputType:
                                self.outputConnector.trigger()


class OR(GATES):
        '''A n-input OR Gate object. (n > 2)
        Input values can be 0, 1 or None.'''

        def __init__(self, *inputs):

                if len(inputs) < 2:
                        raise Exception("ERROR: Too few inputs given")
                        return None
                else:
                        GATES.__init__(self, list(inputs))

        def trigger(self):

                if self._compareHistory() is True:
                        self.history_active = 1
                        self.result = False
                        self._updateHistory()  # Update the inputs after a computation

                        for i in self.inputs:
                                if (isinstance(i, Connector) and (i.state or i.state == None)) or (i or i == None):
                                        self.result = True
                                        break

                        self._updateResult()

                        if self.outputType:
                                self.outputConnector.trigger()


class NOT(GATES):
        '''A single input NOT Gate object.
        Input values can be 0, 1 or None.'''

        def __init__(self, *inputs):

                if len(inputs) != 1:
                        raise Exception("ERROR: NOT Gates take only one input")
                        return None

                else:
                        GATES.__init__(self, list(inputs))

        def trigger(self):
                if self._compareHistory() is True:
                        self.history_active = 1
                        self._updateHistory()  # Update the inputs after a computation
                        if (isinstance(self.inputs[0], Connector)):
                                self.result = (not self.inputs[0].state) and (self.inputs[0].state != None)
                        else:
                                self.result = (not self.inputs[0]) and (self.inputs[0] != None)
                        self._updateResult()

                        if self.outputType:
                                self.outputConnector.trigger()


class BUFFER(GATES):
        '''A single input Buffer Gate object
        Assumes that the first argument is an input to the gate and the second one is the enable input of the buffer.
        Input values can be 0, 1 or None.'''

        def __init__(self, *inputs):

                if len(inputs) != 2:
                        raise Exception("ERROR: BUFFER Gates take only two inputs - Input and Enable")
                        return None
                else:
                        GATES.__init__(self, list(inputs))

        def trigger(self):

                if self._compareHistory() is True:
                        self.history_active = 1
                        self.result = None
                        self._updateHistory()  # Update the inputs after a computation
                        if (isinstance(self.inputs[1], Connector) and self.inputs[1].state == 1):
                                self.result = not not self.inputs[0].state
                        elif (not isinstance(self.inputs[1], Connector) and self.inputs[1]):
                                self.result = not not self.inputs[0]
                        self._updateResult()
                        if self.outputType:
                                self.outputConnector.trigger()


class XOR(GATES):
        '''A n-input XOR Gate object. (n > 2)
        Input values can be 0, 1 or None.'''
        
        def __init__(self, *inputs):

                if len(inputs) < 2:
                        raise Exception("ERROR: Too few inputs given")
                        return None

                else:
                        GATES.__init__(self, list(inputs))

        def trigger(self):

                if self._compareHistory() is True:
                        self.history_active = 1
                        self._updateHistory()  # Update the inputs after a computation

                        temp = 1

                        for i in self.inputs:
                                if isinstance(i, Connector):
                                        temp = temp ^ (i.state or i.state == None)
                                else:
                                        temp = temp ^ (i or i == None)
                        temp = temp ^1
                        self.result = temp
                        self._updateResult()

                        if self.outputType:
                                self.outputConnector.trigger()


class XNOR(GATES):
        '''A n-input XNOR Gate object. (n > 2)
        Input values can be 0, 1 or None.'''
        
        def __init__(self, *inputs):

                if len(inputs) < 2:
                        raise Exception("ERROR: Too few inputs given")
                        return None

                else:
                        GATES.__init__(self, list(inputs))

        def trigger(self):

                if self._compareHistory() is True:
                        self.history_active = 1
                        self._updateHistory()  # Update the inputs after a computation
                        temp = 1
                        for i in self.inputs:
                                if isinstance(i, Connector):
                                        temp = temp ^ (i.state or i.state == None)
                                else:
                                        temp = temp ^ (i or i == None)
                        temp = temp^1
                        self.result = (not temp)
                        self._updateResult()

                        if self.outputType:
                                self.outputConnector.trigger()


class NAND(GATES):
        '''A n-input NAND Gate object. (n > 2)
        Input values can be 0, 1 or None.'''
        
        def __init__(self, *inputs):

                if len(inputs) < 2:
                        raise Exception("ERROR: Too few inputs given")
                        return None

                else:
                        GATES.__init__(self, list(inputs))

        def trigger(self):

                if self._compareHistory() is True:
                        self.history_active = 1
                        self.result = False
                        self._updateHistory()  # Update the inputs after a computation

                        for i in self.inputs:
                                if (isinstance(i, Connector) and (not i.state and i.state != None)) or (not i and i != None):
                                        self.result = True
                                        break

                        self._updateResult()
                        if self.outputType:
                                self.outputConnector.trigger()


class NOR(GATES):
        '''A n-input NOR Gate object. (n > 2)
        Input values can be 0, 1 or None.'''
        
        def __init__(self, *inputs):

                if len(inputs) < 2:
                        raise Exception("ERROR: Too few inputs given")
                        return None

                else:
                        GATES.__init__(self, list(inputs))

        def trigger(self):

                if self._compareHistory() is True:
                        self.history_active = 1
                        self.result = True
                        self._updateHistory()  # Update the inputs after a computation

                        for i in self.inputs:
                                if (isinstance(i, Connector) and (i.state or i.state == None)) or (i or i == None):
                                        self.result = False
                                        break
                        self._updateResult()

                        if self.outputType:
                                self.outputConnector.trigger()
