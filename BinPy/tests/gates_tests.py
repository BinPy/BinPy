from BinPy.Gates.gates import *
from nose.tools import with_setup, nottest


inputLogic = [(0, 0), (1, 0), (1, 1), (0, 1),
              (0, 2), (0, 3), (1, 2), (1, 3)]

def AND_test():
    c = [Connector() for i in range(3)]
    g = AND(*c)
    outputLogic = []

    for logic in inputLogic:
        c[1].set(logic[0])
        c[2].set(logic[1])
        outputLogic.append(c[0].state)
    assert outputLogic == [0, 0, 1, 0, 0, 0, 3, 3]

def OR_test():
    c = [Connector() for i in range(3)]
    g = OR(*c)
    outputLogic = []

    for logic in inputLogic:
        c[1].set(logic[0])
        c[2].set(logic[1])
        outputLogic.append(c[0].state)
    assert outputLogic == [0, 1, 1, 1, 3, 3, 1, 1]

def NAND_test():
    # Output connector state can also be accessed through the gate's output
    c = [Connector() for i in range(3)]
    g = NAND(*c)
    outputLogic = []

    for logic in inputLogic:
        c[1].set(logic[0])
        c[2].set(logic[1])
        outputLogic.append(g.output.state)
    assert outputLogic == [1, 1, 0, 1, 1, 1, 3, 3]

def NOR_test():
    c = [Connector() for i in range(3)]
    g = NOR(*c)
    outputLogic = []

    for logic in inputLogic:
        c[1].set(logic[0])
        c[2].set(logic[1])
        outputLogic.append(c[0].state)
    assert outputLogic == [1, 0, 0, 0, 3, 3, 0, 0]

def XOR_test():
    c = [Connector() for i in range(3)]
    g = XOR(*c)
    outputLogic = []

    for logic in inputLogic:
        c[1].set(logic[0])
        c[2].set(logic[1])
        outputLogic.append(c[0].state)
    assert outputLogic == [0, 1, 0, 1, 3, 3, 3, 3]

def XNOR_test():
    c = [Connector() for i in range(3)]
    g = XNOR(*c)
    outputLogic = []

    for logic in inputLogic:
        c[1].set(logic[0])
        c[2].set(logic[1])
        outputLogic.append(c[0].state)
    assert outputLogic == [1, 0, 1, 0, 3, 3, 3, 3]

def NOT_test():
    inputLogic = [0, 1, 2, 3]
    c = [Connector() for i in range(2)]
    g = NOT(*c)
    outputLogic = []

    for logic in inputLogic:
        c[1].set(logic)
        outputLogic.append(c[0].state)
    assert outputLogic == [1, 0, 3, 3]

def connection_test():
    c = [Connector(i) for i in range(4)]
    g = AND(*c)
    for i in range(4):
        c2 = c[i:] + c[:i]
        g.connect(*c2)
        assert c2[0].connections['output'] == [g]
        for j in range(1,4):
            assert c2[j].connections['input'] == [g]
        assert g.output == c2[0]
        assert g.inputs == c2[1:4]
    g.disconnect()
    for i in range(4):
        assert not c[i].connections['input']
        assert not c[i].connections['output']

