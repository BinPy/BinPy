import threading
import BinPy
import networkx as nx
import time


class AutoUpdater(threading.Thread):

    _graph = nx.DiGraph()
    
    @staticmethod
    def add_link(a, b):
        AutoUpdater._graph.add_edge(a, b)

    @staticmethod
    def remove_link(a, b):
        AutoUpdater._graph.remove_edge(a, b)
    
    def __init__(self):
        threading.Thread.__init__(self) 

        self.daemon = True
        self.start()

    def run(self):
        while True:
            nodes = AutoUpdater._graph.nodes()

            for i in nodes:
                for pair in AutoUpdater._graph.edges(i):
                    pair[1].set_voltage(pair[0])
                    # Copies the value of the 0th index connector to the 1st
                    # index connector
                    
                    time.sleep(0.01)

            # One circuit has been traversed.


# Initiating the auto updater.
#auto_updater_instance = AutoUpdater()


class BinPyIndexer(object):

    _indices = {}     # { gates.AND : { 1:<AND instance> } }
    _rev_indices = {}  # { gates.AND : { <AND instance>:1 } }

    _max_index = {}   # { gates.AND : 1 }

    @staticmethod
    @property
    def indices():
        return BinPyIndexer._indices

    @staticmethod
    @property
    def indices():
        return BinPyIndexer._rev_indices

    @staticmethod
    def index(element):
        """ Add an element to the indexed list and return its unique ID """
        if element.__class__ not in BinPyIndexer._indices:
            BinPyIndexer._indices[element.__class__] = {}
            BinPyIndexer._rev_indices[element.__class__] = {}
            BinPyIndexer._max_index[element.__class__] = 0

        if BinPyIndexer.get_index(element) is not None:
            return BinPyIndexer.get_index(element)

        # Unique ID numbers are not recycled.
        BinPyIndexer._max_index[element.__class__] += 1

        # Unique ID for the element
        uid = BinPyIndexer._max_index[element.__class__]

        BinPyIndexer._indices[element.__class__][
            uid] = element       # UniqueID:element

        BinPyIndexer._rev_indices[element.__class__][
            element] = uid   # element:UniqueID

        return uid

    @staticmethod
    def unindex(element=None, index=None, cls=None):
        if (element, index, cls) == (None, None, None):
            raise Exception("Specify atleast one parameter")

        if element is not None:
            index = BinPyIndexer.get_index(element)
            cls = element.__class__

        if (index, cls) == (None, None):
            raise Exception("Insufficient parameters passed")

        BinPyIndexer._indices[element.__class__].pop(index)
        BinPyIndexer._rev_indices[element.__class__].pop(element)

    @staticmethod
    def get_index(element):
        """ Get the index of the element """
        if element in BinPyIndexer._rev_indices[element.__class__]:
            return BinPyIndexer._rev_indices[element.__class__][element]

    @staticmethod
    def get_element(index, cls):
        """
        Get the element of the specified index and class

        USAGE:
        ======
        >>> g1 = AND(1,0)
        >>> BinPyIndexer.get_element(g1, AND)
        1

        """
        if (cls in BinPyIndexer._indices) and (index in BinPyIndexer._indices[cls]):
            return BinPyIndexer._indices[cls][index]
