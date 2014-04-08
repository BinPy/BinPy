from __future__ import print_function
from BinPy.tools.digital import Clock
from BinPy.Gates import Connector
from BinPy.tools.multivibrator import Multivibrator
from BinPy.tools.oscilloscope import Oscilloscope
import time

# MODE selects the mode of operation of the multivibrator.

# Mode No. :  Description
#   1          Monostable
#   2          Astable
#   3          Bistable

out = Connector()

# MODE 1

m = Multivibrator(0, mode=1, time_period=1)
m.start()
m.setOutput(out)

o = Oscilloscope((out, 'OUT'))
o.start()
o.setScale(0.005)  # Set scale by trial and error.
o.unhold()
time.sleep(0.1)
m.trigger()  # Also works with m()
time.sleep(0.1)
o.display()
m.kill()
o.kill()
