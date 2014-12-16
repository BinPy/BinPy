# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Bistable Multivibrator - Multivibrator in Mode 3

# <codecell>

from __future__ import print_function
from BinPy.tools.clock import Clock
from BinPy.Gates import Connector
from BinPy.tools.multivibrator import Multivibrator
from BinPy.tools.oscilloscope import Oscilloscope
import time

# <codecell>

# MODE selects the mode of operation of the multivibrator.

# Mode No. :  Description
#   1          Monostable
#   2          Astable
#   3          Bistable

out = Connector(0)

# <codecell>

# Initialize mutivibrator in MODE 3

m = Multivibrator(0, mode=3)
m.start()
m.setOutput(out)

# <codecell>

# Initialize the oscilloscope
o = Oscilloscope((out, 'OUT'))
o.start()
o.setScale(0.05)
o.setWidth(100)
o.unhold()
# This is done to let the oscilloscope thread to synchronize with the main
# thread...
time.sleep(0.001)

# <codecell>

# Trigger the multivibrator to change the state
print(out())
time.sleep(0.1)
m.trigger()

time.sleep(0.001)  # This is done to synchronize the multivibrator thread ...

print(out())
time.sleep(0.5)
m.trigger()

time.sleep(0.001)  # This is done to synchronize the multivibrator thread ...

print(out())
time.sleep(1)
m.trigger()

time.sleep(0.001)  # This is done to synchronize the multivibrator thread ...

print(out())
time.sleep(2)
m.trigger()

time.sleep(0.001)  # This is done to synchronize the multivibrator thread ...

print(out())

# <codecell>

# Display the oscilloscope
o.display()

# <codecell>

# Kill the multivibrator and the oscilloscope threads
m.kill()
o.kill()
