# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Example usage for Analog Buffers

# <codecell>

from BinPy import *

# Source Bus
a = Bus(4)
a.set_type(analog=True)
a.set_voltage_all(3.5, 6.7, 2.2, 1.1)

# Ouput Bus
b = Bus(4)
b.set_type(analog=True)

# Enable input
e = Bus(1)
e.set_logic_all(1)

# <codecell>

# Initializing an analog Buffer
# With an attenuation of 0.8, relay the input to the output
buff1 = AnalogBuffer(a, b, e, 0.8)

# <codecell>

print b.get_voltage_all()

# <codecell>

# BinPy automatically converts the voltage to logic state based on 5v-0v logic
print b.get_logic_all()

# <codecell>

print b.get_voltage_all()

# <codecell>

# Changing the input

a.set_voltage_all(1, 1, 1, 1)

# <codecell>

b.get_voltage_all()

# <codecell>

# Changing the attenuation level

buff1.set_attenuation(0)

# <codecell>

b.get_voltage_all()
