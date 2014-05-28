
Example for DEMUX class.
------------------------

.. code:: python

    from __future__ import print_function
    from BinPy.Combinational.combinational import *
.. code:: python

    # Initializing the DEMUX class
    
    # Must be a single input
    
    demux = DEMUX(1)
    
    # Put select lines
    
    # Select Lines must be power of 2
    
    demux.selectLines(0)
    
    # Output of demux
    
    print (demux.output())

.. parsed-literal::

    [1, 0]


.. code:: python

    # Input changes
    
    # Input at index 1 is changed to 0
    
    demux.setInput(0, 0)
    
    # New Output of the demux
    
    print (demux.output())

.. parsed-literal::

    [0, 0]


.. code:: python

    # Get Input States
    
    print (demux.getInputStates())

.. parsed-literal::

    [0]


.. code:: python

    # Using Connectors as the input lines
    
    # Take a Connector
    
    conn = Connector()
    
    # Set Output of demux to Connector conn
    
    # sets conn as the output at index 0
    
    demux.setOutput(0, conn)
    
    # Put this connector as the input to gate1
    
    gate1 = AND(conn, 0)
    
    # Output of the gate1
    
    print (gate1.output())

.. parsed-literal::

    0


.. code:: python

    # Changing select lines
    
    #selects input line 2
    
    demux.selectLine(0, 1)
    
    # New output of demux
    
    print (demux.output())

.. parsed-literal::

    [0, 0]


.. code:: python

    # Information about demux instance can be found by
    
    print (demux)

.. parsed-literal::

    DEMUX Gate; Output: [0, 0]; Inputs: [0];

