"""
Contains
=======

* Tree
"""


from __future__ import print_function
from sys import stdout
from BinPy.Gates.gates import *
from BinPy.Gates.connector import *


class Tree:

    '''
    This class returns a tree representation of a digital element, such as a
    gate, and its inputs. The second argument specifies the depth to which the
    representation shows digital elements instead of inputs. To illustrate a
    use case, suppose the following code:

    Examples
    ========

    >>> g1 = AND(True, False)
    >>> g2 = AND(True, False)
    >>> g3 = AND(g1, g2)
    >>> tree = Tree(g3, 2)
    >>> tree.backtrack()
    (g3, [(g1, [True, False]), (g2, [True, False])])

    This tree representation is made using tuples, where the first element of
    tuple is the node (gate, connector, mux, etc.), and the second is a list
    of inputs. In that list each element will also be a tuple with the same
    representation. In some cases instead of a tuple there will be a boolean
    or int value, meaning the maximum depth as been reached.
    '''

    def __init__(self, element, depth):
        self.element = element
        self.depth = depth
        self.node = self.element

    def depth(self, val):
        self.depth = depth

    def backtrack(self):
        '''
        Returns the backtrack hierarchy of the tree upto self.depth
        '''

        # Depth must be bigger than 0
        if self.depth < 0:
            raise Exception(
                "ERROR: Depth of backtrack function must be bigger or\
                    equal to 0")

        # Check if the element is a gate, connector or a final value, bool or
        # int
        if not (isinstance(self.element, GATES) or isinstance(self.element, Connector)
                or type(self.element) in [bool, int]):
            raise Exception(
                "ERROR: Element must be either a Gate or Connector")

        # Return value
        ret_value = None

        # If the element is a gate
        if isinstance(self.element, GATES):
            if self.depth == 0:
                ret_value = (self.element, bool(self.element.output()))

            else:
                ret_value_list = []
                for i in self.element.inputs:
                    j = Tree(i, self.depth - 1)
                    ret_value_list.append(j.backtrack())
                ret_value = (self.element, ret_value_list)

        # If the element is a connector
        elif isinstance(self.element, Connector):
            if self.depth == 0:
                ret_value = (self.element, self.element.state)

            else:
                ret_value_list = []
                for i in self.element.connections["output"]:
                    j = Tree(i, self.depth - 1)
                    ret_value_list.append(j.backtrack())
                ret_value = (self.element, ret_value_list)

        # If it is none of the above
        else:
            ret_value = self.element

        self.node = ret_value
        return ret_value

    def printTree(self):
        '''
        This function takes a tree  and prints that tree in a readable way.
        The way a gate, or a mux or any other digital element gets
        represented depends on it's __str__() implementation.

        Examples
        ========

        >>> g1 = AND(True, False)
        >>> g2 = AND(True, False)
        >>> g3 = AND(g1, g2)
        >>> tree = Tree(g3, 2)
        >>> tree.backtrack()
        >>> tree.printTree()
        |- AND Gate; Output: 0; Inputs: [0, 0];
           |- AND Gate; Output: 0; Inputs: [True, False];
              |- True
              |- False
           |- AND Gate; Output: 0; Inputs: [True, False];
              |- True
              |- False
        '''
        self.printTuple(self.node)

    def printTuple(self, tree_node, space=0):

        if isinstance(tree_node, tuple):
            self.printSpaces(space)
            stdout.write("|- ")
            print(tree_node[0])

            for i in tree_node[1]:
                self.printTuple(i, space + 1)

        else:
            self.printSpaces(space)
            stdout.write("|- ")
            print(tree_node)

    def printSpaces(self, space):
        for i in range(space):
            stdout.write("   ")

    def __repr__(self):
        return str(self.node)

    def __call__(self):
        return self.printTree()
