# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Examples for Tree class.

# <codecell>

from __future__ import print_function
from BinPy.gates import *

# <codecell>

# Initializing the Tree class

# Initialize some gates to form a tree

# Input is of the form Tree(root element, depth of treversal)

g1 = AND(0, 1)
g2 = AND(1, 1)
g3 = AND(g1, g2)

tree = Tree(g3, 2)

# Backtrack traversal of tree upto a depth given

print (tree.backtrack())

# <codecell>

# Print tree traversed

print (tree.print_tree())

# <codecell>

# print (tree())

# <codecell>

print (tree)

