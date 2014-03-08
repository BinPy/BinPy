from BinPy.ic import *
from nose.tools import with_setup, nottest

######## IC's with 14 pins #################################


def test_IC_4000():
    testIC = IC_4000()
    p = {3: 1, 4: 1, 5: 1, 7: 0, 8: 1, 11: 0, 12: 0, 13: 0, 14: 1}
    testIC.setIC(p)
    q = {6: 0, 9: 0, 10: 1}
    if q != testIC.run():
        assert False


def test_IC_4001():
    testIC = IC_4001()
    p = {1: 0, 2: 0, 5: 0, 6: 1, 7: 0, 8: 1, 9: 0, 12: 1, 13: 1, 14: 1}
    testIC.setIC(p)
    q = {3: 1, 4: 0, 10: 0, 11: 0}
    if q != testIC.run():
        assert False


def test_IC_4002():
    testIC = IC_4002()
    p = {2: 0, 3: 0, 4: 0, 5: 0, 7: 0, 9: 1, 10: 1, 11: 1, 12: 1, 14: 1}
    testIC.setIC(p)
    q = {1: 1, 13: 0}
    if q != testIC.run():
        assert False


def test_IC_4011():
    testIC = IC_4011()
    p = {1: 0, 2: 0, 5: 0, 6: 1, 7: 0, 8: 1, 9: 0, 12: 1, 13: 1, 14: 1}
    testIC.setIC(p)
    q = {3: 1, 4: 1, 10: 1, 11: 0}
    if q != testIC.run():
        assert False


def test_IC_4012():
    testIC = IC_4012()
    p = {2: 0, 3: 1, 4: 0, 5: 1, 7: 0, 9: 1, 10: 1, 11: 1, 12: 1, 14: 1}
    testIC.setIC(p)
    q = {1: 1, 13: 0}
    if q != testIC.run():
        assert False


def test_IC_4023():
    testIC = IC_4023()
    p = {1: 1, 2: 1, 3: 0, 4: 0, 5: 0, 7: 0, 8: 1, 11: 0, 12: 1, 13: 1, 14: 1}
    testIC.setIC(p)
    q = {6: 1, 9: 0, 10: 1}
    if q != testIC.run():
        assert False


def test_IC_4025():
    testIC = IC_4025()
    p = {1: 1, 2: 1, 3: 0, 4: 0, 5: 0, 7: 0, 8: 1, 11: 0, 12: 1, 13: 1, 14: 1}
    testIC.setIC(p)
    q = {6: 1, 9: 0, 10: 0}
    if q != testIC.run():
        assert False


def test_IC_4068():
    testIC = IC_4068()
    p = {2: 1, 3: 1, 4: 0, 5: 1, 7: 0, 9: 1, 10: 0, 11: 1, 12: 1, 14: 1}
    testIC.setIC(p)
    q = {13: 1}
    if q != testIC.run():
        assert False


def test_IC_4069():
    testIC = IC_4069()
    p = {1: 0, 3: 1, 5: 1, 7: 0, 9: 0, 11: 0, 13: 0, 14: 1}
    testIC.setIC(p)
    q = {2: 1, 4: 0, 6: 0, 8: 1, 10: 1, 12: 1}
    if q != testIC.run():
        assert False


def test_IC_4070():
    testIC = IC_4070()
    p = {1: 0, 2: 0, 5: 0, 6: 1, 7: 0, 8: 1, 9: 0, 12: 1, 13: 1, 14: 1}
    testIC.setIC(p)
    q = {3: 0, 4: 1, 10: 1, 11: 0}
    if q != testIC.run():
        assert False


def test_IC_4071():
    testIC = IC_4071()
    p = {1: 0, 2: 0, 5: 0, 6: 1, 7: 0, 8: 1, 9: 0, 12: 1, 13: 1, 14: 1}
    testIC.setIC(p)
    q = {3: 0, 4: 1, 10: 1, 11: 1}
    if q != testIC.run():
        assert False


def test_IC_4072():
    testIC = IC_4072()
    p = {2: 0, 3: 0, 4: 0, 5: 0, 7: 0, 9: 1, 10: 1, 11: 1, 12: 1, 14: 1}
    testIC.setIC(p)
    q = {1: 0, 13: 1}
    if q != testIC.run():
        assert False


def test_IC_4073():
    testIC = IC_4073()
    p = {1: 1, 2: 1, 3: 0, 4: 0, 5: 0, 7: 0, 8: 1, 11: 0, 12: 1, 13: 1, 14: 1}
    testIC.setIC(p)
    q = {6: 0, 9: 1, 10: 0}
    if q != testIC.run():
        assert False


def test_IC_4075():
    testIC = IC_4075()
    p = {1: 1, 2: 1, 3: 0, 4: 0, 5: 0, 7: 0, 8: 1, 11: 0, 12: 1, 13: 1, 14: 1}
    testIC.setIC(p)
    q = {6: 0, 9: 1, 10: 1}
    if q != testIC.run():
        assert False


def test_IC_4077():
    testIC = IC_4077()
    p = {1: 0, 2: 0, 5: 0, 6: 1, 7: 0, 8: 1, 9: 0, 12: 1, 13: 1, 14: 1}
    testIC.setIC(p)
    q = {3: 1, 4: 0, 10: 0, 11: 1}
    if q != testIC.run():
        assert False


def test_IC_4078():
    testIC = IC_4078()
    p = {2: 1, 3: 1, 4: 0, 5: 1, 7: 0, 9: 1, 10: 0, 11: 1, 12: 1, 14: 1}
    testIC.setIC(p)
    q = {13: 0}
    if q != testIC.run():
        assert False


def test_IC_4081():
    testIC = IC_4081()
    p = {1: 0, 2: 0, 5: 0, 6: 1, 7: 0, 8: 1, 9: 0, 12: 1, 13: 1, 14: 1}
    testIC.setIC(p)
    q = {3: 0, 4: 0, 10: 0, 11: 1}
    if q != testIC.run():
        assert False


def test_IC_4082():
    testIC = IC_4082()
    p = {2: 0, 3: 1, 4: 0, 5: 1, 7: 0, 9: 1, 10: 1, 11: 1, 12: 1, 14: 1}
    testIC.setIC(p)
    q = {1: 0, 13: 1}
    if q != testIC.run():
        assert False
