
Example usage for Analog Buffers
--------------------------------

.. code:: python

    from BinPy import *
    
    # Source Bus
    a = Bus(4)
    a.set_type(analog=True)
    a.set_voltage_all(3.5, 6.7, 2.2, 1.1)
    
    # Ouput Bus
    b = Bus(4)
    b.set_type(analog=True)
    
    # Enable input
    e = Bus(1)
    e.set_logic_all(1)
.. code:: python

    # Initializing an analog Buffer
    buff1 = AnalogBuffer(a, b, e, 0.8) # With an attenuation of 0.8, relay the input to the output
.. code:: python

    print b.get_voltage_all()

.. parsed-literal::

    [3.1920379377456842, 6.110472623684595, 2.0064238465830018, 1.0032119232915009]


.. code:: python

    # BinPy automatically converts the voltage to logic state based on 5v-0v logic
    print b.get_logic_all()

.. parsed-literal::

    [1, 1, 0, 0]


.. code:: python

    print b.get_voltage_all()

.. parsed-literal::

    [3.1920379377456842, 6.110472623684595, 2.0064238465830018, 1.0032119232915009]


.. code:: python

    # Changing the input
    
    a.set_voltage_all(1,1,1,1)
.. code:: python

    b.get_voltage_all()



.. parsed-literal::

    [0.9120108393559098,
     0.9120108393559098,
     0.9120108393559098,
     0.9120108393559098]



.. code:: python

    # Changing the attenuation level
    
    buff1.set_attenuation(0)
.. code:: python

    b.get_voltage_all()



.. parsed-literal::

    [1.0, 1.0, 1.0, 1.0]


