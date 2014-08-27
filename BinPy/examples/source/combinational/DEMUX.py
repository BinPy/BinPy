
# coding: utf-8

# Example for DEMUX class.

# In[1]:

from __future__ import print_function
from BinPy.Combinational.combinational import *


# In[2]:

# Initializing the DEMUX class

# Must be a single input

demux = DEMUX(1)

# Put select lines

# Select Lines must be power of 2

demux.selectLines(0)

# Output of demux

print (demux.output())


# In[3]:

# Input changes

# Input at index 1 is changed to 0

demux.setInput(0, 0)

# New Output of the demux

print (demux.output())


# In[4]:

# Get Input States

print (demux.getInputStates())


# In[5]:

# Using Connectors as the input lines

# Take a Connector

conn = Connector()

# Set Output of demux to Connector conn

# sets conn as the output at index 0

demux.setOutput(0, conn)

# Put this connector as the input to gate1

gate1 = AND(conn, 0)

# Output of the gate1

print (gate1.output())


# In[6]:

# Changing select lines

# selects input line 2

demux.selectLine(0, 1)

# New output of demux

print (demux.output())


# In[7]:

# Information about demux instance can be found by

print (demux)
