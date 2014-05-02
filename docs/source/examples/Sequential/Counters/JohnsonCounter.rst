
Example for N Bit Johnson Counter.
----------------------------------

.. code:: python

    # imports
    
    from __future__ import print_function
    from BinPy.tools import Clock
    from BinPy.Sequential.counters import JohnsonCounter
    from BinPy.Gates import Connector
.. code:: python

    # Initializing the Clock
    # A clock of 50 hertz frequency
    
    clock = Clock(1, 50)
    clock.start()
.. code:: python

    # Initialize enable
    
    enable = Connector(1)
    
    # Initializing the counter
    
    # Initializing Johnson with 8 bits and clock
    
    b = JohnsonCounter(8, clock)
    
    # Initial State
    
    print (b.state())

.. parsed-literal::

    []


.. code:: python

    # Triggering the counter 24 times
    
    for i in range(24):
        b.trigger()
        print (b.state())
    
    # Calling the instance will trigger
    
    b()
    
    print(b.state())

.. parsed-literal::

    [1, 1, 0, 0, 0, 0, 0, 0]
    [1, 1, 1, 0, 0, 0, 0, 0]
    [1, 1, 1, 1, 0, 0, 0, 0]
    [1, 1, 1, 1, 1, 0, 0, 0]
    [1, 1, 1, 1, 1, 1, 0, 0]
    [1, 1, 1, 1, 1, 1, 1, 0]
    [1, 1, 1, 1, 1, 1, 1, 1]
    [0, 1, 1, 1, 1, 1, 1, 1]
    [0, 0, 1, 1, 1, 1, 1, 1]
    [0, 0, 0, 1, 1, 1, 1, 1]
    [0, 0, 0, 0, 1, 1, 1, 1]
    [0, 0, 0, 0, 0, 1, 1, 1]
    [0, 0, 0, 0, 0, 0, 1, 1]
    [0, 0, 0, 0, 0, 0, 0, 1]
    [0, 0, 0, 0, 0, 0, 0, 0]
    [1, 0, 0, 0, 0, 0, 0, 0]
    [1, 1, 0, 0, 0, 0, 0, 0]
    [1, 1, 1, 0, 0, 0, 0, 0]
    [1, 1, 1, 1, 0, 0, 0, 0]
    [1, 1, 1, 1, 1, 0, 0, 0]
    [1, 1, 1, 1, 1, 1, 0, 0]
    [1, 1, 1, 1, 1, 1, 1, 0]
    [1, 1, 1, 1, 1, 1, 1, 1]
    [0, 1, 1, 1, 1, 1, 1, 1]
    [0, 0, 1, 1, 1, 1, 1, 1]


.. code:: python

    # Setting the Counter
    
    #b.setCounter()
    
    print(b.state())

.. parsed-literal::

    [0, 0, 1, 1, 1, 1, 1, 1]


.. code:: python

    # Resetting the Counter
    
    # b.resetCounter()
    
    print(b.state())

.. parsed-literal::

    [0, 0, 1, 1, 1, 1, 1, 1]


.. code:: python

    # Disabling the Counter
    
    b.disable()
    
    b.trigger()
    
    print(b.state())

.. parsed-literal::

    [0, 0, 0, 1, 1, 1, 1, 1]


.. code:: python

    # Enabling the Counter
    
    b.enable()
    
    b.trigger()
    
    print(b.state())

.. parsed-literal::

    [0, 0, 0, 0, 1, 1, 1, 1]


.. code:: python

    # Kill the clock thread after use
    
    clock.kill()