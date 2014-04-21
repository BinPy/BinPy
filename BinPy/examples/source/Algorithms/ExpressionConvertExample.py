
# coding: utf-8

### An example to demostrate functionality of ExpressionConvert.py

# In[1]:

from __future__ import print_function
from BinPy.Algorithms.ExpressionConvert import *


# In[2]:

# Given Expression:
expr = '~(((A^B)|(~a^b^C))) ~^ c'


# In[3]:

# Obtained Expression
converted = convertExpression(expr)

print(converted)


# In[4]:

# Given Expression:
expr = '((A AND B)xor(NOT(B) and C) xor(C and NOT(D)))or   E or NOT(F)'


# In[5]:

# Obtained Expression
converted = convertExpression(expr)

print(converted)


# In[6]:

# Obtained Expression with two input gate contraint
converted2 = convertExpression(expr, two_input = 1)

print(converted2)


# In[7]:

# Given Expression:
expr = '(A XOR B XOR C)'


# In[8]:

# Obtained Expression
converted = convertExpression(expr)

print(converted)


# In[9]:

# Obtained Expression with two input gate contraint
converted2 = convertExpression(expr, two_input = 1)

print(converted2)


# In[10]:

# Equivalent Expression with only AND, OR & NOT gates
converted3 = convertExpression(expr, only_and_or_not=1)

print(converted3)


# In[11]:

# Given Expression
expr = 'A XOR B'


# In[12]:

# Equivalent Expression with only NAND gates
converted = convertExpression(expr, only_nand=1)

print(converted)


# In[13]:

# Equivalent Expression with only NOR gates
converted2 = convertExpression(expr, only_nor=1)

print(converted2)

