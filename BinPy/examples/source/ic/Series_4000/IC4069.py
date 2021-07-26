# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Usage of IC 4069

# <codecell>

from __future__ import print_function
from BinPy import *

# <codecell>

# Usage of IC 4069:

ic = IC_4069()

print(ic.__doc__)

# <codecell>

# The Pin configuration is:

inp = {2: 0, 3: 1, 4: 0, 5: 1, 7: 0, 9: 1, 10: 1, 11: 1, 12: 1, 14: 1}

# Pin initialization

# Powering up the IC - using -- ic.setIC({14: 1, 7: 0}) -- \n

ic.setIC({14: 1, 7: 0})

# Setting the inputs of the ic

ic.setIC(inp)

# Draw the IC with the current configuration\n

ic.drawIC()

# <codecell>

# Run the IC with the current configuration using -- print ic.run() --

# Note that the ic.run() returns a dict of pin configuration similar to

print (ic.run())

# <codecell>

# Seting the outputs to the current IC configuration using --
# ic.setIC(ic.run()) --\n

ic.setIC(ic.run())

# Draw the final configuration

ic.drawIC()

# <codecell>

# Seting the outputs to the current IC configuration using --
# ic.setIC(ic.run()) --

ic.setIC(ic.run())

# Draw the final configuration

ic.drawIC()

# Run the IC

print (ic.run())

# <codecell>

# Connector Outputs
c = Connector()

# Set the output connector to a particular pin of the ic
ic.setOutput(2, c)

print(c)
