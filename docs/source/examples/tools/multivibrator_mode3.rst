
Bistable Multivibrator - Multivibrator in Mode 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
    
    out = Connector(0)
.. code:: python

    # Initialize mutivibrator in MODE 3
    
    m = Multivibrator(0, mode = 3)
    m.start()
    m.setOutput(out)
.. code:: python

    # Initialize the oscilloscope 
    o = Oscilloscope((out, 'OUT'))
    o.start()
    o.setScale(0.1)
    o.setWidth(75)
    o.unhold()
    time.sleep(0.001) # This is done to let the oscilloscope thread to synchronize with the main thread...

.. parsed-literal::

    [0m
    [0m


.. code:: python

    # Trigger the multivibrator to change the state
    print(out())
    time.sleep(0.1)
    m.trigger()
    
    time.sleep(0.001) # This is done to synchronize the multivibrator thread ... 
    
    print(out())
    time.sleep(0.5)
    m.trigger()
    
    time.sleep(0.001) # This is done to synchronize the multivibrator thread ... 
    
    print(out())
    time.sleep(1)
    m.trigger()
    
    time.sleep(0.001) # This is done to synchronize the multivibrator thread ... 
    
    print(out())
    time.sleep(2)
    m.trigger()
    
    time.sleep(0.001) # This is done to synchronize the multivibrator thread ... 
    
    print (out())

.. parsed-literal::

    0
    1
    0
    1
    0


.. code:: python

    # Display the oscilloscope
    o.display()

.. parsed-literal::

    [0m==========================================================================================
    BinPy - Oscilloscope
    ==========================================================================================
                                                           SCALE - X-AXIS : 1 UNIT WIDTH = 0.1
    ==========================================================================================
              │
              │
              │   ┌────┐         ┌───────────────────┐                                     
         OUT  │   │    │         │                   │                                     
              ─ ──┘    └─────────┘                   └─────────────────────────────────────
              │
              │
    ││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││
    ──────────────────────────────────────────────────────────────────────────────────────────
    [0m


.. code:: python

    # Kill the multivibrator and the oscilloscope threads
    m.kill()
    o.kill()