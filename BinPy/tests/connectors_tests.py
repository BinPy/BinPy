from BinPy.gates.gates import *
from nose.tools import with_setup, nottest


class Buffer_Block:

    def __init__(self):

        self.inputs = Bus(4)

        # Tests Bus initiation from another Bus
        self.outputs = Bus(self.inputs)

    def trigger(self):
        # Testing Copy values to
        self.outputs.copy_values_to(self.inputs)


def connectors_test():

    a = Buffer_Block()
    b = Buffer_Block()
    c = Buffer_Block()

    # Basic list test
    assert isinstance(a.outputs.bus, list)

    # Test for Connector initiation of bus
    a.inputs.set_logic_all('1011')
    a.trigger()

    # Test for __reversed__
    [int(i) for i in reversed(a.outputs)] == [1, 1, 0, 1]
    # a.outputs will have '1011'

    # Test __getitem__
    conn3 = a.outputs[3]

    # Test Connector
    assert isinstance(conn3, Connector)
    assert conn3.get_logic() == 1
    assert bool(conn3)
    assert float(conn3) == 5.0

    # Set voltage test
    a.outputs[3].set_voltage(0.0)

    # Test get_voltage_all as binary literal test
    assert int(a.outputs.get_logic_all(as_list=False), 2) == 10

    a.outputs.set_voltage_all(list(reversed(a.outputs)))

    assert float(a.outputs[0]) == 0
    assert int(a.outputs[3]) == 1

    # Testing copy_values_from
    b.inputs.set_logic_all(
        Connector(1),
        Connector(0),
        Connector(1),
        Connector(1))
    b.trigger()

    # Testing comparison operations

    assert b.outputs.get_logic_all() == [1, 0, 1, 1]

    assert b.outputs.get_voltage_all() == [5, 0, 5, 5]

    assert b.outputs == [1, 0, 1, 1]

    b.outputs.set_type(analog=True)

    assert b.outputs == [5, 0, 5, 5]

    assert b.outputs.get_logic_all(as_list=False)

    c = a.outputs + b.outputs
    c.trigger()

    assert c == [0, 1, 0, 1, 1, 0, 1, 1]
