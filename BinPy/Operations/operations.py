class Operations:

    """
    This class implements the primary arithmetic binary functions ADD, SUB, MUL, DIV, COMP(complement).
    Inputs are in the form of unsigned integers. Negative numbers will have - sign.
    """

    def __parseInput(self, input1, input2):

        if isinstance(input1, list):
            input1 = ''.join(map(str, input1))
        elif not isinstance(input1, str):
            input1 = str(input1)

        if isinstance(input2, list):
            input2 = ''.join(map(str, input2))
        elif not isinstance(input2, str):
            input2 = str(input2)

        return input1, input2

    def ADD(self, input1, input2):
        """
        This function implements the binary addition
        It takes two binary number and gives their sum
        How to use:
            >>> opr = Operations()
            >>> opr.ADD('1100','0001')
            '1101'
        """

        a, b = self.__parseInput(input1, input2)
        c = bin(int(a, 2) + int(b, 2))
        if c[0] == '-':
            return c[3:]
        else:
            return c[2:]

    def SUB(self, input1, input2):
        """
        This function implements the binary subtraction
        It takes two binary number and gives their difference
        How to use:
            >>> opr = Operations()
            >>> opr.SUB('1100','0100')
            '1000'
        """

        a, b = self.__parseInput(input1, input2)
        c = bin(int(a, 2) - int(b, 2))
        if c[0] == '-':
            return c[3:]
        else:
            return c[2:]

    def MUL(self, input1, input2):
        """
        This function implements the binary multiplication
        It takes two binary number and gives their product
        How to use:
            >>> opr = Operations()
            >>> opr.MUL('1100','0100')
            '110000'
        """

        a, b = self.__parseInput(input1, input2)
        c = bin(int(a, 2) * int(b, 2))
        if c[0] == '-':
            return c[3:]
        else:
            return c[2:]

    def DIV(self, input1, input2):
        """
        This function implements the binary division
        It takes two binary number and gives their quotient
        How to use:
            >>> opr = Operations()
            >>> opr.DIV('1000','0010')
            '100'
        """

        a, b = self.__parseInput(input1, input2)
        c = bin(int(a, 2) // int(b, 2))
        if c[0] == '-':
            return c[3:]
        else:
            return c[2:]

    def COMP(self, input1, option):
        """
        This function gives the complement of the input
        Note: In this case the input is put in the form of signed/unsigned number
        It takes two parameters, number to be complemented and the nth complement you want.
        How to use:
            >>> opr = Operations()
            >>> opr.COMP('1000','1')
            '0111'
        """

        if isinstance(input1, list):
            input1 = ''.join(map(str, input1))
        elif not isinstance(input1, str):
            input1 = str(input1)

        result = bin(int(input1, 2) ^ int(len(input1) * '1', 2))[2:]
        temp = bin(int(result, 2) + int('1', 2))[2:]
        if str(option) == '1':
            return (len(input1) - len(result)) * '0' + result
        else:
            return (len(input1) - len(temp)) * temp[0] + temp

@staticmethod

def  binToDec(number):
"""
        This function converts binary number into decimal number
        How to use:
            >>> Operations.binToDec('1001.1')
            >>> 9.5
        """
	i=0
	j=1
	length=len(number)
	num=0
	while i<length and number[i]!='.' :
		num=num*2 + int(number[i])
		i+=1
	if(number[i] == "."):
		i+=1
	while i<length:
		num+=int(number[i])/((2**j)+0.0)
		j+=1
		i+=1
	return num
	
@staticmethod
"""
        This function converts positive decimal number into binary number
        How to use:
            >>> Operations.decToBin(12.5)
            >>> 1100.1
        """
def DecTobin(number):
	x=number
	number=int(number)
	x=x-number
	k=[]
	string1=""
	if(number==0):
		string1+=str(0)
	while (number>0):
		a=int(float(number%2))
		k.append(a)
		number=(number-a)/2
	for j in k[::-1]:
		string1=string1+str(j)
	j=1
	string2=""
	if x !=0.0:
		string2+='.'
	while x >0.0 and j<15:
		if x>= 1/((2**j)+0.0):
			string2+=str(1)
			x-= 1/((2**j)+0.0)
		else:
			string2+=str(0)
		j+=1
	return string1+string2
