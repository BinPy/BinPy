from BinPy.Gates import *

class SRLatch:

	def __init__(self, R, S):
		"""
		Construct an SRLatch with initial reset input R and set input S.
		"""

		self.a = Connector()
		self.b = Connector()

		self.g1 = NOR(R, self.b)
		self.g1.setOutput(self.a)

		self.g2 = NOR(S, self.a)
		self.g2.setOutput(self.b)

	def setInputs(self, R, S):
		"""
		Set this SRLatch's reset input to R and set input to S.
		Unstable behaviour when transitioning directly from RS = 11 to RS = 00.
		"""

		self.g1.setInputs(R, self.b)
		self.g2.setInputs(S, self.a)

	def output(self):
		"""
		Return the output of this SRLatch in the format [Q, ~Q].
		"""

		return [self.g1.output(), self.g2.output()]

class DFlipFlop:

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
