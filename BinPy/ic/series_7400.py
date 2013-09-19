
"""
	This file has all the classes of ICs belong to 7400 series
"""
from BinPy import Gates
import sys

class IC_7400:
	"""
	This is a Quad 2 input NAND gate IC
	"""
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


class IC_741G03:
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


class IC_7404:
	'''
	This is hex inverter IC
	'''
	def __init__(self):
		self.pins = [None,0,None,0,None,0,None,0,None,0,None,0,None,0,0]
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
		output[2] = self.gates.NOT(self.pins[1])
		output[4] = self.gates.NOT(self.pins[3])
		output[6] = self.gates.NOT(self.pins[5])
		output[8] = self.gates.NOT(self.pins[9])
		output[10] = self.gates.NOT(self.pins[11])
		output[12] = self.gates.NOT(self.pins[13])
		if self.pins[7] == 0 and self.pins[14] == 1:
			return output
		else:
			print "Ground and VCC pins have not been configured correctly."


class IC_741G04:
	'''
	This is a single inverter IC
	'''
	def __init__(self):
		self.pins = [None,None,0,0,None,0]
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
		output[4] = self.gates.NOT(self.pins[2])
		if self.pins[3] == 0 and self.pins[5] == 1:
			return output
		else:
			print "Ground and VCC pins have not been configured correctly."


class IC_7405:
	'''
	This is hex inverter IC
	'''
	def __init__(self):
		self.pins = [None,0,None,0,None,0,None,0,None,0,None,0,None,0,0]
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
		output[2] = self.gates.NOT(self.pins[1])
		output[4] = self.gates.NOT(self.pins[3])
		output[6] = self.gates.NOT(self.pins[5])
		output[8] = self.gates.NOT(self.pins[9])
		output[10] = self.gates.NOT(self.pins[11])
		output[12] = self.gates.NOT(self.pins[13])
		if self.pins[7] == 0 and self.pins[14] == 1:
			return output
		else:
			print "Ground and VCC pins have not been configured correctly."

class IC_741G05:
	'''
	This is a single inverter IC
	'''
	def __init__(self):
		self.pins = [None,None,0,0,None,0]
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
		output[4] = self.gates.NOT(self.pins[2])
		if self.pins[3] == 0 and self.pins[5] == 1:
			return output
		else:
			print "Ground and VCC pins have not been configured correctly."


class IC_7408:
	'''
	This is a Quad 2 input AND gate IC
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
		output[3] = self.gates.AND(self.pins[1],self.pins[2])
		output[6] = self.gates.AND(self.pins[4],self.pins[5])
		output[8] = self.gates.AND(self.pins[9],self.pins[10])
		output[11] = self.gates.AND(self.pins[12],self.pins[13])
		if self.pins[7] == 0 and self.pins[14] == 1:
			return output
		else:
			print "Ground and VCC pins have not been configured correctly."


class IC_741G08:
	'''
	This is a single 2 input AND gate IC
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
		output[4] = self.gates.AND(self.pins[1],self.pins[2])
		if self.pins[3] == 0 and self.pins[5] == 1:
			return output
		else:
			print "Ground and VCC pins have not been configured correctly."

#IC_7409 and IC_741G09 to be added

class IC_7410:
	'''
	This is a Triple 3 input NAND gate IC
	'''
	def __init__(self):
		self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,None,0,0]
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
		output[12] = self.gates.NAND(self.pins[1],self.pins[2],self.pins[13])
		output[6] = self.gates.NAND(self.pins[3],self.pins[4],self.pins[5])
		output[8] = self.gates.NAND(self.pins[9],self.pins[10],self.pins[11])
		if self.pins[7] == 0 and self.pins[14] == 1:
			return output
		else:
			print "Ground and VCC pins have not been configured correctly."


class IC_7411:
	'''
	This is a Triple 3 input AND gate IC
	'''
	def __init__(self):
		self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,None,0,0]
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
		output[12] = self.gates.AND(self.pins[1],self.pins[2],self.pins[13])
		output[6] = self.gates.AND(self.pins[3],self.pins[4],self.pins[5])
		output[8] = self.gates.AND(self.pins[9],self.pins[10],self.pins[11])
		if self.pins[7] == 0 and self.pins[14] == 1:
			return output
		else:
			print "Ground and VCC pins have not been configured correctly."


class IC_7412:
	'''
	This is a Triple 3 input NAND gate IC with open collector outputs
	'''
	def __init__(self):
		self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,None,0,0]
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
		output[12] = self.gates.NAND(self.pins[1],self.pins[2],self.pins[13])
		output[6] = self.gates.NAND(self.pins[3],self.pins[4],self.pins[5])
		output[8] = self.gates.NAND(self.pins[9],self.pins[10],self.pins[11])
		if self.pins[7] == 0 and self.pins[14] == 1:
			return output
		else:
			print "Ground and VCC pins have not been configured correctly."



# IC_7413,IC_7414,IC_741G14to be added


class IC_7415:
	'''
	This is a Triple 3 input AND gate IC with open collector outputs
	'''
	def __init__(self):
		self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,None,0,0]
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
		output[12] = self.gates.AND(self.pins[1],self.pins[2],self.pins[13])
		output[6] = self.gates.AND(self.pins[3],self.pins[4],self.pins[5])
		output[8] = self.gates.AND(self.pins[9],self.pins[10],self.pins[11])
		if self.pins[7] == 0 and self.pins[14] == 1:
			return output
		else:
			print "Ground and VCC pins have not been configured correctly."	

# IC_7416,IC_7417,IC_741G17,IC_7418,IC_7419 to be added

class IC_7420:
	'''
	This is a is a dual 4-input NAND gate
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
		
		output[6] = self.gates.NAND(self.pins[1],self.pins[2],self.pins[4],self.pins[5])
		output[8] = self.gates.NAND(self.pins[9],self.pins[10],self.pins[12],self.pins[13])
		if self.pins[7] == 0 and self.pins[14] == 1:
			return output
		else:
			print "Ground and VCC pins have not been configured correctly."


class IC_7421:
	'''
	This is a is a dual 4-input AND gate
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
		
		output[6] = self.gates.AND(self.pins[1],self.pins[2],self.pins[4],self.pins[5])
		output[8] = self.gates.AND(self.pins[9],self.pins[10],self.pins[12],self.pins[13])
		if self.pins[7] == 0 and self.pins[14] == 1:
			return output
		else:
			print "Ground and VCC pins have not been configured correctly."	

class IC_7422:
	'''
	This is a is a dual 4-input NAND gate with open collector outputs
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
		
		output[6] = self.gates.NAND(self.pins[1],self.pins[2],self.pins[4],self.pins[5])
		output[8] = self.gates.NAND(self.pins[9],self.pins[10],self.pins[12],self.pins[13])
		if self.pins[7] == 0 and self.pins[14] == 1:
			return output
		else:
			print "Ground and VCC pins have not been configured correctly."









