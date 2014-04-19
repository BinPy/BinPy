Expression Convert
==================

This examples shows you how to use inbuilt function convertExpression
to convert one form of expression to other.

.. code:: python

    from __future__ import print_function
    from BinPy.Algorithms.ExpressionConvert import *
.. code:: python

    expr = '~(((A^B)|(~a^b^C))) ~^ c'  # Given Expression
.. code:: python

    converted = convertExpression(expr)
.. code:: python

    print("Obtained Expression:\n" + converted)

.. parsed-literal::

    Obtained Expression:
    OR(XNOR(A, B), XNOR(a, b, C, c))


.. code:: python

    expr = '((A AND B)xor(NOT(B) and C) xor(C and NOT(D)))or   E or NOT(F)'
.. code:: python

    converted = convertExpression(expr)
    converted2 = convertExpression(expr, two_input=1)
.. code:: python

    print("Obtained Expression:\n" + converted)
    print("Obtained Expression with two input gate constraint:\n" + converted2)

.. parsed-literal::

    Obtained Expression:
    OR(XOR(AND(A, B), AND(NOT(B), C), AND(C, NOT(D))), E, NOT(F))
    Obtained Expression with two input gate constraint:
    OR(XOR(XOR(AND(A, B), AND(NOT(B), C)), AND(C, NOT(D))), OR(E, NOT(F)))


.. code:: python

    expr = '(A XOR B XOR C)'
    converted = convertExpression(expr)
.. code:: python

    print("Obtained Expression:\n" + converted)

.. parsed-literal::

    Obtained Expression:
    XOR(A, B, C)


.. code:: python

    converted = convertExpression(expr, two_input=1)
.. code:: python

    print("Obtained Expression with 2 input constraint:\n" + converted)

.. parsed-literal::

    Obtained Expression with 2 input constraint:
    XOR(A, XOR(B, C))


.. code:: python

    converted = convertExpression(expr, only_and_or_not=1)
.. code:: python

    print("Equivalent Expression with only AND, OR & NOT gates is:\n" + converted)

.. parsed-literal::

    Equivalent Expression with only AND, OR & NOT gates is:
    OR(AND(A, NOR(AND(B, NOT(C)), AND(NOT(B), C))), AND(NOT(A), OR(AND(B, NOT(C)), AND(NOT(B), C))))


.. code:: python

    expr = 'A XOR B'
.. code:: python

    print("\nGiven Expression:\n" + expr)

.. parsed-literal::

    
    Given Expression:
    A XOR B


.. code:: python

    converted = convertExpression(expr, only_nand=1)
.. code:: python

    print("Equivalent Expression with only NAND gates is:\n" + converted)

.. parsed-literal::

    Equivalent Expression with only NAND gates is:
    NAND(NAND(A, NAND(A, B)), NAND(B, NAND(A, B)))


.. code:: python

    converted = convertExpression(expr, only_nor=1)
.. code:: python

    print("Equivalent Expression with only NAND gates is:\n" + converted)

.. parsed-literal::

    Equivalent Expression with only NAND gates is:
    NOR(NOR(NOR(A, NOR(A, B)), NOR(B, NOR(A, B))), NOR(NOR(A, NOR(A, B)), NOR(B, NOR(A, B))))


