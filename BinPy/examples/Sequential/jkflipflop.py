#Example for JKFlipFlop

from BinPy import *

j = Connector(1)
k = Connector(0)
p = Connector(0)
q = Connector(1)

enable = Connector(1)

jkff = JKFlipFlop(j,k,enable)
#To connect different outputs use s.setOutputs(op1,op2)
jkff.setOutputs(A = p, B = q)

#set
j.state = 1
k.state = 0
jkff.trigger()
print jkff.state()
#The same thing can also be dont by --> jkff.setInputs(j = 1, k = 0)

#reset
j.state = 0
k.state = 1
jkff.trigger()
print jkff.state()

#toggle
j.state = 0
k.state = 1
jkff.trigger()
print jkff.state()

#No change
j.state = 0
k.state = 1
jkff.trigger()
print jkff.state()

print p(), q()

#To connect different set of connectors use s.setInputs(conn1,conn2,enab)