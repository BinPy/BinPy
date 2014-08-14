# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Examples for NOT class

# <codecell>

# imports
from __future__ import print_function
from BinPy.gates import *

# <codecell>

# Initializing the NOT class

gate = NOT(0)

# Output of the NOT gate

print (gate.output())

# <codecell>

# Input is changed to 0

gate.set_input(1)

# To get the input states

print (gate.get_input_states())

# <codecell>

# New Output of the NOT gate

print (gate.output())

# <codecell>

# Using Connectors as the input lines

# Take a Connector

conn = Connector()

# Set Output of gate to Connector conn

gate.set_output(conn)

# Put this connector as the input to gate1

gate1 = NOT(conn)

# Output of the gate1

print (gate1.output())

# <codecell>

# Information about gate instance

print (gate)
