
Example for BinaryAdder class
-----------------------------

.. code:: python

    # Imports
    
    from __future__ import print_function
    from BinPy.Combinational.combinational import *
.. code:: python

    # Initializing the BinaryAdder class
    
    # Input is of the form ([Binary number 1],[ BInary number 2], Carry]
    
    ba = BinaryAdder([0, 1], [1, 0], 0)
    
    # Output of BinaryAdder
    # Output is of the form [ [SUM], CARRY]
    
    print (ba.output())

.. parsed-literal::

    [0, 1, 1]


.. code:: python

    # Input changes
    
    ba.setInput(1, [0])
    
    # New Output of the BinaryAdder
    
    print (ba.output())

.. parsed-literal::

    [0, 0, 1]


.. code:: python

    # Changing the number of inputs
    # No need to set the number, just change the inputs
    # Input length must be three
    
    ba.setInputs([1, 1], [0, 1], 1)
    
    # To get the input states
    
    print (ba.getInputStates())

.. parsed-literal::

    [[1, 1], [0, 1], 1]


.. code:: python

    # New output of BinaryAdder
    
    print (ba.output())

.. parsed-literal::

    [1, 0, 0]


.. code:: python

    # Using Connectors as the input lines
    # Take a Connector
    
    conn = Connector()
    
    # Set Output of Binary Adder to Connector conn
    
    ba.setOutput(0, conn)
    
    # Put this connector as the input to gate1
    
    gate1 = AND(conn, 0)
    
    # Output of the gate1
    
    print (gate1.output())

.. parsed-literal::

    0


.. code:: python

    # Information about Binary Adder instance can be found by
    
    print (ba)

.. parsed-literal::

    [1, 0, 0]

