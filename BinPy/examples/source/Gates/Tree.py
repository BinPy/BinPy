
# coding: utf-8

### Examples for Tree class.

# In[1]:

from __future__ import print_function
from BinPy.Gates import *


# In[2]:

# Initializing the Tree class

# Initialize some gates to form a tree

# Input is of the form Tree(root element, depth of treversal)

g1 = AND(0, 1)
g2 = AND(1, 1)
g3 = AND(g1, g2)

tree = Tree(g3, 2)

# Backtrack traversal of tree upto a depth given

print (tree.backtrack())


# In[3]:

# Print tree traversed

# print (tree.printTree())


# In[4]:

# print (tree())


# In[5]:

print (tree)

