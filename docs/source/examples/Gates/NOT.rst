
Examples for NOT class
----------------------

.. code:: python

    # imports
    from __future__ import print_function
    from BinPy.Gates import *
.. code:: python

    # Initializing the NOT class
    
    gate = NOT(0)
    
    # Output of the NOT gate
    
    print (gate.output())

.. parsed-literal::

    1


.. code:: python

    # Input is changed to 0
    
    gate.setInput(1)
    
    # To get the input states
    
    print (gate.getInputStates())

.. parsed-literal::

    [1]


.. code:: python

    # New Output of the NOT gate
    
    print (gate.output())

.. parsed-literal::

    0


.. code:: python

    # Using Connectors as the input lines
    
    # Take a Connector
    
    conn = Connector()
    
    # Set Output of gate to Connector conn
    
    gate.setOutput(conn)
    
    # Put this connector as the input to gate1
    
    gate1 = NOT(conn)
    
    # Output of the gate1
    
    print (gate1.output())

.. parsed-literal::

    1


.. code:: python

    # Information about gate instance
    
    print (gate)

.. parsed-literal::

    NOT Gate; Output: 0; Inputs: [1];

