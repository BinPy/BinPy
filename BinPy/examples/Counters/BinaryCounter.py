#Example for Binary Counter a 2 bit counter.

from BinPy import *

#Initialize the clock
clock = Clock(1,1)
clock.start()
#A clock of 1 hertz frequency
clk_conn = clock.A

b = BinaryCounter(clk_conn)

print 'INITIAL STATE'
print b.state()

print 'TRIGGERING THE COUNTER SEQUENTIALLY'

b.trigger()
print b.state()

b.trigger()
print b.state()

b.trigger()
print b.state()

b.trigger()
print b.state()

b.trigger()
print b.state()

b.trigger()
print b.state()