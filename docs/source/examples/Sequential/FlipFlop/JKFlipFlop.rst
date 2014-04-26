
Example for JKFlipFlop
----------------------

.. code:: python

    from __future__ import print_function
    from BinPy.Sequential.sequential import JKFlipFlop
    from BinPy.tools.clock import Clock
    from BinPy.Gates import Connector
    from BinPy.tools.oscilloscope import Oscilloscope
.. code:: python

    j = Connector(1)
    k = Connector(0)
    
    p = Connector(0)
    q = Connector(1)
.. code:: python

    # Initialize the clock
    clock = Clock(1, 4)
    clock.start()
    
    # A clock of 4 hertz frequency initialized to 1
    clk_conn = clock.A
    
    enable = Connector(1)
    
    jkff = JKFlipFlop(j, k, enable, clk_conn, clear=enable)
    
    # To connect outputs use s.setOutputs(op1,op2)
    jkff.setOutputs(A=p, B=q)
.. code:: python

    # Initiating the oscilloscope
    
    o = Oscilloscope((clk_conn, 'CLK'), (j, 'J'), (
        k, 'k'), (p, 'OUT'), (q, 'OUT!'), (enable, 'ENABLE'))
    
    o.start()
    o.setScale(0.02)  # Set scale by trial and error.
    o.setWidth(100)
    o.unhold()

.. parsed-literal::

    [0m
    [0m


.. code:: python

    print ("SET STATE - J = 1, K = 0")
    
    # Set State
    j.state = 1
    k.state = 0
    
    # The same thing can also be done by --> jkff.setInputs(j = 1, k = 0)
    while True:
        if clk_conn.state == 0:
            # Falling edge will trigger the FF
            jkff.trigger()
            break
    print (jkff.state())
    
    # Sending a positive edge to jkff
    while True:
        if clk_conn.state == 1:
            # Falling edge will trigger the FF
            jkff.trigger()
            break

.. parsed-literal::

    SET STATE - J = 1, K = 0
    [1, 0]


.. code:: python

    print ("RESET STATE - J = 0, K = 1")
    
    # Reset State
    j.state = 0
    k.state = 1
    
    # The same thing can also be done by --> jkff.setInputs(j = 1, k = 0)
    while True:
        if clk_conn.state == 0:
            # Falling edge will trigger the FF
            jkff.trigger()
            break
    
            print ("[Printing the output using the output connectors:]\n", p(), q())
    
    # Sending a positive edge to jkff
    while True:
        if clk_conn.state == 1:
            # Falling edge will trigger the FF
            jkff.trigger()
            break

.. parsed-literal::

    RESET STATE - J = 0, K = 1


.. code:: python

    print ("TOGGLE STATE - J = 1, K = 1")
    # Toggle State
    j.state = 1
    k.state = 1
    # The same thing can also be done by --> jkff.setInputs(j = 1, k = 0)
    while True:
        if clk_conn.state == 0:
            # Falling edge will trigger the FF
            jkff.trigger()
            break
    print (jkff.state())
    
    # Sending a positive edge to jkff
    while True:
        if clk_conn.state == 1:
            # Falling edge will trigger the FF
            jkff.trigger()
            break

.. parsed-literal::

    TOGGLE STATE - J = 1, K = 1
    [1, 0]


.. code:: python

    print ("NO CHANGE STATE - J = 0, K = 0")
    # No change state
    j.state = 0
    k.state = 0
    # The same thing can also be done by --> jkff.setInputs(j = 1, k = 0)
    while True:
        if clk_conn.state == 0:
            # Falling edge will trigger the FF
            jkff.trigger()
            break
    print (jkff.state())
    
    # Sending a positive edge to jkff
    while True:
        if clk_conn.state == 1:
            # Falling edge will trigger the FF
            jkff.trigger()
            break
    
    # To connect different set of connectors use s.setInputs(conn1,conn2,enab)

.. parsed-literal::

    NO CHANGE STATE - J = 0, K = 0
    [1, 0]


.. code:: python

    # Display the oscilloscope
    o.display()

.. parsed-literal::

    [0m===================================================================================================================
    BinPy - Oscilloscope
    ===================================================================================================================
                                                                                   SCALE - X-AXIS : 1 UNIT WIDTH = 0.02
    ===================================================================================================================
              │
              │
              │                   ┌────────────┐           ┌──────────┐           ┌───────────┐                     
         CLK  │                   │            │           │          │           │           │                     
              ─ ──────────────────┘            └───────────┘          └───────────┘           └─────────────────────
              │
              │
              │
              │
              │ ┌──────────────────┐                       ┌───────────────────────┐                                
           J  │ │                  │                       │                       │                                
              ─ ┘                  └───────────────────────┘                       └────────────────────────────────
              │
              │
              │
              │
              │                    ┌───────────────────────────────────────────────┐                                
           k  │                    │                                               │                                
              ─ ───────────────────┘                                               └────────────────────────────────
              │
              │
              │
              │
              │      ┌─────────────────────────┐                      ┌───────────────────────────────────┐         
         OUT  │      │                         │                      │                                   │         
              ─ ─────┘                         └──────────────────────┘                                   └─────────
              │
              │
              │
              │
              │ ┌────┐                         ┌──────────────────────┐                                             
        OUT!  │ │    │                         │                      │                                             
              ─ ┘    └─────────────────────────┘                      └─────────────────────────────────────────────
              │
              │
              │
              │
              │ ┌─────────────────────────────────────────────────────────────────────────────────────────┐         
       ENABL  │ │                                                                                         │         
              ─ ┘                                                                                         └─────────
              │
              │
    │││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││││
    ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    [0m


.. code:: python

    # Kill the oscilloscope and clock threads
    o.kill()
    clock.kill()