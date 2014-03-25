# Example for Binary Counter a 2 bit counter.

from __future__ import print_function
from BinPy.tools.digital import Clock
from BinPy.Sequential.counters import BinaryCounter
from BinPy.Gates import Connector
from BinPy.tools.oscilloscope import Oscilloscope
import time

# Initialize the clock
clock = Clock(0, 1)
clock.start()
# A clock of 1 hertz frequency
clk_conn = clock.A

b = BinaryCounter(clk_conn)

# Initiating the oscilloscope
o = Oscilloscope((clk_conn, 'CLK'), (b.out[0], 'MSB'), (b.out[1], 'LSB'))
o.start()
o.setScale(0.05)  # Set scale by trial and error.
o.unhold()

print ('INITIAL STATE')
print (b.state())

print ('TRIGGERING THE COUNTER SEQUENTIALLY')

for i in range(5):
    b.trigger()
    print (b.state())

print ('DISPLAYING THE TIME-WAVEFORM')
o.display()
clock.kill()
o.kill()
