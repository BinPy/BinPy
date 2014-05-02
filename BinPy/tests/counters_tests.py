from BinPy import *
from nose.tools import with_setup, nottest


def test_BinaryCounter():

    clock = Clock(1, 500)
    clock.start()
    test_BinaryCounter = BinaryCounter(2, clock.A)
    op = []
    for i in range(5):
        test_BinaryCounter.trigger()
        op += test_BinaryCounter.state()

    assert op == [0, 1, 1, 0, 1, 1, 0, 0, 0, 1]

    clock.kill()


def test_NBitRippleCounter():

    clock = Clock(1, 500)
    clock.start()
    test_NBitRippleCounter = NBitRippleCounter(3, clock.A)
    op = []
    for i in range(9):
        test_NBitRippleCounter.trigger()
        op += test_NBitRippleCounter.state()

    assert op == [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0,
                  0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1]

    clock.kill()


def test_NBitDownCounter():

    clock = Clock(1, 500)
    clock.start()
    test_NBitDownCounter = NBitDownCounter(3, clock.A)
    op = []
    for i in range(9):
        test_NBitDownCounter.trigger()
        op += test_NBitDownCounter.state()

    assert op == [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0,
                  0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1]

    clock.kill()


def test_DecadeCounter():

    clock = Clock(1, 500)
    clock.start()
    test_DecadeCounter = DecadeCounter(clock.A)
    op = []
    for i in range(14):
        test_DecadeCounter.trigger()
        op += test_DecadeCounter.state()

    assert op == [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1,
                  1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1,
                  1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1,
                  0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
                  0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0]

    clock.kill()


def test_RingCounter():

    clock = Clock(1, 500)
    clock.start()
    test_RingCounter = RingCounter(8, clock)
    op = []
    for i in range(8):
        test_RingCounter.trigger()
        op += test_RingCounter.state()

    assert op == [0, 1, 0, 0, 0, 0, 0, 0,
                  0, 0, 1, 0, 0, 0, 0, 0,
                  0, 0, 0, 1, 0, 0, 0, 0,
                  0, 0, 0, 0, 1, 0, 0, 0,
                  0, 0, 0, 0, 0, 1, 0, 0,
                  0, 0, 0, 0, 0, 0, 1, 0,
                  0, 0, 0, 0, 0, 0, 0, 1,
                  1, 0, 0, 0, 0, 0, 0, 0]
    clock.kill()


def test_JohnsonCounter():

    clock = Clock(1, 500)
    clock.start()
    test_JohnsonCounter = JohnsonCounter(4, clock)
    op = []
    for i in range(8):
        test_JohnsonCounter.trigger()
        op += test_JohnsonCounter.state()

    assert op == [1, 1, 0, 0, 1, 1, 1, 0,
                  1, 1, 1, 1, 0, 1, 1, 1,
                  0, 0, 1, 1, 0, 0, 0, 1,
                  0, 0, 0, 0, 1, 0, 0, 0]
    clock.kill()
