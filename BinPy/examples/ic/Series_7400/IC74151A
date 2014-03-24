from __future__ import print_function
from BinPy import *
print ('Usage of IC 74151A:\n')

ic = IC_74151A()
print ("""This is 16-pin 8:1 multiplexer featuring complementary W and Y outputs"""")
print ('\nThe input Pin configuration is:\n')
p = {1:1 ,2:0 ,4:1 ,3:1 ,7:0 ,9:0 ,10:0 ,11:0 ,12:0 ,13:0 ,14:1 ,15:1 }
print (p)
print ('\nPin initialization -using -- ic.setIC(p) --\n')
ic.setIC(p)
print ('\nPowering up the IC - using -- ic.setIC({16:1, 8:0}) -- \n')
ic.setIC({16: 1, 8: 0})
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
