from connector import *

class GATES:
	'''
	Base Class implementing all common functions used by Logic Gates
	'''

	inputs = [] #To store the list of inputs given to the gate
	history_inputs = [] # To store the last set of inputs
	history_active = 0 # Ignore history for first computation
	outputType = 0 # 1->output goes to a connector class
	result = 0 #To store the result
	outputConnector = None #Valid only is outputType = 1

	def __init__(self,inputs):

		#Clean Connections before updating new connections
		self.inputs = inputs # Set the inputs
		self.history_inputs = inputs[:] # Save a copy of the inputs
		self.__updateConnections(self.inputs)

		self.trigger() # Any change in the input will trigger change in the output
	
	def __updateConnections(self,inputs):

		for i in inputs:
			if isinstance(i,Connector):
				i.tap(self,'input')

		self.trigger()

	def setInputs(self,*inputs):

		#Clean Connections before updating new connections
		if len(inputs) < 2:
			raise Exception("ERROR: Too few inputs given")
			return None

		else:
			self.history_active = 1 #Use history before computing
			self.inputs = list(inputs) # Set the inputs
			self.__updateConnections(self.inputs)

		self.trigger() # Any change in the input will trigger change in the output

	def setInput(self,index,value):

		if index > len(self.inputs):
			self.history_inputs.append(value)
			self.inputs.append(value) #If the index is more than the length then append to the list
			self.history_active = 0 # Dont use history after a new input is added

		else:
			self.history_active = 1 # Use history before computing
			self.history_inputs[index] = self.inputs[index] # Modify the history
			self.inputs[index] = value

		if isinstance(value,Connector):
			value.tap(self,'input')

		self.trigger()

	def inputs(self):

		return self.inputs

	def _updateResult(self,value):
		
		self.result = int(value) #Set True or False
		if self.outputType == 1:
			self.outputConnector.state = self.result

	def setOutput(self, value):

		if not isinstance(value,Connector):
			raise Exception("ERROR: Expecting a Connector Class Object")
			return None
		value.tap(self,'output')
		self.outputType = 1
		self.outputConnector = value
		self.trigger()

	def output(self):
		
		self.trigger()
		return self.result

	def _compareHistory(self):

		if self.history_active == 1: # Only check history if it is active
			for i,j in zip(self.history_inputs, self.inputs):
				if isinstance(i,Connector) and isinstance(j,Connector):
					if i.state != j.state:
						return True
				elif isinstance(i,Connector) or isinstance(j,Connector):
					return True
				elif i != j:
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
			self._updateResult(True)
			self.history_inputs = self.inputs[:] # Update the inputs after a computation

			for i in self.inputs:
				if (isinstance(i,Connector) and i.state == False) or i == False:
					self._updateResult(False)

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
			self._updateResult(True)
			self.history_inputs = self.inputs[:] # Update the inputs after a computation
			
			for i in self.inputs:
				if (isinstance(i,Connector) and i.state == True) or i == True:
					self._updateResult(True)

			if self.outputType:
				self.outputConnector.trigger()

class NOT(GATES):

	def __init__(self,*inputs):

		if len(inputs) != 1:
			raise Exception("ERROR: NOT Gates takes only one input")
			return None

		else:
			GATES.__init__(self,list(inputs))

	def trigger(self):

		if self._compareHistory() == True:
			self.history_active = 1
			self._updateResult(True)
			self.history_inputs = self.inputs[:] # Update the inputs after a computation
			
			self._updateResult( not self.inputs[0] )

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
			self._updateResult(True)
			self.history_inputs = self.inputs[:] # Update the inputs after a computation
			
			temp = self.inputs[0]

			for i in self.inputs[1:]:
				temp = temp ^ i

			self._updateResult(temp)

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
			self._updateResult(True)
			self.history_inputs = self.inputs[:] # Update the inputs after a computation
			
			temp = self.inputs[0]

			for i in self.inputs[1:]:
				temp = temp ^ i

			self._updateResult( not temp)

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
			self._updateResult(True)
			self.history_inputs = self.inputs[:] # Update the inputs after a computation
			
			temp = self.inputs[0]

			self._updateResult(False)

			for i in self.inputs:
				if (isinstance(i,Connector) and i.state == False) or i == False:
					self._updateResult(True)

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
			self._updateResult(True)
			self.history_inputs = self.inputs[:] # Update the inputs after a computation
			
			self._updateResult(True)

			for i in self.inputs:
				if (isinstance(i,Connector) and i.state == True) or i == True:
					self._updateResult(False)

			if self.outputType:
				self.outputConnector.trigger()
