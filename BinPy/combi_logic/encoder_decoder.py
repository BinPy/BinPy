import sys
from BinPy import Gates

class Decoder:
	'''
	This class can be used to create decoder in your circuit. It has a method for each kind of
	decoder, namely, decoder_2_4
	All the methods take 2 parameters(inputs and strobe) and give . Strobe is high by default
	inputs are lists. It give a list a output.
	Last index of inputs is 'a', second last index is 'b' and so on...
	'''
	def __init__(self):
		self.gates = Gates()

	def run(self,inputs,strobe=1):
		'''
			This method takes 2 parameters [inputs(list),optional strobe(int)]
			This method automatically classifies the type of decoder and returns the computed s(list)
		'''
		allowed = [1,2,3]
		decoder_type = len(inputs)
		if decoder_type not in allowed:
			sys.exit("ERROR: only 3 types of decoders are supported, namely, 1:2,2:4,3:8")
	
		if decoder_type==1:
			return self.decoder_1_2(inputs,strobe)
		elif decoder_type == 2:
			return self.decoder_2_4(inputs,strobe)
		elif decoder_type == 3:
			return self.decoder_3_8(inputs,strobe)
		
	def decoder_1_2(self,inputs,strobe=1):
		'''
		This method implements 1:2 decoder using logic gates
		Input and output is same as run() method
		'''
		s =[0 for i in range(2)]
		a = inputs[0]
		s[0] = self.gates.AND(self.gates.NOT(a),1)
		s[1] = self.gates.AND(a,1)
		
		if strobe==1:
			return s
		else:
			return false
	
	def decoder_2_4(self,inputs,strobe=1):
		'''
		This method implements 2:4 decoder using logic gates
		Input and output is same as run() method
		'''
		s =[0 for i in range(4)]
		a,b = inputs[0],inputs[1]
		s[0] = self.gates.AND(self.gates.NOT(a),self.gates.NOT(b))
		s[1] = self.gates.AND(a,self.gates.NOT(b))
		s[2] = self.gates.AND(self.gates.NOT(a),b)
		s[3] = self.gates.AND(a,b)
		
		if strobe==1:
			return s
		else:
			return false

	def decoder_3_8(self,inputs,strobe=1):
		'''
		This method implements 3:8 decoder using logic gates
		Input and output is same as run() method
		'''
		s =[0 for i in range(4)]
		inputs =inputs[::-1]
		a,b,c = inputs[0],inputs[1],inputs[2]
		s[0] = self.gates.AND(self.gates.NOT(c),self.gates.NOT(b),self.gates.NOT(a))
		s[1] = self.gates.AND(self.gates.NOT(c),self.gates.NOT(b),a)
		s[2] = self.gates.AND(self.gates.NOT(c),b,self.gates.NOT(a))
		s[3] = self.gates.AND(self.gates.NOT(c),b,a)
		s[4] = self.gates.AND(c,self.gates.NOT(b),self.gates.NOT(a))
		s[5] = self.gates.AND(c,self.gates.NOT(b),a)
		s[6] = self.gates.AND(c,b,self.gates.NOT(a))
		s[7] = self.gates.AND(c,b,a)
		
		if strobe==1:
			return s
		else:
			return false


	


	