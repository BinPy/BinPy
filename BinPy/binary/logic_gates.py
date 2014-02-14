
class Gates:
	'''
	This class gives access to all the basic logic gates
	'''
	def NOT(self, a):
		'''
		This method takes one input and returns its inverted value
		'''
		
		return int ( not a )
	
	def OR(self, *inputs):
		'''
		This method takes n>1 inputs and returns its OR
		'''
		
		if (isinstance(inputs[0],list) and len(inputs[0]) > 1) or len(inputs) > 1 :
			if isinstance(inputs[0],list) :
				data = inputs[0]
			else:
				data = inputs

			for i in data:
				if i==True:
					return 1
		
			return 0
		else:
			raise Exception("ERROR: Too few inputs given")
			return

	def NOR(self, *inputs):
		'''
		This method takes n>1 inputs and returns its NOR
		'''
		
		if (isinstance(inputs[0],list) and len(inputs[0]) > 1) or len(inputs) > 1 :
			if isinstance(inputs[0],list) :
				data = inputs[0]
			else:
				data = inputs

			for i in data:
				if i==True:
					return 0
			return 1
		else:
			raise Exception("ERROR: Too few inputs given")
			return
		
	def AND(self, *inputs):
		'''
		This method takes n>1 inputs and returns its AND
		'''
		
		if (isinstance(inputs[0],list) and len(inputs[0]) > 1) or len(inputs) > 1 :
			if isinstance(inputs[0],list) :
				data = inputs[0]
			else:
				data = inputs

			for i in data:
				if i == False:
					return 0
			return 1
		else:
			raise Exception("ERROR: Too few inputs given")
			return

	def NAND(self, *inputs):
		'''
		This method takes n>1 inputs and returns its NAND
		'''

		if (isinstance(inputs[0],list) and len(inputs[0]) > 1) or len(inputs) > 1 :
			if isinstance(inputs[0],list) :
				data = inputs[0]
			else:
				data = inputs

			for i in data:
				if i == False:
					return 1
			return 0
		else:
			raise Exception("ERROR: Too few inputs given")
			return
	
	def XOR(self, *inputs):
		'''
		This method takes n>1 inputs and returns its XOR
		'''

		if (isinstance(inputs[0],list) and len(inputs[0]) > 1) or len(inputs) > 1 :
			if isinstance(inputs[0],list) :
				data = inputs[0]
			else:
				data = inputs

			temp = data[0]

			for i in data[1:]:
				temp = temp ^ i

		else:
			raise Exception("ERROR: Too few inputs given")
			return

		return int( temp )
					
	def XNOR(self, *inputs):
		'''
		This method takes n>1 inputs and returns its XNOR
		'''
		
		if (isinstance(inputs[0],list) and len(inputs[0]) > 1) or len(inputs) > 1 :
			if isinstance(inputs[0],list) :
				data = inputs[0]
			else:
				data = inputs

			temp = data[0]

			for i in data[1:]:
				temp = temp ^ i

		else:
			raise Exception("ERROR: Too few inputs given")
			return

		return int( not temp )
