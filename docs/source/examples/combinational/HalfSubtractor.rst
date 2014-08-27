
Example for Half Subtractor class
---------------------------------

.. code:: python

    # Imports
    from __future__ import print_function
    from BinPy.combinational.combinational import *
.. code:: python

    # Initializing the HalfSubtractor class
    
    hs = HalfSubtractor(0, 1)
    
    # Output of HalfSubtractor
    
    print (hs.output())

.. parsed-literal::

    [1, 1]


.. code:: python

    # The output is of the form [DIFFERENCE, BORROW]
    
    # Input changes
    
    # Input at index 1 is changed to 0
    
    hs.set_input(1, 0)
    
    # New Output of the HalfSubtractor
    
    print (hs.output())

.. parsed-literal::

    [0, 0]


.. code:: python

    # Changing the number of inputs
    
    # No need to set the number, just change the inputs
    
    # Input length must be two
    
    hs.set_inputs(1, 1)
.. code:: python

    # New output of HalfSubtractor
    
    print (hs.output())

.. parsed-literal::

    [0, 0]


.. code:: python

    # Using Connectors as the input lines
    
    # Take a Connector
    
    conn = Connector()
    
    # Set Output at index to Connector conn
    
    hs.set_output(0, conn)
    
    # Put this connector as the input to gate1
    
    gate1 = AND(conn, 0)
    
    # Output of the gate1
    
    print (gate1.output())

.. parsed-literal::

    0

