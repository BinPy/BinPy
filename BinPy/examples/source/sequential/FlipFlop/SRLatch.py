# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Example for SRLatch

# <codecell>

from __future__ import print_function
from BinPy.Sequential.sequential import SRLatch
from BinPy.tools.clock import Clock
from BinPy.Gates import Connector
from BinPy.tools.oscilloscope import Oscilloscope

# <codecell>

s = Connector(1)
r = Connector(0)

p = Connector(0)
q = Connector(1)

# <codecell>

# Initialize the clock
clock = Clock(1, 4)
clock.start()
# A clock of 1 hertz frequency
clk_conn = clock.A

enable = Connector(1)

# <codecell>

# Initialize the sr latch
srff = SRLatch(s, r, enable, clk_conn)

# To connect outputs use s.setOutputs(op1,op2)
srff.setOutputs(A=p, B=q)

# <codecell>

# Initialize the oscilloscope

o = Oscilloscope((clk_conn, 'CLK'), (s, 'S'), (
    r, 'R'), (p, 'OUT'), (q, 'OUT!'), (enable, 'ENABLE'))
o.start()
o.setScale(0.015)  # Set scale by trial and error.
o.setWidth(100)
o.unhold()

# <codecell>

print("SET STATE - S = 1, R = 0")
# Set State
s.state = 1
r.state = 0
# The same thing can also be done by --> srff.setInputs(s = 1, r = 0)
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        srff.trigger()
        break
print(srff.state())
# Sending a positive edge to srff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        srff.trigger()
        break

# <codecell>

print("RESET STATE - S = 0, R = 1")
# Reset State
s.state = 0
r.state = 1
# The same thing can also be done by --> srff.setInputs(s = 1, r = 0)
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        srff.trigger()
        break
# Displaying the output using the connector instances
print("[", p(), ",", q(), "]")

# Sending a positive edge to srff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        srff.trigger()
        break

# <codecell>

print("INVALID STATE - S = 1, R = 1")
# Invalid state
s.state = 1
r.state = 1
# The same thing can also be done by --> srff.setInputs(s = 1, r = 1)
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        srff.trigger()
        break
print(srff.state())

# Sending a positive edge to srff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        srff.trigger()
        break

# <codecell>

print("2nd INVALID STATE - S = 0, R = 0")
# Invalid state
s.state = 1
r.state = 1
# The same thing can also be done by --> srff.setInputs(s = 1, r = 1)
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        srff.trigger()
        break
print(srff.state())

# Sending a positive edge to srff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        srff.trigger()
        break

# <codecell>

# Display the oscilloscope
o.display()

# <codecell>

# Kill the clock and the oscilloscope threads after use
o.kill()
clock.kill()
