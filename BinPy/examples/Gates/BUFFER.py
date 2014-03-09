from BinPy.Gates import *
print ('Usage of BUFFER gate')
print ('a and b are connectors')
print ('''BUF1 is a BUFFER with inputs- a,b where a is the input
and b is the enable input\n''')
print ('BUF1 = BUFFER(a, b)')
a = Connector()
b = Connector()
BUF1 = BUFFER(a, b)
print ('''\nSetting states to the inputs of the connector
using BUF1.setInputs(0,1)\n''')
print ('Also remember that BUFFER gate can have only two inputs\n')
BUF1.setInputs(0, 1)
print ('Printing inputs using BUF1.getInputStates():')
print ((BUF1.getInputStates()))
print ('Output is:')
print ((BUF1.output()))
print ('''\nSetting state of connector a which is input to
BUF1 using BUF1.setInput(1,0)\n''')
BUF1.setInput(1, 0)
print ('Inputs are:')
print ((BUF1.getInputStates()))
print ('Output is:')
print ((BUF1.output()))
