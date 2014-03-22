from __future__ import print_function
from BinPy.tools.digital import Clock
from BinPy.Gates import Connector
from BinPy.tools.multivibrator import Multivibrator
from BinPy.tools.oscilloscope import Oscilloscope
import time

#MODE selects the mode of operation of the multivibrator.

#Mode No. :  Description
#   1          Monostable
#   2          Astable
#   3          Bistable

out = Connector()

#MODE 1

m = Multivibrator(init_state=0,  mode=1, time_period=1, on_time = 0.2, off_time = 0.8)
m.start()
m.setOutput(out)

o = Oscilloscope((out,'OUT'))
o.start()
o.setScale(0.005) #Set scale by trial and error.
o.unhold()
time.sleep(0.1)
m.trigger() # Also works with m()
time.sleep(0.1)
o.display()


#MODE 2

o.unhold()
o.setScale(0.5)

m.setMode(2)
time.sleep(0.01)
m.trigger()
m.trigger()
time.sleep(4)

o.display()

#MODE 3

o.setScale(0.05)
o.unhold()

m.setMode(3)

time.sleep(0.1)
m.trigger()
time.sleep(0.1)
m.trigger()
time.sleep(0.3)
m.trigger()
time.sleep(0.5)
m.trigger()

o.display()

