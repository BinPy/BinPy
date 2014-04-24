
Examples for XOR class
----------------------

.. code:: python

    # imports
    from __future__ import print_function
    from BinPy.Gates import *
.. code:: python

    # Initializing the XOR class
    
    gate = XOR(0, 1)
    
    # Output of the XOR gate
    
    print (gate.output())

.. parsed-literal::

    1


.. code:: python

    # Input changes
    # Input at index 1 is changed to 0
    
    gate.setInput(1, 0)
    
    # New Output of the XOR gate
    
    print (gate.output())

.. parsed-literal::

    0


.. code:: python

    # Changing the number of inputs
    
    # No need to set the number, just change the inputs
    
    gate.setInputs(1, 1, 1, 1)
    
    # To get the input states
    
    print (gate.getInputStates())

.. parsed-literal::

    [1, 1, 1, 1]


.. code:: python

    # New output of the XOR gate
    
    print (gate.output())

.. parsed-literal::

    0


.. code:: python

    # Using Connectors as the input lines
    
    # Take a Connector
    
    conn = Connector()
.. code:: python

    # Set Output of gate to Connector conn
    
    gate.setOutput(conn)
.. code:: python

    # Put this connector as the input to gate1
    
    gate1 = XOR(conn, 0)
.. code:: python

    # Output of the gate1
    
    print (gate1.output())

.. parsed-literal::

    0


.. code:: python

    # Information about gate instance
    
    print (gate)

.. parsed-literal::

    XOR Gate; Output: 0; Inputs: [1, 1, 1, 1];

