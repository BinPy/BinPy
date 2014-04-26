
Monostable Multivibrator - Multivibrator in Mode 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from __future__ import print_function
    from BinPy.tools.clock import Clock
    from BinPy.Gates import Connector
    from BinPy.tools.multivibrator import Multivibrator
    from BinPy.tools.oscilloscope import Oscilloscope
    import time
.. code:: python

    # MODE selects the mode of operation of the multivibrator.
    
    # Mode No. :  Description
    #   1          Monostable
    #   2          Astable
    #   3          Bistable
    
    out = Connector()
.. code:: python

    # Initialize mutivibrator in MODE 1
    
    m = Multivibrator(0, mode=1, time_period=1)
    m.start()
    m.setOutput(out)
.. code:: python

    # Initialize the oscilloscope 
    o = Oscilloscope((out, 'OUT'))
    o.start()
    o.setScale(0.005)  # Set scale by trial and error.
    o.setWidth(100)
    o.unhold()
    time.sleep(0.1)
    m.trigger()  # Also works with m()
    time.sleep(0.1)

.. parsed-literal::

    [0m
    [0m


.. code:: python

    # Display the oscilloscope
    o.display()

.. parsed-literal::

    [0m===================================================================================================================
    BinPy - Oscilloscope
    ===================================================================================================================
                                                                                  SCALE - X-AXIS : 1 UNIT WIDTH = 0.005
    ===================================================================================================================
              │
              │
              │                ┌────────────────────┐                                                               
         OUT  │                │                    │                                                               
              ─ ───────────────┘                    └───────────────────────────────────────────────────────────────
              │
              │
    │││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││
    ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    [0m


.. code:: python

    # Kill the multivibrator and the oscilloscope threads
    m.kill()
    o.kill()