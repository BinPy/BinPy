from BinPy.Gates.backtrack import *
from BinPy.Gates.gates import *
from BinPy.Gates.connector import *
from BinPy.Combinational.combinational import *

from nose.tools import with_setup, nottest

'''
Testing backtrack function for depth 0 to 4
'''

def backtrack_depth_0_test():
    c1 = Connector()
    g1 = AND(True, True)
    g1.setOutput(c1)

    c2 = Connector()
    g2 = AND(False, False)
    g2.setOutput(c2)

    g3 = AND(c1, c2)

    if not backtrack(g3, 0) == (g3, False):
        assert False

def backtrack_depth_1_test():
    c1 = Connector()
    g1 = AND(True, True)
    g1.setOutput(c1)

    c2 = Connector()
    g2 = AND(False, False)
    g2.setOutput(c2)

    g3 = AND(c1, c2)

    if not backtrack(g3, 1) == (g3, [(c1, True), (c2, False)]):
        assert False

def backtrack_depth_2_test():
    c1 = Connector()
    g1 = AND(True, True)
    g1.setOutput(c1)

    c2 = Connector()
    g2 = AND(False, False)
    g2.setOutput(c2)

    g3 = AND(c1, c2)

    if not backtrack(g3, 2) == (g3, [(c1, [(g1, True)]), (c2, [(g2, False)])]):
        assert False

def backtrack_depth_3_test():
    c1 = Connector()
    g1 = AND(True, True)
    g1.setOutput(c1)

    c2 = Connector()
    g2 = AND(False, False)
    g2.setOutput(c2)

    g3 = AND(c1, c2)

    if not backtrack(g3, 3) == (g3, [(c1, [(g1, [True, True])]), (c2, [(g2, [False, False])])]):
        assert False

def backtrack_depth_4_test():
    c1 = Connector()
    g1 = AND(True, True)
    g1.setOutput(c1)

    c2 = Connector()
    g2 = AND(False, False)
    g2.setOutput(c2)

    g3 = AND(c1, c2)

    if not backtrack(g3, 4) == (g3, [(c1, [(g1, [True, True])]), (c2, [(g2, [False, False])])]):
        assert False

'''
Testing backtrack with all gates
'''

def backtrack_all_gates_depth_0_test():
    g1 = OR(False, True)
    g2 = NOT(True)
    g3 = XOR(False, True)
    g4 = XNOR(False, True)
    g5 = NAND(False, True)
    g6 = NOR(False, True)
    final = AND(g1, g2, g3, g4, g5, g6)

    if not backtrack(final, 0) == (final, False):
        assert False

def backtrack_all_gates_depth_1_test():
    g1 = OR(False, True)
    g2 = NOT(True)
    g3 = XOR(False, True)
    g4 = XNOR(False, True)
    g5 = NAND(False, True)
    g6 = NOR(False, True)
    final = AND(g1, g2, g3, g4, g5, g6)

    if not backtrack(final, 1) == (final, [(g1, True), (g2, False), (g3, True), (g4, False), (g5, True), (g6, False)]):
        assert False

def backtrack_all_gates_depth_2_test():
    g1 = OR(False, True)
    g2 = NOT(True)
    g3 = XOR(False, True)
    g4 = XNOR(False, True)
    g5 = NAND(False, True)
    g6 = NOR(False, True)
    final = AND(g1, g2, g3, g4, g5, g6)

    if not backtrack(final, 2) == (final, [(g1, [False, True]), (g2, [True]), (g3, [False, True]), (g4, [False, True]), (g5, [False, True]), (g6, [False, True])]):
        assert False

def backtrack_all_gates_depth_4_test():
    g1 = OR(False, True)
    g2 = NOT(True)
    g3 = XOR(False, True)
    g4 = XNOR(False, True)
    g5 = NAND(False, True)
    g6 = NOR(False, True)
    final = AND(g1, g2, g3, g4, g5, g6)

    if not backtrack(final, 3) == (final, [(g1, [False, True]), (g2, [True]), (g3, [False, True]), (g4, [False, True]), (g5, [False, True]), (g6, [False, True])]):
        assert False

'''
Testing with Combinational (mux, demux, encoder and decoder)
'''

def backtrack_combinational_test():
    c0 = Connector()
    c1 = Connector()
    c2 = Connector()
    c3 = Connector()
    c4 = Connector()
    c5 = Connector()

    demux = DEMUX(True)
    demux.selectLines(1)
    demux.setOutput(0, c0)
    demux.setOutput(1, c1)
    a1 = AND(c0, c1)

    dec = Decoder(0, 1)
    dec.setOutput(0, c2)
    dec.setOutput(1, c3)
    a2 = AND(c2, c3)

    enc = Encoder(False, False, True, False)
    enc.setOutput(0, c4)
    enc.setOutput(1, c5)
    a3 = AND(c4, c5)

    final_a = AND(a1, a2, a3)

    print backtrack(final_a, 0)
    print backtrack(final_a, 1)
    print backtrack(final_a, 2)
    print backtrack(final_a, 3)
    print backtrack(final_a, 4)
    print backtrack(final_a, 5)

    if not backtrack(final_a, 4) == (final_a, [(a1, [(c0, [(demux, [True])]), (c1, [(demux, [True])])]), (a2, [(c2, [(dec, [False, True])]), (c3, [(dec, [False, True])])]), (a3, [(c4, [(enc, [False, False, True, False])]), (c5, [(enc, [False, False, True, False])])])]):
        assert False

