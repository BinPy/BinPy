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

# MODE 3

m = Multivibrator(0, mode=3)

m.start()
m.setOutput(out)
m.trigger()

o = Oscilloscope((m.A, 'OUT'))
o.start()
o.setScale(0.01)
o.unhold()

m.trigger()
print (m.A())
time.sleep(0.3)
m.trigger()
print (m.A())
time.sleep(0.5)
m.trigger()
print (m.A())
time.sleep(0.5)
m.trigger()
print (m.A())
o.display()
o.kill()
m.kill()
