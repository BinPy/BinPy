
# coding: utf-8

# Example for Encoder class

# In[1]:

from __future__ import print_function
from BinPy.combinational.combinational import *


# In[2]:

# Initializing the Encoder class

# Exacly 1 input must be 1

encoder = Encoder(0, 1)

# Output of encoder

print (encoder.output())


# In[3]:

# Changing the number of inputs

# No need to set the number, just change the inputs
# Input must be power of 2
# Inputs must be power of 2

encoder.set_inputs(0, 0, 0, 1)

# To get the input states

print (encoder.get_input_states())


# In[4]:

# New output of encoder

print (encoder.output())


# In[5]:

# Using Connectors as the input lines
# Take a Connector

conn = Connector()

# Set Output of decoder to Connector conn

encoder.set_output(1, conn)

# Put this connector as the input to gate1

gate1 = AND(conn, 1)

# Output of the gate1

print (gate1.output())


# In[6]:

# Information about encoder instance can be found by

print (encoder)
