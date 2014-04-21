
# coding: utf-8

# Example for Binary Counter [ A 2 bit Ripple Counter ]

# In[1]:

# Imports

from __future__ import print_function
from BinPy.tools.clock import Clock
from BinPy.Sequential.counters import BinaryCounter
from BinPy.Gates import Connector
from BinPy.tools.oscilloscope import Oscilloscope
import time


# In[2]:

# A clock of 1 hertz frequency  With initial value as 0

clock = Clock(0, 1)
clock.start()
clk_conn = clock.A


# In[3]:

# Initializing Binary Counter with 2 bits and clock_conn
b = BinaryCounter(2, clk_conn)

# Initializing the Oscillioscope
o = Oscilloscope((clk_conn, 'CLK'), (b.out[0], 'MSB'), (b.out[1], 'LSB'))

# Starting the oscillioscope
o.start()

# Set scale by trial and error.
o.setScale(0.15)

# Set the width of the oscilloscope [ To fit the ipython Notebook ]
o.setWidth(100)


# In[4]:

# Then unhold [ Run the Oscilloscope ]
o.unhold()

print(b.state())

# Triggering the Binary Counter 10 times.
for i in range(10):
    b.trigger()
    print (b.state())

# Display the time-Waveform.
o.display()

# Kill the oscilloscope thread.
o.kill()


# In[5]:

# Calling the instance will also trigger the counter.
print("b()")


# In[6]:

# Setting the Counter

b.setCounter()

print(b.state())


# In[7]:

# Resetting the Counter

b.resetCounter()

print(b.state())


# In[8]:

# Disabling the Counter

b.disable()

# Now triggering it has no effect.

b.trigger()

print(b.state())


# In[9]:

# Enabling the Counter

b.enable()
b.trigger()

print(b.state())


# In[10]:

# Kill the clock thread.
clock.kill()
