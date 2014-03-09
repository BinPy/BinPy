from BinPy.Gates.gates import *
print ('This is an exampe to illustrate the usage of BUFFER')
print ('a, b, c, d, e are connectors')
print ('NOR1 is a NOR gate with inputs = [1, 0] and output = connector a')
print ('NOR2 is a NOR gate with inputs = [0, 0] and output = connector b')
print ('BUF1 is a BUFFER with inputs a(input)) and e(enable) and output c')
print ('BUF2 is a BUFFER with inputs b(input)) and b(enable) and output c')
print ('NOT1 is a NOT gate with input e and output d')
a = Connector()
b = Connector()
c = Connector()
d = Connector()
e = Connector()

NOR1 = NOR(1, 0)
NOR1.setOutput(a)

NOR2 = NOR(0, 0)
NOR2.setOutput(b)

BUF1 = BUFFER(a, e)
BUF1.setOutput(c)

NOT1 = NOT(e)
NOT1.setInputs(1)
NOT1.setOutput(d)


BUF2 = BUFFER(b, d)
BUF2.setOutput(c)

print()
print("e = 1 implies NOR1 is selected")
print("NOR1 output is " + str(NOR1.output()))
print("Common output of buffers, c is " + str(c.state))
print("changing inputs of NOR1 from [1,0] to [0,0]")
NOR1.setInputs(1,0)
a.state
NOR1.setInputs(0,0)
a.state
print("NOR1 output is " + str(NOR1.output()))
print("Common output of buffers, c is " + str(c.state))

print()
print("changing e to 0 implies selecting output of NOR2")
NOT1.setInputs(0)
print("NOR2 output is " + str(NOR2.output()))
print("Common output of buffers, c is " + str(c.state))
print("changing inputs of NOR1 from [0,0] to [0,1]")
NOR2.setInputs(0,1)
print("NOR2 output is " + str(NOR2.output()))
print("Common output of buffers, c is " + str(c.state))
