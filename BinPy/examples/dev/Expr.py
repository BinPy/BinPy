from __future__ import print_function
from BinPy.dev import *
""" Examples for Expr class """
print ("\n---Initializing the Expr class--- ")
print ("expr = Expr('A & B | C')")
expr = Expr('A & B | C')
print ("\n---Parsing the expression----")
print ("expr.parse()")
print (expr.parse())
print ("\n---Alternate way of defining an expression---")
print ("expr1 = Expr('AND(NOT(A), B)', 'A', 'B')")
print ("Input is of the format: Expr(expression, variables)")
expr1 = Expr('AND(NOT(A), B)', 'A', 'B')
print ("expr.parse()")
print (expr.parse())
print("Printing the truth table")
print("expr.truthTable()")
expr.truthTable()
