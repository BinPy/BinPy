import sys
from BinPy import Gates

class Operation:
	'''
	This class serves binary addition and subtraction on n-bit numbers
	'''
	def __init__(self):
		self.gates = Gates()
	
	def add_one_bit(self,a,b,c=0):
		'''
		This method takes two one bit numbers and returns a dictionary of their sum and carry
		DictKeys: 'sum', 'carry'
		'''
		a_xor_b = self.gates.XOR(a,b)
		asum = self.gates.XOR(a_xor_b,c)
		a_and_b = self.gates.AND(a,b)
		a_xor_b_and_c = self.gates.AND(a_xor_b,c)
		carry = self.gates.OR(a_xor_b_and_c, a_and_b) 
		return {'sum':asum, 'carry':carry}

	def add(self,a,b,carry=0):
		'''
		This method takes 2 lists of binary numbers with an optional carry
		it uses add_one_bit method to add those numbers
		This method returns a dictionary of a list and an integer
		DictKeys: 'sum', 'carry'
		'''
		a = a[::-1]
		b = b[::-1]
		hold = []
		if len(a)!=len(b):
			diff = abs(len(a)-len(b))
			if len(a)>len(b):
				for i in range(diff):
					b.append(0)
			else:
				for i in range(diff):
					a.append(0)			
		for i in xrange(len(a)):
			step=self.add_one_bit(a[i],b[i],carry)
			hold.append(step['sum'])
			carry=step['carry']
		hold=hold[::-1]
		return {'sum':hold,'carry':carry}
		
	def subtract(self,a,b,carry=1):
		'''
		This method takes 2 lists of binary numbers with an optional carry
		it uses add method to subtract those numbers using 1's complement method
		This method returns a dictionary of a list and an integer
		DictKeys: 'difference', 'carry'
		'''
		a = a[::-1]
		b = b[::-1]
		
		if len(a)!=len(b):
			diff = abs(len(a)-len(b))
			if len(a)>len(b):
				for i in range(diff):
					b.append(0)
			else:
				for i in range(diff):
					a.append(0)	
		a=a[::-1]
		b=b[::-1]
		for i in range(len(b)):
			b[i]=self.gates.NOT(b[i])
		temp = self.add(a,b,carry)
		return {'difference':temp['sum'],'carry':temp['carry']}
				
	
	def multiply(self,a,b):
		'''
		This method takes 2 lists of binary numbers 
		and multiplies those numbers using and add function			
		This method returns a binary number
		'''
		a = a[::-1]
		b = b[::-1]
		hold = [[] for i in range(len(b))]
		for i in range(len(b)):
			for j in range(len(a)+len(b)):
				hold[i].append(0) 
		for i in range(len(b)):
			k=0
			for j in range(i,len(a)+i):
				hold[i][j]=self.gates.AND(a[k],b[i])
				k+=1
		for i in range(len(hold)):
			hold[i]=hold[i][::-1]
		last_out = self.add(hold[0],hold[1])['sum']
		last_out.insert(self.add(hold[0],hold[1])['carry'],0)
		for i in range(1,len(hold)-1):
			temp = self.add(hold[i],last_out)
			last_out = temp['sum'].insert(0,temp['carry'])
		return last_out
	



