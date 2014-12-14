# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Usage of IC 4077

# <codecell>

from __future__ import print_function
from BinPy import *

# <codecell>

# Usage of IC 4077:

ic = IC_4077()

print(ic.__doc__)

# <codecell>

# The Pin configuration is:

inp = {1: 0, 2: 0, 5: 0, 6: 1, 7: 0, 8: 1, 9: 0, 12: 1, 13: 1, 14: 1}

# Pin initinalization

# Powering up the IC - using -- ic.set_IC({14: 1, 7: 0}) -- \n

ic.set_IC({14: 1, 7: 0})

# Setting the inputs of the ic

ic.set_IC(inp)

# Draw the IC with the current configuration\n

ic.draw_IC()

# <codecell>

# Run the IC with the current configuration using -- print ic.run() --

# Note that the ic.run() returns a dict of pin configuration similar to

print (ic.run())

# <codecell>

# Seting the outputs to the current IC configuration using --
# ic.set_IC(ic.run()) --\n

ic.set_IC(ic.run())

# Draw the final configuration

ic.draw_IC()

# <codecell>

# Seting the outputs to the current IC configuration using --
# ic.set_IC(ic.run()) --

ic.set_IC(ic.run())

# Draw the final configuration

ic.draw_IC()

# Run the IC

print (ic.run())

# <codecell>

# Connector Outputs
c = Connector()

# Set the output connector to a particular pin of the ic
ic.set_output(11, c)

print(c)
