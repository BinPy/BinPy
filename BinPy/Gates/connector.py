from __future__ import division
import BinPy.config.constants
import itertools


"""
Contains
========

* Connector
* Bus
* make_bus

"""


class Connector:

    """
    This class is the primary medium for data transfer. Objects of this
    class can be connected to any digital object.

    Example
    =======

    >>> from BinPy import *
    >>> conn = Connector(1)  #Initializing connector with initial state = 1
    >>> conn.state
    1
    >>> gate = OR(0, 1)
    >>> conn.tap(gate, 'output')  #Tapping the connector

    Methods
    =======

    * tap
    * untap
    * is_input_of
    * is_output_of
    * trigger
    """

    _index = 0

    def __init__(self, state=None, name=""):
        self.connections = {"output": [], "input": []}
        # To store the all the taps onto this connection
        self.state = state  # To store the state of the connection
        self.oldstate = None
        # voltage for analog components
        self.voltage = 0.0
        self.oldvoltage = 0.0
        self._name = name
        self.name_set = (name != "")
        Connector._index += 1
        self._index = Connector._index

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
        if type(val) in [int, None, bool]:
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
        if type(val) in [float, int]:
            self.voltage = float(val)
        elif isinstance(val, Connector):
            self.voltage = val.get_voltage()

        else:
            raise Exception("ERROR: Voltage must be a float or int")

        state = constants.LOGIC_HIGH_STATE if self.voltage > constants.LOGIC_THRESHOLD_VOLT else constants.LOGIC_LOW_STATE
        self.set_logic(state)

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

    @property
    def name(self):
        return self._name

    # This could replace the trigger method all together.
    def __setattr__(self, name, val):
        self.__dict__[name] = val
        # self.trigger()

    # Overloads the bool method
    # For python3
    def __bool__(self):
        return True if self.state == 1 else False

    # To be compatible with Python 2.x
    __nonzero__ = __bool__

    # Overloads the int() method
    def __int__(self):
        return 1 if self.state == 1 else 0

    def __float__(self):
        return float(self.voltage)

    def __repr__(self):
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


class Bus:

    """
    This class provides an array of Connector Objects.
    Objects of this class can be used :
    1. As input and output interfaces for modules and other blocks
    2. When a lot of connectors are needed
    """

    _index = 0

    def __init__(self, *inputs):
        """
        Initialized through a list of connectors or another Bus
        or a integer (width) to create a Bus of new Connectors of the specified width
        """

        self.bus = []
        self.analog = False

        # Each Bus will have an unique index. Good for debugging Connections.
        Bus._index += 1
        self._index = Bus._index

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

    def set_width(self, width, *connectors):
        """Used to decrease the width of the bus or increase it and appending new additional connectors."""

        # Use this method sparingly. It would be good practice to keep Bus
        # objects of fixed size.

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

    # PLEASE DO NOT ADD A SET INPUT METHOD. WE DO NOT WANT TO CHANGE THE BUS CONNECTORS DYNAMICALLY.
    # IT CAN ONLY BE APPENDED OR DELETED BUT NOT UPDATED.

    def set_type(self, analog):
        self.analog = bool(analog)

    get_type = lambda self: "ANALOG" if self.analog else "DIGITAL"

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
            word = bin(word)[2:0].zfill(self._width)

        elif isinstance(values[0], str):
            word = values[0]
            # This will convert '11', '0011' and '0b0011' to '0011'
            word = bin(int(word, 2))[2:].zfill(self._width)

        elif isinstance(values[0], list):
            word = values[0]
            str_int_bool = lambda o: str(int(bool(o)))
            # This is done to convert Connector elements to logic states or to
            # ensure the list passed is binary
            word = "".join(map(str_int_bool, word))

        elif isinstance(values[0], Bus):
            word = values.get_logic_all(as_list=False)

        elif isinstance(values[0], Connector):
            str_int_bool = lambda o: str(int(bool(o)))
            word = map(str_int_bool, values)

        else:
            raise Exception("ERROR: Invalid input")

        word = map(int, word)

        if len(word) != self._width:
            # If input width is not of same size as the bus raise an exception
            raise Exception(
                "ERROR: Input width is not the same as that of the bus")

        for (bit, conn) in itertools.izip(word, self.bus):
            conn.set_logic(bit)

    def get_logic_all(self, as_list=True):
        if as_list:
            return map(int, self.bus)

        return "0b" + "".join((map(lambda o: str(int(o)), self.bus)))

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
            values = map(float, values)
            # This serves dual purpose:
            # 1. Converts 5 to 5.0
            # 2. When inputs are connectors it extracts the voltage data from
            # them.

        if isinstance(values[0], Bus):
            values = float(values[0])

        if len(values) != self._width:
            raise Exception(
                "ERROR: Input width is not the same as that of the bus")

        for (volt, conn) in itertools.izip(values, self.bus):
            conn.set_voltage(volt)

    def get_voltage_all(self):
        return map(float, self.bus)

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

        if bus.width() != self._width:
            raise Exception("ERROR: Width of both the busses must be same")

        self.set_voltage_all(bus.get_voltage_all())

    def __get__(self, index):
        return self.bus[index]

    def tap(self, index, element, mode):
        if index < 0 or index > self._width:
            raise Exception("ERROR: Invalid Index Value")
        self.bus[index].tap(element, mode)

    def untap(self, index, element, mode):
        if index < 0 or index > self._width:
            raise Exception("ERROR: Invalid Index Value")
        self.bus[index].untap(element, mode)

    @property
    def width(self):
        """
        Gives width of the Bus
        """
        return self._width

    @property
    def index(self):
        return self._index

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
            return value in map(bool, self.bus)
        elif isinstance(value, float):
            return value in map(float, self.bus)
        elif isinstance(value, int):
            return value in map(int, self.bus)
        else:
            return False

    def __reversed__(self):
        return reversed(self.bus)

    # def __getattr__(self, name):
        # pass

    def __getitem__(self, index):
        return self.bus[index]

    def __len__(self):
        return self._width

    def __int__(self):
        return map(int, self.bus)

    def __float__(self):
        return map(float, self.bus)

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

    def __rshift__(self):
        """ Clock wise right shift """
        return self.bus[-1] + self.bus[1:-1]

    def __lshift__(self):
        """ Clock wise left shift """
        return self.bus[1:] + self.bus[:1]

    def __add__(self, other):
        """ Returns the concatenated Bus with the passed bus"""
        return Bus(self.bus + other.bus)

    def __bool__(self):
        return map(bool, self.bus)

    __nonzero__ = __bool__
