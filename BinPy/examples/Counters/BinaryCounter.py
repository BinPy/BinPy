# Example for Binary Counter a n bit counter.

from __future__ import print_function
from BinPy.tools.digital import Clock
from BinPy.Sequential.counters import BinaryCounter
from BinPy.Gates import Connector
from BinPy.tools.oscilloscope import Oscilloscope
import time

print("Initializing the Clock")
print("clock = Clock(0, 1)")
print("clock.start()")
clock = Clock(0, 1)
clock.start()
# A clock of 1 hertz frequency
print("clk_conn = clock.A")
clk_conn = clock.A
print("\n")
print("Initializing Binary Counter with 2 bits and clock_conn")
print("b = BinaryCounter(2, clk_conn)")
b = BinaryCounter(2, clk_conn)

print("\n")
print("Initializing the Oscillioscope")
print("o=Oscilloscope((clk_conn, 'CLK'), (b.out[0], 'MSB'), (b.out[1],
                                                             'LSB')')")
print("o.start() # starting the oscillioscope")
print("o.setScale(0.05) # setting the scale")

o = Oscilloscope((clk_conn, 'CLK'), (b.out[0], 'MSB'), (b.out[1], 'LSB'))
o.start()
o.setScale(0.05)  # Set scale by trial and error.
print("o.unhold() #then unhold")
o.unhold()

print ("Initial State")
print (b.state())

print("\n")
print ("Triggering the counter Sequentially")
print ("
       for i in range(5):
       b.trigger()
       print (b.state())")

for i in range(5):
    b.trigger()
    print (b.state())

print("\n")
print ("Displey the time-Waveform")
print ("o.display()")
print ("clock.kill()")
print ("o.kill()")
o.display()
clock.kill()
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
