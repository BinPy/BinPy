# Example for 4Bit Decade Counter.

from __future__ import print_function
from BinPy.tools.digital import Clock
from BinPy.Sequential.counters import DecadeCounter
from BinPy.Gates import Connector
from BinPy.tools.oscilloscope import Oscilloscope

toggle = Connector(1)

# Initialize the clock
clock = Clock(1, 25)
clock.start()
# A clock of 50 hertz frequency
clk_conn = clock.A

enable = Connector(1)

print ("Setting No of Bits to 4")
print ("Clock frequency is 100 Hz")

# Initializing the counter
b = DecadeCounter(clk_conn)

# Initiating the oscilloscope
o = Oscilloscope((clk_conn, 'CLK'), (b.out[0], 'BIT3'), (b.out[1], 'BIT2'), (
    b.out[2], 'BIT1'), (b.out[3], 'BIT0'), (enable, 'EN1'))
o.start()
o.setScale(0.001)  # Set scale by trial and error.
o.unhold()

print ("INITIAL STATE")
print (b.state())

print ("TRIGGERING THE COUNTER SEQUENTIALLY 2^4 + 1 times")

for i in range(1, 2 ** 4 + 1):
    b.trigger()
    print (b.state())

o.display()
o.kill()
clock.kill()
