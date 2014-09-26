
Example for Adders from combinational module
--------------------------------------------

.. code:: python

    # Imports
    
    from __future__ import print_function
    from BinPy.combinational.combinational import *
Half Adder
~~~~~~~~~~

.. code:: python

    print(HalfAdder.__doc__)

.. parsed-literal::

    This Class implements Half Adder, Arithmetic sum of two bits and return its
        Sum and Carry
        Output: [CARRY, SUM]
        Example:
            >>> from BinPy import *
            >>> ha = HalfAdder(0, 1)
            >>> ha.output()
            [0, 1]
    
        


.. code:: python

    # Initializing the HalfAdder
    
    # Input is of the form (bit_1, bit_2)
    ha = HalfAdder(1, 1)
    
    # Output of HalfAdder
    # Output is of the form [ CARRY, SUM ]
    
    print (ha.output())

.. parsed-literal::

    [1, 0]


.. code:: python

    # Input changes ( index, value )
    
    ha.set_input(1, 0)
    
    # New Output of the BinaryAdder
    
    print (ha.output())

.. parsed-literal::

    [0, 1]


.. code:: python

    # Using Connectors as the input lines
    # Take a Connector
    
    conn_1 = Connector(1)
    conn_2 = Connector(0)
    conn_3 = Connector()
    
    # Setting the input of the Half Adder to the Connector conn_1 and conn_2
    
    ha.set_inputs(conn_1, conn_2)
    
    # Set Carry Output of Binary Adder to Connector conn_3
    
    ha.set_output(0, conn_3)
    
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
    print (ha.output())

.. parsed-literal::

    [0, 1]


Full Adder
~~~~~~~~~~

.. code:: python

    print(FullAdder.__doc__)

.. parsed-literal::

    This Class implements Full Adder, Arithmetic sum of three bits and
        return its Sum and Carry
        Output: [CARRY, SUM]
        Example:
            >>> from BinPy import *
            >>> fa = FullAdder(0, 1, 1)
            >>> fa.output()
            [1, 0]
        


.. code:: python

    a, b, ci, s, co = Connector(1), Connector(1), Connector(1), Connector(), Connector()
    
    # Initializing full adder using connectors
    fa = FullAdder(a, b, ci)
    
    # Connect outputs
    fa.set_output(0, co)
    fa.set_output(1, s)
.. code:: python

    print (co.get_logic(), s.get_logic())

.. parsed-literal::

    1 1

