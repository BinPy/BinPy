
# coding: utf-8

# Example for N Bit Johnson Counter.

# In[1]:

# imports

from __future__ import print_function
from BinPy.tools import Clock
from BinPy.Sequential.counters import JohnsonCounter
from BinPy.Gates import Connector


# In[2]:

# Initializing the Clock
# A clock of 50 hertz frequency

clock = Clock(1, 50)
clock.start()


# In[3]:

# Initialize enable

enable = Connector(1)

# Initializing the counter

# Initializing Johnson with 8 bits and clock

b = JohnsonCounter(8, clock)

# Initial State

print(b.state())


# In[4]:

# Triggering the counter 24 times

for i in range(24):
    b.trigger()
    print(b.state())

# Calling the instance will trigger

b()

print(b.state())


# In[5]:

# Setting the Counter

# b.setCounter()

print(b.state())


# In[6]:

# Resetting the Counter

# b.resetCounter()

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

# Kill the clock thread after use

clock.kill()
