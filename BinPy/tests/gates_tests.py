from BinPy.Gates.gates import *
from nose.tools import with_setup, nottest


def AND_test():
    lgate = AND(1, 0)
    outputLogic = []

    inputLogic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in inputLogic:
        lgate.setInputs(logic[0], logic[1])
        outputLogic.append(lgate.output())
    if outputLogic != [0, 0, 1, 0]:
        assert False


def OR_test():
    lgate = OR(0, 0)
    outputLogic = []

    inputLogic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in inputLogic:
        lgate.setInputs(logic[0], logic[1])
        outputLogic.append(lgate.output())
    if outputLogic != [0, 1, 1, 1]:
        assert False


def NAND_test():
    lgate = NAND(0, 0)
    outputLogic = []

    inputLogic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in inputLogic:
        lgate.setInputs(logic[0], logic[1])
        outputLogic.append(lgate.output())
    if outputLogic != [1, 1, 0, 1]:
        assert False


def NOR_test():
    lgate = NOR(0, 0)
    outputLogic = []

    inputLogic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in inputLogic:
        lgate.setInputs(logic[0], logic[1])
        outputLogic.append(lgate.output())
    if outputLogic != [1, 0, 0, 0]:
        assert False


def XOR_test():
    lgate = XOR(0, 0)
    outputLogic = []

    inputLogic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in inputLogic:
        lgate.setInputs(logic[0], logic[1])
        outputLogic.append(lgate.output())
    if outputLogic != [0, 1, 0, 1]:
        assert False


def XNOR_test():
    lgate = XNOR(0, 0)
    outputLogic = []

    inputLogic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in inputLogic:
        lgate.setInputs(logic[0], logic[1])
        outputLogic.append(lgate.output())
    if outputLogic != [1, 0, 1, 0]:
        assert False
