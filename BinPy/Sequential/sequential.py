from BinPy.Gates import *

class SRLatch:

	def __init__(self,input1,input2):
		
		self.a = Connector()
		self.b = Connector()

		self.g1 = NOR(input1,self.b)
		self.g1.setOutput(self.a)

		self.g2 = NOR(input2,self.a)
		self.g2.setOutput(self.b)

	def setInputs(self, *inputs):

		if len(inputs) != 2:
			raise Exception("ERROR: Latch takes two inputs!")
			return None

		self.g1.setInput(0,list(inputs)[0])
		self.g2.setInput(0,list(inputs)[1])

	def getOutput(self):

		return [self.g1.output(), self.g2.output()]

class DLatch:
        """
        This is a gated D latch
        """
	def __init__(self,input1,input2):

		self.a = Connector()
		self.b = Connector()
		self.c = Connector()
		self.d = Connector()

		self.g1 = NAND(input1,input2)
		self.g1.setOutput(self.a)

		self.g2 = NAND(self.a,input2)
		self.g2.setOutput(self.b)

		self.g3 = NAND(self.a,self.d)
		self.g3.setOutput(self.c)

		self.g4 = NAND(self.b,self.c)
		self.g4.setOutput(self.d)

	def output(self):

		return [self.g3.output(),self.g4.output()]

	def setInputs(self,input1,input2):

		self.g1.setInput(0,input1)
		self.g1.setInput(1,input2)
		self.g2.setInput(1,input2)
