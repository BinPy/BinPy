from __future__ import division, with_statement
from BinPy.config import *
from BinPy.connectors.linker import *


"""
Contains
========

* Connector
* Bus

"""


class Connector(object):

    """
    This class is the primary medium for data transfer. Objects of this
    class can be connected to any digital object.

    Example
    =======

    >>> from BinPy import *
    >>> conn = Connector(1)  #Initializing connector with initial state = 1
    >>> conn.get_logic()
    1
    >>> gate = OR(0, 1)
    >>> conn.tap(gate, 'output')  #Tapping the connector

    METHODS
    =======

    set_logic         :      To set the logic state of the connector.
    get_logic         :      To get the logic state of the connector.
    set_voltage       :      To set the floating point volatage of the connector.
    get_voltage       :      To get the floating point volatage of the connector.
    is_input_of       :      To check whether this connector is the input of the given element.
    is_output_of      :      To check whether this connector is the output of the given element.
    tap               :      Tap this connector as input / output of another element
    untap             :      Untap this connector from another element



    PROPERTIES
    ==========

    index             :      The index of the connector instance registered with the BinPyIndexer
    name              :      Get the name of the connector
    state             :      [ Currently read / write supported. In future versions this will be read-only ]
                             To get ( and set ) the logic state of the connector.
    enabled           :      Return True if the connector is enabled.
    disabled          :      Return True if the connector is not enabled.

    """

    def __init__(self, state=None, voltage=None, analog=False, name=""):
        self.__dict__["_enable"] = True  # To bypass the __setattr__

        self.connections = {"output": [], "input": []}
        # To store the all the taps onto this connection
        self.set_logic(state)
        self.oldstate = None

        self.analog = analog
        # voltage for analog components
        if voltage is not None:
            self.set_voltage(voltage)
            self.analog = True

        self.oldvoltage = 0.0
        self._name = name
        self.name_set = (name != "")
        self._index = BinPyIndexer.index(self)

    @property
    def index(self):
        return self._index

    def tap(self, element, mode):
        # Can't serve output for multiple devices
        if mode == "output":
            self.connections["output"] = []

        if element not in self.connections[mode]:
            self.connections[mode].append(
                element)  # Add an element to the connections list

    def untap(self, element, mode):
        if element in self.connections[mode]:
            self.connections[mode].remove(
                element)  # Delete an element from the connections list
        else:
            raise Exception(
                "ERROR:Connector is not the %s of the passed element" %
                mode)

    def set_logic(self, val):

        if not self._enable:
            return

        if type(val) in [int, type(None), bool]:
            self.state = val if val is not None else None
            self.voltage = constants.LOGIC_HIGH_VOLT if self.state == constants.LOGIC_HIGH_STATE else constants.LOGIC_LOW_VOLT
            self.trigger()

        elif isinstance(val, Connector):
            self.state = val.get_logic()

        else:
            raise Exception("ERROR: Invalid input type")

        self.trigger()
        # All set functions ultimately call this. So one trigger here should
        # suffice.

    def get_logic(self):
        return self.state

    def set_voltage(self, val):
        if not self._enable:
            return

        if type(val) in [float, int]:
            self.voltage = float(val)
        elif isinstance(val, Connector):
            self.voltage = val.get_voltage()

        else:
            raise Exception("ERROR: Voltage must be a float or int")

        self.state = constants.LOGIC_HIGH_STATE if self.voltage > constants.LOGIC_THRESHOLD_VOLT else constants.LOGIC_LOW_STATE

    def get_voltage(self):
        return self.voltage

    def is_input_of(self, element):
        return element in self.connections["input"]

    def is_output_of(self, element):
        return element in self.connections["output"]

    # This function is called when the value of the connection changes
    def trigger(self):
        for i in self.connections["input"]:
            i.trigger()

    def __call__(self):
        return self.state

    def set_name(self, name):
        if (self.name is None) and (not self.name_set):
            for k, v in list(globals().iteritems()):
                if (id(v) == id(self)) and (k != "self"):
                    self.name = k
            self.name_set = True

        elif self.name is not None:
            self._name = name

    @property
    def name(self):
        return self._name

    # This could replace the trigger method all together.
    def __setattr__(self, name, val):
        # To enable the connector when it is disabled.
        if (not self._enable) and (name != "_enable"):
            return
        self.__dict__[name] = val

    # Overloads the bool method
    # For python3
    def __bool__(self):
        return True if self.state == 1 else False

    # To be compatible with Python 2.x
    __nonzero__ = __bool__

    def enable(self):
        self._enable = True

    def disable(self):
        self._enable = False

    @property
    def enabled(self):
        return self._enable

    @property
    def disabled(self):
        return (not self._enable)

    # Overloads the int() method
    def __int__(self):
        return 1 if self.state == 1 else 0

    def __float__(self):
        return float(self.voltage)

    def __repr__(self):
        if (self.analog):
            return str(float(self))
        else:
            return str(self.state)

    def __str__(self):
        return "Connector; Name: %s; Index: %d; State: " % (
            self.name, self.index) + str(self.state)

    def __add__(self, other):
        return self.voltage + other.voltage

    def __sub__(self, other):
        return self.voltage - other.voltage

    def __mul__(self, other):
        return self.voltage * other.voltage

    def __truediv__(self, other):
        return self.voltage / other.voltage

    def __del__(self):
        try:
            AutoUpdater.remove_link([self])
            BinPyIndexer.unindex(self)
        except (AttributeError, KeyError, ValueError) as e:
            pass


