
# coding: utf-8

### Example for N Bit Ring Counter.

# In[1]:

# imports
from __future__ import print_function
from BinPy.tools import Clock
from BinPy.Sequential.counters import RingCounter
from BinPy.Gates import Connector


# In[2]:

# Initializing the Clock
# Clock frequency is 50 Hz

clock = Clock(1, 50)
clock.start()


# In[3]:

# Initialize enable

enable = Connector(1)


# In[4]:

# Initializing RingCounter with 8 bits and clock

b = RingCounter(8, clock)


# In[5]:

# Initial State

print (b.state())


# In[6]:

# Triggering the counter 8 times

for i in range(8):
    b.trigger()
    print (b.state())


# In[7]:

# Calling the instance will trigger

b()

print(b.state())


# In[8]:

# Setting the Counter

# b.setCounter()

print(b.state())


# In[9]:

# Resetting the Counter

# b.resetCounter()

print(b.state())


# In[10]:

# Disabling the Counter

b.disable()
b.trigger()

print(b.state())


# In[11]:

# Enabling the Counter

b.enable()
b.trigger()

print(b.state())


# In[12]:

# Kill the clock thread.

clock.kill()

