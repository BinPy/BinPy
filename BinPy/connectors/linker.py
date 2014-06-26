import threading
import networkx as nx
import re
import time
import BinPy


class simulated_lock:
    def __enter__(*inputs):
        pass
    
    def __exit__(*inputs):
        pass

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
    #_lock = threading.RLock()
    _lock = simulated_lock()
    _graph = nx.DiGraph()
    modified = False
    imported = False

    @staticmethod
    def add_link(
            a,
            b,
            directed=True,
            bind_to=(
                lambda *
                inputs: None),
            params=[]):
        """
        Link a list of Connectors ( or  a Bus of connectors ) with another list / Bus for auto-updation.
        Give 2 lists containing elements to be linked to each other element ( one to one map ).
        Functions can be bound with the links to be called upon traversal of the graph.

        The function binding can happen in two ways :
        same function for a group of connectors  - specify  inputs as lists / Busses of connectors.
        individual function for each connector - specify input links individually.

        USAGE
        =====

        >>> a = Bus(4)
        >>> b = Bus(2)
        >>> c = Bus(2)
        >>> d = Connector(0)
        >>> e = Connector(0)
        >>> def update_val(a, b)
        >>> AutoUpdater.add_link(a[:2], b)
        >>> AutoUpdater.add_link(a[2:], c)
        >>> AutoUpdater.add_link((b+c),a)
        >>> AutoUpdater.add_link(Bus(d,e),c)

        """
        try:
            Bus = BinPy.connectors.connector.Bus
            Connector = BinPy.connectors.connector.Connector

            # Is a list ( of connectors ) or bus or connector ?
            if type(a) not in [Connector, Bus, list]:
                raise Exception("Invalid input. ( First argument )")

            # Is b list ( of connectors ) or bus or connector ?
            if type(b) not in [Connector, Bus, list]:
                raise Exception("Invalid input. ( Second argument )")

            # If list, are all the contents Connectors ?
            if isinstance(a, list):
                for i in a:
                    if not isinstance(i, Connector):
                        raise Exception(
                            "Invalid input. List ( first argument ) contains non connector Objects")

            if isinstance(b, list):
                for i in b:
                    if not isinstance(i, Connector):
                        raise Exception(
                            "Invalid input. List ( second argument ) contains non connector Objects")

            # After all validation convert them to Bus containers to add to
            # graph.

            Bus_a = Bus(a)
            Bus_b = Bus(b)

            # Final check - Check if a and b are of equal lengths
            if len(Bus_a) != len(Bus_b):
                raise Exception("Unequal lengths")

        except (Exception) as e:
            raise Exception(
                "ERROR: Unable to convert inputs to Bus. : " +
                str(e))

        # Checking whether the bind_to object is '__call__' - able
        if (not hasattr(bind_to, '__call__')):
            raise Exception(
                "ERROR: Only  functions can be bound to links.")

        if (not isinstance(params, list)):
            raise Exception(
                "ERROR: Pass parameters to the bind_to function as a list.")

        with AutoUpdater._lock:
            if not AutoUpdater._graph.has_edge(Bus_a, Bus_b):
                # This check of presence of already existing edge does not work
                # if the connectors are wrapped in different bus containers
                AutoUpdater._graph.add_edge(Bus_a, Bus_b, object=bind_to)
                AutoUpdater._graph[Bus_a][Bus_b]['params'] = list(params)
                AutoUpdater.modified = True

                if (not directed) and (not AutoUpdater._graph.has_edge(Bus_b, Bus_a)):
                    AutoUpdater._graph.add_edge(Bus_b, Bus_a, object=bind_to)
                    AutoUpdater._graph[Bus_b][Bus_a]['params'] = list(params)

    @staticmethod
    def remove_link(a, b=None, directed=True):
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
        try:
            Bus = BinPy.connectors.connector.Bus
            Connector = BinPy.connectors.connector.Connector

            if b is not None:
                if (type(a) in (list, Bus)) and (type(b) in (list, Bus)):
                    if len(a) != len(b):
                        raise Exception("ERROR: Lengths are not equal")
                    for i, j in zip(a, b):
                        if (isinstance(i, Connector), isinstance(j, Connector)) != (True, True):
                            raise Exception(
                                "ERROR: Only Connector objects can be Unlinked")
                        with AutoUpdater._lock:
                            for pair in AutoUpdater._graph.edges():
                                # pair is ( bus_0, bus_1 )
                                for index in range(len(pair[0])):
                                    # Traverse through the bus_0 ( = pair[0] )
                                    if ((pair[0])[index] is i) and ((pair[1])[index] is j):
                                        # If ( i , j ) is ( bus_0[index] , bus_1[index] )
                                        # Where ( i, j ) is the input link to
                                        # be removed ( i --> j )
                                        del pair[0][index]
                                        del pair[1][index]
                                        break

                                # Separate for loop since when the first pair (
                                # above ) is deleted the length of pair[0]
                                # varies.
                                if not directed:
                                    for index in range(len(pair[0])):
                                        if (((pair[0])[index] is j) and ((pair[1])[index] is i)):
                                            del pair[1][index]
                                            del pair[0][index]

                                            AutoUpdater.modified = True
                                            break

                else:
                    raise Exception(
                        "ERROR: Specify inputs as list of Connectors or a Bus")

            else:
                # If b is None delete all links containing connectors from Bus
                # / list of Connectors
                with AutoUpdater._lock:
                    # if only a is given remove all links to and from it.
                    if (type(a) in [Bus, list]):
                        # Bus is passed:
                        for conn in a:
                            if isinstance(conn, Connector):
                                for pair in AutoUpdater._graph.edges():
                                    # pair is ( bus_0, bus_1 )
                                    for index in range(len(pair[0])):
                                        if ((pair[0])[index] is conn) or ((pair[1])[index] is conn):
                                            # if the conn is found either as
                                            # the start / end point of the link
                                            # ...

                                            if (pair[0])[index] is conn:
                                                del pair[0][index]
                                                del pair[1][index]

                                            else:
                                                del pair[1][index]
                                                del pair[0][index]

                                            AutoUpdater.modified = True

                                            break
                            else:
                                raise Exception(
                                    "ERROR: Only Connector objects can be Unlinked")
                    else:
                        raise Exception(
                            "ERROR: Specify inputs as list of Connectors or a Bus")

            with AutoUpdater._lock:
                # Clean up the graph removing isolated Busses ( if any )

                isolated_connectors = [
                    n for n,
                    d in AutoUpdater._graph.degree_iter() if d == 0]
                AutoUpdater._graph.remove_nodes_from(isolated_connectors)
                AutoUpdater.modified = True

                # clean up empty busses.
                for pair in AutoUpdater._graph.edges():
                    if (len(pair[0]) == 0):
                        AutoUpdater._graph.remove_edge(pair[0], pair[1])
                        continue

                    if (len(pair[1]) == 0):
                        AutoUpdater._graph.remove_edge(pair[1], pair[0])

        except (nx.NetworkXError) as e:
            if re.search(r'not in', repr(e)):
                pass
            else:
                raise nx.NetworkXError(str(e))


