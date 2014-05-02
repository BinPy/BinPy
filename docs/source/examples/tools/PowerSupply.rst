
Example to show the usage of PowerSupply

.. code:: python

    from __future__ import print_function
    from BinPy.tools import *
.. code:: python

    # Usage of PowerSource and Ground classes:
    # Creating Power Source POW and Ground terminal, GND
    
    POW = PowerSource()
    GND = Ground()
.. code:: python

    # Creating connectors a,b,c
    
    a = Connector()
    b = Connector()
    c = Connector()
.. code:: python

    # Creating AND gate with inputs a and b and setting it output as c
    AND1 = AND(a, b)
    AND1.setOutput(c)
.. code:: python

    # Connecting the connectors a, b to the Power Source
    POW.connect(a)
    POW.connect(b)
    
    # a and b connected to Power Source, POW
    
    # Printing Status of AND1
    
    print('The inputs to the AND1 are: ' + str(AND1.getInputStates()))
    
    print('The output of AND1 is: ' + str(AND1.output()))

.. parsed-literal::

    The inputs to the AND1 are: [1, 1]
    The output of AND1 is: 1


.. code:: python

    # Disconnecting b from Power Source and printing inputs of AND1
    
    print('\nAfter disconnecting b from the Power Source, POW')

.. parsed-literal::

    
    After disconnecting b from the Power Source, POW


.. code:: python

    POW.disconnect(b)
    
    print('The inputs of the AND1 are: ' + str(AND1.getInputStates()))

.. parsed-literal::

    The inputs of the AND1 are: [1, None]


.. code:: python

    # Conneting b to Ground and printing the status AND1
    
    print('\nAfter connecting b to the Ground, GND')
    
    GND.connect(b)

.. parsed-literal::

    
    After connecting b to the Ground, GND


.. code:: python

    print('The inputs of the AND1 are: ' + str(AND1.getInputStates()))
    
    print('The output of AND1 is: ' + str(AND1.output()))

.. parsed-literal::

    The inputs of the AND1 are: [1, 0]
    The output of AND1 is: 0

