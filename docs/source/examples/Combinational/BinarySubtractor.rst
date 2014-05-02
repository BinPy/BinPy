
Example for BinarySubtractor class.
-----------------------------------

.. code:: python

    # Imports
    
    from __future__ import print_function
    from BinPy.Combinational.combinational import *
.. code:: python

    # Initializing the BinarySubtractor class
    
    # Input is of the form [Binary number 1],[ Binary number 2], Carry
    
    bs = BinarySubtractor([0, 1], [1, 0], 0)
    
    # Output of BinarySubtractor
    
    # Output is of the form [ [Difference], Borrow]
    
    print (bs.output())

.. parsed-literal::

    [1, 1, 1]


.. code:: python

    # Input changes
    
    # Input at index 1 is changed to [0, 0]
    
    bs.setInput(1, [0, 0])
    
    # New Output of the BinarySubtractor
    
    print (bs.output())

.. parsed-literal::

    [0, 0, 1]


.. code:: python

    # Changing the number of inputs
    
    # No need to set the number, just change the inputs
    
    # Input length must be three
    
    bs.setInputs([1, 0], [1, 1], 1)
    
    # To get the input states
    
    print (bs.getInputStates())

.. parsed-literal::

    [[1, 0], [1, 1], 1]


.. code:: python

    # New output of BinarySubtractor
    
    print (bs.output())

.. parsed-literal::

    [1, 1, 1]


.. code:: python

    # Using Connectors as the input lines
    
    # Take a Connector
    
    conn = Connector()
    
    # Set Output of Binary Subtractor to Connector conn
    
    # sets the conn at index 0
    
    bs.setOutput(0, conn)
    
    # Put this connector as the input to gate1
    
    gate1 = AND(conn, 0)
    
    # Output of the gate1
    
    print (gate1.output())

.. parsed-literal::

    0


.. code:: python

    # Information about bs instance can be found by
    
    print (bs)

.. parsed-literal::

    [1, 1, 1]

