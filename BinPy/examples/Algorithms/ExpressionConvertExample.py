from __future__ import print_function
from BinPy.Algorithms import *
print('An example to demostrate functionality of ExpressionConvert.py\n')

expr = '~(((A^B)|(~a^b^C))) ~^ c'
print("Given Expression:\n" + expr)
converted = convertExpression(expr)
print("Obtained Expression:\n" + converted)

expr = '((A AND B)xor(NOT(B) and C) xor(C and NOT(D)))or   E or NOT(F)'
print("Given Expression:\n" + expr)
converted = convertExpression(expr)
converted2 = convertExpression(expr, two_input=1)
print("Obtained Expression:\n" + converted)
print("Obtained Expression with two input gate constraint:\n" + converted2)

expr = '(A XOR B XOR C)'
print("\nGiven Expression:\n" + expr)
converted = convertExpression(expr)
print("Obtained Expression:\n" + converted)
converted = convertExpression(expr, two_input=1)
print("Obtained Expression with 2 input constraint:\n" + converted)
converted = convertExpression(expr, only_and_or_not=1)
print("Equivalent Expression with only AND, OR & NOT gates is:\n" + converted)
expr = 'A XOR B'
print("\nGiven Expression:\n" + expr)
converted = convertExpression(expr, only_nand=1)
print("Equivalent Expression with only NAND gates is:\n" + converted)
converted = convertExpression(expr, only_nor=1)
print("Equivalent Expression with only NAND gates is:\n" + converted)
