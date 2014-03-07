from BinPy import *
from nose.tools import with_setup, nottest


def test_SRLatch():
    testLatch = SRLatch(1, 0)
    assert testLatch.output() == [0, 1]

    testLatch.setInputs(0, 0)
    assert testLatch.output() == [0, 1]

    testLatch.setInputs(0, 1)
    assert testLatch.output() == [1, 0]

    testLatch.setInputs(0, 0)
    assert testLatch.output() == [1, 0]

    testLatch.setInputs(1, 1)
    assert testLatch.output() == [0, 0]
