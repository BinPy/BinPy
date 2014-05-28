from BinPy.ic import *
from nose.tools import with_setup, nottest

#################################
# IC's with 14 pins
#################################


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


def test_IC_4013():
    testIC = IC_4013()
    p = {
        1: 1,
        2: 0,
        3: 1,
        4: 0,
        5: 1,
        6: 1,
        7: 0,
        8: 0,
        9: 1,
        10: 1,
        11: 1,
        12: 1,
        13: 0,
        14: 1}
    c1 = Clock(1, 500)
    c1.start()
    c2 = Clock(1, 500)
    c2.start()
    p[3] = c1
    p[11] = c2

    testIC.setIC(p)
    assert testIC.run() == {1: 1, 2: 0, 12: 1, 13: 0}
    p[8] = 1
    testIC.setIC(p)
    assert testIC.run() == {1: 1, 2: 0, 12: 0, 13: 1}

    c1.kill()
    c2.kill()


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


def test_IC_4030():
    testIC = IC_4030()
    p = {1: 1, 2: 1, 3: 0, 4: 0, 5: 0, 7: 0, 8: 1, 11: 0, 12: 1, 13: 1, 14: 1}
    testIC.setIC(p)
    q = {11: 0, 10: 1, 3: 0, 4: 0}
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

#################################
# IC's with 16 pins
#################################


def test_IC_4008():
    testIC = IC_4008()
    p = {
        1: 1,
        2: 0,
        3: 1,
        4: 0,
        5: 1,
        6: 1,
        7: 0,
        8: 0,
        9: 1,
        10: 1,
        11: 1,
        12: 1,
        13: 0,
        14: 1,
        15: 0,
        16: 1}
    testIC.setIC(p)
    q = {10: 0, 11: 0, 12: 0, 13: 0, 14: 1}
    if q != testIC.run():
        assert False


def test_IC_4009():
    testIC = IC_4009()
    p = {
        1: 1,
        2: 0,
        3: 1,
        4: 0,
        5: 1,
        6: 1,
        7: 0,
        8: 0,
        9: 1,
        10: 1,
        11: 1,
        12: 1,
        13: 0,
        14: 1,
        15: 0,
        16: 1}
    testIC.setIC(p)
    q = {2: 0, 4: 0, 6: 1, 10: 0, 12: 0, 15: 0}
    if q != testIC.run():
        assert False


def test_IC_4010():
    testIC = IC_4010()
    p = {
        1: 1,
        2: 0,
        3: 1,
        4: 0,
        5: 1,
        6: 1,
        7: 0,
        8: 0,
        9: 1,
        10: 1,
        11: 1,
        12: 1,
        13: 0,
        14: 1,
        15: 0,
        16: 1}
    testIC.setIC(p)
    q = {2: 1, 4: 1, 6: 0, 10: 1, 12: 1, 15: 1}
    if q != testIC.run():
        assert False


def test_IC_4015():
    testIC = IC_4015()
    c = Clock(1, 500)
    c.start()
    p = {
        1: c,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 1,
        8: 0,
        9: c,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
        15: 1,
        16: 1}
    testIC.setIC(p)

    assert testIC.run() == {2: 0, 3: 0, 4: 1, 5: 1, 10: 0, 11: 0, 12: 1, 13: 1}
    assert testIC.run() == {2: 0, 3: 1, 4: 1, 5: 1, 10: 0, 11: 1, 12: 1, 13: 1}
    assert testIC.run() == {2: 1, 3: 1, 4: 1, 5: 1, 10: 1, 11: 1, 12: 1, 13: 1}

    c.kill()


def test_IC_4017():
    testIC = IC_4017()
    c = Clock(1, 500)
    c.start()
    p = {8: 0, 16: 1, 13: c, 14: c, 15: 0}
    testIC.setIC(p)

    assert testIC.run() == {1: 0, 2: 0, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 10: 0, 11: 0, 12: 1}
    assert testIC.run() == {1: 0, 2: 1, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 10: 0, 11: 0, 12: 1}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 10: 0, 11: 0, 12: 1}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 1, 8: 0, 9:
                            0, 10: 0, 11: 0, 12: 1}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 10: 1, 11: 0, 12: 1}
    assert testIC.run() == {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 10: 0, 11: 0, 12: 0}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 0, 7: 0, 8: 0, 9:
                            0, 10: 0, 11: 0, 12: 0}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1, 7: 0, 8: 0, 9:
                            0, 10: 0, 11: 0, 12: 0}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            1, 10: 0, 11: 0, 12: 0}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 10: 0, 11: 1, 12: 0}
    assert testIC.run() == {1: 0, 2: 0, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 10: 0, 11: 0, 12: 1}
    c.kill()


def test_IC_4019():
    testIC = IC_4019()
    p = {
        1: 1,
        2: 0,
        3: 1,
        4: 0,
        5: 1,
        6: 1,
        7: 0,
        8: 0,
        9: 1,
        10: 1,
        11: 1,
        12: 1,
        13: 0,
        14: 1,
        15: 0,
        16: 1}
    testIC.setIC(p)
    assert testIC.run() == {10: 1, 11: 1, 12: 1, 13: 1}


