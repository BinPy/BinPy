from BinPy import *
import sys

print 'Usage of IC 7400:\n'
ic = IC_7400()

print '\nThe Pin configuration is:\n'
p = {1:1,2:1,4:1,5:0,8:0,9:0,13:1,12:1}
print p

print '\nPin initialization\n'
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

if(str(raw_input('Quit - Y/y or N/n - or Simply press Enter to Continue')).lower() == 'y'):
    sys.exit()











print '\nUsage of IC 7401:\n'
ic = IC_7401()

print '\nPin configuration\n'
p = {2:1,3:1,5:1,6:0,8:0,9:0,11:1,12:1}
print p

print '\nPin initialization ... '
ic.setIC(p)

print '\nPowering up the IC ...'
ic.setIC({14:1,7:0})

print '\nDraw the IC with the configuration ...'
ic.drawIC()

print '\nRun the IC with the current configuration ...'
print ic.run()

print '\nSet the outputs to the current IC configuration ...'
ic.setIC(ic.run())

print '\nThe final configuration ...'
ic.drawIC()

if(str(raw_input('Quit - Y/y or N/n - or Simply press Enter to Continue')).lower() == 'y'):
    sys.exit()







print '\nUsage of IC 7402:\n'
ic = IC_7402()

print '\nPin configuration\n'
p = {1:1,3:1,5:1,9:0,11:0,13:1}
print p

print '\nPin initialization ... '
ic.setIC(p)

print '\nPowering up the IC ...'
ic.setIC({14:1,7:0})

print '\nDraw the IC with the configuration ...'
ic.drawIC()

print '\nRun the IC with the current configuration ...'
print ic.run()

print '\nSet the outputs to the current IC configuration ...'
ic.setIC(ic.run())

print '\nThe final configuration ...'
ic.drawIC()

if(str(raw_input('Quit - Y/y or N/n - or Simply press Enter to Continue')).lower() == 'y'):
    sys.exit()











print '\nUsage of IC 7403:\n'
ic = IC_7403()

print '\nPin configuration\n'
p = {2:1,3:1,5:1,6:0,8:0,9:0,11:1,12:1}
print p

print '\nPin initialization ... '
ic.setIC(p)

print '\nPowering up the IC ...'
ic.setIC({14:1,7:0})

print '\nDraw the IC with the configuration ...'
ic.drawIC()

print '\nRun the IC with the current configuration ...'
print ic.run()

print '\nSet the outputs to the current IC configuration ...'
ic.setIC(ic.run())

print '\nThe final configuration ...'
ic.drawIC()

if(str(raw_input('Quit - Y/y or N/n - or Simply press Enter to Continue')).lower() == 'y'):
    sys.exit()










print '\nUsage of IC 7404:\n'
ic = IC_7404()

print '\nPin configuration\n'
p = {1:1,2:1,4:1,5:0,8:0,9:0,13:1,12:1}
print p

print '\nPin initialization ... '
ic.setIC(p)

print '\nPowering up the IC ...'
ic.setIC({14:1,7:0})

print '\nDraw the IC with the configuration ...'
ic.drawIC()

print '\nRun the IC with the current configuration ...'
print ic.run()

print '\nSet the outputs to the current IC configuration ...'
ic.setIC(ic.run())

print '\nThe final configuration ...'
ic.drawIC()

if(str(raw_input('Quit - Y/y or N/n - or Simply press Enter to Continue')).lower() == 'y'):
    sys.exit()











print '\nUsage of IC 7405:\n'
ic = IC_7405()

print '\nPin configuration\n'
p = {1:1,3:1,5:1,9:0,11:0,13:1}
print p

print '\nPin initialization ... '
ic.setIC(p)

print '\nPowering up the IC ...'
ic.setIC({14:1,7:0})

print '\nDraw the IC with the configuration ...'
ic.drawIC()

print '\nRun the IC with the current configuration ...'
print ic.run()

print '\nSet the outputs to the current IC configuration ...'
ic.setIC(ic.run())

