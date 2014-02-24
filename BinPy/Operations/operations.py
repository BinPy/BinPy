class Operations:

	def __parseInput(self,input1,input2):

		if isinstance(input1,list):
			input1 = ''.join(map(str,input1))
		elif not isinstance(input1,str):
			input1 = str(input1)

		if isinstance(input2,list):
			input2 = ''.join(map(str,input2))
		elif not isinstance(input2,str):
			input2 = str(input2)

		return input1,input2

	def ADD(self,input1,input2):

		a,b = self.__parseInput(input1,input2)
		return bin(int(a,2) + int(b,2))[2:]

	def SUB(self,input1,input2):

		a,b = self.__parseInput(input1,input2)
		return bin(int(a,2) - int(b,2))[2:]

	def MUL(self,input1,input2):

		a,b = self.__parseInput(input1,input2)
		return bin(int(a,2) * int(b,2))[2:]		
	
	def DIV(self,input1,input2):

		a,b = self.__parseInput(input1,input2)
		return bin(int(a,2) / int(b,2))[2:]	

	def COMP(self,input1,option):

		if isinstance(input1,list):
			input1 = ''.join(map(str,input1))
		elif not isinstance(input1,str):
			input1 = str(input1)

		result = bin(int(input1,2) ^ int(len(input1)*'1',2))[2:]
		temp = bin(int(result,2) + int('1',2))[2:]
		if str(option) == '1':
			return (len(input1) - len(result)) * '0' + result
		else:
			return (len(input1) - len(temp)) * temp[0] + temp

