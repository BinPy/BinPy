from BinPy.Gates import *
from BinPy.tools import *
from nose.tools import with_setup, nottest


def PowerSourceTest():
    POW = PowerSource()
    a = Connector()

    POW.connect(a)
    print((a.state))
    if a.state != 1:
        assert False

    POW.disconnect(a)
    print((a.state))
    if a.state is not None:
        assert False


def GroundTest():
    GND = Ground()
    a = Connector()

    GND.connect(a)
    print((a.state))
    if a.state != 0:
        assert False

    GND.disconnect(a)
    print((a.state))
    if a.state is not None:
        assert False
