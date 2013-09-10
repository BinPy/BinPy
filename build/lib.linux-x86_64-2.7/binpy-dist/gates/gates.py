import sys

class Gates:
	'''
	This class gives access to all the basic logic gates
	'''
	def NOT(self, a):
		'''
		This method takes one input and returns its inverted value
		'''
		if a==True:
			return 0
		elif a==False:
			return 1
	
	def OR(self, *inputs):
		'''
		This method takes n>1 inputs and returns its OR
		'''
		if len(inputs)<2:
			sys.exit("ERROR: Number of inputs must be more than 1")
		for i in inputs:
			if i==True:
				return 1
		return 0

	def NOR(self, *inputs):
		'''
		This method takes n>1 inputs and returns its NOR
		'''
		if len(inputs)<2:
			sys.exit("ERROR: Number of inputs must be more than 1")
		for i in inputs:
			if i==True:
				return 0
		return 1
		
	def AND(self, *inputs):
		'''
		This method takes n>1 inputs and returns its AND
		'''
		if len(inputs)<2:
			sys.exit("ERROR: Number of inputs must be more than 1")
		for i in inputs:
			if i==False:
				return 0
		return 1
		
	def NAND(self, *inputs):
		'''
		This method takes n>1 inputs and returns its NAND
		'''
		if len(inputs)<2:
			sys.exit("ERROR: Number of inputs must be more than 1")
		for i in inputs:
			if i==False:
				return 1
		return 0
	
	def XOR(self, *inputs):
		'''
		This method takes n>1 inputs and returns its XOR
		'''
		if len(inputs)<2:
			sys.exit("ERROR: Number of inputs must be more than 1")
		elif len(inputs)==2:
			return inputs[0]^inputs[1]
		else:
			last_out = inputs[0]
			for i in range(1,len(inputs)):
				 last_out =  self.XOR(last_out,inputs[i])
			if last_out==True:
				return 1
			else:
				return 0
					
	def XNOR(self, *inputs):
		'''
		This method takes n>1 inputs and returns its XNOR
		'''
		if len(inputs)<2:
			sys.exit("ERROR: Number of inputs must be more than 1")
		elif len(inputs)==2:
			return inputs[0]^inputs[1]
		else:
			last_out = inputs[0]
			for i in range(1,len(inputs)):
				 last_out =  self.XOR(last_out,inputs[i])
			if last_out==True:
				return 0
			else:
				return 1

