import sys
from BinPy import *
from nose.tools import with_setup, nottest


def test_make_booelan():
    a, b = make_boolean(['A', 'B', 'C', 'D'], [1, 5, 7], minterms=True)
    assert a == '((A AND C AND (NOT D)) OR (A AND (NOT B) AND (NOT D)))'
    assert b == 'OR(AND(A, C, NOT(D)), AND(A, NOT(B), NOT(D)))'
    a, b = make_boolean(['A', 'B', 'C', 'D'], [1, 5, 7], maxterms=True)
    if not sys.version_info > (3,4)
        assert a == '((NOT A) OR D OR (B AND (NOT C)))'
    assert b == 'OR(NOT(A), D, AND(B, NOT(C)))'
