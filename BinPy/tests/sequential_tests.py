from BinPy import *
from nose.tools import with_setup, nottest


def test_SRLatch():

    s = Connector(1)
    r = Connector(0)
    clock = Clock(1, 500)
    clock.start()
    test_SRLatch = SRLatch(s, r, Connector(1), clock.A)

    s.state, r.state = 1, 0
    while True:
        if clock.A.state == 0:
            test_SRLatch.trigger()
            break
    while True:
        if clock.A.state == 1:
            test_SRLatch.trigger()
            break
    assert test_SRLatch.state() == [1, 0]

    s.state, r.state = 0, 1
    while True:
        if clock.A.state == 0:
            test_SRLatch.trigger()
            break
    while True:
        if clock.A.state == 1:
            test_SRLatch.trigger()
            break
    assert test_SRLatch.state() == [0, 1]

    s.state, r.state = 1, 1
    while True:
        if clock.A.state == 0:
            test_SRLatch.trigger()
            break
    while True:
        if clock.A.state == 1:
            test_SRLatch.trigger()
            break
    assert test_SRLatch.state() == [0, 1]

    s.state, r.state = 0, 0
    while True:
        if clock.A.state == 0:
            test_SRLatch.trigger()
            break
    while True:
        if clock.A.state == 1:
            test_SRLatch.trigger()
            break
    assert test_SRLatch.state() == [0, 1]

    clock.kill()


def test_DFlipFlop():

    d = Connector(1)
    clock = Clock(1, 500)
    clock.start()
    test_DFF = DFlipFlop(d, Connector(1), clock.A)

    d.state = 1
    while True:
        if clock.A.state == 0:
            test_DFF.trigger()
            break
    while True:
        if clock.A.state == 1:
            test_DFF.trigger()
            break
    assert test_DFF.state() == [1, 0]

    d.state = 0
    while True:
        if clock.A.state == 0:
            test_DFF.trigger()
            break
    while True:
        if clock.A.state == 1:
            test_DFF.trigger()
            break
    assert test_DFF.state() == [0, 1]
    clock.kill()


def test_JKFlipFlop():

    j, k = Connector(0), Connector(0)

    clock = Clock(1, 500)
    clock.start()
    test_JKFF = JKFlipFlop(j, k, Connector(1), clock.A)

    j.state, k.state = 1, 0
    while True:
        if clock.A.state == 0:
            test_JKFF.trigger()
            break
    while True:
        if clock.A.state == 1:
            test_JKFF.trigger()
            break
    assert test_JKFF.state() == [1, 0]

    j.state, k.state = 0, 1
    while True:
        if clock.A.state == 0:
            test_JKFF.trigger()
            break
    while True:
        if clock.A.state == 1:
            test_JKFF.trigger()
            break
    assert test_JKFF.state() == [0, 1]

    j.state, k.state = 1, 1
    while True:
        if clock.A.state == 0:
            test_JKFF.trigger()
            break
    while True:
        if clock.A.state == 1:
            test_JKFF.trigger()
            break
    assert test_JKFF.state() == [1, 0]

    j.state, k.state = 1, 1
    while True:
        if clock.A.state == 0:
            test_JKFF.trigger()
            break
    while True:
        if clock.A.state == 1:
            test_JKFF.trigger()
            break
    assert test_JKFF.state() == [0, 1]

    j.state, k.state = 0, 0
    while True:
        if clock.A.state == 0:
            test_JKFF.trigger()
            break
    while True:
        if clock.A.state == 1:
            test_JKFF.trigger()
            break
    assert test_JKFF.state() == [0, 1]

    clock.kill()


def test_TFlipFlop():

    t = Connector()
    clock = Clock(1, 500)
    clock.start()
    test_TFF = TFlipFlop(t, Connector(1), clock.A)

    t.state = 1
    while True:
        if clock.A.state == 0:
            test_TFF.trigger()
            break
    while True:
        if clock.A.state == 1:
            test_TFF.trigger()
            break
    assert test_TFF.state() == [1, 0]

    t.state = 1
    while True:
        if clock.A.state == 0:
            test_TFF.trigger()
            break
    while True:
        if clock.A.state == 1:
            test_TFF.trigger()
            break
    assert test_TFF.state() == [0, 1]

    t.state = 0
    while True:
        if clock.A.state == 0:
            test_TFF.trigger()
            break
    while True:
        if clock.A.state == 1:
            test_TFF.trigger()
            break
    assert test_TFF.state() == [0, 1]

    clock.kill()
