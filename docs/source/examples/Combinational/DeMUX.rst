Demultiplexer
=============

This example shows you working procedure of a demultiplexer in BinPy.

.. code:: python

    from __future__ import print_function
    from BinPy.Combinational.combinational import *

.. code:: python

    demux = DEMUX(1) # Must be a single input
.. code:: python

    demux.selectLines(0) #Select Lines must be power of 2
.. code:: python

    print (demux.output())

.. parsed-literal::

    [1, 0]


.. code:: python

    demux.setInput(0, 0) #Input at index 1 is changed to 0"
.. code:: python

    print (demux.output()) # New Output of the demux

.. parsed-literal::

    [0, 0]


.. code:: python

    print (demux.getInputStates()) # Get Input States

.. parsed-literal::

    [0]


.. code:: python

    # Using Connectors as the input lines
    conn = Connector()
    demux.setOutput(0, conn)  # Sets conn as the output at index 0
    gate1 = AND(conn, 0)  # Put this connector as the input to gate1
.. code:: python

    print (gate1.output())  # Output of the gate1

.. parsed-literal::

    0


.. code:: python

    demux.selectLine(0, 1) # Changing select lines
.. code:: python

    print (demux.output()) # New output of demux

.. parsed-literal::

    [0, 0]


.. code:: python

    # Information about demux instance can be found by using
    print(demux)

.. parsed-literal::

    DEMUX Gate; Output: [0, 0]; Inputs: [0];


