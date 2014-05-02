from BinPy import *
from nose.tools import with_setup, nottest


def parse_test():

    assert Expr('A & B').parse() == 'AND(B, A)'

    assert Expr('(A & B)').parse() == 'AND(B, A)'

    assert Expr('(~A) & B').parse() == 'AND(B, NOT(A))'

    assert Expr('~(A & B)').parse() == 'NAND(B, A)'

    assert Expr('A | B').parse() == 'OR(B, A)'

    assert Expr('A ^ B').parse() == 'XOR(B, A)'

    assert Expr('A ^ ~B').parse() == 'XOR(NOT(B), A)'
