
# coding: utf-8

# Example for N Bit Binary Ripple Counter.

# In[1]:

# imports
from __future__ import print_function
from BinPy.tools import Clock
from BinPy.Sequential.counters import NBitRippleCounter
from BinPy.Gates import Connector
from BinPy.tools.oscilloscope import Oscilloscope


# In[2]:

# Initialize a toggle connectr for inpput in TFlipFlop

toggle = Connector(1)

# Initializing the Clock
# A clock of 10 hertz frequency

clock = Clock(1, 10)
clock.start()
clk_conn = clock.A

# Initialize enable

enable = Connector(1)


# In[3]:

# Setting No of Bits to 4

# Clock frequency is 10 Hz

# Initializing Ripple Counter with 4 bits and clock_conn

b = NBitRippleCounter(4, clk_conn)

# Initiating the Oscilloscope

o = Oscilloscope((clk_conn, 'CLK'), (b.out[0], 'BIT3'), (b.out[1], 'BIT2'), (
    b.out[2], 'BIT1'), (b.out[3], 'BIT0'), (enable, 'EN1'))

o.start()

o.setScale(0.035)  # Set scale by trial and error.

o.setWidth(100)

o.unhold()

# Initial State

print (b.state())

# Triggering the counter sequentially 2^4 + 1 times

for i in range(1, 2 ** 4 + 1):
    b.trigger()
    print (b.state())

o.display()


# In[4]:

# Calling the instance will trigger

b()

print(b.state())


# In[5]:

# Setting the Counter

b.setCounter()

print(b.state())


# In[6]:

# Resetting the Counter

b.resetCounter()

print(b.state())


# In[7]:

# Disabling the Counter

b.disable()
b.trigger()

print(b.state())


# In[8]:

# Enabling the Counter

b.enable()
b.trigger()

print(b.state())


# In[9]:

# Kill the clock and the oscilloscope threads.

o.kill()
clock.kill()
