# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# An example to demonstrate functionality of ExpressionConvert.py

# <codecell>

from __future__ import print_function
from BinPy.algorithms.ExpressionConvert import *

# <codecell>

# Given Expression:
expr = '~(((A^B)|(~a^b^C))) ~^ c'

# <codecell>

# Obtained Expression
converted = convertExpression(expr)

print(converted)

# <codecell>

# Given Expression:
expr = '((A AND B)xor(NOT(B) and C) xor(C and NOT(D)))or   E or NOT(F)'

# <codecell>

# Obtained Expression
converted = convertExpression(expr)

print(converted)

# <codecell>

# Obtained Expression with two input gate constraint
converted2 = convertExpression(expr, two_input=1)

print(converted2)

# <codecell>

# Given Expression:
expr = '(A XOR B XOR C)'

# <codecell>

# Obtained Expression
converted = convertExpression(expr)

print(converted)

# <codecell>

# Obtained Expression with two input gate constraint
converted2 = convertExpression(expr, two_input=1)

print(converted2)

# <codecell>

# Equivalent Expression with only AND, OR & NOT gates
converted3 = convertExpression(expr, only_and_or_not=1)

print(converted3)

# <codecell>

# Given Expression
expr = 'A XOR B'

# <codecell>

# Equivalent Expression with only NAND gates
converted = convertExpression(expr, only_nand=1)

print(converted)

# <codecell>

# Equivalent Expression with only NOR gates
converted2 = convertExpression(expr, only_nor=1)

print(converted2)
