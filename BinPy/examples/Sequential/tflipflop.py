#Example for TFlipFlop

from BinPy import *

toggle_ip = Connector(1)
p = Connector(0)
q = Connector(1)

enable = Connector(1)

t = TFlipFlop(toggle_ip,enable)

toggle_ip.state = 1
#The same thing can also be dont by --> t.setInputs(t = 1)
t.trigger()
print t.state()

toggle_ip.state = 1
t.trigger()
print t.state()

toggle_ip.state = 0
t.trigger()
print t.state()

#To connect different set of connectors use t.setInputs(conn1,enab)
#To connect different outputs use t.setOutputs(op1,op2)
t.setOutputs(A = p, B = q)