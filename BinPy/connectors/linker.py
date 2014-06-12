import threading
import networkx as nx
import time
import BinPy
# Cannot import from connector module since connector module requires
# linker ( this ) module to be available first.


class AutoUpdater(threading.Thread):

    """
    AutoUpdater class provides a collection of static methods for linking BinPy connections primitives Bus and Connector.
    Note that since Bus is a collecion of Connectors, AutoUpdater essentially binds together a network of linked Connectors.

    Use this class to provide automatic state propagation between modules ( with Bus input / output )

    EXAMPLES
    ========

    >>> a = Bus(4)
    >>> b = Bus(4)
    >>> AutoUpdator.add_link(a,b)
    >>> a.set_voltage_all(5,0,5,5)
    >>> b.get_voltage_all()
    [5.0, 0.0, 5.0, 5.0]

    METHODS
    =======

    * add_link(a, b, directed)
    * remove_link(a,b)
    * run(b,a) # The main execution loop to keep the connections updated.
    """
    _lock = threading.RLock()
    _graph = nx.DiGraph()

    @staticmethod
    def add_link(a, b, directed=True):
        """
        Link a list of Connectors ( or  a Bus of connectors ) with another list / Bus for auto-updation.
        """
        with AutoUpdater._lock:

            if (type(a) in (list, BinPy.connectors.connector.Bus)) and (type(b) in (list, BinPy.connectors.connector.Bus)):
                if len(a) != len(b):
                    raise Exception("ERROR: Lengths are not equal")
                for i, j in zip(a, b):
                    if (isinstance(i, BinPy.connectors.connector.Connector), isinstance(j, BinPy.connectors.connector.Connector)) != (True, True):
                        raise Exception(
                            "ERROR: Only Connector objects can be linked")
                    if not AutoUpdater._graph.has_edge(i, j):
                        AutoUpdater._graph.add_edge(i, j)

                        if (not directed) and (not AutoUpdater._graph.has_edge(j, i)):
                            AutoUpdater._graph.add_edge(j, i)
            else:
                raise Exception("Invalid Input")

    @staticmethod
    def remove_link(a, b = None, directed=True):
        """
        Unlink a list of Connectors ( or  a Bus of connectors ) with another list / Bus.
        Give a single element list or a multi element single list ( a only ) to unlink all connections
        to and from the node ( Connector )
        
        USAGE
        =====
        
        >>> a = Bus(4)
        >>> b = Bus(2)
        >>> c = Bus(2)
        >>> AutoUpdater.add_link(a[:2], b)
        >>> AutoUpdater.add_link(a[2:], c)
        >>> AutoUpdater.remove_link(a[:2], b)
        >>> AutoUpdater.remove_link(a[2:]) # Single list (Bus) with multiple connector instance ..
        
        """
        if b is not None:
            with AutoUpdater._lock:
                if (type(a) in (list, BinPy.connectors.connector.Bus)) and (type(b) in (list, BinPy.connectors.connector.Bus)):
                    if len(a) != len(b):
                        raise Exception("ERROR: Lengths are not equal")
                    for i, j in zip(a, b):
                        if (isinstance(i, BinPy.connectors.connector.Connector), isinstance(j, BinPy.connectors.connector.Connector)) != (True, True):
                            raise Exception(
                                "ERROR: Only Connector objects can be Unlinked")
                        if AutoUpdater._graph.has_edge(i, j):
                            AutoUpdater._graph.remove_edge(i, j)

                            if not directed and AutoUpdater._graph.has_edge(j, i):
                                AutoUpdater._graph.remove_edge(j, i)

                else:
                    raise Exception("Invalid Input")
         
        else:
            with AutoUpdater._lock:
                # if only a is given remove all links to and from it.
                if ( type(a) in [ BinPy.connectors.connector.Bus, list ] ):
                    # Bus is passed:
                    for conn in a:
                        if isinstance(conn, BinPy.connectors.connector.Connector):
                            AutoUpdater._graph.remove_node(conn)
                        else:
                            raise Exception(
                                "ERROR: Only Connector objects can be Unlinked")
                else:
                    raise Exception("ERROR: Specify inputs as list of Connectors or a Bus")
                         
    def __init__(self):
        threading.Thread.__init__(self)

        self.daemon = True
        self.start()

    def run(self):
        while True:
            with AutoUpdater._lock:
                nodes = AutoUpdater._graph.nodes()

            for i in nodes:
                with AutoUpdater._lock:
                    for pair in AutoUpdater._graph.edges(i):
                        pair[1].set_voltage(pair[0])
                        # Copies the value of the 0th index connector to the 1st
                        # index connector

                # One circuit has been traversed.


# Initiating the auto updater.
auto_updater_instance = AutoUpdater()

# To make the call to link easier.
auto_update_link = auto_updater_instance.add_link

# To make call to unlink shorter.
auto_update_unlink = auto_updater_instance.remove_link

class BinPyIndexer(object):

    """
    The BnPy Indexer is a indexing and inventory listing servic to bind a unique index and store them as key:value

    This makes it easier to debug connections.

    MODULES
    =======

    * index
    * unindex
    * get_element
    * get_index

    EXAMPLES
    ========

    >>> a = Bus(4); b= Bus(4)
    >>> a.index
    1
    >>> b.index
    2

    """

    _indices = {}     # { gates.AND : { 1:<AND instance> } }
    _rev_indices = {}  # { gates.AND : { <AND instance>:1 } }

    _max_index = {}   # { gates.AND : 1 }

    @property
    def indices():
        return BinPyIndexer._indices

    @property
    def rev_indices():
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
        if (element is None) and (index is None) and (cls is None):
            raise Exception("Specify atleast one parameter")

        if element is not None:
            index = BinPyIndexer.get_index(element)
            cls = element.__class__

        elif (index is None) and (cls is None):
            raise Exception("Insufficient parameters passed")

        element = BinPyIndexer._indices[cls].pop(index)
        BinPyIndexer._rev_indices[cls].pop(element)

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