def connections_updater():
    AutoUpdater.lap = 0
    # lap indicates the no of times the entire graph has been traversed and updated.
    # This variable can be used to check if all the circuit elements have been
    # updated ( once or twice as per the requirement )
    try:
        while True:
            with AutoUpdater._lock:
                edges = AutoUpdater._graph.edges()

            AutoUpdater.lap = AutoUpdater.lap % 999 + 1  # Range is 1 to 999

            for pair in edges:
                # call the bind_to function before updation
                try:
                    if not AutoUpdater.modified:

                        AutoUpdater._graph[
                            pair[0]][
                            pair[1]]['object'](
                            *
                            AutoUpdater._graph[
                                pair[0]][
                                pair[1]]['params'])

                        pair[1].set_voltage_all(pair[0])

                    else:

                        # The circuit did not complete ...
                        AutoUpdater.lap -= 1
                        # Break and refresh nodes if the graph has been updated
                        # ...
                        AutoUpdater.modified = False
                        break

                # This exception is since there is no lock implemented to access the data
                # The graph size could vary ( if any element is removed or
                # added ) leading to
                except (IndexError, TypeError, ValueError, KeyError, AttributeError):
                    pass

                # modified flag reduces the occurrences of the same ...
                # but this cannot be avoided completely without lock

                # time.sleep(0.001)
                # To make the _lock available for other
                # operations ...

            # One circuit has been traversed.

    # To avoid errors when the graph itself is garbage collected - Due to
    # interpreter shutdown...
    except (AttributeError, KeyError, ValueError, TypeError) as e:
        # print("DEBUG: Linker - Critical error : ", e)
        return

# Initiating the auto updater.
connections_updater_thread = threading.Thread(target=connections_updater)
connections_updater_thread.daemon = True
connections_updater_thread.start()


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

        >>> g1 = Connector(0)
        >>> g1.index
        5
        >>> BinPyIndexer.get_element(5, Connector).get_state()
        0

        NOTE
        ====

        This method is intended to be used like getElementById() of DOM ( Web Development ) to access
        the various elements of BinPy by its index ( the id ).

        """
        if (cls in BinPyIndexer._indices) and (index in BinPyIndexer._indices[cls]):
            return BinPyIndexer._indices[cls][index]
