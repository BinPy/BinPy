
Examples for Connector class
----------------------------

.. code:: python

    # imports
    from __future__ import print_function
    from BinPy.Gates import *
.. code:: python

    # Initializing the Connector class
    conn = Connector()
    
    # Input contains the initial value of the Connector
    
    # State of the Connector object
    
    print (conn.state)

.. parsed-literal::

    None


.. code:: python

    # Calling the connector intance returns its state
    
    print (conn())

.. parsed-literal::

    None


.. code:: python

    # Tapping the conector
    
    gate = OR(0, 1)
    conn.tap(gate, "output")
.. code:: python

    # Untapping the connector
    
    conn.untap(gate, "output")
.. code:: python

    # Checking the relation ship of gate with the Connector 'conn'
    
    print(conn.isOutputof(gate))
    
    print(conn.isInputof(gate))

.. parsed-literal::

    False
    False


.. code:: python

    # Set Output of gate to Connector conn
    
    gate.setOutput(conn)
.. code:: python

    # Checking the relation ship of gate with the Connector 'conn'
    
    print(conn.isOutputof(gate))
    
    print(conn.isInputof(gate))

.. parsed-literal::

    True
    False


.. code:: python

    # Put this connector as the input to gate1
    
    gate1 = AND(conn, 0)
.. code:: python

    # Output of the gate1
    
    print (gate1.output())

.. parsed-literal::

    0


.. code:: python

    # Information about conn instance
    
    print (conn)

.. parsed-literal::

    Connector; State: 1

