
Examples for Expr class
-----------------------

.. code:: python

    # imports
    from __future__ import print_function
    from BinPy.dev import *
.. code:: python

    # Initializing the Expr class
    
    expr = Expr('A & B | C')
    
    # Parsing the expression
    
    print (expr.parse())

.. parsed-literal::

    AND(OR(C, B), A)


.. code:: python

    # Alternate way of defining an expression
    
    # Input is of the format: Expr(expression, variables)
    
    expr1 = Expr('AND(NOT(A), B)', 'A', 'B')
    
    print (expr.parse())

.. parsed-literal::

    AND(OR(C, B), A)


.. code:: python

    # Printing the truth table
    
    print(expr.truthTable())

.. parsed-literal::

    A B C O
    0 0 0 0
    0 0 1 0
    0 1 0 0
    0 1 1 0
    1 0 0 0
    1 0 1 1
    1 1 0 1
    1 1 1 1
    None

