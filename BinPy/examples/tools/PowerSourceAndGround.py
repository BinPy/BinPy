from __future__ import print_function
from BinPy.tools import *
print('Usage of PowerSource and Ground classes:\n')
# Creating Power Source POW and Ground terminal, GND
POW = PowerSource()
GND = Ground()
# Creating connectors a,b,c
a = Connector()
b = Connector()
c = Connector()
# Creating AND gate with inputs a and b and setting it output as c
AND1 = AND(a, b)
AND1.setOutput(c)
# Connecting the connectors a, b to the Power Source
POW.connect(a)
POW.connect(b)
print('a and b connected to Power Source, POW')
# Printing Status of AND1
print('The inputs to the AND1 are: ' + str(AND1.getInputStates()))
print('The output of AND1 is: ' + str(AND1.output()))
# Disconnecting b from Power Source and printing inputs of AND1
print('\nAfter disconnecting b from the Power Source, POW')
POW.disconnect(b)
print('The inputs of the AND1 are: ' + str(AND1.getInputStates()))
# Conneting b to Ground and printing the status AND1
print('\nAfter connecting b to the Ground, GND')
GND.connect(b)
print('The inputs of the AND1 are: ' + str(AND1.getInputStates()))
print('The output of AND1 is: ' + str(AND1.output()))
