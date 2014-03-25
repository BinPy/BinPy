# Example for N Bit Johnson Counter.

from __future__ import print_function
from BinPy.tools.digital import Clock
from BinPy.Sequential.counters import JohnsonCounter
from BinPy.Gates import Connector

# Initialize the clock
clock = Clock(1, 10)
clock.start()

print ("Setting No of Bits to 8")
print ("Clock frequency is 10 Hz")

# Initializing the counter
b = JohnsonCounter(8, clk_conn)

print ("INITIAL STATE")
print (b.state())

print ("TRIGGERING THE COUNTER 16 times")

for i in range(16):
    b.trigger()
    print (b.state())
