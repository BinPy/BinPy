
# coding: utf-8

# Examples for XNOR class.

# In[1]:

from __future__ import print_function
from BinPy.Gates import *


# In[2]:

# Initializing the XNOR class

gate = XNOR(0, 1)


# In[3]:

# Output of the XNOR gate

print (gate.output())


# In[4]:

# Input changes

# Input at index 1 is changed to 0

gate.setInput(1, 0)


# In[5]:

# New Output of the XNOR gate

print (gate.output())


# In[6]:

# Changing the number of inputs

# No need to set the number, just change the inputs

gate.setInputs(1, 1, 1, 1)


# In[7]:

# To get the input states

print (gate.getInputStates())


# In[8]:

# New output of the XNOR gate

print (gate.output())


# In[9]:

# Using Connectors as the input lines

# Take a Connector

conn = Connector()


# In[10]:

# Set Output of gate to Connector conn

gate.setOutput(conn)


# In[11]:

# Put this connector as the input to gate1

gate1 = XNOR(conn, 0)


# In[12]:

# Output of the gate1

print (gate1.output())


# In[13]:

# Information about gate instance

print (gate)
