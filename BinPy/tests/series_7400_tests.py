from BinPy import *
from nose.tools import with_setup, nottest

#################################
# IC's with 14 pins
#################################


def test_IC_7400():
    test_IC = IC_7400()
    p = {1: 1, 2: 0, 4: 0, 5: 0, 7: 0, 9: 1, 10: 1, 12: 0, 13: 0, 14: 1}
    test_IC.set_IC(p)
    q = {3: 1, 6: 1, 8: 0, 11: 1}
    if q != test_IC.run():
        assert False


def test_IC_7401():
    test_IC = IC_7401()
    p = {2: 0, 3: 0, 5: 0, 6: 1, 7: 0, 8: 1, 9: 1, 11: 1, 12: 1, 14: 1}
    test_IC.set_IC(p)
    q = {1: 1, 4: 1, 10: 0, 13: 0}
    if q != test_IC.run():
        assert False


def test_IC_7402():
    test_IC = IC_7402()
    p = {2: 0, 3: 0, 5: 0, 6: 1, 7: 0, 8: 1, 9: 1, 11: 1, 12: 1, 14: 1}
    test_IC.set_IC(p)
    q = {1: 1, 4: 0, 10: 0, 13: 0}
    if q != test_IC.run():
        assert False


def test_IC_7403():
    test_IC = IC_7403()
    p = {1: 1, 2: 0, 4: 0, 5: 0, 7: 0, 9: 1, 10: 1, 12: 0, 13: 0, 14: 1}
    test_IC.set_IC(p)
    q = {3: 1, 6: 1, 8: 0, 11: 1}
    if q != test_IC.run():
        assert False


def test_IC_7404():
    test_IC = IC_7404()
    p = {1: 1, 3: 0, 5: 0, 7: 0, 9: 0, 11: 0, 13: 1, 14: 1}
    test_IC.set_IC(p)
    q = {2: 0, 4: 1, 6: 1, 8: 1, 10: 1, 12: 0}
    if q != test_IC.run():
        assert False


def test_IC_7405():
    test_IC = IC_7405()
    p = {1: 1, 3: 0, 5: 0, 7: 0, 9: 0, 11: 0, 13: 1, 14: 1}
    test_IC.set_IC(p)
    q = {2: 0, 4: 1, 6: 1, 8: 1, 10: 1, 12: 0}
    if q != test_IC.run():
        assert False


def test_IC_7408():
    test_IC = IC_7408()
    p = {1: 1, 2: 0, 4: 0, 5: 0, 7: 0, 9: 1, 10: 1, 12: 0, 13: 0, 14: 1}
    test_IC.set_IC(p)
    q = {3: 0, 6: 0, 8: 1, 11: 0}
    if q != test_IC.run():
        assert False


def test_IC_7410():
    test_IC = IC_7410()
    p = {1: 1, 2: 0, 13: 0, 3: 0, 4: 0, 5: 0, 9: 1, 10: 1, 11: 1, 14: 1, 7: 0}
    test_IC.set_IC(p)
    q = {12: 1, 6: 1, 8: 0}
    if q != test_IC.run():
        assert False


def test_IC_7411():
    test_IC = IC_7411()
    p = {1: 1, 2: 0, 13: 0, 3: 0, 4: 0, 5: 0, 9: 1, 10: 1, 11: 1, 14: 1, 7: 0}
    test_IC.set_IC(p)
    q = {12: 0, 6: 0, 8: 1}
    if q != test_IC.run():
        assert False


def test_IC_7412():
    test_IC = IC_7412()
    p = {1: 1, 2: 0, 13: 0, 3: 0, 4: 0, 5: 0, 9: 1, 10: 1, 11: 1, 14: 1, 7: 0}
    test_IC.set_IC(p)
    q = {12: 1, 6: 1, 8: 0}
    if q != test_IC.run():
        assert False


def test_IC_7413():
    test_IC = IC_7413()
    p = {1: 1, 2: 0, 4: 0, 5: 0, 9: 1, 10: 1, 12: 1, 13: 1, 14: 1, 7: 0}
    test_IC.set_IC(p)
    q = {6: 1, 8: 0}
    if q != test_IC.run():
        assert False


