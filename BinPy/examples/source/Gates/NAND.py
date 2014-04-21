
# coding: utf-8

### Examples for NAND class

# In[1]:

from __future__ import print_function
from BinPy.Gates import *


# In[2]:

# Initializing the NAND class

gate = NAND(0, 1)

# Output of the NAND gate

print (gate.output())


# In[3]:

# Input changes

# Input at index 1 is changed to 0

gate.setInput(1, 0)

# New Output of the NAND gate

print (gate.output())


# In[4]:

# Changing the number of inputs

# No need to set the number, just change the inputs

gate.setInputs(1, 1, 1, 1)

# To get the input states

print (gate.getInputStates())

# New output of the NAND gate

print (gate.output())


# In[5]:

# Using Connectors as the input lines

# Take a Connector

conn = Connector()

# Set Output of gate to Connector conn

gate.setOutput(conn)
# Put this connector as the input to gate1

gate1 = NAND(conn, 0)

# Output of the gate1

print (gate1.output())


# In[6]:

# Information about gate instance

print (gate)

