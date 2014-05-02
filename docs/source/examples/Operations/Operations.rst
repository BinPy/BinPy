
Examples for operations class
-----------------------------

.. code:: python

    from __future__ import print_function
    from BinPy.Operations.operations import *
.. code:: python

    # Initialize the operation class
    
    op = Operations()
    
    # Binary Addition
    
    print (op.ADD('0', '1'), op.ADD('00', '10'), op.ADD('010', '100'))

.. parsed-literal::

    1 10 110


.. code:: python

    # Binary Subtraction
    
    print (op.SUB('1', '0'), op.SUB('00', '10'), op.SUB('010', '100'))

.. parsed-literal::

    1 10 10


.. code:: python

    # Binary Multiplication
    
    print (op.MUL('0', '1'), op.MUL('00', '10'), op.MUL('010', '100'))

.. parsed-literal::

    0 0 1000


.. code:: python

    # Binary Division
    
    print (op.DIV('0', '1'), op.DIV('00', '10'), op.DIV('010', '100'))

.. parsed-literal::

    0 0 0


.. code:: python

    # Binary Complement
    
    print (
        op.COMP(
            '0', '1'), op.COMP(
            '00', '1'), op.COMP(
            '00', '2'), op.COMP(
            '010', '1'))

.. parsed-literal::

    1 11 100 101


.. code:: python

    # Conversion from binary to decimal
    
    print (Operations.binToDec('111'))

.. parsed-literal::

    7


.. code:: python

    # Conversion from decimal to binary
    
    print (Operations.decToBin(12))

.. parsed-literal::

    1100

