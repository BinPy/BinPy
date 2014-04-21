
# coding: utf-8

# Examples for XOR class

# In[1]:

# imports
from __future__ import print_function
from BinPy.Gates import *


# In[2]:

# Initializing the XOR class

gate = XOR(0, 1)

# Output of the XOR gate

print (gate.output())


# In[3]:

# Input changes
# Input at index 1 is changed to 0

gate.setInput(1, 0)

# New Output of the XOR gate

print (gate.output())


# In[4]:

# Changing the number of inputs

# No need to set the number, just change the inputs

gate.setInputs(1, 1, 1, 1)

# To get the input states

print (gate.getInputStates())


# In[5]:

# New output of the XOR gate

print (gate.output())


# In[6]:

# Using Connectors as the input lines

# Take a Connector

conn = Connector()


# In[7]:

# Set Output of gate to Connector conn

gate.setOutput(conn)


# In[8]:

# Put this connector as the input to gate1

gate1 = XOR(conn, 0)


# In[9]:

# Output of the gate1

print (gate1.output())


# In[10]:

# Information about gate instance

print (gate)
