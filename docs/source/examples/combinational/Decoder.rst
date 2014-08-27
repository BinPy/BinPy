
Example for Decoder class
-------------------------

.. code:: python

    # Imports
    from __future__ import print_function
    from BinPy.combinational.combinational import *
.. code:: python

    # Initializing the Decoder class
    
    decoder = Decoder(0, 1)
    
    # Output of decoder
    
    print (decoder.output())

.. parsed-literal::

    [0, 1, 0, 0]


.. code:: python

    # Input changes
    
    # Input at index 1 is changed to 0
    
    decoder.set_input(1, 0)
    
    # New Output of the decoder
    
    print (decoder.output())

.. parsed-literal::

    [1, 0, 0, 0]


.. code:: python

    # Changing the number of inputs
    # No need to set the number, just change the inputs
    # Input must be power of 2
    
    decoder.set_inputs(1, 0, 0)
    
    # To get the input states
    
    print (decoder.get_input_states())

.. parsed-literal::

    [1, 0, 0]


.. code:: python

    # New output of decoder
    
    print (decoder.output())

.. parsed-literal::

    [0, 0, 0, 0, 1, 0, 0, 0]


.. code:: python

    # Using Connectors as the input lines
    
    conn = Connector()
    
    # Set Output of decoder to Connector conn
    
    decoder.set_output(1, conn)
    
    # Put this connector as the input to gate1
    
    gate1 = AND(conn, 1)
    
    # Output of the gate1
    
    print (gate1.output())

.. parsed-literal::

    0


.. code:: python

    # Information about decoder instance can be found by
    
    print (decoder)

.. parsed-literal::

    Decoder Gate; Output: [0, 0, 0, 0, 1, 0, 0, 0]; Inputs: [1, 0, 0];