def test_IC_7415():
    test_IC = IC_7415()
    p = {1: 1, 2: 0, 13: 0, 3: 0, 4: 0, 5: 0, 9: 1, 10: 1, 11: 1, 14: 1, 7: 0}
    test_IC.set_IC(p)
    q = {12: 0, 6: 0, 8: 1}
    if q != test_IC.run():
        assert False


def test_IC_7416():
    test_IC = IC_7416()
    p = {1: 1, 2: 0, 13: 0, 3: 0, 4: 0, 5: 0, 9: 1, 10: 1, 11: 1, 14: 1, 7: 0}
    test_IC.set_IC(p)
    q = {2: 0, 4: 1, 6: 1, 8: 0, 10: 0, 12: 1}
    if q != test_IC.run():
        assert False


def test_IC_7417():
    test_IC = IC_7417()
    p = {1: 1, 2: 0, 13: 0, 3: 0, 4: 0, 5: 0, 9: 1, 10: 1, 11: 1, 14: 1, 7: 0}
    test_IC.set_IC(p)
    q = {2: 1, 4: 0, 6: 0, 8: 1, 10: 1, 12: 0}
    if q != test_IC.run():
        assert False


def test_IC_7418():
    test_IC = IC_7418()
    p = {
        1: 1,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        9: 1,
        10: 1,
        11: 1,
        12: 1,
        13: 1,
        14: 1,
        7: 0}
    test_IC.set_IC(p)
    q = {6: 1, 8: 0}
    if q != test_IC.run():
        assert False


def test_IC_7419():
    test_IC = IC_7419()
    p = {1: 1, 2: 0, 13: 0, 3: 0, 4: 0, 5: 0, 9: 1, 10: 1, 11: 1, 14: 1, 7: 0}
    test_IC.set_IC(p)
    q = {2: 0, 4: 1, 6: 1, 8: 0, 10: 0, 12: 1}
    if q != test_IC.run():
        assert False


def test_IC_7420():
    test_IC = IC_7420()
    p = {1: 1, 2: 0, 4: 0, 5: 0, 9: 1, 10: 1, 12: 1, 13: 1, 14: 1, 7: 0}
    test_IC.set_IC(p)
    q = {6: 1, 8: 0}
    if q != test_IC.run():
        assert False


def test_IC_7421():
    test_IC = IC_7421()
    p = {1: 1, 2: 0, 4: 0, 5: 0, 9: 1, 10: 1, 12: 1, 13: 1, 14: 1, 7: 0}
    test_IC.set_IC(p)
    q = {6: 0, 8: 1}
    if q != test_IC.run():
        assert False


def test_IC_7422():
    test_IC = IC_7422()
    p = {1: 1, 2: 0, 4: 0, 5: 0, 9: 1, 10: 1, 12: 1, 13: 1, 14: 1, 7: 0}
    test_IC.set_IC(p)
    q = {6: 1, 8: 0}
    if q != test_IC.run():
        assert False


def test_IC_7424():
    test_IC = IC_7424()
    p = {1: 1, 2: 0, 4: 0, 5: 0, 9: 1, 10: 1, 12: 1, 13: 1, 14: 1, 7: 0}
    test_IC.set_IC(p)
    q = {3: 1, 6: 1, 8: 0, 11: 0}
    if q != test_IC.run():
        assert False


def test_IC_7425():
    test_IC = IC_7425()
    p = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        9: 1,
        10: 1,
        11: 1,
        12: 1,
        13: 1,
        14: 1,
        7: 0}
    test_IC.set_IC(p)
    q = {6: 1, 8: 0}
    if q != test_IC.run():
        assert False


def test_IC_7426():
    test_IC = IC_7426()
    p = {1: 1, 2: 0, 4: 0, 5: 0, 9: 1, 10: 1, 12: 1, 13: 1, 14: 1, 7: 0}
    test_IC.set_IC(p)
    q = {3: 1, 6: 1, 8: 0, 11: 0}
    if q != test_IC.run():
        assert False


