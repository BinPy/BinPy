class Decoder:

	def __init__(self,inputs):

		if not (len(inputs) != 0 and (len(inputs) & (len(inputs) - 1) == 0)):
			raise Exception("ERROR: Number inputs should be a power of 2")
			return None
		self.inputs = inputs[:]

	def output(self,select):

		if pow(2,len(select)) == len(self.inputs):
			return self.inputs[int(select,2)]
		else:
			raise Exception("ERROR: Number of select lines not consistent with inputs")
			return None

	def setInputs(self,inputs):

		if not (len(inputs) != 0 and (len(inputs) & (len(inputs) - 1) == 0)):
			raise Exception("ERROR: Number inputs should be a power of 2")
			return None

		self.inputs = inputs[:]
