
# coding: utf-8

# Example for Decade Counter.

# In[27]:

# imports

from __future__ import print_function
from BinPy.tools import Clock
from BinPy.Sequential.counters import DecadeCounter
from BinPy.Gates import Connector
from BinPy.tools.oscilloscope import Oscilloscope


# In[28]:

# Initialize a toggle connectr for inpput in TFlipFlop

toggle = Connector(1)


# In[29]:

# Initializing the Clock
# A clock of 5 hertz frequency

clock = Clock(1, 5)

clock.start()

clk_conn = clock.A


# In[30]:

# Initialize enable

enable = Connector(1)


# In[31]:

# Initializing the counter

# Initializing DecadeCounter with clock_conn

b = DecadeCounter(clk_conn)


# In[32]:

# Initiating the oscilloscope

o = Oscilloscope((clk_conn, 'CLK'), (b.out[0], 'BIT3'), (b.out[1], 'BIT2'), (
    b.out[2], 'BIT1'), (b.out[3], 'BIT0'), (enable, 'EN1'))

# starting the oscillioscope thread - This does not initiate the recording.

o.start()

# setting the scale

o.setScale(0.05)  # Set scale by trial and error.

# Set the width of the oscilloscope to fit the ipython notebook.

o.setWidth(100)


# In[33]:

# unhold the oscilloscope to start the recording.

o.unhold()

# Initial State

print (b.state())

# Triggering the counter sequentially 2^4 times

for i in range(1, 2 ** 4):
    b.trigger()
    print (b.state())

# Display the oscilloscope - Implicitly the o.hold() will be called first
# to stop the recording.

o.display()


# In[34]:

# Calling the instance will trigger

b()

print(b.state())


# In[35]:

# Setting the Counter

b.setCounter()

print(b.state())


# In[36]:

# Resetting the Counter

b.resetCounter()

print(b.state())


# In[37]:

# Disabling the Counter

b.disable()

b.trigger()

print(b.state())


# In[38]:

# Enabling the Counter

b.enable()

b.trigger()

print(b.state())


# In[39]:

# Kill the oscilloscope thread

o.kill()

# Kill the clock thread

clock.kill()
