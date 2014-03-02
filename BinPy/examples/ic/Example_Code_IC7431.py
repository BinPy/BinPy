from BinPy import *
print 'Usage of IC 7431:\n'
ic = IC_7431()
print '\nThe Pin configuration is:\n'
p = {1: 1, 3: 1, 5: 0, 6: 0, 8: 0, 10: 1, 11: 1, 13: 0, 15: 1, 16: 1}
print p
print '\nPin initinalization\n'
print ic.setIC(p)
print '\nPowering up the IC - using -- ic.setIC({14:1,7:0}) -- \n'
ic.setIC({14:1,7:0})
print '\nDraw the IC with the current configuration\n'
ic.drawIC()
print '\nRun the IC with the current configuration using -- print ic.run() -- \n'
print 'Note that the ic.run() returns a dict of pin configuration similar to :'
print ic.run()
print '\nSeting the outputs to the current IC configuration using -- ic.setIC(ic.run()) --\n'
ic.setIC(ic.run())
print '\nDraw the final configuration\n'
ic.drawIC()