def test_IC_7427():
    test_IC = IC_7427()
    p = {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 9: 1, 10: 1, 11: 1, 13: 1, 14: 1, 7: 0}
    test_IC.set_IC(p)
    q = {6: 1, 8: 0, 12: 0}
    if q != test_IC.run():
        assert False


def test_IC_7428():
    test_IC = IC_7428()
    p = {2: 0, 3: 0, 5: 0, 6: 1, 8: 1, 9: 1, 11: 1, 12: 1, 14: 1, 7: 0}
    test_IC.set_IC(p)
    q = {1: 1, 4: 0, 10: 0, 13: 0}
    if q != test_IC.run():
        assert False


def test_IC_7430():
    test_IC = IC_7430()
    p = {1: 0, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 11: 1, 12: 1, 14: 1, 7: 0}
    test_IC.set_IC(p)
    q = {8: 1}
    if q != test_IC.run():
        assert False


def test_IC_7432():
    test_IC = IC_7432()
    p = {1: 1, 2: 0, 4: 0, 5: 0, 9: 1, 10: 1, 12: 1, 13: 1, 14: 1, 7: 0}
    test_IC.set_IC(p)
    q = {3: 1, 6: 0, 8: 1, 11: 1}
    if q != test_IC.run():
        assert False


def test_IC_7433():
    test_IC = IC_7433()
    p = {2: 0, 3: 0, 5: 0, 6: 0, 8: 1, 9: 1, 11: 1, 12: 1, 14: 1, 7: 0}
    test_IC.set_IC(p)
    q = {1: 1, 4: 1, 10: 0, 13: 0}
    if q != test_IC.run():
        assert False


def test_IC_7437():
    test_IC = IC_7437()
    p = {1: 1, 2: 0, 4: 0, 5: 0, 9: 1, 10: 1, 12: 1, 13: 1, 14: 1, 7: 0}
    test_IC.set_IC(p)
    q = {3: 1, 6: 1, 8: 0, 11: 0}
    if q != test_IC.run():
        assert False


def test_IC_7438():
    test_IC = IC_7438()
    m = {1: 1, 2: 1, 4: 0, 5: 0, 7: 0, 9: 0, 10: 0, 12: 0, 13: 1, 14: 1}
    test_IC.set_IC(m)
    n = {3: 0, 6: 1, 8: 1, 11: 1}
    if n != test_IC.run():
        assert False


def test_IC_7440():
    test_IC = IC_7440()
    p = {1: 1, 2: 0, 4: 0, 5: 0, 9: 1, 10: 1, 12: 1, 13: 1, 14: 1, 7: 0}
    test_IC.set_IC(p)
    q = {6: 1, 8: 0}
    if q != test_IC.run():
        assert False


def test_IC_7451():
    test_IC = IC_7451()
    p = {
        2: 1,
        3: 0,
        4: 0,
        5: 0,
        7: 0,
        1: 1,
        13: 1,
        12: 1,
        11: 0,
        10: 0,
        9: 0,
        14: 1}
    test_IC.set_IC(p)
    q = {6: 1, 8: 0}
    if q != test_IC.run():
        assert False


def test_IC_7454():
    test_IC = IC_7454()
    p = {
        1: 1,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        7: 0,
        10: 1,
        9: 1,
        11: 0,
        12: 0,
        13: 0,
        14: 1}
    test_IC.set_IC(p)
    q = {6: 1}
    if q != test_IC.run():
        assert False


def test_IC_7455():
    test_IC = IC_7455()
    p = {1: 1, 2: 0, 3: 0, 4: 0, 7: 0, 10: 1, 9: 1, 11: 0, 12: 0, 13: 0, 14: 1}
    test_IC.set_IC(p)
    q = {8: 1}
    if q != test_IC.run():
        assert False


def test_IC_7458():
    test_IC = IC_7458()
    p = {
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        7: 0,
        1: 1,
        13: 1,
        12: 1,
        11: 0,
        10: 0,
        9: 0,
        14: 1}
    test_IC.set_IC(p)
    q = {6: 0, 8: 1}
    if q != test_IC.run():
        assert False


