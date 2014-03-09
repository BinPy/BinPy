from __future__ import print_function
from BinPy.Gates.gates import *
""" Examples for XOR class """
print ( "\n---Initializing the XOR class--- ")
print ( "gate = XOR(0, 1)")
gate = XOR(0, 1)
print ( "\n---Output of the XOR gate----")
print ( "gate.output()")
print ( gate.output())
print ( "\n---Input changes---")
print ( "gate.setInput(1, 0) #Input at index 1 is changed to 0")
gate.setInput(1, 0)
print ( "\n---New Output of the XOR gate---")
print ( gate.output())
print ( "\n\n---Using Connectors as the input and output lines---")
print ( "conn1 = Connector()")
print ( "conn2 = Connector()")
print ( "conn3 = Connector()")
conn1 = Connector()
conn2 = Connector()
conn3 = Connector()
print ( "\n---Initializing the XOR class--- ")
print ( "gate1 = NAND(1, conn1, 1, conn2)")
gate1 = XOR(1, conn1, 1, conn2)
print ( "\n---Set Output of gate to Connector conn3---")
print ( "gate1.setOutput(conn3)")
gate1.setOutput(conn3)
print ('\nSetting states to the inputs of the gate using gate1.setInputs(1, "~", 1, 1)')
gate1.setInputs(1, '~', 1, 1)
print ('Printing Inputs of gate1 using gate1.getInputStates()')
print ((gate1.getInputStates()))
print ( "\n---Output of the gate1---")
print ( "gate1.output()")
print ( gate1.output())
print ( "\n---State of conn3---")
print ( "conn3.state")
print ( conn3.state)
