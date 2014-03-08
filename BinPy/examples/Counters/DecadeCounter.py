# Example for 4Bit Decade Counter.

from __future__ import print_function
from BinPy.tools.digital import Clock
from BinPy.Sequential.counters import DecadeCounter
from BinPy.Gates import Connector

toggle = Connector(1)

# Initialize the clock
clock = Clock(1, 100)
clock.start()
# A clock of 100 hertz frequency
clk_conn = clock.A

enable = Connector(1)

print ("Setting No of Bits to 4")
print ("Clock frequency is 100 Hz")

# Initializing the counter
b = DecadeCounter(clk_conn)

print ("INITIAL STATE")
print (b.state())

print ("TRIGGERING THE COUNTER SEQUENTIALLY 2^4 + 1 times")

for i in range(1, 2 ** 4 + 1):
    b.trigger()
    print (b.state())

clock.kill()