print '\nThe final configuration ...'
ic.drawIC()

if(str(raw_input('Quit - Y/y or N/n - or Simply press Enter to Continue')).lower() == 'y'):
    sys.exit()








print '\nUsage of IC 7408:\n'
ic = IC_7408)

print '\nPin configuration\n'
p = {1:1,2:0,4:0,5:0,7:0,9:1,10:1,12:0,13:0,14:1}
print p

print '\nPin initialization ... '
ic.setIC(p)

print '\nDraw the IC with the configuration ...'
ic.drawIC()

print '\nRun the IC with the current configuration ...'
print ic.run()

print '\nSet the outputs to the current IC configuration ...'
ic.setIC(ic.run())

print '\nThe final configuration ...'
ic.drawIC()

if(str(raw_input('Quit - Y/y or N/n - or Simply press Enter to Continue')).lower() == 'y'):
    sys.exit()








print '\nUsage of IC 7410:\n'
ic = IC_7410()

print '\nPin configuration\n'
p = {1:1,2:0,13:0,3:0,4:0,5:0,9:1,10:1,11:1,14:1,7:0}
print p

print '\nPin initialization ... '
ic.setIC(p)

print '\nDraw the IC with the configuration ...'
ic.drawIC()

print '\nRun the IC with the current configuration ...'
print ic.run()

print '\nSet the outputs to the current IC configuration ...'
ic.setIC(ic.run())

print '\nThe final configuration ...'
ic.drawIC()

if(str(raw_input('Quit - Y/y or N/n - or Simply press Enter to Continue')).lower() == 'y'):
    sys.exit()








print '\nUsage of IC 7411:\n'
ic = IC_7411()

print '\nPin configuration\n'
p = {1:1,2:0,13:0,3:0,4:0,5:0,9:1,10:1,11:1,14:1,7:0}
print p

print '\nPin initialization ... '
ic.setIC(p)

print '\nDraw the IC with the configuration ...'
ic.drawIC()

print '\nRun the IC with the current configuration ...'
print ic.run()

print '\nSet the outputs to the current IC configuration ...'
ic.setIC(ic.run())

print '\nThe final configuration ...'
ic.drawIC()

if(str(raw_input('Quit - Y/y or N/n - or Simply press Enter to Continue')).lower() == 'y'):
    sys.exit()








print '\nUsage of IC 7412:\n'
ic = IC_7412()

print '\nPin configuration\n'
p = {1:1,2:0,13:0,3:0,4:0,5:0,9:1,10:1,11:1,14:1,7:0}
print p

print '\nPin initialization ... '
ic.setIC(p)

print '\nDraw the IC with the configuration ...'
ic.drawIC()

print '\nRun the IC with the current configuration ...'
print ic.run()

print '\nSet the outputs to the current IC configuration ...'
ic.setIC(ic.run())

print '\nThe final configuration ...'
ic.drawIC()

if(str(raw_input('Quit - Y/y or N/n - or Simply press Enter to Continue')).lower() == 'y'):
    sys.exit()








print '\nUsage of IC 7413:\n'
ic = IC_7413()

print '\nPin configuration\n'
p = {1:1,2:0,4:0,5:0,9:1,10:1,12:1,13:1,14:1,7:0}
print p

print '\nPin initialization ... '
ic.setIC(p)

print '\nDraw the IC with the configuration ...'
ic.drawIC()

print '\nRun the IC with the current configuration ...'
print ic.run()

print '\nSet the outputs to the current IC configuration ...'
ic.setIC(ic.run())

print '\nThe final configuration ...'
ic.drawIC()

if(str(raw_input('Quit - Y/y or N/n - or Simply press Enter to Continue')).lower() == 'y'):
    sys.exit()








print '\nUsage of IC 7415:\n'
ic = IC_7415()

print '\nPin configuration\n'
p = {1:1,2:0,13:0,3:0,4:0,5:0,9:1,10:1,11:1,14:1,7:0}
print p

print '\nPin initialization ... '
ic.setIC(p)

