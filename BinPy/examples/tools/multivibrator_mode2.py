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


# MODE 2

m = Multivibrator(0, 2, on_time=0.2, off_time=0.8)

m.start()
m.setOutput(out)
m.trigger()

o = Oscilloscope((out, 'OUT'))
o.start()
o.setScale(0.2)
o.unhold()

time.sleep(10)

o.display()

m.kill()
