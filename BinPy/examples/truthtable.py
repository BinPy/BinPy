from BinPy import *


print ('Initialising IC_4001:\n-- t = IC4001()\n')
t=IC_4001()
print ('\nGiving a pinConfig in the form of a dict:')
p = {'i':[13,12],'o':[11]}
print ('--p =')+(str(p))
print ('\nRunning the truthtable method:\n-- t.truthtable(p)\n')

t.truthtable(p)
