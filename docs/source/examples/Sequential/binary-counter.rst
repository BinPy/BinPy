Binary Counter
==============

In digital logic and computing, a counter is a device which stores (and sometimes displays) the number of times a particular event or process has occurred, often in relationship to a clock signal.

This examples shows a basic implementation of binary counter in BinPy.

.. code:: python

    from __future__ import print_function
    from BinPy.tools import Clock
    from BinPy.Sequential.counters import BinaryCounter
    from BinPy.Gates import Connector
    from BinPy.tools.oscilloscope import Oscilloscope
    import time
    
    # Initializing the clock
    clock = Clock(0, 1)
    # This is a clock with leading edge = 0 and frequency = 1 Hz
    
    # This is important to start the clock
    # You might forget to start the clock after initialization
    clock.start()
    
    clk_conn = clock.A  # Clock connector
    
    # Initializing Binary Counter with 2 bits and clock_conn
    b = BinaryCounter(2, clk_conn)
    
    # Initializing the Oscillioscope
    o = Oscilloscope((clk_conn, 'CLK'), (b.out[0], 'MSB'), (b.out[1], 'LSB'))
    o.start()
    o.setScale(0.15)  # Set scale by trial and error.
    o.setWidth(70)  # Set the rendering width of the oscilloscope
    o.unhold()
    print (b.state()) #Initial State

.. parsed-literal::

    [0, 0]


.. code:: python

    # Triggering the counter sequentially
    for i in range(5):
        b.trigger()
        print (b.state())
    
    for i in range(5):
        b.trigger()
        print (b.state())

.. parsed-literal::

    [0, 1]
    [1, 0]
    [1, 1]
    [0, 0]
    [0, 1]
    [1, 0]
    [1, 1]
    [0, 0]
    [0, 1]
    [1, 0]


.. code:: python

    o.display()

.. parsed-literal::

    =====================================================================================
    BinPy - Oscilloscope
    =====================================================================================
                                                     SCALE - X-AXIS : 1 UNIT WIDTH = 0.15
    =====================================================================================
              │
              │
              │       ┌──────┐     ┌──────┐      ┌─────┐     ┌──────┐     ┌──────┐    
         CLK  │       │      │     │      │      │     │     │      │     │      │    
              ─ ──────┘      └─────┘      └──────┘     └─────┘      └─────┘      └────
              │
              │
              │
              │
              │                                        ┌─────────────────────────┐    
         MSB  │                                        │                         │    
              ─ ───────────────────────────────────────┘                         └────
              │
              │
              │
              │
              │                           ┌────────────┐            ┌────────────┐    
         LSB  │                           │            │            │            │    
              ─ ──────────────────────────┘            └────────────┘            └────
              │
              │
    │││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││
    ─────────────────────────────────────────────────────────────────────────────────────


.. code:: python

    # To stop the oscilloscope you need to call it's kill method
    o.kill() # Stop the oscilloscope
.. code:: python

    # Disabling the Counter
    b.disable()
    
    # Now triggering it has no effect.
    b.trigger()
    print(b.state())

.. parsed-literal::

    [1, 0]


.. code:: python

    # Kill the clock thread.
    clock.kill()
