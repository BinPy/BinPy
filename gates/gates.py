import sys

class Gates:
	'''
	This class gives access to all the basic logic gates
	'''
	def NOT(self, a):
		return not a
	
	def OR(self, *inputs):
		if len(inputs)<2:
			sys.exit("ERROR: Number of inputs must be more than 1")
		for i in inputs:
			if i==True:
				return True
		return False

	def NOR(self, *inputs):
		if len(inputs)<2:
			sys.exit("ERROR: Number of inputs must be more than 1")
		for i in inputs:
			if i==True:
				return False
		return True
		
	def AND(self, *inputs):
		if len(inputs)<2:
			sys.exit("ERROR: Number of inputs must be more than 1")
		for i in inputs:
			if i==False:
				return False
		return True
		
	def NAND(self, *inputs):
		if len(inputs)<2:
			sys.exit("ERROR: Number of inputs must be more than 1")
		for i in inputs:
			if i==False:
				return True
		return False
	
	def XOR(self, *inputs):
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