def test_IC_4020():
    testIC = IC_4020()
    c = Clock(1, 500)
    c.start()
    p = {8: 0, 16: 1, 10: c}
    testIC.setIC(p)

    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            1, 12: 0, 13: 0, 14: 0, 15: 0}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 12: 0, 13: 0, 14: 0, 15: 0}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 12: 0, 13: 0, 14: 0, 15: 0}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 1, 8: 0, 9:
                            0, 12: 0, 13: 0, 14: 0, 15: 0}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 0, 7: 0, 8: 0, 9:
                            0, 12: 0, 13: 0, 14: 0, 15: 0}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 12: 0, 13: 0, 14: 0, 15: 0}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1, 7: 0, 8: 0, 9:
                            0, 12: 0, 13: 0, 14: 0, 15: 0}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 12: 0, 13: 1, 14: 0, 15: 0}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 12: 1, 13: 0, 14: 0, 15: 0}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 12: 0, 13: 0, 14: 1, 15: 0}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 12: 0, 13: 0, 14: 0, 15: 1}
    assert testIC.run() == {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 12: 0, 13: 0, 14: 0, 15: 0}
    assert testIC.run() == {1: 0, 2: 1, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 12: 0, 13: 0, 14: 0, 15: 0}
    assert testIC.run() == {1: 0, 2: 0, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 12: 0, 13: 0, 14: 0, 15: 0}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            1, 12: 0, 13: 0, 14: 0, 15: 0}
    c.kill()


def test_IC_4022():
    testIC = IC_4022()
    c = Clock(1, 500)
    c.start()
    p = {8: 0, 16: 1, 13: c, 14: c, 15: 0}
    testIC.setIC(p)

    assert testIC.run() == {1: 0, 2: 1, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 10: 0, 11: 0, 12: 1}
    assert testIC.run() == {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 10: 0, 11: 0, 12: 1}
    assert testIC.run() == {1: 0, 2: 0, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 10: 0, 11: 0, 12: 1}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 1, 8: 0, 9:
                            0, 10: 0, 11: 0, 12: 1}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 10: 0, 11: 1, 12: 0}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 10: 0, 11: 0, 12: 0}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 0, 7: 0, 8: 0, 9:
                            0, 10: 0, 11: 0, 12: 0}
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 10: 1, 11: 0, 12: 0}
    assert testIC.run() == {1: 0, 2: 1, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:
                            0, 10: 0, 11: 0, 12: 1}
    c.kill()


def test_IC_4027():
    clk = Clock(1, 500)
    clk.start()
    testIC = IC_4027()
    p = {
        1: 0,
        2: 0,
        3: clk,
        4: 1,
        5: 0,
        6: 0,
        7: 1,
        8: 0,
        9: 1,
        10: 0,
        11: 0,
        12: 1,
        13: clk,
        14: 0,
        15: 0,
        16: 1}
    testIC.setIC(p)
    assert testIC.run() == {1: 0, 2: 1, 14: 1, 15: 0}
    p = {
        1: 0,
        2: 0,
        3: clk,
        4: 0,
        5: 0,
        6: 0,
        7: 1,
        8: 0,
        9: 1,
        10: 0,
        11: 0,
        12: 0,
        13: clk,
        14: 0,
        15: 0,
        16: 1}
    testIC.setIC(p)
    assert testIC.run() == {1: 1, 2: 0, 14: 0, 15: 1}
    p = {
        1: 0,
        2: 0,
        3: clk,
        4: 1,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 1,
        13: clk,
        14: 0,
        15: 0,
        16: 1}
    testIC.setIC(p)
    assert testIC.run() == {1: 0, 2: 1, 14: 1, 15: 0}
    clk.kill()


def test_IC_2028():
    testIC = IC_4028()
    p = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 1,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
        15: 0,
        16: 1}
    testIC.setIC(p)
    assert testIC.run() == {1: 0, 2: 0, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 9: 0, 14:
                            0, 15: 0}
    p[10] = 1
    testIC.setIC(p)
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 9: 1, 14:
                            0, 15: 0}
    p[11] = 1
    testIC.setIC(p)
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 0, 7: 0, 9: 0,
                            14: 0, 15: 0}

    p[12] = 1
    testIC.setIC(p)
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 9: 0,
                            14: 0, 15: 0}

    p[13] = 1
    testIC.setIC(p)
    assert testIC.run() == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 9: 0,
                            14: 0, 15: 0}


