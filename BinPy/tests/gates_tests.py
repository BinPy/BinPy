from BinPy.connectors.connector import *
from BinPy.gates.gates import *
from nose.tools import with_setup, nottest


def NOT_test():
    lgate = NOT(1)
    output_logic = []

    input_logic = [1, 0]

    for logic in input_logic:
        lgate.set_inputs(logic)
        output_logic.append(lgate.output())
    if output_logic != [0, 1]:
        assert False


def AND_test():
    lgate = AND(1, 0)
    output_logic = []

    input_logic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in input_logic:
        lgate.set_inputs(logic[0], logic[1])
        output_logic.append(lgate.output())
    if output_logic != [0, 0, 1, 0]:
        assert False

    lgate = AND(1, 0)
    try:
        lgate.add_input(1)
        if lgate.output() is not 0:
            assert False

        lgate.remove_input(1)
        if lgate.output() is not 1:
            assert False
    except Exception:
        assert False


def OR_test():
    lgate = OR(0, 0)
    output_logic = []

    input_logic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in input_logic:
        lgate.set_inputs(logic[0], logic[1])
        output_logic.append(lgate.output())
    if output_logic != [0, 1, 1, 1]:
        assert False

    lgate = OR(1, 0)
    try:
        lgate.add_input(1)
        if lgate.output() is not 1:
            assert False

        lgate.remove_input(1)
        if lgate.output() is not 1:
            assert False
    except Exception:
        assert False


def NAND_test():
    lgate = NAND(0, 0)
    output_logic = []

    input_logic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in input_logic:
        lgate.set_inputs(logic[0], logic[1])
        output_logic.append(lgate.output())
    if output_logic != [1, 1, 0, 1]:
        assert False

    lgate = NAND(1, 1)
    try:
        lgate.add_input(1)
        if lgate.output() is not 0:
            assert False

        lgate.remove_input(1)
        if lgate.output() is not 0:
            assert False
    except Exception:
        assert False


def NOR_test():
    lgate = NOR(0, 0)
    output_logic = []

    input_logic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in input_logic:
        lgate.set_inputs(logic[0], logic[1])
        output_logic.append(lgate.output())
    if output_logic != [1, 0, 0, 0]:
        assert False

    lgate = NOR(1, 0)
    try:
        lgate.add_input(1)
        if lgate.output() is not 0:
            assert False

        lgate.remove_input(1)
        if lgate.output() is not 0:
            assert False
    except Exception:
        assert False


def XOR_test():
    lgate = XOR(0, 0)
    output_logic = []

    input_logic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in input_logic:
        lgate.set_inputs(logic[0], logic[1])
        output_logic.append(lgate.output())
    if output_logic != [0, 1, 0, 1]:
        assert False

    lgate = XOR(1, 0)
    try:
        lgate.add_input(1)
        if lgate.output() is not 0:
            assert False

        lgate.remove_input(1)
        if lgate.output() is not 0:
            assert False
    except Exception:
        assert False


def XNOR_test():
    lgate = XNOR(0, 0)
    output_logic = []

    input_logic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in input_logic:
        lgate.set_inputs(logic[0], logic[1])
        output_logic.append(lgate.output())
    if output_logic != [1, 0, 1, 0]:
        assert False

        lgate = XNOR(1, 0)
    try:
        lgate.add_input(1)
        if lgate.output() is not 1:
            assert False

        lgate.remove_input(1)
        if lgate.output() is not 0:
            assert False
    except Exception:
        assert False
