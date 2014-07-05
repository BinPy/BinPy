"""
Contains
=======

* Tree
* CycleHist
* CycleHistValue
"""


from __future__ import print_function
from sys import stdout
from BinPy.gates.gates import *
from BinPy.connectors.connector import *


class Tree:

    '''
    This class is a tree representation of a digital element, such as a
    gate, and its inputs. The class uses the backtrack() function which follows
    the element and tracks the inputs, and inputs of inputs, and so on, thus
    constructing the backtrack tree.

    The tree construction has the possibility to not follow cycles so the final
    output is simpler.

    The print_tree() function can be used to print the Tree in a readable way.
    The following examples show two use cases, one of which shows what happens
    if cycles are not being followed.

    Examples
    ========

    >>> g1 = AND(True, False)
    >>> g2 = AND(True, False)
    >>> g3 = AND(g1, g2)
    >>> tree = Tree(g3, 2)
    >>> tree.backtrack()
    >>> tree.print_tree()
    |- AND Gate; Output: 0; Inputs: [0, 0];
       |- AND Gate; Output: 0; Inputs: [True, False];
          |- True
          |- False
       |- AND Gate; Output: 0; Inputs: [True, False];
          |- True
          |- False

    If the algorithm was executed to not follow cycles, the output will have
    marks indicating repetitions. In the following example the elements
    marked with [0] are the same and have no sons to avoid repetitive
    output. The same for the elements with [1].

    >>> c1 = Connector(True)
    >>> c2 = Connector(True)
    >>> g1 = AND(True, c1)
    >>> g2 = AND(c2, False)
    >>> g3 = AND(g1, g2)
    >>> g4 = AND(g3, True)
    >>> g3.set_output(c1)
    >>> g4.set_output(c2)
    |- [1] AND Gate; Output: 0; Inputs: [0, True];
       |- [0] AND Gate; Output: 0; Inputs: [0, 0];
          |- AND Gate; Output: 0; Inputs: [True, 0];
             |- True
             |- Connector; State: 0
                |- [0] AND Gate; Output: 0; Inputs: [0, 0];
          |- AND Gate; Output: 0; Inputs: [0, False];
             |- Connector; State: 0
                |- [1] AND Gate; Output: 0; Inputs: [0, True];
             |- False
       |- True
    '''

    def __init__(self, element, depth=0, cycles=True):
        '''
        Constructor for the tree class

        Keyword arguments:
        element -- Any digital element, such as a gate. This gate will be
                   the root of the tree. The inputs will be the sons.
        depth   -- Depth until which the inputs are tracked. (default 0)
        cycles  -- If the tree such track cycles in the circuits or not. (default True)
        '''
        self.element = element
        self.depth = depth
        self.cycles = cycles

        self.sons = []

    def set_depth(self, val):
        '''
        Sets depth until which the tree is constructed.

        val -- New depth.
        '''

        self.depth = val
        self.reset_tree()

    def reset_tree(self):
        self.sons = []
        self.hist = None

    def backtrack(self, hist=None):
        '''
        Constructs the backtrack hierarchy of the tree up to self.depth.

        Keyword arguments:
        hist -- An instance of CycleHist. A class which maintains the passed
                tracked if backtrack is not following cycles. Should only be
                used internally.
        '''

        # Store new history if available, or create new one
        if hist is not None:
            self.hist = hist
        else:
            self.hist = CycleHist()

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

        # If the algorithm is not following cycles and this element is not in
        # the history, add it
        if not self.cycles and type(self.element) not in [bool, int]:
            self.hist.reg_occurrence(self.element)

            if self.hist.is_repeated(self.element):
                return

        # If the element is a gate
        if isinstance(self.element, GATES):
            if self.depth != 0:
                self.sons = []
                for i in self.element.inputs:
                    son = Tree(i, self.depth - 1, self.cycles)
                    son.backtrack(self.hist)
                    self.sons.append(son)

        # If the element is a connector
        elif isinstance(self.element, Connector):
            if self.depth != 0:
                self.sons = []
                for i in self.element.connections["output"]:
                    son = Tree(i, self.depth - 1, self.cycles)
                    son.backtrack(self.hist)
                    self.sons.append(son)

    def print_tree(self, space=0):
        '''
        This function prints the tree in a readable way.
        The way a gate, or a mux or any other digital element gets
        represented depends on it's __str__() implementation.

        Keyword arguments:
        space -- Number of spaces which are going to be printed in each
                 recursive step. Should only be used internally. (default 0)
        '''
        self.print_tuple(self.node)

    def print_tuple(self, tree_node, space=0):

        # Print a few spaces
        self.print_spaces(space)
        stdout.write("|- ")

        # Print the element
        if not self.cycles:
            if type(self.element) not in [int, bool] and\
                    self.hist.is_repeated(self.element):
                stdout.write(
                    "[" + str(self.hist.get_index(self.element)) + "] ")

        print(self.element)

        # Print the sons
        for i in self.sons:
            i.print_tree(space + 1)

    def print_spaces(self, space):
        for i in range(space):
            stdout.write("   ")

    def __call__(self):
        self.print_tree()


class CycleHist:

    '''
    This class helps to keep the cycle history of a circuit by registering
    occurrences of a digital element. The class has a dictionary that stores
    an instance of CycleHistValue for each key element.
    '''

    def __init__(self):
        self.hist = {}
        self.current_index = 0

    def reg_occurrence(self, element):
        '''
        Register an occurrence for an element. If the element has been seen
        before, mark that element has a repeating element.

        Keyword arguments:
        element -- Any digital element to be added to the dictionary.
        '''

        # If the element has been seen before
        if element in self.hist.keys():
            val = self.hist[element]

            # If it has been seen before and this is the first repetition, mark
            # it has repeating and give it an index
            if not val.is_repeated():
                val.set_repeated()
                val.set_index(self.current_index)
                self.current_index += 1

        # If not, create a CycleHistValue object for it
        else:
            self.hist[element] = CycleHistValue()

    def get_index(self, element):
        '''
        Get the repetition index for the given element

        Keyword arguments:
        element -- A digital element in the dictionary
        '''

        return self.hist[element].get_index()

    def is_repeated(self, element):
        '''
        Check if the given element is repeating or not

        Keyword arguments:
        element -- The element that is being check if it is repeated or not.
        '''

        return self.hist[element].is_repeated()


class CycleHistValue:

    '''
    This class represents the value in the dictionary of the CycleHist class.
    It has the index of the element and if it has been repeated or not.
    '''

    def __init__(self):
        self.repeated = False
        self.index = 0

    def set_index(self, index):
        '''
        Set the index of the element for which this instance is associated.

        Keyword arguments:
        index -- The index in question.
        '''

        self.index = index

    def get_index(self):
        '''
        Get index of the element of this instance.
        '''

        return self.index

    def set_repeated(self):
        '''
        Set is the element of this instance is repeated or not.
        '''

        self.repeated = True

    def is_repeated(self):
        '''
        Check if the element for which this instance is associated is repeated
        or not.
        '''

        return self.repeated
