
# coding: utf-8

# Monostable Multivibrator - Multivibrator in Mode 1

# In[1]:

from __future__ import print_function
from BinPy.tools.clock import Clock
from BinPy.connectors import Connector
from BinPy.tools.multivibrator import Multivibrator
from BinPy.tools.oscilloscope import Oscilloscope
import time


# In[2]:

# MODE selects the mode of operation of the multivibrator.

# Mode No. :  Description
#   1          Monostable
#   2          Astable
#   3          Bistable

out = Connector()


# In[3]:

# Initialize mutivibrator in MODE 1

m = Multivibrator(0, mode=1, time_period=1)
m.start()
m.setOutput(out)


# In[4]:

# Initialize the oscilloscope
o = Oscilloscope((out, 'OUT'))
o.start()
o.set_scale(0.005)  # Set scale by trial and error.
o.set_width(100)
o.unhold()
time.sleep(0.1)
m.trigger()  # Also works with m()
time.sleep(0.1)


# In[5]:

# Display the oscilloscope
o.display()


# In[6]:

# Kill the multivibrator and the oscilloscope threads
m.kill()
o.kill()
