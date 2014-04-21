
# coding: utf-8

# Example for Decoder class

# In[1]:

# Imports
from __future__ import print_function
from BinPy.Combinational.combinational import *


# In[2]:

# Initializing the Decoder class

decoder = Decoder(0, 1)

# Output of decoder

print (decoder.output())


# In[3]:

# Input changes

# Input at index 1 is changed to 0

decoder.setInput(1, 0)

# New Output of the decoder

print (decoder.output())


# In[4]:

# Changing the number of inputs
# No need to set the number, just change the inputs
# Input must be power of 2

decoder.setInputs(1, 0, 0)

# To get the input states

print (decoder.getInputStates())

# New output of decoder

print (decoder.output())


# In[5]:

# Using Connectors as the input lines

conn = Connector()

# Set Output of decoder to Connector conn

decoder.setOutput(1, conn)

# Put this connector as the input to gate1

gate1 = AND(conn, 1)

# Output of the gate1

print (gate1.output())


# In[6]:

# Information about decoder instance can be found by

print (decoder)
