#  Define classes for Connector, Logic Circuit, Gate

class Connector :

	'''
	The Connector class is the basic object connecting Gate Type Objects. Connectors can
	be both input and output. There is no method to check for circular references, so
	avoid them. The change in an output is propogated in the output it has. 


	Following are the parameters of the Connector Class:

	owner		: This parameter specifies the Logic Object (Gate, Latch, Flip-Flop) that  
						owns this connection.

	name		: This parameter gives a string name to identify the object

	monitor : This parameter toggles monitoring the logic level of connection. Useful for 
						understanding a function, or debugging purposes

	activates: This parameter activates the Logic Object of the owner object. Every Logic
						object has an evaluate function which is triggered by this object.

	The connector class has two methods, connect() and set() method.

	connect() : This method connects the given set of inputs to the Logic Object

	set()			: This method sets the value for the connection, depending on whether it 
							needs to be assigned values or evaluated as output,
	'''


	def __init__ (self, owner, name, activates=0, monitor=0,connected=0) :
		self.value = None
		self.owner = owner
		self.name  = name
		self.monitor  = monitor
		self.connects = []
		self.activates = activates 
		self.connected = connected  

	def connect (self, inputs) :
		if type(inputs) != type([]) : inputs = [inputs]
		for input in inputs : self.connects.append(input)


	def set (self, value) :
		if self.value == value : return 

		self.value = value

		if self.activates : self.owner.evaluate()
		if self.monitor :
			#print "Connector %s-%s set to %s" % (self.owner.name,self.name,self.value)
			pass
		for con in self.connects : con.set(value)

	def getState(self):
		return self.value


class LC :

	'''
	Basic Logic Class object. Every Object class has an evaluate function which is 
	inherited in all the classes derived from it. 
	'''
	def __init__ (self, name) :
		self.name = name
	def evaluate (self) : return


class Not (LC) : 
	'''
	Not gate using the LC class
	''' 																							
	def __init__ (self, name="NOT") :
		LC.__init__ (self, name)
		self.A = Connector(self,'A', activates=1)
		self.B = Connector(self,'B',monitor=1)

	def evaluate (self) : self.B.set(not self.A.value)			


class Gate2 (LC) :
	'''
	Base class for 2 input gates
	''' 
	def __init__ (self, name) :
		LC.__init__ (self, name)
		self.A = Connector(self,'A',activates=1)
		self.B = Connector(self,'B',activates=1)
		self.C = Connector(self,'C', monitor=1)

class And (Gate2) :   
	'''
	And gate using the Gate2 class
	''' 
	def __init__ (self, name="AND") :
		Gate2.__init__ (self, name)
	def evaluate (self) : self.C.set(self.A.value and self.B.value)

class Or (Gate2) : 
	'''
	Or gate using the Gate2 class
	''' 
	def __init__ (self, name="OR") :
		Gate2.__init__ (self, name)
	def evaluate (self) : self.C.set(self.A.value or self.B.value)

class Xor (Gate2) :
	'''
	Xor gate using the Gate2 class.
	This class uses the previous And and Not classes from above and connects them via a
	connector object. This forms the basis of combinational logic with these objects
	''' 
	def __init__ (self, name="XOR") :
		Gate2.__init__ (self, name)
		self.A1 = And("A1") 
		self.A2 = And("A2")
		self.I1 = Not("I1")
		self.I2 = Not("I2")
		self.O1 = Or ("O1")
		self.A.connect([ self.A1.A, self.I2.A])
		self.B.connect([ self.I1.A, self.A2.A])
		self.I1.B.connect ([ self.A1.B ])
		self.I2.B.connect ([ self.A2.B ])
		self.A1.C.connect ([ self.O1.A ])
		self.A2.C.connect ([ self.O1.B ])
		self.O1.C.connect ([ self.C ])

class Nand (Gate2) :
	'''
	Nand gate using the Gate2 class
	'''       
	def __init__ (self, name="NAND") :
		Gate2.__init__ (self, name)
	def evaluate (self) :
		self.C.set(not(self.A.value and self.B.value))

class Nor (Gate2) :       
	'''
	Nor gate using the Gate2 class
	'''
	def __init__ (self, name="NOR") :
		Gate2.__init__ (self, name)
	def evaluate (self) :
		self.C.set(not(self.A.value or self.B.value))

class Xnor (Gate2) :
	'''
	Xnor gate using the Gate2 class
	'''
	def __init__ (self,name="XNOR"):
		Gate2.__init__(self,name)
		self.A1 = And("A1") 
		self.A2 = And("A2")
		self.I1 = Not("I1")
		self.I2 = Not("I2")
		self.N1 = Nor ("O1")
		self.A.connect    ([ self.A1.A, self.I2.A])
		self.B.connect    ([ self.I1.A, self.A2.A])
		self.I1.B.connect ([ self.A1.B ])
		self.I2.B.connect ([ self.A2.B ])
		self.A1.C.connect ([ self.N1.A ])
		self.A2.C.connect ([ self.N1.B ])
		self.N1.C.connect ([ self.C ])


class HalfAdder (LC) : 
	'''
	Half Adder class using Xor and And objects
	''' 
	def __init__ (self, name="HALFADDER") :
		LC.__init__ (self, name)
		self.A = Connector(self,'A',1)
		self.B = Connector(self,'B',1)
		self.S = Connector(self,'S',monitor=1)
		self.Cout = Connector(self,'Cout',monitor=1)
		self.X1= Xor("X1")
		self.A1= And("A1")
		self.A.connect([ self.X1.A, self.A1.A])
		self.B.connect([ self.X1.B, self.A1.B])
		self.X1.C.connect ([ self.S])
		self.A1.C.connect ([ self.Cout])

class FullAdder (LC) : 
	'''
	Full Adder class using the Half Adder object
	''' 
	def __init__ (self, name="FULLADDER") :
		LC.__init__ (self, name)
		self.A= Connector(self,'A',1)
		self.B= Connector(self,'B',1)
		self.Cin  = Connector(self,'Cin',1)
		self.S= Connector(self,'S',monitor=1)
		self.Cout = Connector(self,'Cout',monitor=1)
		self.H1= HalfAdder("H1")
		self.H2= HalfAdder("H2")
		self.O1= Or("O1")
		self.A.connect([ self.H1.A ])
		self.B.connect([ self.H1.B ])
		self.Cin.connect  ([ self.H2.A ])
		self.H1.S.connect ([ self.H2.B ])
		self.H1.Cout.connect ([ self.O1.B])
		self.H2.Cout.connect ([ self.O1.A])
		self.H2.S.connect ([ self.S])
		self.O1.C.connect ([ self.Cout])

class logicGate(Not, Nand, Or, Nor, And, Xor, Xnor):
	def __init__(self, name):
		lname = name.lower()
		if lname == "not":
			Not.__init__(self, name)
		elif lname == "or":
			Or.__init__(self, name)
		elif lname == "and":
			And.__init__(self, name)
		elif lname == "nor":
			Nor.__init__(self, name)
		elif lname == "nand":
			Nand.__init__(self, name)
		elif lname == "xor":
			Xor.__init__(self, name)
		elif lname == "xnor":
			Xnor.__init__(self, name)
		else:
			#raise ExceptionError("No standard logic gate")
			return None
