from logic_objects import *

class Latch (LC) :
	def __init__ (self, name="LATCH") :
		LC.__init__ (self, name)
		self.A = Connector(self,'A',1)
		self.B = Connector(self,'B',1)
		self.C = Connector(self,'Q',monitor=1)
		self.N1 = Nand ("N1")
		self.N2 = Nand ("N2")
		self.A.connect ([self.N1.A])
		self.B.connect ([self.N2.B])
		self.N1.C.connect ([self.N2.A, self.C])
		self.N2.C.connect ([self.N1.B])

class DFlipFlop (LC) :
	def __init__ (self, name="DFlipFlop") :
		LC.__init__ (self, name)
		self.A = Connector(self,'D',1)
		self.B = Connector(self,'C',1)
		self.C = Connector(self,'Q',monitor=1)
		self.C.value=0
		self.prev=None

	def evaluate (self) :
		if self.B.value==0 and self.prev==1 :  #clock drop
			self.C.set(self.A.value)
		self.prev = self.B.value

class Div2 (LC) :
	def __init__ (self, name="DIV2") :
		LC.__init__ (self, name)
		self.B = Connector(self,'C',activates=1)
		self.A = Connector(self,'D')
		self.C = Connector(self,'Q',monitor=1)
		self.C.value=0
		self.A.value=1
		self.DFF = DFlipFlop('DFF')
		self.NOT = Not('NOT')
		self.B.connect ([self.DFF.B])
		self.A.connect ([self.DFF.A])
		self.DFF.C.connect ([self.NOT.A,self.C])
		self.NOT.B.connect ([self.DFF.A])
		self.DFF.C.activates = 1
		self.DFF.A.value = 1 - self.DFF.C.value

class Counter (LC) :
	def __init__ (self, name="Counter") :
		LC.__init__ (self, name)
		self.B0 = Div2('B0')
		self.B1 = Div2('B1')
		self.B2 = Div2('B2')
		self.B3 = Div2('B3')
		self.A = Connector(self,'D')
		self.A.value = 1
		self.B = Connector(self,'C',activates=1)
		self.C = Connector(self,'Q',monitor=1)
		self.A.connect(self.B0.A)
		self.B.connect(self.B0.B)
		self.B3.C.connect(self.C)
		self.B0.C.connect( self.B1.B )
		self.B1.C.connect( self.B2.B )
		self.B2.C.connect( self.B3.B )

class Clock (LC):
	def __init__(self,name="Clock"):
		LC.__init__(self,name)
		self.A = Connector(self,'A',monitor=1)
		self.A.set(1)

def testDivBy2 () :
	x = Div2("X")
	c = 0; x.B.set(c)
	while 1 :
		raw_input("Clock is %d. Hit return to toggle clock" % c)
		c = not c
		x.B.set(c)

def testCounter () :
	x = Counter("x")    # x is a four bit counter
	x.B0.B.set(1)       # set the clock line 1
	while 1 :
		print "Count is ", x.B3.C.value, x.B2.C.value,
		print              x.B1.C.value, x.B0.C.value,
		ans = raw_input("\nHit return to pulse the clock")
		x.B0.B.set(0)   # toggle the clock
		x.B0.B.set(1)

def testLatch () :
	x = Latch("ff1")
	x.A.set(1); x.B.set(1)
	while 1 :
		ans = raw_input("Input A or B to drop:")
		if ans == "" : break
		if ans == 'A' : x.A.set(0); x.A.set(1); print x.C.getState()
		if ans == 'B' : x.B.set(0); x.B.set(1); print x.C.getState()
