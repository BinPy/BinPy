# Example for N Bit Ring Counter.

from __future__ import print_function
from BinPy.tools.digital import Clock
from BinPy.Sequential.counters import RingCounter
from BinPy.Gates import Connector

print("Initializing the Clock")
print("clock = Clock(1, 50)")
print("clock.start()")
clock = Clock(1, 50)
clock.start()
# A clock of 100 hertz frequency
print("clk_conn = clock.A")
clk_conn = clock.A
print("\n")

print("Initialize enable")
print("enable = Connector(1)")
enable = Connector(1)

print ("Setting No of Bits to 4")
print ("Clock frequency is 10 Hz")

# Initializing the counter
print("\n")
print("Initializing RingCounter with 8 bits and clock_conn")
print("b = RingCounter(8, clk_conn)")
b = RingCounter(8, clk_conn)

print ("Initial State")
print (b.state())

print ("Triggering the counter 8 times")
print("for i in range(8):\nb.trigger()\nprint (b.state())")

for i in range(8):
    b.trigger()
    print (b.state())

print("\n")
print("Calling the instance will trigger")
print("b()")
b()
print("b.state()")
print(b.state())

print("\n")
print("Setting the Counter")
print("b.setCounter()")
b.setCounter()
print("b.state()")
print(b.state())

print("\n")
print("Resetting the Counter")
print("b.resetCounter()")
b.resetCounter()
print("b.state()")
print(b.state())

print("\n")
print("Disabling the Counter")
print("b.disable()\nb.trigger()")
b.disable()
b.trigger()
print("b.state()")
print(b.state())

print("\n")
print("Enabling the Counter")
print("b.enable()\nb.trigger()")
b.enable()
b.trigger()
print("b.state()")
print(b.state())
