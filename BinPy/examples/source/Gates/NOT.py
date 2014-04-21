
# coding: utf-8

# Examples for NOT class

# In[1]:

# imports
from __future__ import print_function
from BinPy.Gates import *


# In[2]:

# Initializing the NOT class

gate = NOT(0)

# Output of the NOT gate

print (gate.output())


# In[3]:

# Input is changed to 0

gate.setInput(1)

# To get the input states

print (gate.getInputStates())


# In[4]:

# New Output of the NOT gate

print (gate.output())


# In[5]:

# Using Connectors as the input lines

# Take a Connector

conn = Connector()

# Set Output of gate to Connector conn

gate.setOutput(conn)

# Put this connector as the input to gate1

gate1 = NOT(conn)

# Output of the gate1

print (gate1.output())


# In[6]:

# Information about gate instance

print (gate)
