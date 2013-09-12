from BinPy import Gates
import sys

class IC_7400:
	'''
	This is a Quad 2 input NAND gate IC
	'''
	def __init__(self):
		self.pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]
		self.gates = Gates()

	def setIC(self,pin_conf):
		'''
		This method takes a dictionary with key:pin_no and value:pin_value
		'''
		for i in pin_conf:
			self.pins[i] = pin_conf[i]

	def setPin(self, pin_no, pin_value):
		if pin_no<1 or pin_no>14:
			sys.exit("ERROR: there are only 14 pins in this IC")
		self.pins[pin_no] = pin_value

	def run(self):
		output = {}
		output[3] = self.gates.NAND(self.pins[1],self.pins[2])
		output[6] = self.gates.NAND(self.pins[4],self.pins[5])
		output[8] = self.gates.NAND(self.pins[9],self.pins[10])
		output[11] = self.gates.NAND(self.pins[12],self.pins[13])
		if self.pins[7] == 0 and self.pins[14] == 1:
			return output
		else:
			print "Ground and VCC pins have not been configured correctly."

class IC_741G00:
	'''
	This is a single 2 input NAND gate IC
	'''
	def __init__(self):
		self.pins = [None,0,0,0,None,0]
		self.gates = Gates()

	def setIC(self,pin_conf):
		'''
		This method takes a dictionary with key:pin_no and value:pin_value
		'''
		for i in pin_conf:
			self.pins[i] = pin_conf[i]

	def setPin(self, pin_no, pin_value):
		if pin_no<1 or pin_no>5:
			sys.exit("ERROR: there are only 5 pins in this IC")
		self.pins[pin_no] = pin_value

	def run(self):
		output = {}
		output[4] = self.gates.NAND(self.pins[1],self.pins[2])
		if self.pins[3] == 0 and self.pins[5] == 1:
			return output
		else:
			print "Ground and VCC pins have not been configured correctly."


class IC_7401:
	'''
	This is a Quad 2 input NAND gate IC
	'''
	def __init__(self):
		self.pins = [None,None,0,0,None,0,0,0,0,0,None,0,0,None,0]
		self.gates = Gates()

	def setIC(self,pin_conf):
		'''
		This method takes a dictionary with key:pin_no and value:pin_value
		'''
		for i in pin_conf:
			self.pins[i] = pin_conf[i]

	def setPin(self, pin_no, pin_value):
		if pin_no<1 or pin_no>14:
			sys.exit("ERROR: there are only 14 pins in this IC")
		self.pins[pin_no] = pin_value

	def run(self):
		output = {}
		output[1] = self.gates.NAND(self.pins[2],self.pins[3])
		output[4] = self.gates.NAND(self.pins[5],self.pins[6])
		output[10] = self.gates.NAND(self.pins[8],self.pins[9])
		output[13] = self.gates.NAND(self.pins[11],self.pins[12])
		if self.pins[7] == 0 and self.pins[14] == 1:
			return output
		else:
			print "Ground and VCC pins have not been configured correctly."


class IC_7402:
	'''
	This is a Quad 2 input NOR gate IC
	'''
	def __init__(self):
		self.pins = [None,None,0,0,None,0,0,0,0,0,None,0,0,None,0]
		self.gates = Gates()

	def setIC(self,pin_conf):
		'''
		This method takes a dictionary with key:pin_no and value:pin_value
		'''
		for i in pin_conf:
			self.pins[i] = pin_conf[i]

	def setPin(self, pin_no, pin_value):
		if pin_no<1 or pin_no>14:
			sys.exit("ERROR: there are only 14 pins in this IC")
		self.pins[pin_no] = pin_value

	def run(self):
		output = {}
		output[1] = self.gates.NOR(self.pins[2],self.pins[3])
		output[4] = self.gates.NOR(self.pins[5],self.pins[6])
		output[10] = self.gates.NOR(self.pins[8],self.pins[9])
		output[13] = self.gates.NOR(self.pins[11],self.pins[12])
		if self.pins[7] == 0 and self.pins[14] == 1:
			return output
		else:
			print "Ground and VCC pins have not been configured correctly."


class IC_741G02:
	'''
	This is a single 2 input NOR gate IC
	'''
	def __init__(self):
		self.pins = [None,0,0,0,None,0]
		self.gates = Gates()

	def setIC(self,pin_conf):
		'''
		This method takes a dictionary with key:pin_no and value:pin_value
		'''
		for i in pin_conf:
			self.pins[i] = pin_conf[i]

	def setPin(self, pin_no, pin_value):
		if pin_no<1 or pin_no>5:
			sys.exit("ERROR: there are only 14 pins in this IC")
		self.pins[pin_no] = pin_value

	def run(self):
		output = {}
		output[4] = self.gates.NOR(self.pins[1],self.pins[2])
		if self.pins[3] == 0 and self.pins[5] == 1:
			return output
		else:
			print "Ground and VCC pins have not been configured correctly."


class IC_7403:
	'''
	This is a Quad 2 input NAND gate IC
	'''
	def __init__(self):
		self.pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]
		self.gates = Gates()

	def setIC(self,pin_conf):
		'''
		This method takes a dictionary with key:pin_no and value:pin_value
		'''
		for i in pin_conf:
			self.pins[i] = pin_conf[i]

	def setPin(self, pin_no, pin_value):
		if pin_no<1 or pin_no>14:
			sys.exit("ERROR: there are only 14 pins in this IC")
		self.pins[pin_no] = pin_value

	def run(self):
		output = {}
		output[3] = self.gates.NAND(self.pins[1],self.pins[2])
		output[6] = self.gates.NAND(self.pins[4],self.pins[5])
		output[8] = self.gates.NAND(self.pins[9],self.pins[10])
		output[11] = self.gates.NAND(self.pins[12],self.pins[13])
		if self.pins[7] == 0 and self.pins[14] == 1:
			return output
		else:
			print "Ground and VCC pins have not been configured correctly."

