
Example for Subtractors from combinational module
-------------------------------------------------

.. code:: python

    # Imports
    
    from __future__ import print_function
    from BinPy.combinational.combinational import *
Half Subtractor
~~~~~~~~~~~~~~~

.. code:: python

    print(HalfSubtractor.__doc__)

.. parsed-literal::

    This Class implements Half Subtractor, Arithmetic difference of two bits and return its
        Difference and Borrow output
        Output: [BORROW, DIFFERENCE]
        Example:
            >>> from BinPy import *
            >>> hs = HalfSubtractor(0, 1)
            >>> hs.output()
            [1, 1]
    
        


.. code:: python

    # Initializing the HalfSubtractor
    
    # Input is of the form (bit_1, bit_2)
    hs = HalfSubtractor(1, 1)
    
    # Output of HalfSubtractor
    # Output is of the form [BORROW, DIFFERENCE]
    
    print (hs.output())

.. parsed-literal::

    [0, 0]


.. code:: python

    # Input changes ( index, value )
    
    hs.set_input(1, 0)
    
    # New Output of the HalfSubtractor
    
    print (hs.output())

.. parsed-literal::

    [0, 1]


.. code:: python

    # Using Connectors as the input lines
    # Take a Connector
    
    conn_1 = Connector(1)
    conn_2 = Connector(0)
    conn_3 = Connector()
    
    # Setting the input of the Half Adder to the Connector conn_1 and conn_2
    
    hs.set_inputs(conn_1, conn_2)
    
    # Set Carry Output of Binary Adder to Connector conn_3
    
    hs.set_output(0, conn_3)
    
    # Use this connector as the input to gate1
    
    gate1 = NOT(conn_3)
    
    # Output of the gate1
    print (gate1.output())

.. parsed-literal::

    1


.. code:: python

    # Change the value of the conn_2
    conn_2.set_logic(0)
    
    # Verify with the output of the HalfAdder
    print (hs.output())

.. parsed-literal::

    [0, 1]


Full Adder
~~~~~~~~~~

.. code:: python

    print(FullSubtractor.__doc__)

.. parsed-literal::

    This Class implements Full Subtractor, Arithmetic difference of three bits and
        return its Difference and Borrow
        Output: [BORROW, DIFFERENCE]
        Example:
            >>> from BinPy import *
            >>> fs = FullSubtractor(0, 1, 1)
            >>> fs.output()
            [0, 1]
        


.. code:: python

    a, b, bi, d, bo = Connector(0), Connector(1), Connector(1), Connector(), Connector()
    
    # Initializing full adder using connectors
    fa = FullSubtractor(a, b, bi)
    
    # Connect outputs
    fa.set_output(0, bo)
    fa.set_output(1, d)
.. code:: python

    print (bo.get_logic(), d.get_logic())

.. parsed-literal::

    1 0

