# Example for N Bit Ring Counter.

from __future__ import print_function
from BinPy.tools.digital import Clock
from BinPy.Sequential.counters import RingCounter
from BinPy.Gates import Connector

# Initialize the clock
clock = Clock(1, 10)
clock.start()
# A clock of 10 hertz frequency
clk_conn = clock.A

print ("Setting No of Bits to 8")
print ("Clock frequency is 10 Hz")

# Initializing the counter
b = RingCounter(8, clk_conn)

print ("INITIAL STATE")
print (b.state())

print ("TRIGGERING THE COUNTER 8 times")

for i in range(8):
    b.trigger()
    print (b.state())
