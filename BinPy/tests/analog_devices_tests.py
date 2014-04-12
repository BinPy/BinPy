from BinPy.Analog import *
from nose.tools import with_setup, nottest


def test_Resisitor():
    params = {'r': 5}
    r = Resistor(params)
    assert r.getParams()['i'] == 0
    assert r.getParams()['r'] == 5
    assert r.getParams()['+'].state == 0
    assert r.getParams()['-'].state == 0

    r.setVoltage(Connector(5), Connector(0))
    assert r.getParams()['i'] == 1.0
    assert r.getParams()['r'] == 5
    assert r.getParams()['+'].state == 5
    assert r.getParams()['-'].state == 0

    r.setCurrent(10)
    assert r.getParams()['i'] == 10
    assert r.getParams()['r'] == 5
    assert r.getParams()['+'].state == 50
    assert r.getParams()['-'].state == 0

    r.setResistance(10)
    assert r.getParams()['i'] == 5.0
    assert r.getParams()['r'] == 10
    assert r.getParams()['+'].state == 50
    assert r.getParams()['-'].state == 0
