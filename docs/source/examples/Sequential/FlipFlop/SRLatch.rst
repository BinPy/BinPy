
Example for SRLatch
-------------------

.. code:: python

    from __future__ import print_function
    from BinPy.Sequential.sequential import SRLatch
    from BinPy.tools.clock import Clock
    from BinPy.Gates import Connector
    from BinPy.tools.oscilloscope import Oscilloscope
.. code:: python

    s = Connector(1)
    r = Connector(0)
    
    p = Connector(0)
    q = Connector(1)
.. code:: python

    # Initialize the clock
    clock = Clock(1, 4)
    clock.start()
    # A clock of 1 hertz frequency
    clk_conn = clock.A
    
    enable = Connector(1)
.. code:: python

    # Initialize the sr latch
    srff = SRLatch(s, r, enable, clk_conn)
    
    # To connect outputs use s.setOutputs(op1,op2)
    srff.setOutputs(A=p, B=q)
.. code:: python

    # Initialize the oscilloscope
    
    o = Oscilloscope((clk_conn, 'CLK'), (s, 'S'), (
        r, 'R'), (p, 'OUT'), (q, 'OUT!'), (enable, 'ENABLE'))
    o.start()
    o.setScale(0.01)  # Set scale by trial and error.
    o.setWidth(75)
    o.unhold()

.. parsed-literal::

    [0m
    [0m


.. code:: python

    print ("SET STATE - S = 1, R = 0")
    # Set State
    s.state = 1
    r.state = 0
    # The same thing can also be done by --> srff.setInputs(s = 1, r = 0)
    while True:
        if clk_conn.state == 0:
            # Falling edge will trigger the FF
            srff.trigger()
            break
    print (srff.state())
    # Sending a positive edge to srff
    while True:
        if clk_conn.state == 1:
            # Falling edge will trigger the FF
            srff.trigger()
            break

.. parsed-literal::

    SET STATE - S = 1, R = 0
    [1, 0]


.. code:: python

    print ("RESET STATE - S = 0, R = 1")
    # Reset State
    s.state = 0
    r.state = 1
    # The same thing can also be done by --> srff.setInputs(s = 1, r = 0)
    while True:
        if clk_conn.state == 0:
            # Falling edge will trigger the FF
            srff.trigger()
            break
    # Displaying the output using the connector instances
    print ("[", p(), ",", q(), "]")
    
    # Sending a positive edge to srff
    while True:
        if clk_conn.state == 1:
            # Falling edge will trigger the FF
            srff.trigger()
            break

.. parsed-literal::

    RESET STATE - S = 0, R = 1
    [ 0 , 1 ]


.. code:: python

    print ("INVALID STATE - S = 1, R = 1")
    # Invalid state
    s.state = 1
    r.state = 1
    # The same thing can also be done by --> srff.setInputs(s = 1, r = 1)
    while True:
        if clk_conn.state == 0:
            # Falling edge will trigger the FF
            srff.trigger()
            break
    print (srff.state())
    
    # Sending a positive edge to srff
    while True:
        if clk_conn.state == 1:
            # Falling edge will trigger the FF
            srff.trigger()
            break

.. parsed-literal::

    INVALID STATE - S = 1, R = 1
    ERROR: Invalid State - Resetting the Latch
    [0, 1]


.. code:: python

    print ("2nd INVALID STATE - S = 0, R = 0")
    # Invalid state
    s.state = 1
    r.state = 1
    # The same thing can also be done by --> srff.setInputs(s = 1, r = 1)
    while True:
        if clk_conn.state == 0:
            # Falling edge will trigger the FF
            srff.trigger()
            break
    print (srff.state())
    
    # Sending a positive edge to srff
    while True:
        if clk_conn.state == 1:
            # Falling edge will trigger the FF
            srff.trigger()
            break

.. parsed-literal::

    2nd INVALID STATE - S = 0, R = 0
    ERROR: Invalid State - Resetting the Latch
    [0, 1]


.. code:: python

    # Display the oscilloscope     
    o.display()

.. parsed-literal::

    [0m==========================================================================================
    BinPy - Oscilloscope
    ==========================================================================================
                                                          SCALE - X-AXIS : 1 UNIT WIDTH = 0.01
    ==========================================================================================
              │
              │
              │                       ┌───────────────────────┐                  ┌─────────
         CLK  │                       │                       │                  │         
              ─ ──────────────────────┘                       └──────────────────┘         
              │
              │
              │
              │
              │ ┌──────────────────────┐                                          ┌────────
           S  │ │                      │                                          │        
              ─ ┘                      └──────────────────────────────────────────┘        
              │
              │
              │
              │
              │                        ┌───────────────────────────────────────────────────
           R  │                        │                                                   
              ─ ───────────────────────┘                                                   
              │
              │
              │
              │
              │ ┌─────────────────────────────────────────────┐                            
         OUT  │ │                                             │                            
              ─ ┘                                             └────────────────────────────
              │
              │
              │
              │
              │                                               ┌────────────────────────────
        OUT!  │                                               │                            
              ─ ──────────────────────────────────────────────┘                            
              │
              │
              │
              │
              │ ┌──────────────────────────────────────────────────────────────────────────
       ENABL  │ │                                                                          
              ─ ┘                                                                          
              │
              │
    ││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││
    ──────────────────────────────────────────────────────────────────────────────────────────
    [0m


.. code:: python

    # Kill the clock and the oscilloscope threads after use
    o.kill()
    clock.kill()