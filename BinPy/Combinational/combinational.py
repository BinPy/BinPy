from BinPy.Gates import *
from BinPy.ic import *
from BinPy.Algorithms import *
from BinPy.tools import *
from BinPy.base import *
from BinPy.Operations import *
from BinPy.Sequential import *
from BinPy.Combinational import *


class Decoder:

	def __init__(self,inputs):

		if not (len(inputs) != 0 and (len(inputs) & (len(inputs) - 1) == 0)):
			raise Exception("ERROR: Number inputs should be a power of 2")
			return None
		self.inputs = inputs[:]

	def output(self,select):

		if pow(len(select),2) == len(self.inputs):
			return self.inputs[int(select,2)]
		else:
			raise Exception("ERROR: Number of select lines not consistent with inputs")
			return None

	def setInputs(self,inputs):

		if not (len(inputs) != 0 and (len(inputs) & (len(inputs) - 1) == 0)):
			raise Exception("ERROR: Number inputs should be a power of 2")
			return None

		self.inputs = inputs[:]
		

"""
ENCODER:
input lines, output lines
if output lines = n, input lines = 2 power n
input lines must be a power of 2
"""    
class Encoder:

    def __init__(self, inputs):

        if not (len(inputs) != 0 and (len(inputs) & (len(inputs) - 1) == 0)):
            raise Exception("ERROR: Number inputs should be a power of 2")
            return None
        self.inputs = inputs[:]

    def output(self,output):

        if pow(2,len(output)) == len(self.inputs):
            for i in self.inputs:
                if self.inputs[i] == "1":
                    index = i
            return self.inputs[bin(index)];
        else:
            raise Exception("ERROR: Number of output lines not consistent with inputs")
            return None

    def setInputs(self,inputs):

        if not (len(inputs) != 0 and (len(inputs) & (len(inputs) - 1) == 0)):
            raise Exception("ERROR: Number inputs should be a power of 2")
            return None

        self.inputs = inputs[:]        


		
"""
DEMULTIPLEXER:
data line = 1
no. of output lines must be a power  of 2
if No. of select lines = n,
no. of output lines = 2 raised to power n
"""
class Demultiplexer:

    def __init__(self, inputs):

        if not (len(inputs) != 0 and (len(inputs) & (len(inputs) - 1) == 0)):
            raise Exception("ERROR: Number inputs should be a power of 2")
            return None
        self.inputs = inputs[:]

    def output(self,select,data):

        if (pow(2,len(select)) == len(self.inputs) and data == 1):   
            return self.inputs[int(select,2)]
        else:
            raise Exception("ERROR: Number of select lines not consistent with inputs")
            return None

    def setInputs(self,inputs):

        if not (len(inputs) != 0 and (len(inputs) & (len(inputs) - 1) == 0)):
            raise Exception("ERROR: Number inputs should be a power of 2")
            return None

        self.inputs = inputs[:]        
