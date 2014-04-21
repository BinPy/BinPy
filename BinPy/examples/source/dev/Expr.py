
# coding: utf-8

# Examples for Expr class

# In[1]:

# imports
from __future__ import print_function
from BinPy.dev import *


# In[2]:

# Initializing the Expr class

expr = Expr('A & B | C')

# Parsing the expression

print (expr.parse())


# In[3]:

# Alternate way of defining an expression

# Input is of the format: Expr(expression, variables)

expr1 = Expr('AND(NOT(A), B)', 'A', 'B')

print (expr.parse())


# In[4]:

# Printing the truth table

print(expr.truthTable())
