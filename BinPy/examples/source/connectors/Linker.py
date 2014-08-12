# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Example for BinPy Linker module.

# <codecell>

# Imports 

from __future__ import print_function
from BinPy import *

# <codecell>

# Initiating the Bus with connectors

bit_1 = Connector(0)
bit_2 = Connector(1)
bit_3 = Connector(0)
bit_4 = Connector(0)

bus_a = Bus(bit_1, bit_2, bit_3, bit_4)

# <codecell>

# Probing the logic of the Bus

bus_a.get_logic_all()

# <codecell>

# Linking 2 Bus-es

bus_b = Bus(4)

print(bus_b)

# <codecell>

# Add a link from bus_a to bus_b

AutoUpdater.add_link(bus_a, bus_b)

# <codecell>

# Run this after a leaving a minor update interval
print (bus_b)

# <codecell>

# More complex connections

CNTRL_V = Bus(4)

CNTRL_V.set_logic_all(1,1,1,1)

VCC = Bus(Connector(voltage = 5.2), Connector(voltage=0))

# <codecell>

SLAVE0, SLAVE1 = Bus(4), Bus(4)

SLAVE0.set_type(analog = True)
SLAVE1.set_type(analog = True)

# Connecting the first two bits of CNTRL_V to the middle two bits of SLAVE0
AutoUpdater.add_link(CNTRL_V[:2], SLAVE0[1:-1])

# Connecting the last two bits of CNTRL_V to the middle two bits of SLAVE1
AutoUpdater.add_link(CNTRL_V[-2:], SLAVE1[1:-1])

# Impressing 5v and 0v on the SLAVE0 Bus
AutoUpdater.add_link(VCC[0], SLAVE0[0])
AutoUpdater.add_link(VCC[1], SLAVE0[-1])

# Impressing 5v and 0v on the SLAVE1 Bus
AutoUpdater.add_link(VCC[0], SLAVE1[0])
AutoUpdater.add_link(VCC[1], SLAVE1[-1])

# <codecell>

print (SLAVE0.get_voltage_all())

# <codecell>

print (SLAVE1.get_voltage_all())

# <codecell>

CNTRL_V.set_voltage_all(5.0, 6.0, 2.0, 1.1)

# <codecell>

# The Slave Bus-es have been updated with the updated voltage in CNTRL_V

print (SLAVE0.get_voltage_all())

# <codecell>

print (SLAVE1.get_voltage_all())

# <codecell>

# Unlinking the SLAVE0 from CNTRL_V

AutoUpdater.remove_link(SLAVE0[1:-1]) # Only the middle 2 ports are connected to CNTRL_V
# VCC is still connected to SLAVE0

# <codecell>

CNTRL_V.set_voltage_all(3.0, 2, 1, 6.2)

# <codecell>

# SLAVE0 Retains the last held value

print (SLAVE0.get_voltage_all())

# <codecell>

# SLAVE1 however is updated

print (SLAVE1.get_voltage_all())

# <codecell>

# Change in VCC is reflected to both SLAVE0 and SLAVE1

VCC[0].set_voltage(5.5)

print (SLAVE0[0].get_voltage())

print (SLAVE1[0].get_voltage())

