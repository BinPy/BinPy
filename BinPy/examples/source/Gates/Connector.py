
# coding: utf-8

### Examples for Connector class

# In[1]:

# imports
from __future__ import print_function
from BinPy.Gates import *


# In[2]:

# Initializing the Connector class
conn = Connector()

# Input contains the initial value of the Connector

# State of the Connector object

print (conn.state)


# In[3]:

# Calling the connector intance returns its state

print (conn())


# In[4]:

# Tapping the conector

gate = OR(0, 1)
conn.tap(gate, "output")


# In[5]:

# Untapping the connector

conn.untap(gate, "output")


# In[6]:

# Checking the relation ship of gate with the Connector 'conn'

print(conn.isOutputof(gate))

print(conn.isInputof(gate))


# In[7]:

# Set Output of gate to Connector conn

gate.setOutput(conn)


# In[8]:

# Checking the relation ship of gate with the Connector 'conn'

print(conn.isOutputof(gate))

print(conn.isInputof(gate))


# In[9]:

# Put this connector as the input to gate1

gate1 = AND(conn, 0)


# In[10]:

# Output of the gate1

print (gate1.output())


# In[11]:

# Information about conn instance

print (conn)

