from __future__ import print_function
from BinPy.Algorithms import *
print('An example to demostrate functionality of ExpressionConvert.py\n')

expr = '~(((A^B)|(~a^b^C))) ~^ c'
print("Given Expression:\n"+expr)
converted = convertExpression(expr)
print("Obtained Expression:\n"+converted)

expr = '((A AND B)xor(NOT(B) and C) xor(C and NOT(D)))or   E or NOT(F)'
print("Given Expression:\n"+expr)
converted = convertExpression(expr)
converted2 = convertExpression(expr,1)
print("Obtained Expression:\n"+converted)
print("Obtained Expression with two input gate constraint:\n"+converted2)
