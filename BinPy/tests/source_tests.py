from BinPy.Gates import *
from BinPy.tools import *
from nose.tools import with_setup, nottest


def test_PowerSourceTest():
    POW = PowerSource()
    a = Connector()

    POW.connect(a)
    if a.state != 1:
        assert False

    POW.disconnect(a)
    if a.state is not None:
        assert False


def test_GroundTest():
    GND = Ground()
    a = Connector()

    GND.connect(a)
    if a.state != 0:
        assert False

    GND.disconnect(a)
    if a.state is not None:
        assert False
