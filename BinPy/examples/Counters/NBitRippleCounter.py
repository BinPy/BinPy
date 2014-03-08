# Example for N Bit Binary Ripple Counter.

from __future__ import print_function
from BinPy.tools.digital import Clock
from BinPy.Sequential.counters import NBitRippleCounter
from BinPy.Gates import Connector

toggle = Connector(1)

# Initialize the clock
clock = Clock(1, 100)
clock.start()
# A clock of 100 hertz frequency
clk_conn = clock.A

enable = Connector(1)

print ("Setting No of Bits to 8")
print ("Clock frequency is 100 Hz")

# Initializing the counter
b = NBitRippleCounter(8, clk_conn)

print ("INITIAL STATE")
print (b.state())

print ("TRIGGERING THE COUNTER SEQUENTIALLY 2^8 + 1 times")

for i in range(1, 2 ** 8 + 1):
    b.trigger()
    print (b.state())
