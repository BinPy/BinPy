
# coding: utf-8

# Examples for NOR class

# In[1]:

# imports
from __future__ import print_function
from BinPy.Gates import *


# In[2]:

# Initializing the NOR class

gate = NOR(0, 1)

# Output of the NOR gate

print (gate.output())


# In[3]:

# Input changes

# Input at index 1 is changed to 0

gate.setInput(1, 0)

# New Output of the NOR gate

print (gate.output())


# In[4]:

# Changing the number of inputs

# No need to set the number, just change the inputs

gate.setInputs(1, 1, 1, 1)

# To get the input states

print (gate.getInputStates())


# In[5]:

# New output of the NOR gate

print (gate.output())


# In[6]:

# Using Connectors as the input lines

# Take a Connector

conn = Connector()

# Set Output of gate to Connector conn

gate.setOutput(conn)

# Put this connector as the input to gate1

gate1 = NOR(conn, 0)


# In[7]:

# Output of the gate1

print (gate1.output())


# In[8]:

# Information about gate instance

print (gate)
