
Examples for AND class
----------------------

.. code:: python

    from __future__ import print_function
    from BinPy.Gates import *
.. code:: python

    # Initializing the AND class
    
    gate = AND(0, 1)
    
    # Output of the AND gate
    
    print (gate.output())

.. parsed-literal::

    0


.. code:: python

    # Input changes
    
    # Input at index 1 is changed to 0
    
    gate.setInput(1, 0)
    
    # New Output of the AND gate
    
    print (gate.output())

.. parsed-literal::

    0


.. code:: python

    # Changing the number of inputs
    
    # No need to set the number, just change the inputs
    
    gate.setInputs(1, 1, 1, 1)
.. code:: python

    # To get the input states
    
    print (gate.getInputStates())

.. parsed-literal::

    [1, 1, 1, 1]


.. code:: python

    # New output of the AND gate
    
    print (gate.output())

.. parsed-literal::

    1


.. code:: python

    # Using Connectors as the input lines
    
    # Take a Connector
    
    conn = Connector()
    
    # Set Output of gate to Connector conn
    
    gate.setOutput(conn)
    
    # Put this connector as the input to gate1
    
    gate1 = AND(conn, 0)
.. code:: python

    # Output of the gate1
    
    print (gate1.output())

.. parsed-literal::

    0


.. code:: python

    # Information about gate instance
    
    print (gate)

.. parsed-literal::

    AND Gate; Output: 1; Inputs: [1, 1, 1, 1];

