
# coding: utf-8

### Example for Half Adder class.

# In[1]:

# Imports

from __future__ import print_function
from BinPy.Combinational.combinational import *


# In[2]:

# Initializing the HalfAdder class

ha = HalfAdder(0, 1)

# Output of HalfAdder

print (ha.output())


# In[3]:

# The output is of the form [SUM, CARRY]"

# Input changes

# Input at index 1 is changed to 0

ha.setInput(1, 0)

# New Output of the HalfAdder

print (ha.output())


# In[4]:

# Changing the number of inputs

# No need to set the number, just change the inputs

# Input length must be two

ha.setInputs(1, 1)

# To get the input states

print (ha.getInputStates())


# In[5]:

# New output of HalfAdder

print (ha.output())


# In[6]:

# Using Connectors as the input lines

# Take a Connector

conn = Connector()

# Set Output at index to Connector conn

ha.setOutput(0, conn)

# Put this connector as the input to gate1

gate1 = AND(conn, 0)

# Output of the gate1

print (gate1.output())


# In[7]:

# Information about ha instance can be found by

print (ha)