def test_IC_4029():
    clk = Clock(1, 500)
    clk.start()

    p = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
        15: clk,
        16: 1}
    testIC = IC_4029()
    testIC.setIC(p)

    assert testIC.run() == {2: 1, 11: 0, 14: 0, 6: 1}
    assert testIC.run() == {2: 0, 11: 0, 14: 0, 6: 1}
    assert testIC.run() == {2: 1, 11: 1, 14: 1, 6: 0}
    assert testIC.run() == {2: 0, 11: 1, 14: 1, 6: 0}
    assert testIC.run() == {2: 1, 11: 1, 14: 0, 6: 0}
    assert testIC.run() == {2: 0, 11: 1, 14: 0, 6: 0}
    assert testIC.run() == {2: 1, 11: 0, 14: 1, 6: 0}
    assert testIC.run() == {2: 0, 11: 0, 14: 1, 6: 0}
    assert testIC.run() == {2: 1, 11: 0, 14: 0, 6: 0}
    assert testIC.run() == {2: 0, 11: 0, 14: 0, 6: 0}
    assert testIC.run() == {2: 1, 11: 0, 14: 0, 6: 1}
    assert testIC.run() == {2: 0, 11: 0, 14: 0, 6: 1}
    assert testIC.run() == {2: 1, 11: 1, 14: 1, 6: 0}
    assert testIC.run() == {2: 0, 11: 1, 14: 1, 6: 0}
    assert testIC.run() == {2: 1, 11: 1, 14: 0, 6: 0}

    p = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 1,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
        15: clk,
        16: 1}
    testIC.setIC(p)
    assert testIC.run() == {2: 0, 11: 1, 14: 1, 6: 0}
    assert testIC.run() == {2: 1, 11: 1, 14: 1, 6: 0}
    assert testIC.run() == {2: 0, 11: 0, 14: 0, 6: 1}
    assert testIC.run() == {2: 1, 11: 0, 14: 0, 6: 1}
    assert testIC.run() == {2: 0, 11: 0, 14: 0, 6: 0}
    assert testIC.run() == {2: 1, 11: 0, 14: 0, 6: 0}
    assert testIC.run() == {2: 0, 11: 0, 14: 1, 6: 0}
    assert testIC.run() == {2: 1, 11: 0, 14: 1, 6: 0}
    assert testIC.run() == {2: 0, 11: 1, 14: 0, 6: 0}
    assert testIC.run() == {2: 1, 11: 1, 14: 0, 6: 0}
    assert testIC.run() == {2: 0, 11: 1, 14: 1, 6: 0}
    assert testIC.run() == {2: 1, 11: 1, 14: 1, 6: 0}
    assert testIC.run() == {2: 0, 11: 0, 14: 0, 6: 1}
    assert testIC.run() == {2: 1, 11: 0, 14: 0, 6: 1}
    assert testIC.run() == {2: 0, 11: 0, 14: 0, 6: 0}

    p = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 1,
        10: 1,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
        15: clk,
        16: 1}
    testIC.setIC(p)
    assert testIC.run() == {2: 1, 11: 0, 14: 0, 6: 0}
    assert testIC.run() == {2: 0, 11: 0, 14: 1, 6: 0}
    assert testIC.run() == {2: 1, 11: 0, 14: 1, 6: 0}
    assert testIC.run() == {2: 0, 11: 1, 14: 0, 6: 0}
    assert testIC.run() == {2: 1, 11: 1, 14: 0, 6: 0}
    assert testIC.run() == {2: 0, 11: 1, 14: 1, 6: 0}
    assert testIC.run() == {2: 1, 11: 1, 14: 1, 6: 0}
    assert testIC.run() == {2: 0, 11: 0, 14: 0, 6: 1}
    assert testIC.run() == {2: 1, 11: 0, 14: 0, 6: 1}
    assert testIC.run() == {2: 0, 11: 0, 14: 1, 6: 1}
    assert testIC.run() == {2: 1, 11: 0, 14: 1, 6: 1}
    assert testIC.run() == {2: 0, 11: 1, 14: 0, 6: 1}
    assert testIC.run() == {2: 1, 11: 1, 14: 0, 6: 1}
    assert testIC.run() == {2: 0, 11: 1, 14: 1, 6: 1}
    assert testIC.run() == {2: 1, 11: 1, 14: 1, 6: 1, 7: 1}

    p = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 1,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
        15: clk,
        16: 1}
    testIC.setIC(p)
    assert testIC.run() == {2: 0, 11: 1, 14: 1, 6: 1}
    assert testIC.run() == {2: 1, 11: 1, 14: 0, 6: 1}
    assert testIC.run() == {2: 0, 11: 1, 14: 0, 6: 1}
    assert testIC.run() == {2: 1, 11: 0, 14: 1, 6: 1}
    assert testIC.run() == {2: 0, 11: 0, 14: 1, 6: 1}
    assert testIC.run() == {2: 1, 11: 0, 14: 0, 6: 1}
    assert testIC.run() == {2: 0, 11: 0, 14: 0, 6: 1}
    assert testIC.run() == {2: 1, 11: 1, 14: 1, 6: 0}
    assert testIC.run() == {2: 0, 11: 1, 14: 1, 6: 0}
    assert testIC.run() == {2: 1, 11: 1, 14: 0, 6: 0}
    assert testIC.run() == {2: 0, 11: 1, 14: 0, 6: 0}
    assert testIC.run() == {2: 1, 11: 0, 14: 1, 6: 0}
    assert testIC.run() == {2: 0, 11: 0, 14: 1, 6: 0}
    assert testIC.run() == {2: 1, 11: 0, 14: 0, 6: 0}
    assert testIC.run() == {2: 0, 11: 0, 14: 0, 6: 0, 7: 0}

    clk.kill()
