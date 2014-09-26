
Example to illustrate the usage of bittools
-------------------------------------------

``BinPyBits`` is a class inheriting from the ``bitstring.BitArray`` class. It will be used for efficient manipulation / handling of Bit vectors.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    from BinPy import *
    
    # Initializing a BinPyBits object
    
    bit_vector = BinPyBits(5)
.. code:: python

    # By default all BinPyBits objects are not signed
    
    bit_vector.signed



.. parsed-literal::

    False



.. code:: python

    # Getting the decimal value
    
    bit_vector.uint



.. parsed-literal::

    5



.. code:: python

    # Getting the binary string
    
    bit_vector.bin



.. parsed-literal::

    '101'



.. code:: python

    # Do not use int with unsigned BinPyBits objects
    
    bit_vector.int



.. parsed-literal::

    -3



.. code:: python

    # This returns -3 since '101' ==> -3 ( 2's Complement representation )
    
    # You could use :
    
    int_value = bit_vector.int if bit_vector.signed else bit_vector.uint
    
    print int_value

.. parsed-literal::

    5


.. code:: python

    # Creating a BinPyBits object using binary string
    
    bit_vector = BinPyBits('1111', signed=False)
    
    # Converting to decimal
    
    int_value = bit_vector.int if bit_vector.signed else bit_vector.uint
    
    print int_value

.. parsed-literal::

    15


.. code:: python

    # Creating a signed BinPyBits
    
    bit_vector = BinPyBits('1111', signed=True)
    
    # Converting to decimal
    
    int_value = bit_vector.int if bit_vector.signed else bit_vector.uint
    
    print int_value

.. parsed-literal::

    -1


.. code:: python

    # Converting to hex
    
    bit_vector.hex



.. parsed-literal::

    'f'



Refer `the documentation of
bittstring <https://pypi.python.org/pypi/bitstring/3.1.3>`__ to discover
additional functionality.

.. code:: python

    # The speciality of BinPyBits lies in the fact that it can be initialized from various types of inputs
    # Except for the initialization, the rest of the functionalities remain similar to that of the bitstring.BitArray
    
    # Initializing a signed value using - sign
    
    bit_vector = BinPyBits('-1111', signed=True)
    
    print bit_vector.int

.. parsed-literal::

    -15

