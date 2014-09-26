# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Examples for ShiftRegister class

# <codecell>

from __future__ import print_function
from BinPy.Sequential import *

# <codecell>

# Initializing the ShiftRegister class

# Input is of the form ([A0, A1, A2, A3], CLOCK, CIRCULAR)

# Initialise clock

c = Clock(1, 500)
c.start()

# Simple shift register

fr = ShiftRegister([1, 0, 1, 1], c, 0)

# Output of the register

print (fr.output())

# <codecell>

# Circular shift register

fr = ShiftRegister([1, 0, 1, 1], c, 1)

# Output of the register

print (fr.output())

# <codecell>

# Input changes

# Input at index 1 is changed to 0

fr.setInput(1, 0)

# New Output of the register

print (fr.output())

# <codecell>

#  Changing the inputs

# No need to set the number, just change the inputs

fr.setInputs(1, 1, 1, 1)

# To get the input states

print (fr.getInputStates())

# <codecell>

# New output of the register

print (fr.output())

# <codecell>

# Using Connectors as the input lines

# Take a Connector

conn = Connector()

# Set Output of gate to Connector conn

fr.setOutput(2, conn)

# Put this connector as the input to gate1

gate1 = AND(conn, 0)

# Output of the gate1

print (gate1.output())
