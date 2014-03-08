# Example for Binary Counter a 2 bit counter.

from __future__ import print_function
from BinPy.tools.digital import Clock
from BinPy.Sequential.counters import BinaryCounter
from BinPy.Gates import Connector

# Initialize the clock
clock = Clock(1, 1)
clock.start()
# A clock of 1 hertz frequency
clk_conn = clock.A

b = BinaryCounter(clk_conn)

print ('INITIAL STATE')
print (b.state())

print ('TRIGGERING THE COUNTER SEQUENTIALLY')

for i in range(5):
    b.trigger()
    print (b.state())