class Bus(object):

    """
    Bus is a container class for  Connectors.
    It maintains a list of Connectors on which a variety of operations can be performed.

    Busses can be used :
    1. As input and output interfaces for modules and other blocks
    2. When a lot of connectors are needed

    EXAMPLES
    ========

    >>> a = Connector()
    >>> b = Connector()
    >>> c = Connector()
    >>> d = Connector()

    # Initiating Bus from connectors
    >>> a = Bus(a, b, c, d)

    # Creating a Bus from another Bus
    >>> b = Bus(a)

    # Initializing and methods.
    >>> b.set_voltage_all()
    >>> b.get_voltage.all()
    [ None, None, None, None ]
    >>> b.set_logic_all('1011')
    >>> b.get_logic_all()
    [ 1, 0, 1, 1 ]

    # Since busses only wrap around Connectors the original connectors are referenced by the Bus objects
    # Hence any change to the containing Bus also exhibits in the Connectors

    >>> a.get_logic()
    1
    >>> b.get_logic()
    0

    # Busses can be sliced, iterated, inplace modified ( removal ), index-retrieved etc like lists

    >>> for connector in a[1:3] :
    ...     print ( connector.get_logic_all() )
    ...

    0
    1

    >>> del a[1:3]   # Deletes connectors a.bus[1] and a.bus[2]
    >>> a.pop()   # pop without argument removes the last connector
    1
    >>> print a.get_logic_all()
    [ 1 ]

    """

    def __init__(self, *inputs):
        """
        Initialized through a list of connectors or another Bus
        or a integer (width) to create a Bus of new Connectors of the specified width
        """
        self.bus = []
        self.analog = False

        # width specified
        if (len(inputs) == 1) and (isinstance(inputs[0], int)) and (inputs[0] >= 0):
            self.bus += [Connector() for i in range(inputs[0])]
            self._width = inputs[0]

        # create from Bus; Similar to a = list(b)
        elif (len(inputs) == 1) and isinstance(inputs[0], Bus):
            self.bus = list(inputs[0].bus)
            self.analog = inputs[0].analog
            self._width = len(self.bus)

        # create from a list of connectors
        else:
            # if inputs is a list of connectors
            if (len(inputs) == 1) and (isinstance(inputs[0], list)):
                inputs = inputs[0]

            # if inputs is an unpacked list of connectors
            if (len(inputs) > 0) and (False not in [isinstance(i, Connector) for i in inputs]):
                self.bus += inputs
                self._width = len(self.bus)

            else:
                raise Exception("ERROR: Invalid input")

        if self.analog:
            for i in self:
                i.analog = True

        # Each Bus will have an unique index. Good for debugging Connections.
        self._index = BinPyIndexer.index(self)

    @property
    def index(self):
        return self._index

    def set_width(self, width, *connectors):
        """Used to decrease the width of the bus or increase it and appending new additional connectors."""

        # Use this method sparingly. It would be good practice to keep Bus
        # objects of fixed si
        if width <= 0:
            raise Exception("ERROR: Enter non-negative width")
        if width == self._width:
            return
        elif width < self._width:
            self.bus = self.bus[:width]
        elif width > self._width:
            if len(connectors) == width - self._width:
                self.bus += [(conn if isinstance(conn, Connector)
                              else Connector()) for conn in connectors]

            self.bus += [Connector() for i in range(width - len(self.bus))]

        self._width = width

    # DEV NOTE:
    # PLEASE DO NOT ADD A SET INPUT METHOD. WE DO NOT WANT TO CHANGE THE BUS CONNECTORS DYNAMICALLY.
    # IT CAN ONLY BE APPENDED OR DELETED BUT NOT UPDATED.

    def set_type(self, analog):
        self.analog = bool(analog)

    def get_type(self):
        return "ANALOG" if self.analog else "DIGITAL"

    def set_logic(self, index, value):
        if index > 0 and index < self._width:
            self.bus[index].set_logic(value)
        else:
            raise Exception("ERROR: Invalid Index value")

    def get_logic(self, index):
        if index > 0 and index < self._width:
            return self.bus[index].get_logic()
        raise Exception("ERROR: Invalid Index value")

    def set_logic_all(self, *values):
        """
        Sets the passed word to the connectors in 4 ways
        1. word as an int representation of the bits of bus ( trucated to digital voltage levels ) : 4 ( 0100 )
        2. word as a binary literal : '0b0001' or '1111'
        3. A packed or unpacked list of  connector objects or
           a packed or unpacked list of integer binary values. : [ a, b, c, d ] or *[ 1, 0, None, 1]
        4. A Bus : bus1
        """

        if isinstance(values[0], int):
            word = values[0]
            if word < 0:
                raise Exception("ERROR: Negative value passed")
            word = bin(word)[2:].zfill(self._width)

        elif isinstance(values[0], str):
            word = values[0]
            # This will convert '11', '0011' and '0b0011' to '0011'
            word = bin(int(word, 2))[2:].zfill(self._width)

        elif isinstance(values[0], list):
            word = values[0]
            str_int_bool = lambda o: str(int(bool(o)))
            # This is done to convert Connector elements to logic states or to
            # ensure the list passed is binary
            word = "".join(list(map(str_int_bool, word)))

        elif isinstance(values[0], Bus):
            word = values[0].get_logic_all(as_list=False)[2:]

        elif isinstance(values[0], Connector):
            str_int_bool = lambda o: str(int(bool(o)))
            word = list(map(str_int_bool, values))

        else:
            raise Exception("ERROR: Invalid input")

        word = list(map(int, word))

        if len(word) != self._width:
            # If input width is not of same size as the bus raise an exception
            raise Exception(
                "ERROR: Input width is not the same as that of the bus")

        for (bit, conn) in zip(word, self.bus):
            conn.set_logic(bit)

    def get_logic_all(self, as_list=True):
        if as_list:
            return list(map(int, self.bus))

        return "0b" + "".join((list(map(lambda o: str(int(o)), self.bus))))

    def set_voltage_all(self, *values):
        """
        Set the voltage of all the connectors in the bus in 4 ways:
        1. Packed or unpacked List of connectors
        2. Bus
        3. Packed or unpacked List of voltage values
        """

        # If a list is passed as such or the values[0] is a Bus

        if isinstance(values[0], list):
            values = values[0]
            values = list(map(float, values))
            # This serves dual purpose:
            # 1. Converts 5 to 5.0
            # 2. When inputs are connectors it extracts the voltage data from
            # them.

        if isinstance(values[0], Bus):
            self.set_voltage_all(values[0].get_voltage_all())
            return

        if len(values) != self._width:
            raise Exception(
                "ERROR: Input width is not the same as that of the bus")

        for (volt, conn) in zip(values, self.bus):
            conn.set_voltage(volt)

    def get_voltage_all(self):
        return list(map(float, self.bus))

    def copy(self):
        # Returns a copy of bus
        return Bus(self)

    __copy__ = copy

    def copy_values_to(self, bus):
        """Copy values between two busses"""
        if not isinstance(bus, Bus):
            raise Exception("ERROR: Invalid input""")

        if bus.width != self._width:
            raise Exception("ERROR: Width of both the busses must be same")

        bus.set_voltage_all(self.get_voltage_all())

    def copy_values_from(self, bus):
        """Copy values between two busses"""
        if not isinstance(bus, Bus):
            raise Exception("ERROR: Invalid input""")

        if bus.width != self._width:
            raise Exception("ERROR: Width of both the busses must be same")

        self.set_voltage_all(bus.get_voltage_all())

    def tap(self, index, element, mode):
        if index < 0 or index > self._width:
            raise Exception("ERROR: Invalid Index Value")
        self.bus[index].tap(element, mode)

    def untap(self, index, element, mode):
        if index < 0 or index > self._width:
            raise Exception("ERROR: Invalid Index Value")
        self.bus[index].untap(element, mode)

    def pop(self, index=-1):
        """ Remove connectors with the specified index ( or last connector if None specified ) from Bus """
        popped = self.bus.pop(index)
        self._width = len(self.bus)  # update the new length
        return popped

    def __repr__(self):
        return str(self.bus)

    @property
    def width(self):
        """
        Gives width of the Bus
        """
        return self._width

    def trigger(self):
        for conn in self.bus:
            conn.trigger()

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        # self.trigger()

    def __contains__(self, value):

        if isinstance(value, Connector):
            return value in self.bus
        elif isinstance(value, bool):
            return value in list(map(bool, self.bus))
        elif isinstance(value, float):
            return value in list(map(float, self.bus))
        elif isinstance(value, int):
            return value in list(map(int, self.bus))
        else:
            return False

    def __reversed__(self):
        return reversed(self.bus)

    # def __getattr__(self, name):
        # pass

    def __getitem__(self, index):
        return self.bus[index]

    def __delitem__(self, index):
        del self.bus[index]
        self._width = len(self.bus)

    def __len__(self):
        return self._width

    def __str__(self):
        return str(self.bus)

    def __repr__(self):
        return str(self.bus)

    def __iter__(self):
        return iter(self.bus)
        # Make bus iterable

    def __eq__(self, val):

        bus_values = self.get_voltage_all(
        ) if self.analog else self.get_logic_all()

        if isinstance(val, Bus):
            return bus_values == (
                val.get_voltage_all() if self.analog else val.get_logic_all())

        elif isinstance(val, list):
            return bus_values == val

        elif isinstance(val, str):
            return int(val, 2) == self.get_logic_all(as_list=False)

        raise Exception("ERROR: Invalid Comparison")

    def __hash__(self):
        return id(self)

    def __rshift__(self, times):
        """ Circular right shift """
        times = times % self._width

        if times == 0:
            return self.bus[:]
        else:
            return self.bus[-times:] + self.bus[:self._width - times]

    def __lshift__(self, times):
        """ Circular left shift """
        times = times % self._width

        if times == 0:
            return self.bus[:]
        else:
            return self.bus[times:] + self.bus[:times]

    def __add__(self, other):
        """ Returns the concatenated Bus with the passed bus"""
        return Bus(self.bus + other.bus)

    def __bool__(self):
        return list(map(bool, self.bus))

    __nonzero__ = __bool__

    def __del__(self):
        try:
            AutoUpdater.remove_link(self)
            BinPyIndexer.unindex(self)
        except (AttributeError, KeyError, ValueError) as e:
            pass
