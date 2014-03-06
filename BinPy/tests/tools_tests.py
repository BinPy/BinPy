import time
from nose.tools import with_setup, nottest
from BinPy.tools.clock import *
from BinPy.gates.connector import *

def CLOCK_test():
    t = 0.02
    clk = Clock(0, time_period = t)
    a = Connector()
    clk.connect(a)
    clk.start()
    time.sleep(t/4.0)
    output = []

    for i in range(5):
        output.append(int(a.state))
        time.sleep(t/2.0)

    if output != [0,1,0,1,0]:
        assert False
