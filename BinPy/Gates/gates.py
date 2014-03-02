from connector import *

class GATES:
	'''
	Base Class implementing all common functions used by Logic Gates
	'''

	def __init__(self,inputs):

		#Clean Connections before updating new connections
		self.history_active = 0 # Ignore history for first computation
		self.outputType = 0 # 1->output goes to a connector class
		self.result = 0 #To store the result
		self.outputConnector = None #Valid only if outputType = 1
		self.inputs = inputs[:] # Set the inputs
		self.history_inputs = [] # Save a copy of the inputs
		self._updateConnections(self.inputs)
		self._updateHistory()

		self.trigger() # Any change in the input will trigger change in the output
	
	def _updateConnections(self,inputs):

		for i in inputs:
			if isinstance(i,Connector):
				i.tap(self,'input')

        def setInput(self, index, value):
                '''Sets the value of an input at the specified index if the input.

                index - Starting from zero, the index of the input whose value is to be set.
                value - The value to be assigned (can be 0,1 or None)
                Exception is raised if an input which is not present is tried to be set.
                Exception is raised if the output of a logic object is tried to be set.'''

                if index >= len(self.inputs) or index < 0:
                        raise Exception("ERROR: Index value greater than number of inputs to the gate")
                if len(self.inputs[index].output_of) != 0:
                        raise Exception("ERROR: Tried to assign a value to a connector class")
                if isinstance(self.input[index], Connector):
                        self.inputs[index].state = inputs_list[index]
                        self.inputs[index].trigger()
                else:
                        self.inputs[index] = inputs_list[index]
                        self.trigger()


	def setInputs(self, inputs_list):
                ''' Takes a LIST of input values and assigns it to the corresponding inputs of a Gate.
                An exception is raised if the lengths of the list does not agree with the number of inputs to the Gate.
                The value of 0, 1 or None can be assigned to an input connection if it is not an output of any other logic object.
                If it is an output of any logic object, one HAS to provide the corresponding element in the list as '~'
                Else an exception will be raised.
                '~' can also be used if one does not want to change value of an input.
                Eg. of valid list input: ['~',1,0,'~',0,'~'] if 0th, 3rd and 5th inputs cannot/should not be changed.'''

                if len(inputs_list) != len(self.inputs):
                        raise Exception("ERROR: Given number of inputs does not match with the number of inputs of the gate")

                self.history_active = 1 #Use history before computing
                for index in range(len(inputs_list)):
                        if inputs_list[index] == '~':
                                pass
                        else:
##                              self.history_inputs[index] = self.inputs[index]
                                if len(self.inputs[index].output_of) != 0:
                                        raise Exception("ERROR: Tried to assign a value to a connector class")
                                if isinstance(self.input[index], Connector):
                                        self.inputs[index].state = inputs_list[index]
                                        self.inputs[index].trigger()
                                else:
                                        self.inputs[index] = inputs_list[index]
                                        self.trigger()
                        

	def getInputStates(self):
                input_states = []
                for i in self.inputs:
                        if isinstance(i, Connector):
                                input_states.append(self.inputs[i].state)
                        else:
                                input_states.append(self.inputs[i])
		return input_states

	def _updateResult(self):
		
		#self.result = int(value) 
		if self.outputType == 1:
                        if outputConnector.state != None #if the connector was not having a value of None
                                print('WARNING: Logic Contention detected') #then the new output would mean a contention
			self.outputConnector.state = self.result #the connector would however be loaded with this result of this gate

	def _updateHistory(self):

		for i in range(len(self.inputs)):
			if isinstance(self.inputs[i],Connector):
				val1 = self.inputs[i].state
			else:
				val1 = self.inputs[i]

			if len(self.history_inputs) <= i:
				self.history_inputs.append(val1)
			else:
				self.history_inputs[i] = val1

	def setOutput(self, value):

		if not isinstance(value,Connector):
			raise Exception("ERROR: Expecting a Connector Class Object")
			return None
		value.tap(self,'output')
		self.outputType = 1
		self.outputConnector = value
		self.history_active = 0
		self.trigger()

	def output(self):
		
		self.trigger()
		return self.result

	def _compareHistory(self):

		if self.history_active == 1: # Only check history if it is active
			for i in range(len(self.inputs)):
				if isinstance(self.inputs[i],Connector):
					val1 = self.inputs[i].state
				else:
					val1 = self.inputs[i]

				if self.history_inputs[i] != val1:
					return True
			return False
		return True