def test_IC_7459():
    test_IC = IC_7459()
    p = {
        14: 1,
        7: 0,
        2: 1,
        3: 0,
        4: 0,
        5: 1,
        1: 1,
        13: 1,
        12: 1,
        11: 1,
        10: 1,
        9: 1}
    test_IC.set_IC(p)
    q = {6: 1, 8: 0}
    if q != test_IC.run():
        assert False


def test_IC_7464():
    test_IC = IC_7464()
    p = {1: 1, 7: 0, 13: 1, 12: 1, 11: 1, 14: 1}
    test_IC.set_IC(p)
    q = {8: 0}
    if q != test_IC.run():
        assert False


def test_IC_7486():
    test_IC = IC_7486()
    p = {1: 0, 2: 0, 4: 0, 5: 1, 7: 0, 9: 1, 10: 0, 12: 1, 13: 1, 14: 1}
    test_IC.set_IC(p)
    q = {3: 0, 6: 1, 8: 1, 11: 0}
    if q != test_IC.run():
        assert False


def test_IC_74260():
    test_IC = IC_74260()
    p = {
        1: 0,
        2: 0,
        3: 0,
        4: 1,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 1}
    test_IC.set_IC(p)
    q = {5: 1, 6: 0}
    if q != test_IC.run():
        assert False


def test_IC_74152():
    test_IC = IC_74152()
    m = {
        1: 1,
        2: 0,
        3: 1,
        4: 0,
        5: 1,
        7: 0,
        8: 0,
        9: 0,
        10: 1,
        11: 1,
        12: 0,
        13: 0,
        14: 1}
    test_IC.set_IC(m)
    n = {6: 1}
    if n != test_IC.run():
        assert False

#################################
# IC's with 5 pins
#################################


def test_IC_741G00():
    test_IC = IC_741G00()
    p = {1: 1, 2: 0, 3: 0, 5: 1}
    test_IC.set_IC(p)
    q = {4: 1}
    if q != test_IC.run():
        assert False


def test_IC_741G02():
    test_IC = IC_741G02()
    p = {1: 1, 2: 0, 3: 0, 5: 1}
    test_IC.set_IC(p)
    q = {4: 0}
    if q != test_IC.run():
        assert False


def test_IC_741G03():
    test_IC = IC_741G03()
    p = {1: 1, 2: 0, 3: 0, 5: 1}
    test_IC.set_IC(p)
    q = {4: 1}
    if q != test_IC.run():
        assert False


def test_IC_741G04():
    test_IC = IC_741G04()
    p = {2: 0, 3: 0, 5: 1}
    test_IC.set_IC(p)
    q = {4: 1}
    if q != test_IC.run():
        assert False


def test_IC_741G05():
    test_IC = IC_741G05()
    p = {2: 1, 3: 0, 5: 1}
    test_IC.set_IC(p)
    q = {4: 0}
    if q != test_IC.run():
        assert False


def test_IC_741G08():
    test_IC = IC_741G08()
    p = {1: 1, 2: 0, 3: 0, 5: 1}
    test_IC.set_IC(p)
    q = {4: 0}
    if q != test_IC.run():
        assert False

#################################
# IC's with 16 pins
#################################


def test_IC_7431():
    test_IC = IC_7431()
    p = {1: 1, 5: 0, 6: 0, 15: 1, 10: 1, 11: 1, 3: 1, 13: 0, 8: 0, 16: 1}
    test_IC.set_IC(p)
    q = {2: 0, 7: 1, 14: 0, 9: 0, 4: 1, 12: 0}
    if q != test_IC.run():
        assert False


def test_IC_7442():
    test_IC = IC_7442()
    p = {15: 1, 14: 0, 13: 0, 12: 0, 8: 0, 16: 1}
    test_IC.set_IC(p)
    q = {1: 1, 2: 0, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1}
    if q != test_IC.run():
        assert False


def test_IC_7443():
    test_IC = IC_7443()
    p = {15: 1, 14: 0, 13: 1, 12: 0, 8: 0, 16: 1}
    test_IC.set_IC(p)
    q = {1: 1, 2: 1, 3: 0, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1}
    if q != test_IC.run():
        assert False


