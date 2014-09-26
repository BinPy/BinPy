
Example to illustrate the usage of Analog Converter modules in BinPy.
---------------------------------------------------------------------

.. code:: python

    from BinPy import *
Analog to Digital Converter module - A2D
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    # Initiating the input analog Bus
    input_analog = Bus(Connector(voltage = 3.2))
    input_analog.set_type(analog=True)
.. code:: python

    # Initiating the output digital Bus
    output_digital = Bus(16)
    
    # Building the power supply
    VREF = Connector(voltage = 5.0)
    GND = Connector(voltage = 0)
.. code:: python

    # Initializing the A2D converter
    a2d_16bit = A2D(input_analog, output_digital, 3, VREF, GND, scale=0.5 )
.. code:: python

    time.sleep(0.5) # Setup time
    print output_digital.get_logic_all(as_list = False)

.. parsed-literal::

    0b0101000111101011


.. code:: python

    # Varying the input
    input_analog[0].set_voltage(3.2)
    time.sleep(0.5) # To allow conversion to take place.
.. code:: python

    print output_digital.get_logic_all(as_list = False)

.. parsed-literal::

    0b0101000111101011


.. code:: python

    # 64 Bit A2D Converter
    ieee_64bit = Bus(64)
    a2d_IEEE64 = A2D(input_analog, ieee_64bit, 5)
    time.sleep(0.5) # To allow conversion to take place.
    print ieee_64bit.get_logic_all(as_list = False)

.. parsed-literal::

    0b0100000000001001100110011001100110011001100110011001100110011010


Refer : http://babbage.cs.qc.cuny.edu/IEEE-754.old/Decimal.html
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Digital to Analog Converter module - D2A
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    # Output Bus-es
    output_of_D2A   = Bus(Connector(voltage = 0.0))
    output_of_D2A.set_type(analog = True)
    
    # Input Bus
    input_digital = output_digital # The input_digital refers to the output_digital, the output of the A2D of the last section
.. code:: python

    d2a_16bit = D2A(input_digital, output_of_D2A, 3, VREF, GND, scale = 2)
    time.sleep(0.1) # Setup time
.. code:: python

    print output_of_D2A[0].get_voltage()

.. parsed-literal::

    3.1999206543


.. code:: python

    ieee_packed = Bus(1)
    ieee_packed.set_type(analog = True)
    d2a_ieee64 = D2A(ieee_64bit, ieee_packed, 5) # Setting the input from the output of the previous A2D Block
    time.sleep(0.1) # Setup time
.. code:: python

    print  ieee_packed[0].get_voltage()

.. parsed-literal::

    3.2

