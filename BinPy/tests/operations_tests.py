from BinPy.Operations import *
from nose.tools import with_setup, nottest

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