print '\nDraw the IC with the configuration ...'
ic.drawIC()

print '\nRun the IC with the current configuration ...'
print ic.run()

print '\nSet the outputs to the current IC configuration ...'
ic.setIC(ic.run())

print '\nThe final configuration ...'
ic.drawIC()

if(str(raw_input('Quit - Y/y or N/n - or Simply press Enter to Continue')).lower() == 'y'):
    sys.exit()








print '\nUsage of IC 7416:\n'
ic = IC_7416()

print '\nPin configuration\n'
p = {1:1,2:0,13:0,3:0,4:0,5:0,9:1,10:1,11:1,14:1,7:0}
print p

print '\nPin initialization ... '
ic.setIC(p)

print '\nDraw the IC with the configuration ...'
ic.drawIC()

print '\nRun the IC with the current configuration ...'
print ic.run()

print '\nSet the outputs to the current IC configuration ...'
ic.setIC(ic.run())

print '\nThe final configuration ...'
ic.drawIC()

if(str(raw_input('Quit - Y/y or N/n - or Simply press Enter to Continue')).lower() == 'y'):
    sys.exit()








print '\nUsage of IC 7417:\n'
ic = IC_7417()

print '\nPin configuration\n'
p = {1:1,2:0,13:0,3:0,4:0,5:0,9:1,10:1,11:1,14:1,7:0}
print p

print '\nPin initialization ... '
ic.setIC(p)

print '\nDraw the IC with the configuration ...'
ic.drawIC()

print '\nRun the IC with the current configuration ...'
print ic.run()

print '\nSet the outputs to the current IC configuration ...'
ic.setIC(ic.run())

print '\nThe final configuration ...'
ic.drawIC()

if(str(raw_input('Quit - Y/y or N/n - or Simply press Enter to Continue')).lower() == 'y'):
    sys.exit()








print '\nUsage of IC 7418:\n'
ic = IC_7418()

print '\nPin configuration\n'
p = {1:1,2:0,3:0,4:0,5:0,9:1,10:1,11:1,12:1,13:1,14:1,7:0}
print p

print '\nPin initialization ... '
ic.setIC(p)

print '\nDraw the IC with the configuration ...'
ic.drawIC()

print '\nRun the IC with the current configuration ...'
print ic.run()

print '\nSet the outputs to the current IC configuration ...'
ic.setIC(ic.run())

print '\nThe final configuration ...'
ic.drawIC()

if(str(raw_input('Quit - Y/y or N/n - or Simply press Enter to Continue')).lower() == 'y'):
    sys.exit()








print '\nUsage of IC 7419:\n'
ic = IC_7419()

print '\nPin configuration\n'
p = {1:1,2:0,13:0,3:0,4:0,5:0,9:1,10:1,11:1,14:1,7:0}
print p

print '\nPin initialization ... '
ic.setIC(p)

print '\nDraw the IC with the configuration ...'
ic.drawIC()

print '\nRun the IC with the current configuration ...'
print ic.run()

print '\nSet the outputs to the current IC configuration ...'
ic.setIC(ic.run())

print '\nThe final configuration ...'
ic.drawIC()

if(str(raw_input('Quit - Y/y or N/n - or Simply press Enter to Continue')).lower() == 'y'):
    sys.exit()








print '\nUsage of IC 7420:\n'
ic = IC_7420()

print '\nPin configuration\n'
p = {1:1,2:0,4:0,5:0,9:1,10:1,12:1,13:1,14:1,7:0}
print p

print '\nPin initialization ... '
ic.setIC(p)

print '\nDraw the IC with the configuration ...'
ic.drawIC()

print '\nRun the IC with the current configuration ...'
print ic.run()

print '\nSet the outputs to the current IC configuration ...'
ic.setIC(ic.run())

print '\nThe final configuration ...'
ic.drawIC()

if(str(raw_input('Quit - Y/y or N/n - or Simply press Enter to Continue')).lower() == 'y'):
    sys.exit()