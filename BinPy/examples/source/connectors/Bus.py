# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Example for Bus

# <codecell>

# Imports

from __future__ import print_function
from BinPy import Bus, Connector

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

# Probing the voltage of the Bus

bus_a.get_voltage_all()

# <codecell>

# Creating another Bus from an existing Bus

bus_b = Bus(bus_a)

bus_b.get_voltage_all()

# <codecell>

# Concatenating the two Bus-es

bus_c = bus_a + bus_b

bus_c

# <codecell>

# Copying values between buses

# 8 indicates the length of the Bus. By default all busses will be digital
# in type
bus_d = Bus(8)

print(bus_d)

# <codecell>

bus_d.copy_values_from(bus_c)
print(bus_d)

# <codecell>

# Iterating through a bus and setting names ( TAG's ) for connectors
i = 7
for connector in bus_d:
    connector.set_name("B" + str(i))
    print(connector)
    i -= 1

# <codecell>

# Probing the connector tags

print(" ".join([connector.name for connector in bus_d]))

# <codecell>

# Analog Bus

VCC = Bus(Connector(voltage=5.2), Connector(voltage=0))

print(VCC)

# <codecell>

# Slicing Bus-es

bus_e = Bus(bus_d[:-4])

print(bus_e == bus_b)

# <codecell>

# Circulary rotating the bits of the Bus-es

print("Before rotation, bus_e : ", bus_e)

print(
    "After circularly rotating right by 3 positions, bits of bus_e: ",
    bus_e >> 3)

# Note that this returns a list of the Connectors and not a bus object.
# Use Bus(bus_e>>2) to return a Bus object

print(
    "After circularly rotating left by 3 positions, bits of bus_e: ",
    bus_e << 3)
