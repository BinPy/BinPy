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

	activate: This parameter activates the Logic Object of the owner object. Every Logic
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
			print "Connector %s-%s set to %s" % (self.owner.name,self.name,self.value)
		for con in self.connects : con.set(value)


class LC :

	'''
	Basic Logic Class object. Every Object class has an evaluate function which is 
	inherited in all the classes derieved from it. 
	'''
	def __init__ (self, name) :
		self.name = name
	def evaluate (self) : return

class Not (LC) : 																					#NOT gate - Simple LC object
	def __init__ (self, name) :
		LC.__init__ (self, name)
		self.A = Connector(self,'A', activates=1)
		self.B = Connector(self,'B',monitor=1)

	def evaluate (self) : self.B.set(not self.A.value)			#NOT gate evaluate function


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
	def __init__ (self, name) :
		Gate2.__init__ (self, name)
	def evaluate (self) : self.C.set(self.A.value and self.B.value)

class Or (Gate2) : 
	def __init__ (self, name) :
		Gate2.__init__ (self, name)
	def evaluate (self) : self.C.set(self.A.value or self.B.value)

class Xor (Gate2) :
	def __init__ (self, name) :
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


class HalfAdder (LC) : 
	def __init__ (self, name) :
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
	def __init__ (self, name) :
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
