# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Examples for OR class

# <codecell>

# imports
from __future__ import print_function
from BinPy.gates import *

# <codecell>

# Initializing the OR class

gate = OR(0, 1)

# Output of the OR gate

print (gate.output())

# <codecell>

# Input changes

# Input at index 1 is changed to 0

gate.set_input(1, 0)

# New Output of the OR gate

print (gate.output())

# <codecell>

# Changing the number of inputs

# No need to set the number, just change the inputs

gate.set_inputs(1, 1, 1, 1)

# To get the input states

print (gate.get_input_states())

# <codecell>

# New output of the OR gate

print (gate.output())

# <codecell>

# Using Connectors as the input lines

# Take a Connector

conn = Connector()

# Set Output of gate to Connector conn

gate.set_output(conn)

# Put this connector as the input to gate1

gate1 = OR(conn, 0)

# Output of the gate1

print (gate1.output())

# <codecell>

# Information about gate instance

print (gate)

