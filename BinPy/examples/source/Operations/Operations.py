
# coding: utf-8

### Examples for operations class

# In[1]:

from __future__ import print_function
from BinPy.Operations.operations import *


# In[2]:

# Initialize the operation class

op = Operations()

# Binary Addition

print (op.ADD('0', '1'), op.ADD('00', '10'), op.ADD('010', '100'))


# In[3]:

# Binary Subtraction

print (op.SUB('1', '0'), op.SUB('00', '10'), op.SUB('010', '100'))


# In[4]:

# Binary Multiplication

print (op.MUL('0', '1'), op.MUL('00', '10'), op.MUL('010', '100'))


# In[5]:

# Binary Division

print (op.DIV('0', '1'), op.DIV('00', '10'), op.DIV('010', '100'))


# In[6]:

# Binary Complement

print (
    op.COMP(
        '0', '1'), op.COMP(
        '00', '1'), op.COMP(
        '00', '2'), op.COMP(
        '010', '1'))


# In[7]:

# Conversion from binary to decimal

print (Operations.binToDec('111'))


# In[8]:

# Conversion from decimal to binary

print (Operations.decToBin(12))