def test_IC_7444():
    test_IC = IC_7444()
    p = {15: 1, 14: 0, 13: 1, 12: 0, 8: 0, 16: 1}
    test_IC.set_IC(p)
    q = {1: 1, 2: 1, 3: 1, 4: 0, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1}
    if q != test_IC.run():
        assert False


def test_IC_7445():
    test_IC = IC_7445()
    p = {15: 0, 14: 1, 13: 0, 12: 0, 8: 0, 16: 1}
    test_IC.set_IC(p)
    q = {1: 1, 2: 1, 3: 0, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 10: 1, 11: 1}
    if q != test_IC.run():
        assert False


def test_IC_7447():
    test_IC = IC_7447()
    p = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 1, 8: 0, 16: 1}
    test_IC.set_IC(p)
    q = {9: 1, 10: 1, 11: 0, 12: 0, 13: 1, 14: 1, 15: 1}
    if q != test_IC.run():
        assert False


def test_IC_74133():
    test_IC = IC_74133()
    p = {
        1: 0,
        2: 1,
        3: 1,
        4: 1,
        5: 1,
        6: 1,
        7: 1,
        8: 0,
        9: 1,
        10: 1,
        12: 1,
        13: 1,
        14: 1,
        15: 1,
        16: 1}
    test_IC.set_IC(p)
    q = {9: 1}
    if q != test_IC.run():
        assert False


def test_IC_7483():
    test_IC = IC_7483()
    p = {1: 1, 3: 0, 4: 0, 5: 1, 7: 1, 8: 0, 10: 1, 11: 1, 12: 0, 13: 1, 16: 1}
    test_IC.set_IC(p)
    q = {9: 1, 2: 1, 14: 1, 6: 0, 15: 0}
    if q != test_IC.run():
        assert False


def test_IC_74151A():
    test_IC = IC_74151A()
    m = {
        1: 1,
        2: 0,
        4: 1,
        3: 1,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 1,
        15: 1,
        16: 1}
    test_IC.set_IC(m)
    n = {5: 1, 6: 0}
    if n != test_IC.run():
        assert False


def test_IC_74153():
    test_IC = IC_74153()
    m = {
        1: 1,
        2: 1,
        3: 1,
        4: 0,
        5: 0,
        6: 0,
        8: 0,
        10: 0,
        11: 1,
        12: 0,
        13: 0,
        14: 0,
        15: 0,
        16: 1}
    test_IC.set_IC(m)
    n = {7: 0, 9: 0}
    if n != test_IC.run():
        assert False


def test_IC_74156():
    test_IC = IC_74156()
    m = {1: 1, 2: 0, 3: 0, 13: 1, 8: 0, 16: 1, 15: 1, 14: 0}
    test_IC.set_IC(m)
    n = {12: 1, 11: 1, 10: 1, 9: 1, 7: 1, 6: 0, 5: 1, 4: 1}
    if n != test_IC.run():
        assert False


def test_IC_74155():
    test_IC = IC_74155()
    m = {1: 1, 2: 0, 3: 1, 13: 0, 8: 0, 16: 1, 15: 1, 14: 0}
    test_IC.set_IC(m)
    n = {12: 1, 11: 1, 10: 1, 9: 1, 7: 1, 6: 1, 5: 0, 4: 1}
    if n != test_IC.run():
        assert False


def test_IC_74139():
    test_IC = IC_74139()
    m = {1: 0, 2: 0, 3: 0, 8: 0, 14: 0, 13: 1, 15: 0, 16: 1}
    test_IC.set_IC(m)
    n = {4: 0, 5: 1, 6: 1, 7: 1, 9: 1, 10: 0, 11: 1, 12: 1}
    if n != test_IC.run():
        assert False


def test_IC_74138():
    test_IC = IC_74138()
    m = {1: 1, 2: 0, 3: 1, 4: 0, 5: 0, 6: 1, 8: 0, 16: 1}
    test_IC.set_IC(m)
    n = {15: 1, 14: 1, 13: 1, 12: 1, 11: 1, 10: 0, 9: 1, 7: 1}
    if n != test_IC.run():
        assert False
