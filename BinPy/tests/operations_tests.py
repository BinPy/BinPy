from BinPy.Operations import *
from nose.tools import with_setup, nottest, assert_raises

op = Operations()


def ADD_test():
    if op.ADD(0, 1) != '1':
        assert False
    if op.ADD('0', '1') != '1':
        assert False

    if op.ADD('01', '10') != '11':
        assert False
    if op.ADD('110', '111') != '1101':
        assert False


def SUB_test():
    if op.SUB(0, 1) != '1':
        assert False
    if op.SUB('0', '1') != '1':
        assert False

    if op.SUB('10', '01') != '1':
        assert False
    if op.SUB('110', '111') != '1':
        assert False


def MUL_test():
    if op.MUL(0, 1) != '0':
        assert False
    if op.MUL('0', '1') != '0':
        assert False

    if op.MUL('10', '01') != '10':
        assert False
    if op.MUL('110', '111') != '101010':
        assert False


def DIV_test():
    if op.DIV(0, 1) != '0':
        assert False
    if op.DIV('0', '1') != '0':
        assert False

    if op.DIV('10', '01') != '10':
        assert False
    if op.DIV('110', '111') != '0':
        assert False


def COMP_test():
    if op.COMP(0, 1) != '1':
        assert False
    if op.COMP('0', '1') != '1':
        assert False

    if op.COMP('110', '1') != '001':
        assert False
    if op.COMP('100', '1') != '011':
        assert False
    if op.COMP('110', '2') != '110':
        assert False


def decToBin_test():
    if Operations.decToBin(10) != '1010':
        assert False
    if Operations.decToBin(11) != '1011':
        assert False
    if Operations.decToBin(15) != '1111':
        assert False
    if Operations.decToBin(1234) != '10011010010':
        assert False
    if Operations.decToBin(56789) != '1101110111010101':
        assert False
    if Operations.decToBin(13.9876) != '1101.1111110011010011010110101000010110000111100101':
        assert False
    if Operations.decToBin(13.00) != '1101':
        assert False


def binToDec_test():
    if Operations.binToDec('111') != 7:
        assert False
    if Operations.binToDec('0111') != 7:
        assert False
    if Operations.binToDec('10011010010') != 1234:
        assert False
    if Operations.binToDec('0001') != 1:
        assert False
    if Operations.binToDec('1010101') != 85:
        assert False
    if Operations.binToDec('1010101.1010101') != 85.6640625:
        assert False
    if Operations.binToDec([1, 0, 1, 0, 1, 0, 1]) != 85:
        assert False
    assert_raises(Exception, Operations.binToDec, '1010101.10101012')
