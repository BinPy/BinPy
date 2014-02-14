from BinPy import *
from nose.tools import with_setup, nottest

def AND_test():
    lgate = And()
    outputLogic = []

    inputLogic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in inputLogic:
        lgate['A'] = logic[0]
        lgate['B'] = logic[1]
        outputLogic.append(lgate['C'])
    print outputLogic
    if outputLogic != [False, False, True, False]:
        assert False

def OR_test():
    lgate = Or()
    outputLogic = []

    inputLogic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in inputLogic:
        lgate['A'] = logic[0]
        lgate['B'] = logic[1]
        outputLogic.append(lgate['C'])
    print outputLogic
    if outputLogic != [False, True, True, True]:
        assert False

def NAND_test():
    lgate = Nand()
    outputLogic = []

    inputLogic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in inputLogic:
        lgate['A'] = logic[0]
        lgate['B'] = logic[1]
        outputLogic.append(lgate['C'])
    print outputLogic
    if outputLogic != [True, True, False, True]:
        assert False

def NOR_test():
    lgate = Nor()
    outputLogic = []

    inputLogic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in inputLogic:
        lgate['A'] = logic[0]
        lgate['B'] = logic[1]
        outputLogic.append(lgate['C'])
    print outputLogic
    if outputLogic != [True, False, False, False]:
        assert False

def XOR_test():
    lgate = Xor()
    outputLogic = []

    inputLogic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in inputLogic:
        lgate['A'] = logic[0]
        lgate['B'] = logic[1]
        outputLogic.append(lgate['C'])
    print outputLogic
    if outputLogic != [False, True, False, True]:
        assert False

def XNOR_test():
    lgate = Xnor()
    outputLogic = []

    inputLogic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in inputLogic:
        lgate['A'] = logic[0]
        lgate['B'] = logic[1]
        outputLogic.append(lgate['C'])
    print outputLogic
    if outputLogic != [True, False, True, False]:
        assert False