from BinPy import *
print 'Usage of IC 7404:\n'
ic = IC_7404()
print '\nThe Pin configuration is:\n'
p = {1: 1, 3: 0, 5: 0, 7: 0, 9: 0, 11: 0, 13: 1, 14: 1}
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