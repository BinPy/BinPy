# Example for N Bit Binary Ripple Counter.

from __future__ import print_function
from BinPy.tools.digital import Clock
from BinPy.Sequential.counters import NBitRippleCounter
from BinPy.Gates import Connector
from BinPy.tools.oscilloscope import Oscilloscope

print("Initialize a toggle connectr for inpput in TFlipFlop")
print("toggle = Connector(1)")
toggle = Connector(1)

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
print("Initializing Ripple Counter with 4 bits and clock_conn")
print("b = NBitRippleCounter(4, clk_conn)")
b = NBitRippleCounter(4, clk_conn)

# Initiating the oscilloscope
print("\n")
print("Initializing the Oscillioscope")
print(
    "o = Oscilloscope((clk_conn, 'CLK'), (b.out[0], 'BIT3'), (b.out[1], 'BIT2'), (\
    b.out[2], 'BIT1'), (b.out[3], 'BIT0'), (enable, 'EN1'))")
print("o.start() # starting the oscillioscope")
print("o.setScale(0.05) # setting the scale")
o = Oscilloscope((clk_conn, 'CLK'), (b.out[0], 'BIT3'), (b.out[1], 'BIT2'), (
    b.out[2], 'BIT1'), (b.out[3], 'BIT0'), (enable, 'EN1'))
o.start()
o.setScale(0.0005)  # Set scale by trial and error.
o.unhold()


print ("Initial State")
print (b.state())

print ("Triggering the counter sequentially 2^4 + 1 times")

for i in range(1, 2 ** 4 + 1):
    b.trigger()
    print (b.state())
o.display()
o.kill()

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
clock.kill()
