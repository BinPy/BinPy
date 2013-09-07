import sys

class Gates:
	'''
	This class gives access to all the basic logic gates
	'''
	def NOT(self, a):
		'''
		This method takes one input and returns its inverted value
		'''
		return not a
	
	def OR(self, *inputs):
		'''
		This method takes n>1 inputs and returns its OR
		'''
		if len(inputs)<2:
			sys.exit("ERROR: Number of inputs must be more than 1")
		for i in inputs:
			if i==True:
				return True
		return False

	def NOR(self, *inputs):
		'''
		This method takes n>1 inputs and returns its NOR
		'''
		if len(inputs)<2:
			sys.exit("ERROR: Number of inputs must be more than 1")
		for i in inputs:
			if i==True:
				return False
		return True
		
	def AND(self, *inputs):
		'''
		This method takes n>1 inputs and returns its AND
		'''
		if len(inputs)<2:
			sys.exit("ERROR: Number of inputs must be more than 1")
		for i in inputs:
			if i==False:
				return False
		return True
		
	def NAND(self, *inputs):
		'''
		This method takes n>1 inputs and returns its NAND
		'''
		if len(inputs)<2:
			sys.exit("ERROR: Number of inputs must be more than 1")
		for i in inputs:
			if i==False:
				return True
		return False
	
	def XOR(self, *inputs):
		'''
		This method takes n>1 inputs and returns its XOR
		'''
		if len(inputs)<2:
			sys.exit("ERROR: Number of inputs must be more than 1")
		false_count = 0
		for i in inputs:
			if i==False:
				false_count += 1
		if false_count%2!=0:
			return False
		else:
			return True	
			
	def XNOR(self, *inputs):
		'''
		This method takes n>1 inputs and returns its XNOR
		'''
		if len(inputs)<2:
			sys.exit("ERROR: Number of inputs must be more than 1")
		false_count = 0
		for i in inputs:
			if i==False:
				false_count += 1
		if false_count%2!=0:
			return True
		else:
			return False	
