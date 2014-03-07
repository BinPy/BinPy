#Example for SRLatch()

from BinPy import *

a = Connector(1)
b = Connector(0)
p = Connector(0)
q = Connector(1)

enable = Connector(1)

s = SRLatch(a,b,enable)

a.state = 1
b.state = 0
s.trigger()
print s.state()
#The same thing can also be dont by --> s.setInputs(s = 1, r = 1)

a.state = 0
b.state = 1
s.trigger()
print s.state()

#To connect different set of connectors use s.setInputs(conn1,conn2,enab)
#To connect different outputs use s.setOutputs(op1,op2)
s.setOutputs(A = p, B = q)
