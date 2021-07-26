# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Examples for Connector class

# <codecell>

# imports
from __future__ import print_function
from BinPy.gates import *

# <codecell>

# Initializing the Connector class
conn = Connector()

# Input contains the initial value of the Connector

# State of the Connector object

print (conn.state)

# <codecell>

# Calling the connector instance returns its state

print (conn())

# <codecell>

# Tapping the conector

gate = OR(0, 1)
conn.tap(gate, "output")

# <codecell>

# Untapping the connector

conn.untap(gate, "output")

# <codecell>

# Checking the relation ship of gate with the Connector 'conn'

print(conn.is_output_of(gate))

# <codecell>

print(conn.is_input_of(gate))

# <codecell>

# Set Output of gate to Connector conn

gate.set_output(conn)

# <codecell>

# Checking the relation ship of gate with the Connector 'conn'

print(conn.is_output_of(gate))

print(conn.is_input_of(gate))

# <codecell>

# Put this connector as the input to gate1

gate1 = AND(conn, 0)

# <codecell>

# Output of the gate1

print (gate1.output())

# <codecell>

# Information about conn instance

print (conn)
