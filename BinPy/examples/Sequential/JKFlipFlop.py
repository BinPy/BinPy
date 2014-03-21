# Example for JKFlipFlop

from __future__ import print_function
from BinPy.Sequential.sequential import JKFlipFlop
from BinPy.tools.digital import Clock
from BinPy.Gates import Connector

j = Connector(1)
k = Connector(0)

p = Connector(0)
q = Connector(1)

# Initialize the clock
clock = Clock(1, 1)
clock.start()
# A clock of 1 hertz frequency
clk_conn = clock.A

enable = Connector(1)

jkff = JKFlipFlop(j, k, enable, clk_conn, clear=enable)

# To connect outputs use s.setOutputs(op1,op2)
jkff.setOutputs(A=p, B=q)

print ("SET STATE - J = 1, K = 0")
# Set State
j.state = 1
k.state = 0
# The same thing can also be done by --> jkff.setInputs(j = 1, k = 0)
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        jkff.trigger()
        break
print (jkff.state())

# Sending a positive edge to jkff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        jkff.trigger()
        break


print ("RESET STATE - J = 0, K = 1")
# Reset State
j.state = 0
k.state = 1
# The same thing can also be done by --> jkff.setInputs(j = 1, k = 0)
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        jkff.trigger()
        break
print ("[Printing the output using the output connectors:]\n", p(), q())

# Sending a positive edge to jkff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        jkff.trigger()
        break


print ("TOGGLE STATE - J = 1, K = 1")
# Toggle State
j.state = 1
k.state = 1
# The same thing can also be done by --> jkff.setInputs(j = 1, k = 0)
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        jkff.trigger()
        break
print (jkff.state())

# Sending a positive edge to jkff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        jkff.trigger()
        break


print ("NO CHANGE STATE - J = 0, K = 0")
# No change state
j.state = 0
k.state = 0
# The same thing can also be done by --> jkff.setInputs(j = 1, k = 0)
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        jkff.trigger()
        break
print (jkff.state())

# Sending a positive edge to jkff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        jkff.trigger()
        break

# To connect different set of connectors use s.setInputs(conn1,conn2,enab)
