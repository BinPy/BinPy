Decoder
=======


A decoder is a device which does the reverse operation of an encoder, undoing the encoding so that the original information can be retrieved. The same method used to encode is usually just reversed in order to decode. It is a combinational circuit that converts binary information from n input lines to a maximum of 2n unique output lines.

This example shows you the working of decoder in BinPy.

.. code:: python

    from __future__ import print_function
    from BinPy.Combinational.combinational import *
    
    decoder = Decoder(0, 1)  # Initializing a decoder object
    print(decoder.output())

.. parsed-literal::

    [0, 1, 0, 0]


.. code:: python

    decoder.setInput(1, 0)  # Input at index 1 is changed to 0
    print (decoder.output())

.. parsed-literal::

    [1, 0, 0, 0]


.. code:: python

    # Changing the number of inputs
    # No need to set the number, just change the inputs
    # Input must be power of 2
    decoder.setInputs(1, 0, 0) 
.. code:: python

    print (decoder.getInputStates())  # Get input states

.. parsed-literal::

    [1, 0, 0]


.. code:: python

    print (decoder.output())

.. parsed-literal::

    [0, 0, 0, 0, 1, 0, 0, 0]


.. code:: python

    # Using decoders with Connectors
    conn = Connector()
    decoder.setOutput(1, conn)  # Set Output of decoder to Connector conn
    gate1 = AND(conn, 1)  # Put this connector as the input to gate1
    print (gate1.output())

.. parsed-literal::

    0


.. code:: python

    print (decoder) # To get information about the decoder instance

.. parsed-literal::

    Decoder Gate; Output: [0, 0, 0, 0, 1, 0, 0, 0]; Inputs: [1, 0, 0];


