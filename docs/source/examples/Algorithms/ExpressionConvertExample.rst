
An example to demostrate functionality of ExpressionConvert.py
--------------------------------------------------------------

.. code:: python

    from __future__ import print_function
    from BinPy.Algorithms.ExpressionConvert import *
.. code:: python

    # Given Expression:
    expr = '~(((A^B)|(~a^b^C))) ~^ c'
.. code:: python

    # Obtained Expression
    converted = convertExpression(expr)
    
    print(converted)

.. parsed-literal::

    OR(XNOR(A, B), XNOR(a, b, C, c))


.. code:: python

    # Given Expression:
    expr = '((A AND B)xor(NOT(B) and C) xor(C and NOT(D)))or   E or NOT(F)'
.. code:: python

    # Obtained Expression
    converted = convertExpression(expr)
    
    print(converted)

.. parsed-literal::

    OR(XOR(AND(A, B), AND(NOT(B), C), AND(C, NOT(D))), E, NOT(F))


.. code:: python

    # Obtained Expression with two input gate contraint
    converted2 = convertExpression(expr, two_input = 1)
    
    print(converted2)

.. parsed-literal::

    OR(XOR(XOR(AND(A, B), AND(NOT(B), C)), AND(C, NOT(D))), OR(E, NOT(F)))


.. code:: python

    # Given Expression:
    expr = '(A XOR B XOR C)'
.. code:: python

    # Obtained Expression
    converted = convertExpression(expr)
    
    print(converted)

.. parsed-literal::

    XOR(A, B, C)


.. code:: python

    # Obtained Expression with two input gate contraint
    converted2 = convertExpression(expr, two_input = 1)
    
    print(converted2)

.. parsed-literal::

    XOR(A, XOR(B, C))


.. code:: python

    # Equivalent Expression with only AND, OR & NOT gates
    converted3 = convertExpression(expr, only_and_or_not=1)
    
    print(converted3)

.. parsed-literal::

    OR(AND(A, NOR(AND(B, NOT(C)), AND(NOT(B), C))), AND(NOT(A), OR(AND(B, NOT(C)), AND(NOT(B), C))))


.. code:: python

    # Given Expression
    expr = 'A XOR B'
.. code:: python

    # Equivalent Expression with only NAND gates
    converted = convertExpression(expr, only_nand=1)
    
    print(converted)

.. parsed-literal::

    NAND(NAND(A, NAND(A, B)), NAND(B, NAND(A, B)))


.. code:: python

    # Equivalent Expression with only NOR gates
    converted2 = convertExpression(expr, only_nor=1)
    
    print(converted2)

.. parsed-literal::

    NOR(NOR(NOR(A, NOR(A, B)), NOR(B, NOR(A, B))), NOR(NOR(A, NOR(A, B)), NOR(B, NOR(A, B))))

