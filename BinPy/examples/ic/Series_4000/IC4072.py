from __future__ import print_function
from BinPy import *
print ('Usage of IC 4072:\n')
ic = IC_4072()
print ('\nThe Pin configuration is:\n')
input = {2: 0, 3: 0, 4: 0, 5: 0, 7: 0, 9: 1, 10: 1, 11: 1, 12: 1, 14: 1}
print (input)
print ('\nPin initinalization\n')
print ('\nPowering up the IC - using -- ic.setIC({14: 1, 7: 0}) -- \n')
ic.setIC({14: 1, 7: 0})
print ('\nDraw the IC with the current configuration\n')
ic.drawIC()
print (
    '\nRun the IC with the current configuration using -- print ic.run() -- \n')
print (
    'Note that the ic.run() returns a dict of pin configuration similar to :')
print (ic.run())
print (
    '\nSeting the outputs to the current IC configuration using -- ic.setIC(ic.run()) --\n')
ic.setIC(ic.run())
print ('\nDraw the final configuration\n')
ic.drawIC()
print ('\nConnector Inputs\n')
print ('c = Connector(p[1])\np[1] = c\nic.setIC(p)\n')
c = Connector(p[1])
p[1] = c
ic.setIC(p)
print ('Run the IC\n')
print (ic.run())
print ('\nConnector Outputs')
print ('Set the output -- ic.setOutput(8, c)\n')
ic.setOutput(8, c)
print ('Run the IC\n')
print (ic.run())
