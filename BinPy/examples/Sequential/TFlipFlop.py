# Example for TFlipFlop

from __future__ import print_function
from BinPy.Sequential.sequential import TFlipFlop
from BinPy.tools.digital import Clock
from BinPy.Gates import Connector
from BinPy.tools.oscilloscope import Oscilloscope

toggle = Connector(1)

p = Connector(0)
q = Connector(1)

# Initialize the clock
clock = Clock(1, 4)
clock.start()
# A clock of 4 hertz frequency
clk_conn = clock.A

enable = Connector(1)

# Initialize the T-FlipFlop
tff = TFlipFlop(toggle, enable, clk_conn, a=p, b=q)

# To connect different set of connectors use :
# tff.setInputs(conn1,enab,clk)
# To connect different outputs use:
tff.setOutputs(A=p, B=q)

o = Oscilloscope((clk_conn, 'CLK'), (toggle, 'TOGGLE'), (
    p, 'OUT'), (q, 'OUT!'), (enable, 'ENABLE'))
o.start()
o.setScale(0.01)  # Set scale by trial and error.
o.unhold()

print ("Toggle is 1")
toggle.state = 1
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        tff.trigger()
        break
print (tff.state())

# Sending a positive edge to ff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        tff.trigger()
        break

print ("Toggle is 1")
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        tff.trigger()
        break
print (tff.state())

# Sending a positive edge to ff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        tff.trigger()
        break

print ("Toggle is 1")
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        tff.trigger()
        break
print (tff.state())

# Sending a positive edge to ff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        tff.trigger()
        break

print ("Toggle is 0")
toggle.state = 0
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        tff.trigger()
        break
print (tff.state())

# Sending a positive edge to ff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        tff.trigger()
        break

print ("Toggle is 0")
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        tff.trigger()
        break
print (tff.state())

# Sending a positive edge to ff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        tff.trigger()
        break
o.display()
o.kill()
clock.kill()
