
# coding: utf-8

### Example for Octal Counter.

# In[1]:

# imports
from __future__ import print_function
from BinPy.tools import Clock
from BinPy.Sequential.counters import OctalCounter
from BinPy.Gates import Connector
from BinPy.tools.oscilloscope import Oscilloscope


# In[2]:

# Initialize a toggle connectr for inpput in TFlipFlop

toggle = Connector(1)

# Initializing the Clock
# A clock of 5 hertz frequency

clock = Clock(1, 5)
clock.start()

# Initialize enable

enable = Connector(1)

# Initializing OctalCounter with 4 bits and clock

b = OctalCounter(clock.A)


# In[3]:

# Initializing the Oscillioscope

# starting the oscillioscope
# setting the scale

o = Oscilloscope((clock.A, 'CLK'), (b.out[0], 'BIT3'), (b.out[1], 'BIT2'), (
    b.out[2], 'BIT1'), (b.out[3], 'BIT0'), (enable, 'EN1'))

o.start()

o.setWidth(100)

o.setScale(0.05)  # Set scale by trial and error.

o.unhold()


# In[4]:

# Initial State

print (b.state())


# In[5]:

# Triggering the counter sequentially 2^4 + 2 times

for i in range(1, 2 ** 4 + 2):
    b.trigger()
    print (b.state())

o.display()


# In[6]:

# Calling the instance will trigger

b()

print(b.state())


# In[7]:

# Setting the Counter

b.setCounter()

print(b.state())


# In[8]:

# Resetting the Counter

b.resetCounter()

print(b.state())


# In[9]:

# Disabling the Counter

b.disable()
b.trigger()

print(b.state())


# In[10]:

# Enabling the Counter

b.enable()
b.trigger()

print(b.state())


# In[11]:

# Kill the oscilloscope and the clock threads after use.

o.kill()
clock.kill()

