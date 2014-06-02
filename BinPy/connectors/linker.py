import threading
import BinPy

# This is a basic skeleton ... Much has to be developed ...

lock = threading.Lock()
elements = []

'''
def link(*inputs):
    """ Connect the connectors to the network graph. """
    inputs
    instance_check = [inputs[0], inputs[1]]

    if False in instance_check:
        raise('ERROR: Invalid Input')

    for i in inputs:
        if i not in elements:
            elements.append(i)
'''

class Linker:
    def __init__(self):
        pass

class BinPyIndexer:

    _indices = {}     # { gates.AND : { 1:<AND instance> } }
    _rev_indices = {} # { gates.AND : { <AND instance>:1 } }
    
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
        
        BinPyIndexer._max_index[element.__class__] += 1               # Unique ID numbers are not recycled.
        
        uid = BinPyIndexer._max_index[element.__class__]              # Unique ID for the element
        
        BinPyIndexer._indices[element.__class__][uid] = element       # UniqueID:element
        
        BinPyIndexer._rev_indices[element.__class__][element] = uid   # element:UniqueID
        
        return uid
    
    @staticmethod
    def unindex(element = None, index = None, cls = None):
        if ( element, index, cls ) == ( None, None, None ):
            raise Exception("Specify atleast one parameter")
        
        if element is not None:
            index = BinPyIndexer.get_index(element)
            cls = element.__class__
            
        if ( index, cls ) == ( None, None ):
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
        if ( cls in BinPyIndexer._indices ) and ( index in BinPyIndexer._indices[cls] ):
            return BinPyIndexer._indices[cls][index]