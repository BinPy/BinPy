"""
Contains
=======

* Tree
* CycleHist
* CycleHistValue
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

    def __init__(self, element, depth, cycles=True):
        self.element = element
        self.depth = depth
        self.cycles = cycles

        self.sons = []

    def setDepth(self, val):
        self.depth = val

    def backtrack(self, hist=None):
        '''
        Returns the backtrack hierarchy of the tree up to self.depth
        '''

        # Store new history if available, or create new one
        if hist != None:
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
            self.hist.regOccurrence(self.element)

            if self.hist.isRepeated(self.element):
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

    def printTree(self, space=0):
        '''
        This function prints the tree in a readable way.
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

        # Print a few spaces
        self.printSpaces(space)
        stdout.write("|- ")

        # Print the element
        if not self.cycles:
            if type(self.element) not in [int, bool] and\
                    self.hist.isRepeated(self.element):
                stdout.write("[" + str(self.hist.getIndex(self.element)) + "] ")

        print(self.element)

        # Print the sons
        for i in self.sons:
            i.printTree(space + 1)

    def printSpaces(self, space):
        for i in range(space):
            stdout.write("   ")

    def __call__(self):
        self.printTree()


class CycleHist:
    """
    This class helps to keep the cycle history of a circuit by registering
    occurrences of a digital element. The class has a dictionary that stores
    an instance of CycleHistValue for each key element.
    """

    def __init__(self):
        self.hist = {}
        self.current_index = 0

    def regOccurrence(self, element):
        """
        Register an occurrence for an element. If the element has been seen
        before, mark that element has a repeating element.
        """

        # If the element has been seen before
        if element in self.hist.keys():
            val = self.hist[element]

            # If it has been seen before and this is the first repetition, mark
            # it has repeating and give it an index
            if not val.isRepeated():
                val.setRepeated()
                val.setIndex(self.current_index)
                self.current_index += 1

        # If not, create a CycleHistValue object for it
        else:
            self.hist[element] = CycleHistValue()

    def getIndex(self, element):
        """
        Get the repetition index for the given element
        """

        return self.hist[element].getIndex()

    def isRepeated(self, element):
        """
        heck if the given element is repeting or not
        """

        return self.hist[element].isRepeated()


class CycleHistValue:
    """
    This class represents the value in the dictionary of the cycleHist class.
    It has the index of the element and if it has been repeated or not.
    """

    def __init__(self):
        self.repeated = False
        self.index = 0

    def setIndex(self, index):
        self.index = index

    def getIndex(self):
        return self.index

    def setRepeated(self):
        self.repeated = True

    def isRepeated(self):
        return self.repeated
