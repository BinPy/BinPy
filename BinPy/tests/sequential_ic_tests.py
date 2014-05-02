from BinPy.ic import *
from nose.tools import with_setup, nottest

##########################
# IC's with 14 pins
##########################


def test_IC_7470():
    c = Clock(1, 500)
    c.start()
    testIC = IC_7470()
    p = {1: 1, 2: 1, 4: 0, 5: 0, 7: 0, 9: 1, 10: 1, 12: c, 13: 0, 14: 1}
    testIC.setIC(p)
    q = {8: 1, 10: 0}
    if q != testIC.run():
        assert False
    p = {1: 1, 2: 0, 4: 0, 5: 0, 7: 0, 9: 1, 10: 1, 12: c, 13: 1, 14: 1}
    testIC.setIC(p)
    q = {8: 0, 10: 1}
    if q != testIC.run():
        assert False

    p = {1: 1, 2: 1, 4: 0, 5: 0, 7: 0, 9: 1, 10: 1, 12: c, 13: 1, 14: 1}
    testIC.setIC(p)
    q = {8: 0, 10: 1}
    if q != testIC.run():
        assert False

    c.kill()


def test_IC_7472():
    c = Clock(1, 500)
    c.start()
    testIC = IC_7472()
    p = {1: 1, 2: 1, 4: 0, 5: 0, 7: 0, 9: 1, 10: 1, 12: c, 13: 0, 14: 1}
    testIC.setIC(p)
    q = {8: 1, 10: 0}
    if q != testIC.run():
        assert False
    p = {1: 1, 2: 0, 4: 0, 5: 0, 7: 0, 9: 1, 10: 1, 12: c, 13: 1, 14: 1}
    testIC.setIC(p)
    q = {8: 0, 10: 1}
    if q != testIC.run():
        assert False

    p = {1: 1, 2: 1, 4: 0, 5: 0, 7: 0, 9: 1, 10: 1, 12: c, 13: 1, 14: 1}
    testIC.setIC(p)
    q = {8: 0, 10: 1}
    if q != testIC.run():
        assert False

    c.kill()


def test_IC_7473():
    c1 = Clock(1, 500)
    c1.start()
    c2 = Clock(1, 500)
    c2.start()
    testIC = IC_7473()
    p = {1: c1, 2: 1, 4: 0, 5: c2, 7: 0, 9: 1, 10: 1, 12: 0, 13: 0, 14: 1}
    testIC.setIC(p)
    q = {8: 1, 9: 0, 12: 1, 13: 0}
    if q != testIC.run():
        assert False
    p = {1: c1, 2: 0, 4: 0, 5: c2, 7: 0, 9: 1, 10: 1, 12: 0, 13: 1, 14: 1}
    testIC.setIC(p)
    q = {8: 1, 9: 0, 12: 0, 13: 1}
    if q != testIC.run():
        assert False

    p = {
        1: c1,
        2: 1,
        4: 0,
        5: c2,
        6: 1,
        7: 0,
        9: 1,
        10: 1,
        12: 0,
        13: 1,
        14: 1}
    testIC.setIC(p)
    q = {8: 1, 9: 0, 12: 1, 13: 0}
    if q != testIC.run():
        assert False

    c1.kill()
    c2.kill()


def test_IC_7474():
    c1 = Clock(1, 500)
    c1.start()
    c2 = Clock(1, 500)
    c2.start()
    testIC = IC_7474()
    p = {
        1: 1,
        2: 1,
        3: c1,
        4: 0,
        5: 0,
        7: 0,
        9: 1,
        10: 1,
        11: c2,
        13: 0,
        14: 1}
    testIC.setIC(p)
    q = {8: 1, 9: 0, 5: 1, 6: 0}
    if q != testIC.run():
        assert False
    p = {
        1: 1,
        2: 1,
        3: c1,
        4: 0,
        5: 0,
        7: 0,
        9: 1,
        10: 0,
        11: c2,
        13: 1,
        14: 1}
    testIC.setIC(p)
    q = {8: 0, 9: 1, 5: 1, 6: 0}
    if q != testIC.run():
        assert False

    p = {
        1: 1,
        2: 1,
        3: c1,
        4: 0,
        5: 0,
        7: 0,
        9: 1,
        10: 1,
        11: c2,
        13: 1,
        14: 1}
    testIC.setIC(p)
    q = {8: 1, 9: 0, 5: 1, 6: 0}
    if q != testIC.run():
        assert False

    c1.kill()
    c2.kill()


def test_IC_7475():
    c1 = Clock(1, 500)
    c1.start()
    c2 = Clock(1, 500)
    c2.start()
    testIC = IC_7475()
    p = {
        1: 1,
        2: 1,
        3: 0,
        4: c1,
        5: 1,
        7: 0,
        9: 1,
        10: 1,
        11: 0,
        12: 0,
        13: c2,
        14: 1,
        15: 0,
        16: 1}
    testIC.setIC(p)
    q = {1: 0, 8: 1, 9: 0, 10: 0, 11: 1, 14: 1, 15: 0, 16: 1}
    if q != testIC.run():
        assert False

    p = {
        1: 1,
        2: 0,
        3: 0,
        4: c1,
        5: 1,
        7: 0,
        9: 1,
        10: 1,
        11: 0,
        12: 0,
        13: c2,
        14: 1,
        15: 0,
        16: 1}
    testIC.setIC(p)
    q = {1: 1, 8: 1, 9: 0, 10: 0, 11: 1, 14: 1, 15: 0, 16: 0}
    if q != testIC.run():
        assert False

    p = {
        1: 1,
        2: 1,
        3: 0,
        4: c1,
        5: 1,
        7: 1,
        9: 0,
        10: 1,
        11: 0,
        12: 0,
        13: c2,
        14: 1,
        15: 0,
        16: 1}
    testIC.setIC(p)
    q = {1: 0, 8: 0, 9: 1, 10: 0, 11: 1, 14: 1, 15: 0, 16: 1}
    if q != testIC.run():
        assert False

    c1.kill()
    c2.kill()


def test_IC_7476():
    c1 = Clock(1, 500)
    c1.start()
    c2 = Clock(1, 500)
    c2.start()
    testIC = IC_7476()
    p = {
        1: c1,
        2: 1,
        3: 0,
        4: 0,
        5: 1,
        6: c2,
        7: 0,
        8: 1,
        9: 1,
        10: 1,
        11: 0,
        12: 0,
        13: 0,
        14: 1,
        15: 0,
        16: 1}
    testIC.setIC(p)
    q = {10: 0, 11: 1, 14: 1, 15: 0}
    if q != testIC.run():
        assert False

    p = {
        1: c1,
        2: 0,
        3: 1,
        4: 0,
        5: 1,
        6: c2,
        7: 0,
        8: 1,
        9: 1,
        10: 1,
        11: 0,
        12: 0,
        13: 0,
        14: 1,
        15: 0,
        16: 1}
    testIC.setIC(p)
    q = {10: 0, 11: 1, 14: 0, 15: 1}
    if q != testIC.run():
        assert False

    p = {
        1: c1,
        2: 1,
        3: 0,
        4: 0,
        5: 1,
        6: c2,
        7: 1,
        8: 0,
        9: 1,
        10: 1,
        11: 0,
        12: 0,
        13: 0,
        14: 1,
        15: 0,
        16: 1}
    testIC.setIC(p)
    q = {10: 1, 11: 0, 14: 1, 15: 0}
    if q != testIC.run():
        assert False

    c1.kill()
    c2.kill()
