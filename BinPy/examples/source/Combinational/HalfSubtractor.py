
# coding: utf-8

# Example for Half Subtractor class

# In[1]:

# Imports
from __future__ import print_function
from BinPy.Combinational.combinational import *


# In[2]:

# Initializing the HalfSubtractor class

hs = HalfSubtractor(0, 1)

# Output of HalfSubtractor

print (hs.output())


# In[3]:

# The output is of the form [DIFFERENCE, BORROW]

# Input changes

# Input at index 1 is changed to 0

hs.setInput(1, 0)

# New Output of the HalfSubtractor

print (hs.output())


# In[4]:

# Changing the number of inputs

# No need to set the number, just change the inputs

# Input length must be two

hs.setInputs(1, 1)

# To get the input states

print (hs.getInputStates())


# In[5]:

# New output of HalfSubtractor

print (hs.output())


# In[6]:

# Using Connectors as the input lines

# Take a Connector

conn = Connector()

# Set Output at index to Connector conn

hs.setOutput(0, conn)

# Put this connector as the input to gate1

gate1 = AND(conn, 0)

# Output of the gate1

print (gate1.output())


# In[7]:

# Information about hs instance can be found by

print (hs)
