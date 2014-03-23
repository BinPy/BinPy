from BinPy.Gates.gates import *
from BinPy.Combinational.combinational import *

from nose.tools import with_setup, nottest
import re


def AND_print_test():
    gate = AND(0, 1)
    if not re.search("AND Gate; Output: 0; Inputs: \[0, 1];", gate.__str__()):
        assert False


def OR_print_test():
    gate = OR(0, 1)
    if not re.search("OR Gate; Output: 1; Inputs: \[0, 1];", gate.__str__()):
        assert False


def NOT_print_test():
    gate = NOT(1)
    if not re.search("NOT Gate; Output: 0; Inputs: \[1];", gate.__str__()):
        assert False


def XOR_print_test():
    gate = XOR(0, 1)
    if not re.search("XOR Gate; Output: 1; Inputs: \[0, 1];", gate.__str__()):
        assert False


def XNOR_print_test():
    gate = XNOR(0, 1)
    if not re.search("XNOR Gate; Output: 0; Inputs: \[0, 1];", gate.__str__()):
        assert False


def NAND_print_test():
    gate = NAND(0, 1)
    if not re.search("NAND Gate; Output: 1; Inputs: \[0, 1];", gate.__str__()):
        assert False


def NOR_print_test():
    gate = NOR(0, 1)
    if not re.search("NOR Gate; Output: 0; Inputs: \[0, 1];", gate.__str__()):
        assert False


def MUX_print_test():
    gate = MUX(1, 1)
    gate.selectLines(0)
    if not re.search("MUX Gate; Output: 1; Inputs: \[1, 1];", gate.__str__()):
        assert False


def DEMUX_print_test():
    gate = DEMUX(1)
    gate.selectLines(1)
    if not re.search("DEMUX Gate; Output: \[0, 1]; Inputs: \[1];", gate.__str__()):
        assert False


def Encoder_print_test():
    gate = Encoder(0, 0, 0, 1)
    if not re.search("Encoder Gate; Output: \[1, 1]; Inputs: \[0, 0, 0, 1];", gate.__str__()):
        assert False


def Decoder_print_test():
    gate = Decoder(0, 0)
    if not re.search("Decoder Gate; Output: \[1, 0, 0, 0]; Inputs: \[0, 0];", gate.__str__()):
        assert False
