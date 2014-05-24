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

    lgate = AND(1, 0)
    try:
    	lgate.addInput(1)
    	if lgate.output() is not 0:
    		assert False

    	lgate.removeInput(1)
    	if lgate.output() is not 1:
    		assert False
    except Exception, e:
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

    lgate = OR(1, 0)
    try:
    	lgate.addInput(1)
    	if lgate.output() is not 1:
    		assert False

    	lgate.removeInput(1)
    	if lgate.output() is not 1:
    		assert False
    except Exception, e:
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

    lgate = NAND(1, 1)
    try:
    	lgate.addInput(1)
    	if lgate.output() is not 0:
    		assert False

    	lgate.removeInput(1)
    	if lgate.output() is not 0:
    		assert False
    except Exception, e:
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

    lgate = NOR(1, 0)
    try:
    	lgate.addInput(1)
    	if lgate.output() is not 0:
    		assert False

    	lgate.removeInput(1)
    	if lgate.output() is not 0:
    		assert False
    except Exception, e:
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

    lgate = XOR(1, 0)
    try:
    	lgate.addInput(1)
    	if lgate.output() is not 0:
    		assert False

    	lgate.removeInput(1)
    	if lgate.output() is not 0:
    		assert False
    except Exception, e:
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

        lgate = XNOR(1, 0)
    try:
    	lgate.addInput(1)
    	if lgate.output() is not 1:
    		assert False

    	lgate.removeInput(1)
    	if lgate.output() is not 0:
    		assert False
    except Exception, e:
    	assert False