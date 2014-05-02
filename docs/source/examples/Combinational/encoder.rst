Encoder
=======

An encoder is a device, circuit, transducer, software program, algorithm or person that converts information from one format or code to another, for the purposes of standardization, speed, secrecy, security or compressions. A simple encoder assigns a binary code to an active input line.

This example shows you how to use encoder in BinPy.

.. code:: python

    from __future__ import print_function
    from BinPy.Combinational.combinational import *
    
    encoder = Encoder(0, 1)  # Exacly 1 input must be 1
    print (encoder.output())

.. parsed-literal::

    [1]


.. code:: python

    # Changing the number of inputs
    # No need to set the number, just change the inputs
    # Input must be power of 2
    encoder.setInputs(0, 0, 0, 1) # Inputs must be power of 2
    
    # To get the input states
    print (encoder.getInputStates())

.. parsed-literal::

    [0, 0, 0, 1]


.. code:: python

    print (encoder.output())

.. parsed-literal::

    [1, 1]


.. code:: python

    # Using Connectors as the input lines
    conn = Connector()
    encoder.setOutput(1, conn)  # Set Output of decoder to Connector conn
    gate1 = AND(conn, 1)  #Put this connector as the input to gate1
    print (gate1.output())

.. parsed-literal::

    1


.. code:: python

    # Information about encoder instance can be found by
    print(encoder)

.. parsed-literal::

    Encoder Gate; Output: [1, 1]; Inputs: [0, 0, 0, 1];


