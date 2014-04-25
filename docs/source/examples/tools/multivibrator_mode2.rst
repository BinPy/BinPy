
Astable Multivibrator - Multivibrator in Mode 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

    # Initialize mutivibrator in MODE 2 with the adequate on_time and off_time
    
    m = Multivibrator(0, mode = 2, on_time=0.2, off_time=0.8)
    m.start()
    m.setOutput(out)
.. code:: python

    # Initialize the oscilloscope 
    o = Oscilloscope((out, 'OUT'))
    o.start()
    o.setScale(0.05)  # Set scale by trial and error.
    o.setWidth(100)
    o.unhold()
    time.sleep(0.1)
    m.trigger()  # Also works with m()
    time.sleep(5)

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
                                                                                   SCALE - X-AXIS : 1 UNIT WIDTH = 0.05
    ===================================================================================================================
              │
              │
              │  ┌───┐               ┌───┐               ┌───┐               ┌───┐               ┌───┐              
         OUT  │  │   │               │   │               │   │               │   │               │   │              
              ─ ─┘   └───────────────┘   └───────────────┘   └───────────────┘   └───────────────┘   └──────────────
              │
              │
    │││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││
    ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    [0m


.. code:: python

    # Kill the multivibrator and the oscilloscope threads
    m.kill()
    o.kill()