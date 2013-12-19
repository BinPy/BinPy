
class Gates:
	"""
	This class gives access to all the basic logic gates
	"""

	@staticmethod
	def NOT(a):
		"""
		This method takes one input and returns its inverted value
		"""
		if a==True:
			return 0
		elif a==False:
			return 1

	@staticmethod
	def OR(*inputs):
		"""
		This method takes n>1 inputs and returns its OR
		"""
		if len(inputs)<2:
			raise ValueError("Number of inputs must be more than one")
		for i in inputs:
			if i==True:
				return 1
		return 0

	@staticmethod
	def NOR(*inputs):
		"""
		This method takes n>1 inputs and returns its NOR
		"""
		return Gates.NOT(Gates.OR(*inputs))

	@staticmethod	
	def AND(*inputs):
		"""
		This method takes n>1 inputs and returns its AND
		"""
		
		if len(inputs)<2:
			raise ValueError("Number of inputs must be more than one")
		for i in inputs:
			if i==False:
				return 0
		return 1

	@staticmethod
	def NAND(*inputs):
                """
		This method takes n>1 inputs and returns its NAND
		"""
		return Gates.NOT(Gates.AND(*inputs))

	@staticmethod
	def XOR(*inputs):
		"""
		This method takes n>1 inputs and returns its XOR
		"""
		
		if len(inputs)<2:
			raise ValueError("Number of inputs must be more than one")
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

	@staticmethod				
	def XNOR(*inputs):
		"""
		This method takes n>1 inputs and returns its XNOR
		"""		
		return Gates.NOT(Gates.XOR(*inputs))
