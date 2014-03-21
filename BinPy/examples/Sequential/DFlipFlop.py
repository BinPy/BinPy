# Example for DFlipFlop

from __future__ import print_function
from BinPy.Sequential.sequential import DFlipFlop
from BinPy.tools.digital import Clock
from BinPy.Gates import Connector

data = Connector(1)

p = Connector(0)
q = Connector(1)

# Initialize the clock
clock = Clock(1, 1)
clock.start()
# A clock of 1 hertz frequency
clk_conn = clock.A

enable = Connector(1)

# Initialize the D-FlipFlop
dff = DFlipFlop(data, enable, clk_conn, a=p, b=q)
# To connect different set of connectors use :
# dff.setInputs(conn1,enab,clk)
# To connect different outputs use s.setOutputs(op1,op2)
dff.setOutputs(A=p, B=q)

print ("Data is 1")
data.state = 1
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        dff.trigger()
        break
print (dff.state())

# Sending a positive edge to dff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        dff.trigger()
        break

print ("Data is 0")
data.state = 0
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        dff.trigger()
        break
print (dff.state())
# Sending a positive edge to dff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        dff.trigger()
        break

print ("Data is 1")
data.state = 1
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        dff.trigger()
        break
print (dff.state())
# Sending a positive edge to dff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        dff.trigger()
        break
