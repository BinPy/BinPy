
Example for N Bit Ring Counter.
-------------------------------

.. code:: python

    # imports
    from __future__ import print_function
    from BinPy.tools import Clock
    from BinPy.Sequential.counters import RingCounter
    from BinPy.Gates import Connector
.. code:: python

    # Initializing the Clock
    # Clock frequency is 50 Hz
    
    clock = Clock(1, 50)
    clock.start()
.. code:: python

    # Initialize enable
    
    enable = Connector(1)
.. code:: python

    # Initializing RingCounter with 8 bits and clock
    
    b = RingCounter(8, clock)
.. code:: python

    # Initial State
    
    print (b.state())

.. parsed-literal::

    []


.. code:: python

    # Triggering the counter 8 times
    
    for i in range(8):
        b.trigger()
        print (b.state())

.. parsed-literal::

    [0, 1, 0, 0, 0, 0, 0, 0]
    [0, 0, 1, 0, 0, 0, 0, 0]
    [0, 0, 0, 1, 0, 0, 0, 0]
    [0, 0, 0, 0, 1, 0, 0, 0]
    [0, 0, 0, 0, 0, 1, 0, 0]
    [0, 0, 0, 0, 0, 0, 1, 0]
    [0, 0, 0, 0, 0, 0, 0, 1]
    [1, 0, 0, 0, 0, 0, 0, 0]


.. code:: python

    # Calling the instance will trigger
    
    b()
    
    print(b.state())

.. parsed-literal::

    [0, 1, 0, 0, 0, 0, 0, 0]


.. code:: python

    # Setting the Counter
    
    # b.setCounter()
    
    print(b.state())

.. parsed-literal::

    [0, 1, 0, 0, 0, 0, 0, 0]


.. code:: python

    # Resetting the Counter
    
    # b.resetCounter()
    
    print(b.state())

.. parsed-literal::

    [0, 1, 0, 0, 0, 0, 0, 0]


.. code:: python

    # Disabling the Counter
    
    b.disable()
    b.trigger()
    
    print(b.state())

.. parsed-literal::

    [0, 0, 1, 0, 0, 0, 0, 0]


.. code:: python

    # Enabling the Counter
    
    b.enable()
    b.trigger()
    
    print(b.state())

.. parsed-literal::

    [0, 0, 0, 1, 0, 0, 0, 0]


.. code:: python

    # Kill the clock thread.
    
    clock.kill()