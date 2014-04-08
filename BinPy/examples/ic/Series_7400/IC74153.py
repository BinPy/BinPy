from __future__ import print_function
from BinPy import *
print ('Usage of IC 74153:\n')

ic = IC_74153()
print ("""This is 16-pin dual 4:1 multiplexer with output same as the input."""")
print ('\nThe Pin configuration is:\n')
p = {
    1: 1,
    2: 1,
    3: 1,
    4: 0,
    5: 0,
    6: 0,
    10: 0,
    11: 1,
    12: 0,
    13: 0,
    14: 0,
    15: 0}
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
