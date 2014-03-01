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
		self.__updateConnections(self.inputs)
		self._updateHistory()

		self.trigger() # Any change in the input will trigger change in the output
	
	def __updateConnections(self,inputs):

		for i in inputs:
			if isinstance(i,Connector):
				i.tap(self,'input')


	def setInputs(self,*inputs):

		#Clean Connections before updating new connections
		if len(inputs) < 2:
			raise Exception("ERROR: Too few inputs given")
			return None

		else:
			self.history_active = 1 #Use history before computing
			self.inputs = list(inputs)[:] # Set the inputs
			self.__updateConnections(self.inputs)

		self.trigger() # Any change in the input will trigger change in the output

	def setInput(self,index,value):

		if index > len(self.inputs):
			self.inputs.append(value) #If the index is more than the length then append to the list
			self.history_active = 0 # Dont use history after a new input is added
			self._updateHistory() # because history_active is set to 0 trigger will get called irrespective of the history.

		else:
			self.history_active = 1 # Use history before computing
			if isinstance(self.inputs[index],Connector):
				self.history_inputs[index]  = self.inputs[index].state
			else:
				self.history_inputs[index] = self.inputs[index] # Modify the history
			self.inputs[index] = value

		if isinstance(value,Connector):
			value.tap(self,'input')

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
