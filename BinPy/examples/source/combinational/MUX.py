
# coding: utf-8

# Example for MUX class.

# In[1]:

# Imports
from __future__ import print_function
from BinPy.combinational.combinational import *


# In[2]:

# Initializing the MUX class

mux = MUX(0, 1)

# Put select lines

mux.select_lines(0)

# Output of mux

print (mux.output())


# In[3]:

# Input changes

# Input at index 1 is changed to 0

mux.set_input(1, 0)

# New Output of the mux

print (mux.output())


# In[4]:

# Changing the number of inputs

# No need to set the number, just change the inputs

# Input must be power of 2

mux.set_inputs(1, 0, 0, 1)


# In[5]:

# New output of mux

print (mux.output())


# In[6]:

# Using Connectors as the input lines

# Take a Connector

conn = Connector()

# Set Output of mux to Connector conn

mux.set_output(conn)

# Put this connector as the input to gate1

gate1 = AND(conn, 0)

# Output of the gate1

print (gate1.output())


# In[7]:

# Changing select lines

# Selects input line 2

mux.select_line(0, 1)

# New output of mux

print (mux.output())


# In[8]:

# Information about mux instance can be found by

print (mux)
