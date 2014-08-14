# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# An example to demostrate the usage of make boolean function.

# <codecell>

from __future__ import print_function
from BinPy.algorithms.makebooleanfunction import *

# <codecell>

# Usage of make_boolean() function
logical_expression, gate_form = make_boolean(
    ['A', 'B', 'C'], [1, 4, 7], minterms=True)

# <codecell>

# Print the logical function
print(logical_expression)

# <codecell>

# Print the gate form
print(gate_form)

# <codecell>

# Another example
logical_expression, gate_form = make_boolean(
    ['A', 'B', 'C', 'D'], [1, 4, 7, 0], maxterms=True)

# <codecell>

# Print the logical function
print(logical_expression)

# <codecell>

# Print the gate form
print(gate_form)
