from __future__ import print_function
from BinPy import *
print ('Usage of IC 7411:\n')
ic = IC_7411()
print ('\nThe Pin configuration is:\n')
p = {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 7: 0, 9: 1, 10: 1, 11: 1, 13: 0, 14: 1}
print (p)
print ('\nPin initialization -using -- ic.set_IC(p) --\n')
ic.set_IC(p)
print ('\nPowering up the IC - using -- ic.set_IC({14:1,7:0}) -- \n')
ic.set_IC({14: 1, 7: 0})
print ('\nDraw the IC with the current configuration\n')
ic.draw_IC()
print (
    '\nRun the IC with the current configuration using -- print ic.run() -- \n')
print (
    'Note that the ic.run() returns a dict of pin configuration similar to :')
print (ic.run())
print (
    '\nSeting the outputs to the current IC configuration using -- ic.set_IC(ic.run()) --\n')
ic.set_IC(ic.run())
print ('\nDraw the final configuration\n')
ic.draw_IC()
print ('\nConnector Inputs\n')
print ('c = Connector(p[1])\np[1] = c\nic.set_IC(p)\n')
c = Connector(p[1])
p[1] = c
ic.set_IC(p)
print ('Run the IC\n')
print (ic.run())
print ('\nConnector Outputs')
print ('Set the output -- ic.set_output(8, c)\n')
ic.set_output(8, c)
print ('Run the IC\n')
print (ic.run())