class AND(GATES):

	def __init__(self,*inputs):

		if len(inputs) < 2:
			raise Exception("ERROR: Too few inputs given")
			return None

		else:
			GATES.__init__(self,list(inputs))

	def trigger(self):

		if self._compareHistory() == True:
			self.history_active = 1
			self.result = True
			self._updateHistory() # Update the inputs after a computation

			for i in self.inputs:
				if (isinstance(i,Connector) and i.state == False) or i == False:
					self.result = False
					break

			self._updateResult()

			if self.outputType:
				self.outputConnector.trigger()

class OR(GATES):

	def __init__(self,*inputs):

		if len(inputs) < 2:
			raise Exception("ERROR: Too few inputs given")
			return None

		else:
			GATES.__init__(self,list(inputs))

	def trigger(self):

		if self._compareHistory() == True:
			self.history_active = 1
			self.result = False
			self._updateHistory() # Update the inputs after a computation
			
			for i in self.inputs:
				if (isinstance(i,Connector) and i.state == True) or i == True:
					self.result = True
					break

			self._updateResult()

			if self.outputType:
				self.outputConnector.trigger()

class NOT(GATES):

	def __init__(self,*inputs):

		if len(inputs) != 1:
			raise Exception("ERROR: NOT Gates take only one input")
			return None

		else:
			GATES.__init__(self,list(inputs))

	def trigger(self):

		if self._compareHistory() == True:
			self.history_active = 1
			#self._updateResult(True)
			self._updateHistory() # Update the inputs after a computation
			self.result = not self.inputs[0]
			self._updateResult()

			if self.outputType:
				self.outputConnector.trigger()

class BUFFER(GATES):
        ''' Assumes that the first argument is an input to the gate and
        the second one is the enable input of the buffer.'''

	def __init__(self,*inputs):

		if len(inputs) != 2:
			raise Exception("ERROR: BUFFER Gates take only two inputs - Input and Enable")
			return None

		else:
			GATES.__init__(self,list(inputs))

	def trigger(self):

		if self._compareHistory() == True:
			self.history_active = 1
			self.result = None
			self._updateHistory() # Update the inputs after a computation
			if inputs[1] == True
                                self.result = inputs[0]
			self._updateResult()

			if self.outputType:
				self.outputConnector.trigger()


class XOR(GATES):

	def __init__(self,*inputs):

		if len(inputs) < 2:
			raise Exception("ERROR: Too few inputs given")
			return None

		else:
			GATES.__init__(self,list(inputs))

	def trigger(self):

		if self._compareHistory() == True:
			self.history_active = 1
			#self._updateResult(True)
			self._updateHistory() # Update the inputs after a computation
			
			temp = self.inputs[0]

			for i in self.inputs[1:]:
				temp = temp ^ i

                        self.result = temp
			self._updateResult()

			if self.outputType:
				self.outputConnector.trigger()

class XNOR(GATES):

	def __init__(self,*inputs):

		if len(inputs) < 2:
			raise Exception("ERROR: Too few inputs given")
			return None

		else:
			GATES.__init__(self,list(inputs))

	def trigger(self):

		if self._compareHistory() == True:
			self.history_active = 1
			#self._updateResult(True)
			self._updateHistory() # Update the inputs after a computation
			
			temp = self.inputs[0]

			for i in self.inputs[1:]:
				temp = temp ^ i

                        self.result = (not temp)
			self._updateResult()

			if self.outputType:
				self.outputConnector.trigger()

class NAND(GATES):

	def __init__(self,*inputs):

		if len(inputs) < 2:
			raise Exception("ERROR: Too few inputs given")
			return None

		else:
			GATES.__init__(self,list(inputs))

	def trigger(self):

		if self._compareHistory() == True:
			self.history_active = 1
			self.result = False
			self._updateHistory() # Update the inputs after a computation
			
			#temp = self.inputs[0]

			#self._updateResult(False)

			for i in self.inputs:
				if (isinstance(i,Connector) and i.state == False) or i == False:
					self.result=True
					break
				
                        self._updateResult()
			if self.outputType:
				self.outputConnector.trigger()

class NOR(GATES):

	def __init__(self,*inputs):

		if len(inputs) < 2:
			raise Exception("ERROR: Too few inputs given")
			return None

		else:
			GATES.__init__(self,list(inputs))

	def trigger(self):

		if self._compareHistory() == True:
			self.history_active = 1
			self.result = True
			self._updateHistory() # Update the inputs after a computation
			
			#self._updateResult(True)

			for i in self.inputs:
				if (isinstance(i,Connector) and i.state == True) or i == True:
					self.result = False
					break
                        self._updateResult()

			if self.outputType:
				self.outputConnector.trigger()
