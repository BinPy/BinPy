# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Example to illustrate the usage of Analog Signal Generators

# <codecell>

from BinPy import *

# <codecell>

sig1 = SignalGenerator(typ=SignalGenerator.SIN, freq=1000, ampl=5.0)

# <codecell>

# Initiating an output Bus
output = Bus(Connector(voltage=0), Connector(voltage=0))

# Link this to the signal generator
sig1.set_outputs(output)

# <codecell>

# Kill the signal generator after usage
sig1.kill()

# <codecell>

# AM Signal generation using 2 instances of Signal Generator modules.

import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt
import math
import time

# Message sine signal generator of frequency 10 Hz and 1 Vpp amplitude
m_t = SignalGenerator(typ=0, freq=10, ampl=1)
m_t.set_offset(-0.5)

# Carrier sine signal generator of frequency 100 Hz and 10 Vpp amplitude
c_t = SignalGenerator(typ=0, freq=100, ampl=10)
c_t.set_offset(-5)  # To make the range as [-5, 5]
c_t.set_modulation_input(m_t.outputs)
c_t.set_modulation_type(1)

time.sleep(0.5)  # To allow setup time

# <codecell>

c_t.last_updated_time, (c_t.outputs[0].voltage - c_t.outputs[1].voltage)

# Populate the plot points to data array

data = np.zeros(
    shape=(
        2,
        math.ceil(
            m_t.time_period /
            c_t.sampling_time_interval)))

for i in range(data.shape[1]):
    data[0][i] = m_t.last_updated_time + m_t.time_period * i
    data[1][i] = c_t.outputs[0].voltage
    time.sleep(c_t.sampling_time_interval)

# Plot the modulated signal for the given timeframe
fig, ax = plt.subplots()
ax.plot(data[0], data[1])
plt.show()

# <codecell>

# Kill the signal generator threads after use
m_t.kill()
c_t.kill()
