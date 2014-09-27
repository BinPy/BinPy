
An example to demostrate the usage of make boolean function.
------------------------------------------------------------

.. code:: python

    from __future__ import print_function
    from BinPy.algorithms.makebooleanfunction import *
.. code:: python

    # Usage of make_boolean() function
    logical_expression, gate_form = make_boolean(['A', 'B', 'C'], [1, 4, 7], minterms=True)
.. code:: python

    # Print the logical function
    print(logical_expression)

.. parsed-literal::

    ((A AND (NOT B) AND (NOT C)) OR (A AND B AND C) OR ((NOT A) AND (NOT B) AND C))


.. code:: python

    # Print the gate form
    print(gate_form)

.. parsed-literal::

    OR(AND(A, NOT(B), NOT(C)), AND(A, B, C), AND(NOT(A), NOT(B), C))


.. code:: python

    # Another example
    logical_expression, gate_form = make_boolean(['A', 'B', 'C', 'D'], [1, 4, 7, 0], maxterms=True)
.. code:: python

    # Print the logical function
    print(logical_expression)

.. parsed-literal::

    (D OR ((NOT A) AND B) OR (A AND (NOT B) AND C) OR (B AND (NOT C)))


.. code:: python

    # Print the gate form
    print(gate_form)

.. parsed-literal::

    OR(D, AND(NOT(A), B), AND(A, NOT(B), C), AND(B, NOT(C)))

