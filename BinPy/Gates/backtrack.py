from sys import stdout

from BinPy.Gates.gates import *
from BinPy.Gates.connector import *

def backtrack(element, depth):
    '''
    This function returns a tree representation of a digital element, such as a
    gate, and its inputs. The second argument specifies the depth to which the
    representation shows digital elements instead of inputs. To ilustrate a use
    case, suppose the following code:

        >>> g1 = AND(True, False)
        >>> g2 = AND(True, False)
        >>> g3 = AND(g1, g2)
        >>> tree = backtrack(g3, 2)

    The 'tree' variable would have the following content:

        >>> (g3, [(g1, [True, False]), (g2, [True, False])])

    This tree representation is made using tuples, where the first element of
    tuple is the node (gate, connector, mux, etc.), and the second is a list
    of inputs. In that list each element will also be a tuple with the same
    representation. In some cases instead of a tuple there will be a boolean
    or int value, meaning the maximum depth as been reached.

    Note that by doing 'print tree', the first element of the tuples will be
    the __str__() output of the digital element.
    '''

    # Depth must be bigger than 0
    if depth < 0:
        raise Exception("ERROR: Depth of backtrack function must be bigger or\
                equal to 0")

    # Check if the element is a gate, connector or a final value, bool or int
    if not (isinstance(element, GATES) or isinstance(element, Connector)\
            or type(element) in [bool, int]):
        raise Exception("ERROR: Element must be either a Gate or Connector")

    # Return value
    ret_value = None

    # If the element is a gate
    if isinstance(element, GATES):
        if depth == 0:
            ret_value = (element, bool(element.output()))

        else:
            ret_value_list = []
            for i in element.inputs:
                ret_value_list.append(backtrack(i, depth-1))
            ret_value = (element, ret_value_list)

    # If the element is a connector
    elif isinstance(element, Connector):
        if depth == 0:
            ret_value = (element, element.state)

        else:
            ret_value_list = []
            for i in element.connections["output"]:
                ret_value_list.append(backtrack(i, depth-1))
            ret_value = (element, ret_value_list)

    # If it is none of the above
    else:
        ret_value = element

    return ret_value

def printBacktrackTree(tree_node, space=0):
    '''
        This function takes a tree made by the backtrack functions and prints
        that tree in a readable way. The way a gate, or a mux or any other
        digital element gets represented depends on it's __str__()
        implementation.

        >>> g1 = AND(True, False)
        >>> g2 = AND(True, False)
        >>> g3 = AND(g1, g2)
        >>> tree = backtrack(g3, 2)
        >>> printBacktrackTree(tree)
            |- AND Gate; Output: 0; Inputs: [0, 0];
              |- AND Gate; Output: 0; Inputs: [True, False];
                 |- True
                 |- False
              |- AND Gate; Output: 0; Inputs: [True, False];
                 |- True
                 |- False
    '''

    def printSpaces(space):
        for i in range(space): stdout.write("   ")

    if type(tree_node) == tuple:
        printSpaces(space)
        stdout.write("|- ")
        print(tree_node[0])

        for i in tree_node[1]:
            printBacktrackTree(i, space+1)

    else:
        printSpaces(space)
        stdout.write("|- ")
        print(tree_node)

