
# coding: utf-8

### An example to demostrate the usage of make boolean function.

# In[1]:

from __future__ import print_function
from BinPy.algorithms.makebooleanfunction import *


# In[2]:

# Usage of make_boolean() function
logical_expression, gate_form = make_boolean(['A', 'B', 'C'], [1, 4, 7], minterms=True)


# In[3]:

# Print the logical function
print(logical_expression)


# In[4]:

# Print the gate form
print(gate_form)


# In[5]:

# Another example
logical_expression, gate_form = make_boolean(['A', 'B', 'C', 'D'], [1, 4, 7, 0], maxterms=True)


# In[6]:

# Print the logical function
print(logical_expression)


# In[7]:

# Print the gate form
print(gate_form)

