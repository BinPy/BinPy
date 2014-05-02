
Example for Binary Counter [ A 2 bit Ripple Counter ]
-----------------------------------------------------

.. code:: python

    # Imports
    
    from __future__ import print_function
    from BinPy.tools.clock import Clock
    from BinPy.Sequential.counters import BinaryCounter
    from BinPy.Gates import Connector
    from BinPy.tools.oscilloscope import Oscilloscope
    import time
.. code:: python

    # A clock of 1 hertz frequency  With initial value as 0
    
    clock = Clock(0, 1)
    clock.start()
    clk_conn = clock.A
.. code:: python

    # Initializing Binary Counter with 2 bits and clock_conn
    b = BinaryCounter(2, clk_conn)
    
    # Initializing the Oscillioscope
    o = Oscilloscope((clk_conn, 'CLK'), (b.out[0], 'MSB'), (b.out[1], 'LSB'))
    
    # Starting the oscillioscope
    o.start()
    
    # Set scale by trial and error.
    o.setScale(0.15)  
    
    # Set the width of the oscilloscope [ To fit the ipython Notebook ]
    o.setWidth(100)

.. parsed-literal::

    [0m


.. code:: python

    # Then unhold [ Run the Oscilloscope ]
    o.unhold()
    
    print(b.state())
    
    # Triggering the Binary Counter 10 times.
    for i in range(10):
        b.trigger()
        print (b.state())
    
    # Display the time-Waveform.
    o.display()
    
    # Kill the oscilloscope thread.
    o.kill()

.. parsed-literal::

    [0m
    [0, 0]
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
    [0m===================================================================================================================
    BinPy - Oscilloscope
    ===================================================================================================================
                                                                                   SCALE - X-AXIS : 1 UNIT WIDTH = 0.15
    ===================================================================================================================
              │
              │
              │      ┌─────┐      ┌─────┐     ┌──────┐     ┌──────┐     ┌──────┐     ┌──────┐     ┌──────┐     ┌────
         CLK  │      │     │      │     │     │      │     │      │     │      │     │      │     │      │     │    
              ─ ─────┘     └──────┘     └─────┘      └─────┘      └─────┘      └─────┘      └─────┘      └─────┘    
              │
              │
              │
              │
              │            ┌─────────────────────────┐                         ┌─────────────────────────┐          
         MSB  │            │                         │                         │                         │          
              ─ ───────────┘                         └─────────────────────────┘                         └──────────
              │
              │
              │
              │
              │ ┌──────────┐            ┌────────────┐            ┌────────────┐            ┌────────────┐          
         LSB  │ │          │            │            │            │            │            │            │          
              ─ ┘          └────────────┘            └────────────┘            └────────────┘            └──────────
              │
              │
    │││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││
    ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    [0m


.. code:: python

    # Calling the instance will also trigger the counter.
    print("b()")

.. parsed-literal::

    b()


.. code:: python

    # Setting the Counter
    
    b.setCounter()
    
    print(b.state())

.. parsed-literal::

    [1, 1]


.. code:: python

    # Resetting the Counter
    
    b.resetCounter()
    
    print(b.state())

.. parsed-literal::

    [0, 0]


.. code:: python

    # Disabling the Counter
    
    b.disable()
    
    # Now triggering it has no effect.
    
    b.trigger()
    
    print(b.state())

.. parsed-literal::

    [0, 0]


.. code:: python

    # Enabling the Counter
    
    b.enable()
    b.trigger()
    
    print(b.state())

.. parsed-literal::

    [0, 0]


.. code:: python

    # Kill the clock thread.
    clock.kill()