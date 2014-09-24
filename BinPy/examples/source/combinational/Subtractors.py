
# coding: utf-8

# Example for Subtractors from combinational module

# In[1]:

# Imports

from __future__ import print_function
from BinPy.combinational.combinational import *


# Half Subtractor

# In[2]:

print(HalfSubtractor.__doc__)


# In[3]:

# Initializing the HalfSubtractor

# Input is of the form (bit_1, bit_2)
hs = HalfSubtractor(1, 1)

# Output of HalfSubtractor
# Output is of the form [BORROW, DIFFERENCE]

print (hs.output())


# In[4]:

# Input changes ( index, value )

hs.set_input(1, 0)

# New Output of the HalfSubtractor

print (hs.output())


# In[5]:

# Using Connectors as the input lines
# Take a Connector

conn_1 = Connector(1)
conn_2 = Connector(0)
conn_3 = Connector()

# Setting the input of the Half Adder to the Connector conn_1 and conn_2

hs.set_inputs(conn_1, conn_2)

# Set Carry Output of Binary Adder to Connector conn_3

hs.set_output(0, conn_3)

# Use this connector as the input to gate1

gate1 = NOT(conn_3)

# Output of the gate1
print (gate1.output())


# In[6]:

# Change the value of the conn_2
conn_2.set_logic(0)

# Verify with the output of the HalfAdder
print (hs.output())


# Full Adder

# In[7]:

print(FullSubtractor.__doc__)


# In[8]:

a, b, bi, d, bo = Connector(0), Connector(
    1), Connector(1), Connector(), Connector()

# Initializing full adder using connectors
fa = FullSubtractor(a, b, bi)

# Connect outputs
fa.set_output(0, bo)
fa.set_output(1, d)


# In[9]:

print (bo.get_logic(), d.get_logic())
