from __future__ import print_function
from BinPy.Gates.tree import *
from BinPy.Gates.gates import *
from BinPy.Gates.connector import *
from BinPy.Combinational.combinational import *

from nose.tools import with_setup, nottest

'''
Testing backtrack() function for depths from 0 to 5.
'''

def backtrack_depth_0_test():
    # Trees for different nodes in final tree
    g1 = AND(True, False)
    g2 = AND(True, False)
    g3 = AND(g1, g2)

    g4 = AND(True, False)
    g5 = AND(True, False)
    g6 = AND(g4, g5)

    g_final = AND(g3, g6)

    tree = Tree(g_final, 0)
    tree.backtrack()

    if not (tree.element == g_final and\
            len(tree.sons) == 0):
        assert False

def backtrack_depth_1_test():
    # Trees for different nodes in final tree
    g1 = AND(True, False)
    g2 = AND(True, False)
    g3 = AND(g1, g2)

    g4 = AND(True, False)
    g5 = AND(True, False)
    g6 = AND(g4, g5)

    g_final = AND(g3, g6)

    tree = Tree(g_final, 1)
    tree.backtrack()

    if not (tree.element == g_final and\
            len(tree.sons) == 2 and\
            tree.sons[0].element == g3 and\
            tree.sons[1].element == g6 and\
            len(tree.sons[0].sons) == 0 and\
            len(tree.sons[1].sons) == 0):
        assert False

def backtrack_depth_2_test():
    # Trees for different nodes in final tree
    g1 = AND(True, False)
    g2 = AND(True, False)
    g3 = AND(g1, g2)

    g4 = AND(True, False)
    g5 = AND(True, False)
    g6 = AND(g4, g5)

    g_final = AND(g3, g6)

    tree = Tree(g_final, 2)
    tree.backtrack()

    if not (tree.element == g_final and\
            len(tree.sons) == 2 and\
            tree.sons[0].element == g3 and\
            tree.sons[1].element == g6 and\
            len(tree.sons[0].sons) == 2 and\
            len(tree.sons[1].sons) == 2 and\
            tree.sons[0].sons[0].element == g1 and\
            tree.sons[0].sons[1].element == g2 and\
            tree.sons[1].sons[0].element == g4 and\
            tree.sons[1].sons[1].element == g5 and\
            len(tree.sons[0].sons[0].sons) == 0 and\
            len(tree.sons[0].sons[1].sons) == 0 and\
            len(tree.sons[1].sons[0].sons) == 0 and\
            len(tree.sons[1].sons[1].sons) == 0):
        assert False

def backtrack_depth_3_test():
    # Trees for different nodes in final tree
    g1 = AND(True, False)
    g2 = AND(True, False)
    g3 = AND(g1, g2)

    g4 = AND(True, False)
    g5 = AND(True, False)
    g6 = AND(g4, g5)

    g_final = AND(g3, g6)

    tree = Tree(g_final, 3)
    tree.backtrack()

    if not (tree.element == g_final and\
            len(tree.sons) == 2 and\
            tree.sons[0].element == g3 and\
            tree.sons[1].element == g6 and\
            len(tree.sons[0].sons) == 2 and\
            len(tree.sons[1].sons) == 2 and\
            tree.sons[0].sons[0].element == g1 and\
            tree.sons[0].sons[1].element == g2 and\
            tree.sons[1].sons[0].element == g4 and\
            tree.sons[1].sons[1].element == g5 and\
            len(tree.sons[0].sons[0].sons) == 2 and\
            len(tree.sons[0].sons[1].sons) == 2 and\
            len(tree.sons[1].sons[0].sons) == 2 and\
            len(tree.sons[1].sons[1].sons) == 2 and\
            tree.sons[0].sons[0].sons[0].element == True and\
            tree.sons[0].sons[0].sons[1].element == False and\
            tree.sons[0].sons[1].sons[0].element == True and\
            tree.sons[0].sons[1].sons[1].element == False and\
            tree.sons[1].sons[0].sons[0].element == True and\
            tree.sons[1].sons[0].sons[1].element == False and\
            tree.sons[1].sons[1].sons[0].element == True and\
            tree.sons[1].sons[1].sons[1].element == False):
        assert False

def backtrack_depth_4_test():
    # Trees for different nodes in final tree
    g1 = AND(True, False)
    g2 = AND(True, False)
    g3 = AND(g1, g2)

    g4 = AND(True, False)
    g5 = AND(True, False)
    g6 = AND(g4, g5)

    g_final = AND(g3, g6)

    tree = Tree(g_final, 4)
    tree.backtrack()

    if not (tree.element == g_final and\
            len(tree.sons) == 2 and\
            tree.sons[0].element == g3 and\
            tree.sons[1].element == g6 and\
            len(tree.sons[0].sons) == 2 and\
            len(tree.sons[1].sons) == 2 and\
            tree.sons[0].sons[0].element == g1 and\
            tree.sons[0].sons[1].element == g2 and\
            tree.sons[1].sons[0].element == g4 and\
            tree.sons[1].sons[1].element == g5 and\
            len(tree.sons[0].sons[0].sons) == 2 and\
            len(tree.sons[0].sons[1].sons) == 2 and\
            len(tree.sons[1].sons[0].sons) == 2 and\
            len(tree.sons[1].sons[1].sons) == 2 and\
            tree.sons[0].sons[0].sons[0].element == True and\
            tree.sons[0].sons[0].sons[1].element == False and\
            tree.sons[0].sons[1].sons[0].element == True and\
            tree.sons[0].sons[1].sons[1].element == False and\
            tree.sons[1].sons[0].sons[0].element == True and\
            tree.sons[1].sons[0].sons[1].element == False and\
            tree.sons[1].sons[1].sons[0].element == True and\
            tree.sons[1].sons[1].sons[1].element == False):
        assert False

'''
Test not following Cycles functionality
'''

def not_following_cycles_test():
    c1 = Connector(True)
    g1 = AND(c1, True)
    g2 = AND(g1, False)
    g2.setOutput(c1)

    t_no_cycle = Tree(g2, 5, False)
    t_cycle = Tree(g2, 5, True)

    t_no_cycle.backtrack()
    t_cycle.backtrack()

    if not (t_no_cycle.sons[0].sons[0].sons[0].sons == [] and\
            t_cycle.sons[0].sons[0].sons[0].sons[0].element == g1):
        assert False

'''
Test to see if the setDepth method works
'''

def set_depth_test():
    # Trees for different nodes in final tree
    g1 = AND(True, False)
    g2 = AND(True, False)
    g3 = AND(g1, g2)

    g4 = AND(True, False)
    g5 = AND(True, False)
    g6 = AND(g4, g5)

    g_final = AND(g3, g6)

    tree = Tree(g_final, 0)
    tree.backtrack()

    if not (tree.element == g_final and\
            len(tree.sons) == 0):
        assert False

    tree.setDepth(1)

    if not (tree.element == g_final and\
            len(tree.sons) == 2 and\
            tree.sons[0].element == g3 and\
            tree.sons[1].element == g6 and\
            len(tree.sons[0].sons) == 0 and\
            len(tree.sons[1].sons) == 0):
        assert False

