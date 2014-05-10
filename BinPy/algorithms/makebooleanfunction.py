from BinPy.algorithms.ExpressionConvert import *
from BinPy.algorithms.QuineMcCluskey import *
import sys


def make_boolean(vars, min_max, dont_care=None, **kwargs):
    """
    A function which takes in minterms/maxterms and
    returns the Boolean Function and implementable form
    Don't Care Conditions can also be provided (optional)

    Examples
    ========

    >>> from BinPy import *
    >>> le, gf = make_boolean(['A', 'B', 'C'], [1, 4, 7], minterms=True)
    >>> le
    '((A AND (NOT B) AND (NOT C)) OR (A AND B AND C) OR ((NOT A) AND (NOT B) AND C))'
    >>> gf
    'OR(AND(A, NOT(B), NOT(C)), AND(A, B, C), AND(NOT(A), NOT(B), C))'

    """

    ones = []
    while(True):
        if 'minterms' in kwargs:
            if kwargs['minterms'] is True:
                ones = min_max
                if ones[-1] >= pow(2, len(vars)):
                    raise Exception("Error: Invalid minterms")
                break
        elif 'maxterms' in kwargs:
            if kwargs['maxterms'] is True:
                zeros = min_max
                if zeros[-1] >= pow(2, len(vars)):
                    raise Exception("Error: Invalid maxterms")
                for i in range(pow(2, len(vars))):
                    if i not in zeros:
                        ones.append(i)
                break
    if dont_care is not None:
        _dont_care = list(map(int, dont_care))

    qm = QM(vars)
    if dont_care is not None:
        LogicalExpression = qm.get_function(qm.solve(ones, _dont_care)[1])
    else:
        LogicalExpression = qm.get_function(qm.solve(ones)[1])
    GateForm = convertExpression(LogicalExpression)
    return LogicalExpression, GateForm
