"""
This module has all the classes of ICs belonging to 7400 series.

Please note that the length of list self.pins is 1 more than the number of actual pins. This is so because pin0
is not used as a general term referring to the first pin of the IC. Zeroth index of the self.pins is not being used.
"""
from __future__ import print_function
from BinPy.Gates import *
from BinPy.Sequential import *
from BinPy.ic.base import *
from BinPy.tools import *
from BinPy.Combinational.combinational import *

#################################
# IC's with 14 pins
#################################


class IC_74152(Base_14pin):

    """
    This is 14-pin 8:1 multiplexer with inverted input.

    Pin Number	Description
        1	D4
        2	D3
        3	D2
        4	D1
        5	D0
        6	Output W
        7	Ground
        8	select line C
        9	select line B
        10	select line A
        11	D7
        12	D6
        13     D5
        14	Positive Supply

        Selectlines = CBA and Inputlines = D0 D1 D2 D3 D4 D5 D6 D7
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0]

    def run(self):

        output = {}

        mux = MUX(
            self.pins[5],
            self.pins[4],
            self.pins[3],
            self.pins[2],
            self.pins[1],
            self.pins[13],
            self.pins[12],
            self.pins[11])
        mux.selectLines(self.pins[8], self.pins[9], self.pins[10])

        output[6] = NOT(mux.output()).output()

        if self.pins[7] == 0 and self.pins[14] == 1:
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7400(Base_14pin):

    """
    This is a QUAD 2 INPUT NAND gate IC
    Pin Configuration:

    Pin Number	Description
        1	A Input Gate 1
        2	B Input Gate 1
        3	Y Output Gate 1
        4	A Input Gate 2
        5	B Input Gate 2
        6	Y Output Gate 2
        7	Ground
        8	Y Output Gate 3
        9	B Input Gate 3
        10	A Input Gate 3
        11	Y Output Gate 4
        12	B Input Gate 4
        13	A Input Gate 4
        14	Positive Supply

    This class needs 14 parameters. Each parameter being the pin value. The input has to be defined as a dictionary
    with pin number as the key and its value being either 1 or 0

    To initialise the ic 7400:
        1. set pin 7:0
        2. set pin 14:1

    How to use:

        >>> ic = IC_7400()
        >>> pin_config = {1: 1, 2: 0, 4: 0, 5: 0, 7: 0, 9: 1, 10: 1, 12: 0, 13: 0, 14: 1}
        >>> ic.setIC(pin_cofig)
        >>> ic.drawIC()
        >>> ic.run()
        >>> ic.setIC(ic.run())
        >>> ic.drawIC()

    Methods:
        pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]


    """

    def __init__(self):
        self.pins = [
            None,
            0,
            0,
            None,
            0,
            0,
            None,
            0,
            None,
            0,
            0,
            None,
            0,
            0,
            0]

    def run(self):
        output = {}
        output[3] = NAND(self.pins[1], self.pins[2]).output()
        output[6] = NAND(self.pins[4], self.pins[5]).output()
        output[8] = NAND(self.pins[9], self.pins[10]).output()
        output[11] = NAND(self.pins[12], self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7401(Base_14pin):

    """
    This is a Quad 2-input open-collector NAND gate IC
    """

    def __init__(self):
        self.pins = [
            None,
            None,
            0,
            0,
            None,
            0,
            0,
            0,
            0,
            0,
            None,
            0,
            0,
            None,
            0]

    def run(self):
        output = {}
        output[1] = NAND(self.pins[2], self.pins[3]).output()
        output[4] = NAND(self.pins[5], self.pins[6]).output()
        output[10] = NAND(self.pins[8], self.pins[9]).output()
        output[13] = NAND(self.pins[11], self.pins[12]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7402(Base_14pin):

    """
    This is a Quad 2-input NOR gate IC

    Pin Configuration:

    Pin Number	Description
        1	Y Output Gate 1
        2	A Input Gate 1
        3	B Input Gate 1
        4	Y Output Gate 2
        5	A Input Gate 2
        6	B Input Gate 2
        7	Ground
        8	A Input Gate 3
        9	B Input Gate 3
        10	Y Output Gate 3
        11	A Input Gate 4
        12	B Input Gate 4
        13	Y Output Gate 4
        14	Positive Supply

    This class needs 14 parameters. Each parameter being the pin value. The input has to be defined as a dictionary
    with pin number as the key and its value being either 1 or 0

    To initialise the ic 7402:
        1. set pin 7:0
        2. set pin 14:1

    How to use:

        >>> ic = IC_7402()
        >>> pin_config = {2: 0, 3: 0, 5: 0, 6: 1, 7: 0, 8: 1, 9: 1, 11: 1, 12: 1, 14: 1}
        >>> ic.setIC(pin_cofig)
        >>> ic.drawIC()
        >>> ic.run()
        >>> ic.setIC(ic.run())
        >>> ic.drawIC()

    Default pins:
        pins = [None,None,0,0,None,0,0,0,0,0,None,0,0,None,0]


    """

    def __init__(self):
        self.pins = [
            None,
            None,
            0,
            0,
            None,
            0,
            0,
            0,
            0,
            0,
            None,
            0,
            0,
            None,
            0]

    def run(self):
        output = {}
        output[1] = NOR(self.pins[2], self.pins[3]).output()
        output[4] = NOR(self.pins[5], self.pins[6]).output()
        output[10] = NOR(self.pins[8], self.pins[9]).output()
        output[13] = NOR(self.pins[11], self.pins[12]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7403(Base_14pin):

    """
    This is a Quad 2-input open-collector NAND gate IC

    Pin Number	Description
        1	A Input Gate 1
        2	B Input Gate 1
        3	Y Output Gate 1
        4	A Input Gate 2
        5	B Input Gate 2
        6	Y Output Gate 2
        7	Ground
        8	Y Output Gate 3
        9	B Input Gate 3
        10	A Input Gate 3
        11	Y Output Gate 4
        12	B Input Gate 4
        13	A Input Gate 4
        14	Positive Supply


    This class needs 14 parameters. Each parameter being the pin value. The input has to be defined as a dictionary
    with pin number as the key and its value being either 1 or 0

    To initialise the ic 7403:
        1. set pin 7:0
        2. set pin 14:1

    How to use:

        >>> ic = IC_7403()
        >>> pin_config = {1: 1, 2: 0, 4: 0, 5: 0, 7: 0, 9: 1, 10: 1, 12: 0, 13: 0, 14: 1}
        >>> ic.setIC(pin_cofig)
        >>> ic.drawIC()
        >>> ic.run()
        >>> ic.setIC(ic.run())
        >>> ic.drawIC()

    Default pins:
        pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]


    """

    def __init__(self):
        self.pins = [
            None,
            0,
            0,
            None,
            0,
            0,
            None,
            0,
            None,
            0,
            0,
            None,
            0,
            0,
            0]

    def run(self):
        output = {}
        output[3] = NAND(self.pins[1], self.pins[2]).output()
        output[6] = NAND(self.pins[4], self.pins[5]).output()
        output[8] = NAND(self.pins[9], self.pins[10]).output()
        output[11] = NAND(self.pins[12], self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7404(Base_14pin):

    """
    This is a hex inverter IC

    Pin Number	Description
        1	A Input Gate 1
        2	Y Output Gate 1
        3	A Input Gate 2
        4	Y Output Gate 2
        5	A Input Gate 3
        6	Y Output Gate 3
        7	Ground
        8	Y Output Gate 4
        9	A Input Gate 4
        10	Y Output Gate 5
        11	A Input Gate 5
        12	Y Output Gate 6
        13	A Input Gate 6
        14	Positive Supply

    This class needs 14 parameters. Each parameter being the pin value. The input has to be defined as a dictionary
    with pin number as the key and its value being either 1 or 0

    To initialise the ic 7404:
        1. set pin 7:0
        2. set pin 14:1

    How to use:

        >>> ic = IC_7404()
        >>> pin_config = {1: 1, 3: 0, 5: 0, 7: 0, 9: 0, 11: 0, 13: 1, 14: 1}
        >>> ic.setIC(pin_cofig)
        >>> ic.drawIC()
        >>> ic.run()
        >>> ic.setIC(ic.run())
        >>> ic.drawIC()

    Default pins:
        pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]

    """

    def __init__(self):
        self.pins = [
            None,
            0,
            None,
            0,
            None,
            0,
            None,
            0,
            None,
            0,
            None,
            0,
            None,
            0,
            0]

    def run(self):
        output = {}
        output[2] = NOT(self.pins[1]).output()
        output[4] = NOT(self.pins[3]).output()
        output[6] = NOT(self.pins[5]).output()
        output[8] = NOT(self.pins[9]).output()
        output[10] = NOT(self.pins[11]).output()
        output[12] = NOT(self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7405(Base_14pin):

    """
    This is hex open-collector inverter IC
    """

    def __init__(self):
        self.pins = [
            None,
            0,
            None,
            0,
            None,
            0,
            None,
            0,
            None,
            0,
            None,
            0,
            None,
            0,
            0]

    def run(self):
        output = {}
        output[2] = NOT(self.pins[1]).output()
        output[4] = NOT(self.pins[3]).output()
        output[6] = NOT(self.pins[5]).output()
        output[8] = NOT(self.pins[9]).output()
        output[10] = NOT(self.pins[11]).output()
        output[12] = NOT(self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7408(Base_14pin):

    """
    This is a Quad 2 input AND gate IC

    Pin Number	Description
        1	A Input Gate 1
        2	B Input Gate 1
        3	Y Output Gate 1
        4	A Input Gate 2
        5	B Input Gate 2
        6	Y Output Gate 2
        7	Ground
        8	Y Output Gate 3
        9	B Input Gate 3
        10	A Input Gate 3
        11	Y Output Gate 4
        12	B Input Gate 4
        13	A Input Gate 4
        14	Positive Supply

    This class needs 14 parameters. Each parameter being the pin value. The input has to be defined as a dictionary
    with pin number as the key and its value being either 1 or 0

    To initialise the ic 7408:
        1. set pin 7:0
        2. set pin 14:1

    How to use:

        >>> ic = IC_7408()
        >>> pin_config = {1: 1, 2: 0, 4: 0, 5: 0, 7: 0, 9: 1, 10: 1, 12: 0, 13: 0, 14: 1}
        >>> ic.setIC(pin_cofig)
        >>> ic.drawIC()
        >>> ic.run()
        >>> ic.setIC(ic.run())
        >>> ic.drawIC()

    Default pins:
        pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]


    """

    def __init__(self):
        self.pins = [
            None,
            0,
            0,
            None,
            0,
            0,
            None,
            0,
            None,
            0,
            0,
            None,
            0,
            0,
            0]

    def run(self):
        output = {}
        output[3] = AND(self.pins[1], self.pins[2]).output()
        output[6] = AND(self.pins[4], self.pins[5]).output()
        output[8] = AND(self.pins[9], self.pins[10]).output()
        output[11] = AND(self.pins[12], self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7410(Base_14pin):

    """
    This is a Triple 3 input NAND gate IC

    Pin Number	Description
        1	A Input Gate 1
        2	B Input Gate 1
        3	A Input Gate 2
        4	B Input Gate 2
        5	C Input gate 2
        6	Y Output Gate 2
        7	Ground
        8	Y Output Gate 3
        9	A Input Case 3
        10	B Input Case 3
        11	C Input Case 3
        12	Y Output Gate 1
        13	C Input Gate 1
        14	Positive Supply


    This class needs 14 parameters. Each parameter being the pin value. The input has to be defined as a dictionary
    with pin number as the key and its value being either 1 or 0

    To initialise the ic 7410:
        1. set pin 7:0
        2. set pin 14:1

    How to use:

        >>> ic = IC_7410()
        >>> pin_config = {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 7: 0, 9: 1, 10: 1, 11: 1, 13: 0, 14: 1}
        >>> ic.setIC(pin_cofig)
        >>> ic.drawIC()
        >>> ic.run()
        >>> ic.setIC(ic.run())
        >>> ic.drawIC()

    Default pins:
        pins = [None,0,0,0,0,0,None,0,None,0,0,0,None,0,0]

    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, None, 0, 0]

    def run(self):
        output = {}
        output[12] = NAND(self.pins[1], self.pins[2], self.pins[13]).output()
        output[6] = NAND(self.pins[3], self.pins[4], self.pins[5]).output()
        output[8] = NAND(self.pins[9], self.pins[10], self.pins[11]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7411(Base_14pin):

    """
    This is a Triple 3 input AND gate IC

    Pin Number	Description
        1	A Input Gate 1
        2	B Input Gate 1
        3	A Input Gate 2
        4	B Input Gate 2
        5	C Input gate 2
        6	Y Output Gate 2
        7	Ground
        8	Y Output Gate 3
        9	A Input Case 3
        10	B Input Case 3
        11	C Input Case 3
        12	Y Output Gate 1
        13	C Input Gate 1
        14	Positive Supply


    This class needs 14 parameters. Each parameter being the pin value. The input has to be defined as a dictionary
    with pin number as the key and its value being either 1 or 0

    To initialise the ic 7411:
        1. set pin 7:0
        2. set pin 14:1

    How to use:

        >>> ic = IC_7411()
        >>> pin_config = {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 7: 0, 9: 1, 10: 1, 11: 1, 13: 0, 14: 1}
        >>> ic.setIC(pin_cofig)
        >>> ic.drawIC()
        >>> ic.run()
        >>> ic.setIC(ic.run())
        >>> ic.drawIC()

    Default pins:
        pins = [None,0,0,0,0,0,None,0,None,0,0,0,None,0,0]


    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, None, 0, 0]

    def run(self):
        output = {}
        output[12] = AND(self.pins[1], self.pins[2], self.pins[13]).output()
        output[6] = AND(self.pins[3], self.pins[4], self.pins[5]).output()
        output[8] = AND(self.pins[9], self.pins[10], self.pins[11]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7412(Base_14pin):

    """
    This is a Triple 3 input NAND gate IC with open collector outputs

    Pin Number	Description
        1	A Input Gate 1
        2	B Input Gate 1
        3	A Input Gate 2
        4	B Input Gate 2
        5	C Input gate 2
        6	Y Output Gate 2
        7	Ground
        8	Y Output Gate 3
        9	A Input Case 3
        10	B Input Case 3
        11	C Input Case 3
        12	Y Output Gate 1
        13	C Input Gate 1
        14	Positive Supply


    This class needs 14 parameters. Each parameter being the pin value. The input has to be defined as a dictionary
    with pin number as the key and its value being either 1 or 0

    To initialise the ic 7412:
        1. set pin 7:0
        2. set pin 14:1

    How to use:

        >>> ic = IC_7412()
        >>> pin_config = {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 7: 0, 9: 1, 10: 1, 11: 1, 13: 0, 14: 1}
        >>> ic.setIC(pin_cofig)
        >>> ic.drawIC()
        >>> ic.run()
        >>> ic.setIC(ic.run())
        >>> ic.drawIC()

    Default pins:
        pins = [None,0,0,0,0,0,None,0,None,0,0,0,None,0,0]

    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, None, 0, 0]

    def run(self):
        output = {}
        output[12] = NAND(self.pins[1], self.pins[2], self.pins[13]).output()
        output[6] = NAND(self.pins[3], self.pins[4], self.pins[5]).output()
        output[8] = NAND(self.pins[9], self.pins[10], self.pins[11]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7413(Base_14pin):

    """
    This is a dual 4 input NAND gate IC

    Pin Number	Description
        1	A Input Gate 1
        2	B Input Gate 1
        3	Not Connected
        4	C Input Gate 1
        5	D Input Gate 1
        6	Y Output Gate 1
        7	Ground
        8	Y Output Gate 2
        9	A Input Gate 2
        10	B Input Gate 2
        11	Not Connected
        12	C Input Gate 2
        13	D Input Gate 2
        14	Positive Supply


    This class needs 14 parameters. Each parameter being the pin value. The input has to be defined as a dictionary
    with pin number as the key and its value being either 1 or 0

    To initialise the ic 7413:
        1. set pin 7:0
        2. set pin 14:1

    How to use:

        >>> ic = IC_7413()
        >>> pin_config = {1: 1, 2: 0, 4: 0, 5: 0, 7: 0, 9: 1, 10: 1, 12: 1, 13: 1, 14: 1}
        >>> ic.setIC(pin_cofig)
        >>> ic.drawIC()
        >>> ic.run()
        >>> ic.setIC(ic.run())
        >>> ic.drawIC()

    Default pins:
        pins = [None,0,0,0,0,0,None,0,None,0,0,0,0,0,0]

    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, 0, 0, 0]

    def run(self):
        output = {}
        output[6] = NAND(
            self.pins[1],
            self.pins[2],
            self.pins[4],
            self.pins[5]).output()
        output[8] = NAND(
            self.pins[9],
            self.pins[10],
            self.pins[12],
            self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7415(Base_14pin):

    """
    This is a Triple 3 input AND gate IC with open collector outputs

    Pin Number	Description
        1	A Input Gate 1
        2	B Input Gate 1
        3	A Input Gate 2
        4	B Input Gate 2
        5	C Input Gate 2
        6	Y Output Gate 2
        7	Ground
        8	Y Output Gate 3
        9	A Input Gate 3
        10	B Input Gate 3
        11	C Input Gate 3
        12	Y Output Gate 1
        13	C Input Gate 1
        14	Positive Supply


    This class needs 14 parameters. Each parameter being the pin value. The input has to be defined as a dictionary
    with pin number as the key and its value being either 1 or 0

    To initialise the ic 7415:
        1. set pin 7:0
        2. set pin 14:1

    How to use:

        >>> ic = IC_7415()
        >>> pin_config = {1:1, 2:0, 3:0, 4:0, 5:0, 7:0, 9:1, 10:1, 11:1, 13:0, 14:1}
        >>> ic.setIC(pin_cofig)
        >>> ic.drawIC()
        >>> ic.run()
        >>> ic.setIC(ic.run())
        >>> ic.drawIC()

    Default pins:
        pins = [None,0,0,0,0,0,None,0,None,0,0,0,None,0,0]

    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, None, 0, 0]

    def run(self):
        output = {}
        output[12] = AND(self.pins[1], self.pins[2], self.pins[13]).output()
        output[6] = AND(self.pins[3], self.pins[4], self.pins[5]).output()
        output[8] = AND(self.pins[9], self.pins[10], self.pins[11]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7416(Base_14pin):

    """
    This is a Hex open-collector high-voltage inverter
    """

    def __init__(self):
        self.pins = [
            None,
            0,
            None,
            0,
            None,
            0,
            None,
            0,
            None,
            0,
            None,
            0,
            None,
            0,
            0]

    def run(self):
        output = {}
        output[2] = NOT(self.pins[1]).output()
        output[4] = NOT(self.pins[3]).output()
        output[6] = NOT(self.pins[5]).output()
        output[8] = NOT(self.pins[9]).output()
        output[10] = NOT(self.pins[11]).output()
        output[12] = NOT(self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7417(Base_14pin):

    """
    This is a Hex open-collector high-voltage buffer
    """

    def __init__(self):
        self.pins = [
            None,
            0,
            None,
            0,
            None,
            0,
            None,
            0,
            None,
            0,
            None,
            0,
            None,
            0,
            0]

    def run(self):
        output = {}
        output[2] = self.pins[1]
        output[4] = self.pins[3]
        output[6] = self.pins[5]
        output[8] = self.pins[9]
        output[10] = self.pins[11]
        output[12] = self.pins[13]
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7418(Base_14pin):

    """
    This is a Dual 4-input NAND gates with schmitt-trigger inputs.
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, 0, 0, 0]

    def run(self):
        output = {}
        output[6] = NAND(
            self.pins[1],
            self.pins[2],
            self.pins[4],
            self.pins[5]).output()
        output[8] = NAND(
            self.pins[9],
            self.pins[10],
            self.pins[12],
            self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7419(Base_14pin):

    """
    This is a Hex inverters with schmitt-trigger line-receiver inputs.
    """

    def __init__(self):
        self.pins = [
            None,
            0,
            None,
            0,
            None,
            0,
            None,
            0,
            None,
            0,
            None,
            0,
            None,
            0,
            0]

    def run(self):
        output = {}
        output[2] = NOT(self.pins[1]).output()
        output[4] = NOT(self.pins[3]).output()
        output[6] = NOT(self.pins[5]).output()
        output[8] = NOT(self.pins[9]).output()
        output[10] = NOT(self.pins[11]).output()
        output[12] = NOT(self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7420(Base_14pin):

    """
    This is a dual 4-input NAND gate
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, 0, 0, 0]

    def run(self):
        output = {}
        output[6] = NAND(
            self.pins[1],
            self.pins[2],
            self.pins[4],
            self.pins[5]).output()
        output[8] = NAND(
            self.pins[9],
            self.pins[10],
            self.pins[12],
            self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7421(Base_14pin):

    """
    This is a dual 4-input AND gate
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, 0, 0, 0]

    def run(self):
        output = {}
        output[6] = AND(
            self.pins[1],
            self.pins[2],
            self.pins[4],
            self.pins[5]).output()
        output[8] = AND(
            self.pins[9],
            self.pins[10],
            self.pins[12],
            self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7422(Base_14pin):

    """
    This is a dual 4-input NAND gate with open collector outputs
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, 0, 0, 0]

    def run(self):
        output = {}
        output[6] = NAND(
            self.pins[1],
            self.pins[2],
            self.pins[4],
            self.pins[5]).output()
        output[8] = NAND(
            self.pins[9],
            self.pins[10],
            self.pins[12],
            self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7424(Base_14pin):

    """
    This is a Quad 2-input NAND gates with schmitt-trigger line-receiver inputs
    """

    def __init__(self):
        self.pins = [
            None,
            0,
            0,
            None,
            0,
            0,
            None,
            0,
            None,
            0,
            0,
            None,
            0,
            0,
            0]

    def run(self):
        output = {}
        output[3] = NAND(self.pins[1], self.pins[2]).output()
        output[6] = NAND(self.pins[4], self.pins[5]).output()
        output[8] = NAND(self.pins[10], self.pins[9]).output()
        output[11] = NAND(self.pins[12], self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7425(Base_14pin):

    """
    This is a Dual 5-Input NOR Gate with Strobe
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, 0, 0, 0]

    def run(self):
        output = {}
        output[6] = NOR(
            self.pins[1],
            self.pins[2],
            self.pins[3],
            self.pins[4],
            self.pins[5]).output()
        output[8] = NOR(
            self.pins[9],
            self.pins[10],
            self.pins[11],
            self.pins[12],
            self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7426(Base_14pin):

    """
    This is a Quad 2-input open-collector high-voltage NAND gates.
    """

    def __init__(self):
        self.pins = [
            None,
            0,
            0,
            None,
            0,
            0,
            None,
            0,
            None,
            0,
            0,
            None,
            0,
            0,
            0]

    def run(self):
        output = {}
        output[3] = NAND(self.pins[1], self.pins[2]).output()
        output[6] = NAND(self.pins[4], self.pins[5]).output()
        output[8] = NAND(self.pins[9], self.pins[10]).output()
        output[11] = NAND(self.pins[12], self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7427(Base_14pin):

    """
    This is a Triple 3-Input NOR Gate
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, None, 0, 0]

    def run(self):
        output = {}
        output[6] = NOR(self.pins[3], self.pins[4], self.pins[5]).output()
        output[8] = NOR(self.pins[9], self.pins[10], self.pins[11]).output()
        output[12] = NOR(self.pins[1], self.pins[2], self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7428(Base_14pin):

    """
    This is a Quad 2-input NOR gates with buffered outputs.
    """

    def __init__(self):
        self.pins = [
            None,
            None,
            0,
            0,
            None,
            0,
            0,
            0,
            0,
            0,
            None,
            0,
            0,
            None,
            0]

    def run(self):
        output = {}
        output[1] = NOR(self.pins[2], self.pins[3]).output()
        output[4] = NOR(self.pins[5], self.pins[6]).output()
        output[10] = NOR(self.pins[8], self.pins[9]).output()
        output[13] = NOR(self.pins[11], self.pins[12]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7430(Base_14pin):

    """
    This is a 8-Input NAND Gate
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0]

    def run(self):
        output = {}
        output[8] = NAND(
            self.pins[1],
            self.pins[2],
            self.pins[3],
            self.pins[4],
            self.pins[5],
            self.pins[6],
            self.pins[11],
            self.pins[12]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7432(Base_14pin):

    """
    This is a Quad 2-Input OR Gate
    """

    def __init__(self):
        self.pins = [
            None,
            0,
            0,
            None,
            0,
            0,
            None,
            0,
            None,
            0,
            0,
            None,
            0,
            0,
            0]

    def run(self):
        output = {}
        output[3] = OR(self.pins[1], self.pins[2]).output()
        output[6] = OR(self.pins[4], self.pins[5]).output()
        output[8] = OR(self.pins[9], self.pins[10]).output()
        output[11] = OR(self.pins[12], self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7433(Base_14pin):

    """
    This is a Quad 2-input open-collector NOR gate
    """

    def __init__(self):
        self.pins = [
            None,
            None,
            0,
            0,
            None,
            0,
            0,
            0,
            0,
            0,
            None,
            0,
            0,
            None,
            0]

    def run(self):
        output = {}
        output[1] = NOR(self.pins[2], self.pins[3]).output()
        output[4] = NOR(self.pins[5], self.pins[6]).output()
        output[10] = NOR(self.pins[8], self.pins[9]).output()
        output[13] = NOR(self.pins[11], self.pins[12]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7437(Base_14pin):

    """
    This is a Quad 2-input NAND gates with buffered output
    """

    def __init__(self):
        self.pins = [
            None,
            0,
            0,
            None,
            0,
            0,
            None,
            0,
            None,
            0,
            0,
            None,
            0,
            0,
            0]

    def run(self):
        output = {}
        output[3] = NAND(self.pins[1], self.pins[2]).output()
        output[6] = NAND(self.pins[4], self.pins[5]).output()
        output[8] = NAND(self.pins[9], self.pins[10]).output()
        output[11] = NAND(self.pins[12], self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7438(Base_14pin):

    """
    This is a Quad 2-Input NAND Buffer with Open Collector Output
    """

    def __init__(self):
        self.pins = [
            None,
            0,
            0,
            None,
            0,
            0,
            None,
            0,
            None,
            0,
            0,
            None,
            0,
            0,
            0]

    def run(self):
        output = {}
        output[3] = NAND(self.pins[1], self.pins[2]).output()
        output[6] = NAND(self.pins[4], self.pins[5]).output()
        output[8] = NAND(self.pins[9], self.pins[10]).output()
        output[11] = NAND(self.pins[12], self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7440(Base_14pin):

    """
    This is a Dual 4-Input NAND Buffer
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, 0, 0, 0]

    def run(self):
        output = {}
        output[6] = NAND(
            self.pins[1],
            self.pins[2],
            self.pins[4],
            self.pins[5]).output()
        output[8] = NAND(
            self.pins[9],
            self.pins[10],
            self.pins[12],
            self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7451(Base_14pin):

    """
    This is a dual 2-wide 2-input AND-OR Invert gate
    """
    # Datasheet here, http://www.unitechelectronics.com/7451-7497data.htm

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, None, 0, None, 0, 0, 0, 0, 0, 0, 0]

    def run(self):
        output = {}
        output[6] = NOR(AND(self.pins[2], self.pins[3]).output(),
                        AND(self.pins[4], self.pins[5]).output()).output()
        output[8] = NOR(AND(self.pins[1],
                            self.pins[13],
                            self.pins[12]).output(),
                        AND(self.pins[11],
                            self.pins[10],
                            self.pins[9]).output()).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7454(Base_14pin):

    """
    This is a 4-wide 2-input AND-OR Invert gate
    """
    # Datasheet here, http://www.unitechelectronics.com/7451-7497data.htm

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, None, 0, None, 0, 0, 0, 0, 0, 0, 0]

    def run(self):
        output = {}
        temp = []
        temp.append(OR(AND(self.pins[1], self.pins[2]).output(), AND(
            self.pins[3], self.pins[4], self.pins[5]).output()).output())
        temp.append(OR(AND(self.pins[9],
                           self.pins[10],
                           self.pins[11]).output(),
                       AND(self.pins[12],
                           self.pins[13]).output()).output())
        output[6] = NOR(temp[0], temp[1]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7455(Base_14pin):

    """
    This is a 4-wide 2-input AND-OR Invert gate
    """
    # Datasheet here, http://www.unitechelectronics.com/7451-7497data.htm

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0]

    def run(self):
        output = {}
        temp = []
        temp.append(AND(self.pins[1], self.pins[2],
                        self.pins[3], self.pins[4]).output())
        temp.append(AND(self.pins[10], self.pins[11],
                        self.pins[12], self.pins[13]).output())
        output[8] = NOR(temp[0], temp[1]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7458(Base_14pin):

    """
    This is a 2-input and 3-input AND-OR gate
    """
    # Datasheet here, http://www.unitechelectronics.com/7451-7497data.htm

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, None, 0, None, 0, 0, 0, 0, 0, 0, 0]

    def run(self):
        output = {}
        output[6] = OR(AND(self.pins[2], self.pins[3]).output(),
                       AND(self.pins[4], self.pins[5]).output()).output()
        output[8] = OR(AND(self.pins[1],
                           self.pins[13],
                           self.pins[12]).output(),
                       AND(self.pins[11],
                           self.pins[10],
                           self.pins[9]).output()).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7464(Base_14pin):

    """
    This is a 4-2-3-2 input AND-OR-invert gate
    """

    # Datasheet here, http://www.skot9000.com/ttl/datasheets/64.pdf

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0]

    def run(self):
        output = {}
        output[8] = NOR(
            AND(
                self.pins[2], self.pins[3]).output(), AND(
                self.pins[9], self.pins[10]).output(), AND(
                self.pins[1], self.pins[11], self.pins[13], self.pins[12]).output(), AND(
                self.pins[4], self.pins[5], self.pins[6]).output()).output()

        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7486(Base_14pin):

    """
    This is a quad 2-input exclusive OR gate
    """

    # Datasheet here, http://www.skot9000.com/ttl/datasheets/86.pdf

    def __init__(self):
        self.pins = [
            None,
            0,
            0,
            None,
            0,
            0,
            None,
            0,
            None,
            0,
            0,
            None,
            0,
            0,
            0]

    def run(self):
        output = {}

        output[3] = XOR(self.pins[1], self.pins[2]).output()

        output[6] = XOR(self.pins[4], self.pins[5]).output()

        output[8] = XOR(self.pins[9], self.pins[10]).output()

        output[11] = XOR(self.pins[12], self.pins[13]).output()

        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_74260(Base_14pin):

    """
    This is a dual 5-input NOR gate
    """

    # Datasheet here, http://www.skot9000.com/ttl/datasheets/260.pdf

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0]

    def run(self):
        output = {}

        output[5] = NOR(self.pins[1], self.pins[2], self.pins[3],
                        self.pins[12], self.pins[13]).output()

        output[6] = NOR(self.pins[4], self.pins[8], self.pins[9],
                        self.pins[10], self.pins[11]).output()

        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")

#################################
# IC's with 5 pins
#################################


class IC_741G00(Base_5pin):

    """
    This is a single 2 input NAND gate IC
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, None, 0]

    def run(self):
        output = {}
        output[4] = NAND(self.pins[1], self.pins[2]).output()
        if self.pins[3] == 0 and self.pins[5] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_741G02(Base_5pin):

    """
    This is a single 2 input NOR gate IC
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, None, 0]

    def run(self):
        output = {}
        output[4] = NOR(self.pins[1], self.pins[2]).output()
        if self.pins[3] == 0 and self.pins[5] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_741G03(Base_5pin):

    """
    This is a single 2 input NAND gate IC
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, None, 0]

    def run(self):
        output = {}
        output[4] = NAND(self.pins[1], self.pins[2]).output()
        if self.pins[3] == 0 and self.pins[5] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_741G04(Base_5pin):

    """
    This is a single inverter IC
    """

    def __init__(self):
        self.pins = [None, None, 0, 0, None, 0]

    def run(self):
        output = {}
        output[4] = NOT(self.pins[2]).output()
        if self.pins[3] == 0 and self.pins[5] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_741G05(Base_5pin):

    """
    This is a single input NOT gate IC
    """

    def __init__(self):
        self.pins = [None, None, 0, 0, None, 0]

    def run(self):
        output = {}
        output[4] = NOT(self.pins[2]).output()
        if self.pins[3] == 0 and self.pins[5] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_741G08(Base_5pin):

    """
    This is a single 2 input AND gate IC
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, None, 0]

    def run(self):
        output = {}
        output[4] = AND(self.pins[1], self.pins[2]).output()
        if self.pins[3] == 0 and self.pins[5] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


#################################
# IC's with 16 pins
#################################

class IC_7431(Base_16pin):

    """
    This is a Hex delay element.
    """

    def __init__(self):
        self.pins = [
            None,
            0,
            None,
            0,
            None,
            0,
            0,
            None,
            0,
            None,
            0,
            0,
            None,
            0,
            None,
            0,
            0]

    def run(self):
        output = {}
        output[2] = NOT(self.pins[1]).output()
        output[7] = NAND(self.pins[5], self.pins[6]).output()
        output[14] = NOT(self.pins[15]).output()
        output[9] = NAND(self.pins[10], self.pins[11]).output()
        output[4] = self.pins[3]
        output[12] = self.pins[13]

        if self.pins[8] == 0 and self.pins[16] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7442(Base_16pin):

    """
    This is a BCD to Decimal decoder
    BCD Digits are in order of A B C D where pin 15 = A, pin 12 = D
    """

    def __init__(self):
        self.pins = [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            0,
            None,
            None,
            None,
            0,
            0,
            0,
            0,
            0]

    def run(self):
        output = {}
        inputlist = []
        for i in range(12, 16, 1):
            inputlist.append(self.pins[i])

        invalidlist = [
            [
                1, 0, 1, 0], [
                1, 0, 1, 1], [
                1, 1, 0, 0], [
                1, 1, 0, 1], [
                1, 1, 1, 0], [
                1, 1, 1, 1]]

        if inputlist in invalidlist:
            raise Exception("ERROR: Invalid BCD number")

        output[1] = NAND(NOT(self.pins[15]).output(),
                         NOT(self.pins[14]).output(),
                         NOT(self.pins[13]).output(),
                         NOT(self.pins[12]).output()).output()

        output[2] = NAND(
            self.pins[15], NOT(
                self.pins[14]).output(), NOT(
                self.pins[13]).output(), NOT(
                self.pins[12]).output()).output()

        output[3] = NAND(NOT(self.pins[15]).output(),
                         self.pins[14],
                         NOT(self.pins[13]).output(),
                         NOT(self.pins[12]).output()).output()

        output[4] = NAND(
            self.pins[15], self.pins[14], NOT(
                self.pins[13]).output(), NOT(
                self.pins[12]).output()).output()

        output[5] = NAND(NOT(self.pins[15]).output(),
                         NOT(self.pins[14]).output(),
                         self.pins[13],
                         NOT(self.pins[12]).output()).output()

        output[6] = NAND(self.pins[15], NOT(self.pins[14]).output(),
                         self.pins[13], NOT(self.pins[12]).output()).output()

        output[7] = NAND(NOT(self.pins[15]).output(), self.pins[14],
                         self.pins[13], NOT(self.pins[12]).output()).output()

        output[9] = NAND(self.pins[15], self.pins[14],
                         self.pins[13], NOT(self.pins[12]).output()).output()

        output[10] = NAND(NOT(self.pins[15]).output(),
                          NOT(self.pins[14]).output(),
                          NOT(self.pins[13]).output(),
                          self.pins[12]).output()

        output[11] = NAND(self.pins[15], NOT(self.pins[14]).output(),
                          NOT(self.pins[13]).output(), self.pins[12]).output()

        if self.pins[8] == 0 and self.pins[16] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7443(Base_16pin):

    """
    This is an excess-3 to Decimal decoder
    Excess-3 binary digits are in order of A B C D, where pin 15 = A and pin 12 = D
    """

    def __init__(self):
        self.pins = [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            0,
            None,
            None,
            None,
            0,
            0,
            0,
            0,
            0]

    def run(self):
        output = {}
        inputlist = []
        for i in range(12, 16, 1):
            inputlist.append(self.pins[i])

        invalidlist = [
            [
                0, 0, 0, 0], [
                0, 0, 0, 1], [
                0, 0, 1, 0], [
                1, 1, 0, 1], [
                1, 1, 1, 0], [
                1, 1, 1, 1]]

        if inputlist in invalidlist:
            raise Exception("ERROR: Invalid Pin configuration")

        output[1] = NAND(
            self.pins[15], self.pins[14], NOT(
                self.pins[13]).output(), NOT(
                self.pins[12]).output()).output()

        output[2] = NAND(NOT(self.pins[15]).output(),
                         NOT(self.pins[14]).output(),
                         self.pins[13],
                         NOT(self.pins[12]).output()).output()

        output[3] = NAND(self.pins[15], NOT(self.pins[14]).output(),
                         self.pins[13], NOT(self.pins[12]).output()).output()

        output[4] = NAND(NOT(self.pins[15]).output(), self.pins[14],
                         self.pins[13], NOT(self.pins[12]).output()).output()

        output[5] = NAND(self.pins[15], self.pins[14],
                         self.pins[13], NOT(self.pins[12]).output()).output()

        output[6] = NAND(NOT(self.pins[15]).output(),
                         NOT(self.pins[14]).output(),
                         NOT(self.pins[13]).output(),
                         self.pins[12]).output()

        output[7] = NAND(self.pins[15], NOT(self.pins[14]).output(),
                         NOT(self.pins[13]).output(), self.pins[12]).output()

        output[9] = NAND(NOT(self.pins[15]).output(), self.pins[14],
                         NOT(self.pins[13]).output(), self.pins[12]).output()

        output[10] = NAND(self.pins[15], self.pins[14],
                          NOT(self.pins[13]).output(), self.pins[12]).output()

        output[11] = NAND(NOT(self.pins[15]).output(),
                          NOT(self.pins[14]).output(),
                          self.pins[13],
                          self.pins[12]).output()

        if self.pins[8] == 0 and self.pins[16] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7444(Base_16pin):

    """
    This is an excess-3 gray code to Decimal decoder
    Excess-3 gray code digits are in order of A B C D, where pin 15 = A and pin 12 = D
    """

    def __init__(self):
        self.pins = [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            0,
            None,
            None,
            None,
            0,
            0,
            0,
            0,
            0]

    def run(self):
        output = {}
        inputlist = []
        for i in range(12, 16, 1):
            inputlist.append(self.pins[i])

        invalidlist = [
            [
                0, 0, 0, 0], [
                0, 0, 0, 1], [
                0, 0, 1, 1], [
                1, 0, 0, 0], [
                1, 0, 0, 1], [
                1, 0, 1, 1]]

        if inputlist in invalidlist:
            raise Exception("ERROR: Invalid Pin configuration")

        output[1] = NAND(NOT(self.pins[15]).output(),
                         self.pins[14],
                         NOT(self.pins[13]).output(),
                         NOT(self.pins[12]).output()).output()

        output[2] = NAND(NOT(self.pins[15]).output(), self.pins[14],
                         self.pins[13], NOT(self.pins[12]).output()).output()

        output[3] = NAND((self.pins[15]), self.pins[14],
                         self.pins[13], NOT(self.pins[12]).output()).output()

        output[4] = NAND(self.pins[15], NOT(self.pins[14]).output(),
                         self.pins[13], NOT(self.pins[12]).output()).output()

        output[5] = NAND(NOT(self.pins[15]).output(),
                         NOT(self.pins[14]).output(),
                         self.pins[13],
                         NOT(self.pins[12]).output()).output()

        output[6] = NAND(NOT(self.pins[15]).output(),
                         NOT(self.pins[14]).output(),
                         self.pins[13],
                         self.pins[12]).output()

        output[7] = NAND(self.pins[15], NOT(self.pins[14]).output(),
                         self.pins[13], self.pins[12]).output()

        output[9] = NAND(self.pins[15], self.pins[14],
                         self.pins[13], self.pins[12]).output()

        output[10] = NAND(NOT(self.pins[15]).output(), self.pins[14],
                          self.pins[13], self.pins[12]).output()

        output[11] = NAND(NOT(self.pins[15]).output(), self.pins[14],
                          NOT(self.pins[13]).output(), self.pins[12]).output()

        if self.pins[8] == 0 and self.pins[16] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7445(Base_16pin):

    """
    This is a Four-to-Ten (BCD to Decimal) DECODER
    datasheet at http://www.skot9000.com/ttl/datasheets/45.pdf
    """

    def __init__(self):
        self.pins = [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            0,
            None,
            None,
            None,
            0,
            0,
            0,
            0,
            0]

    def run(self):
        output = {}
        inputlist = []
        for i in range(12, 16, 1):
            inputlist.append(self.pins[i])

        invalidlist = [
            [
                1, 0, 1, 0], [
                1, 0, 1, 1], [
                1, 1, 0, 0], [
                1, 1, 0, 1], [
                1, 1, 1, 0], [
                1, 1, 1, 1]]

        if inputlist in invalidlist:
            raise Exception("ERROR: Invalid Pin configuration")

        output[1] = NAND(NOT(self.pins[15]).output(),
                         NOT(self.pins[14]).output(),
                         NOT(self.pins[13]).output(),
                         NOT(self.pins[12]).output()).output()

        output[2] = NAND(
            self.pins[15], NOT(
                self.pins[14]).output(), NOT(
                self.pins[13]).output(), NOT(
                self.pins[12]).output()).output()

        output[3] = NAND(NOT(self.pins[15]).output(),
                         self.pins[14],
                         NOT(self.pins[13]).output(),
                         NOT(self.pins[12]).output()).output()

        output[4] = NAND(self.pins[15],
                         self.pins[14],
                         NOT(self.pins[13]).output(),
                         NOT(self.pins[12]).output()).output()

        output[5] = NAND(NOT(self.pins[15]).output(),
                         NOT(self.pins[14]).output(),
                         self.pins[13],
                         NOT(self.pins[12]).output()).output()

        output[6] = NAND(self.pins[15], NOT(self.pins[14]).output(),
                         self.pins[13], NOT(self.pins[12]).output()).output()

        output[7] = NAND(NOT(self.pins[15]).output(), self.pins[14],
                         self.pins[13], NOT(self.pins[12]).output()).output()

        output[9] = NAND(self.pins[15], self.pins[14],
                         self.pins[13], NOT(self.pins[12]).output()).output()

        output[10] = NAND(NOT(self.pins[15]).output(),
                          NOT(self.pins[14]).output(),
                          NOT(self.pins[13]).output(),
                          self.pins[12]).output()

        output[11] = NAND(self.pins[15], NOT(self.pins[14]).output(),
                          NOT(self.pins[13]).output(), self.pins[12]).output()

        if self.pins[8] == 0 and self.pins[16] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_74133(Base_16pin):

    """
    This is a 13-input NAND gate
    """

    # Datasheet here, http://www.skot9000.com/ttl/datasheets/133.pdf

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0]

    def run(self):
        output = {}

        output[9] = NAND(
            self.pins[1],
            self.pins[2],
            self.pins[3],
            self.pins[4],
            self.pins[5],
            self.pins[6],
            self.pins[7],
            self.pins[10],
            self.pins[11],
            self.pins[12],
            self.pins[13],
            self.pins[14],
            self.pins[15]).output()

        if self.pins[8] == 0 and self.pins[16] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7483(Base_16pin):

    """
    This is a 4-bit full adder with fast carry
    """

    # Datasheet here, http://www.skot9000.com/ttl/datasheets/83.pdf

    def __init__(self):
        self.pins = [
            None,
            0,
            None,
            0,
            0,
            0,
            None,
            0,
            0,
            None,
            0,
            0,
            0,
            0,
            None,
            None,
            0]

    def run(self):
        output = {}

        output[9] = XOR(self.pins[10], self.pins[11], self.pins[13]).output()

        carry = OR(AND(self.pins[13],
                       XOR(self.pins[10],
                           self.pins[11]).output()).output(),
                   AND(self.pins[10],
                       self.pins[11]).output()).output()

        output[6] = XOR(self.pins[8], self.pins[7], carry).output()

        carry = OR(AND(carry, XOR(self.pins[8], self.pins[7]).output()).output(), AND(
            self.pins[8], self.pins[7]).output()).output()

        output[2] = XOR(self.pins[3], self.pins[4], carry).output()

        carry = OR(AND(carry, XOR(self.pins[3], self.pins[4]).output()).output(), AND(
            self.pins[3], self.pins[4]).output()).output()

        output[15] = XOR(self.pins[1], self.pins[16], carry).output()

        output[14] = OR(AND(carry,
                            XOR(self.pins[1],
                                self.pins[16]).output()).output(),
                        AND(self.pins[1],
                            self.pins[16]).output()).output()

        if self.pins[12] == 0 and self.pins[5] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


##############################################
# Sequential Circuits
##############################################

##############################################
# Base_14 Pin
##############################################

class IC_7470(Base_14pin):

    "AND gated JK Positive Edge triggered Flip Flop with preset and clear"

    def __init__(self):
        self.pins = [
            None,
            0,
            0,
            0,
            0,
            0,
            None,
            0,
            None,
            0,
            0,
            0,
            0,
            0,
            0]

    def run(self):
        output = {}
        J = Connector(AND(self.pins[3], self.pins[4], self.pins[5]).output())
        K = Connector(AND(self.pins[9], self.pins[10], self.pins[11]).output())
        if not isinstance(self.pins[12], Clock):
            raise Exception("Error: Invalid Clock Input")
        ff = JKFlipFlop(J, K, Connector(1), self.pins[12].A,
                        self.pins[13], self.pins[2])
        while True:
            if self.pins[12].A.state == 0:
                ff.trigger()
                break
        while True:
            if self.pins[12].A.state == 1:
                ff.trigger()
                break
        output[8] = ff.state()[0]
        output[10] = ff.state()[1]
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7472(Base_14pin):

    "AND gated JK Master-Slave Flip Flop with preset and clear"

    def __init__(self):
        self.pins = [
            None,
            0,
            0,
            0,
            0,
            0,
            None,
            0,
            None,
            0,
            0,
            0,
            0,
            0,
            0]

    def run(self):
        output = {}
        J = Connector(AND(self.pins[3], self.pins[4], self.pins[5]).output())
        K = Connector(AND(self.pins[9], self.pins[10], self.pins[11]).output())
        if not isinstance(self.pins[12], Clock):
            raise Exception("Error: Invalid Clock Input")
        ff = JKFlipFlop(J, K, Connector(1), self.pins[12].A,
                        self.pins[13], self.pins[2])
        while True:
            if self.pins[12].A.state == 0:
                ff.trigger()
                break
        while True:
            if self.pins[12].A.state == 1:
                ff.trigger()
                break
        output[8] = ff.state()[0]
        output[10] = ff.state()[1]
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7473(Base_14pin):

    "DUAL JK Flip Flops with clear"

    def __init__(self):
        self.pins = [
            None,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0]

    def run(self):
        output = {}
        if not (isinstance(self.pins[1], Clock) and
                isinstance(self.pins[5], Clock)):
            raise Exception("Error: Invalid Clock Input")
        ff1 = JKFlipFlop(
            self.pins[14],
            self.pins[3],
            Connector(1),
            self.pins[1].A,
            Connector(1),
            self.pins[2])
        while True:
            if self.pins[1].A.state == 0:
                ff1.trigger()
                break
        while True:
            if self.pins[1].A.state == 1:
                ff1.trigger()
                break
        output[12] = ff1.state()[0]
        output[13] = ff1.state()[1]

        ff2 = JKFlipFlop(
            self.pins[7],
            self.pins[10],
            Connector(1),
            self.pins[5].A,
            Connector(1),
            self.pins[6])
        while True:
            if self.pins[5].A.state == 0:
                ff2.trigger()
                break
        while True:
            if self.pins[5].A.state == 1:
                ff2.trigger()
                break
        output[9] = ff2.state()[0]
        output[8] = ff2.state()[1]
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7474(Base_14pin):

    "Dual D-Type Positive-Edge-Triggered Flip-Flops with preset and clear"

    def __init__(self):
        self.pins = [
            None,
            0,
            0,
            0,
            0,
            None,
            None,
            0,
            None,
            None,
            0,
            0,
            0,
            0,
            0]

    def run(self):
        output = {}
        if not (isinstance(self.pins[3], Clock) and
                isinstance(self.pins[11], Clock)):
            raise Exception("Error: Invalid Clock Input")
        ff1 = DFlipFlop(self.pins[2], Connector(1), self.pins[3].A,
                        self.pins[4], self.pins[1])
        while True:
            if self.pins[3].A.state == 0:
                ff1.trigger()
                break
        while True:
            if self.pins[3].A.state == 1:
                ff1.trigger()
                break
        output[5] = ff1.state()[0]
        output[6] = ff1.state()[1]

        ff2 = DFlipFlop(self.pins[12], Connector(1), self.pins[11].A,
                        self.pins[10], self.pins[13])
        while True:
            if self.pins[11].A.state == 0:
                ff2.trigger()
                break
        while True:
            if self.pins[11].A.state == 1:
                ff2.trigger()
                break
        output[9] = ff2.state()[0]
        output[8] = ff2.state()[1]
        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


##########################################
# Base_16 Pins
##########################################

class IC_7475(Base_16pin):

    "4-Bit Bistable Latches"

    def __init__(self):
        self.pins = [
            None,
            None,
            0,
            0,
            0,
            0,
            0,
            0,
            None,
            None,
            None,
            None,
            None,
            0,
            0,
            None,
            None,
            None]

    def run(self):
        output = {}
        if not (isinstance(self.pins[4], Clock) and
                isinstance(self.pins[13], Clock)):
            raise Exception("Error: Invalid Clock Input")
        ff1 = DFlipFlop(self.pins[2], Connector(1),
                        self.pins[13].A, Connector(1), Connector(1))
        while True:
            if self.pins[13].A.state == 0:
                ff1.trigger()
                break
        while True:
            if self.pins[13].A.state == 1:
                ff1.trigger()
                break
        output[16] = ff1.state()[0]
        output[1] = ff1.state()[1]

        ff2 = DFlipFlop(self.pins[3], Connector(1),
                        self.pins[13].A, Connector(1), Connector(1))
        while True:
            if self.pins[13].A.state == 0:
                ff2.trigger()
                break
        while True:
            if self.pins[13].A.state == 1:
                ff2.trigger()
                break
        output[15] = ff2.state()[0]
        output[14] = ff2.state()[1]

        ff3 = DFlipFlop(self.pins[6], Connector(1),
                        self.pins[4].A, Connector(1), Connector(1))
        while True:
            if self.pins[4].A.state == 0:
                ff3.trigger()
                break
        while True:
            if self.pins[4].A.state == 1:
                ff3.trigger()
                break
        output[10] = ff3.state()[0]
        output[11] = ff3.state()[1]

        ff4 = DFlipFlop(self.pins[7], Connector(1),
                        self.pins[4].A, Connector(1), Connector(1))
        while True:
            if self.pins[4].A.state == 0:
                ff4.trigger()
                break
        while True:
            if self.pins[4].A.state == 1:
                ff4.trigger()
                break
        output[9] = ff4.state()[0]
        output[8] = ff4.state()[1]
        if self.pins[12] == 0 and self.pins[5] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_7476(Base_16pin):

    "Dual JK Flip Flop with preset and clear"

    def __init__(self):
        self.pins = [
            None,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0]

    def run(self):
        output = {}
        if not (isinstance(self.pins[1], Clock) and
                isinstance(self.pins[6], Clock)):
            raise Exception("Error: Invalid Clock Input")
        ff1 = JKFlipFlop(
            self.pins[4],
            self.pins[16],
            Connector(1),
            self.pins[1].A,
            self.pins[2],
            self.pins[3])
        while True:
            if self.pins[1].A.state == 0:
                ff1.trigger()
                break
        while True:
            if self.pins[1].A.state == 1:
                ff1.trigger()
                break
        output[15] = ff1.state()[0]
        output[14] = ff1.state()[1]

        ff2 = JKFlipFlop(
            self.pins[9],
            self.pins[12],
            Connector(1),
            self.pins[6].A,
            self.pins[7],
            self.pins[8])
        while True:
            if self.pins[6].A.state == 0:
                ff2.trigger()
                break
        while True:
            if self.pins[6].A.state == 1:
                ff2.trigger()
                break
        output[11] = ff2.state()[0]
        output[10] = ff2.state()[1]
        if self.pins[12] == 0 and self.pins[5] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_74153(Base_16pin):

    """
    This is 16-pin dual 4:1 multiplexer with output same as the input.

        Pin Number	Description
        1	Strobe1
        2	Select line B
        3	1C3
        4	1C2
        5	1C1
        6	1C0
        7	1Y - OUTPUT1
        8	Ground
        9	2Y - OUTPUT2
        10	2C0
        11	2C1
        12	2C2
        13	2C3
        14     Select line A
        15     Strobe2
        16	Positive Supply

        Selectlines = BA ; Inputlines1 = 1C0 1C1 1C2 1C3 ; Inputlines2 = 2C0 2C1 2C2 2C3
    """

    def __init__(self):
        self.pins = [
            None,
            0,
            0,
            0,
            0,
            0,
            0,
            None,
            0,
            None,
            0,
            0,
            0,
            0,
            0,
            0,
            0]

    def run(self):

        output = {}

        if (self.pins[1] == 1 and self.pins[15] == 1):
            output = {7: 0, 9: 0}

        elif (self.pins[1] == 0 and self.pins[15] == 1):

            mux = MUX(self.pins[6], self.pins[5], self.pins[4], self.pins[3])
            mux.selectLines(self.pins[2], self.pins[14])

            output[9] = 0
            output[7] = mux.output()

        elif (self.pins[1] == 1 and self.pins[15] == 0):

            mux = MUX(
                self.pins[10],
                self.pins[11],
                self.pins[12],
                self.pins[13])
            mux.selectLines(self.pins[2], self.pins[14])

            output[7] = 0
            output[9] = mux.output()

        elif (self.pins[1] == 0 and self.pins[15] == 0):

            mux1 = MUX(self.pins[6], self.pins[5], self.pins[4], self.pins[3])
            mux1.selectLines(self.pins[2], self.pins[14])

            mux2 = MUX(
                self.pins[10],
                self.pins[11],
                self.pins[12],
                self.pins[13])
            mux2.selectLines(self.pins[2], self.pins[14])

            output[7] = mux1.output()
            output[9] = mux2.output()

        if self.pins[8] == 0 and self.pins[16] == 1:
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_74151A(Base_16pin):

    """
    This is 16-pin 8:1 multiplexer featuring complementary W and Y outputs
    """

    def __init__(self):
        self.pins = [
            None,
            0,
            0,
            0,
            0,
            None,
            None,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0]

    def run(self):

        output = {}

        mux = MUX(
            self.pins[4],
            self.pins[3],
            self.pins[2],
            self.pins[1],
            self.pins[15],
            self.pins[14],
            self.pins[13],
            self.pins[12])
        mux.selectLines(self.pins[9], self.pins[10], self.pins[11])

        if self.pins[7] == 1:
            output = {5: 0, 6: 1}
        else:
            output[5] = mux.output()
            output[6] = NOT(output[5]).output()

        if self.pins[8] == 0 and self.pins[16] == 1:
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_74138(Base_16pin):

    """
    This is a 1:8 demultiplexer(3:8 decoder) with output being inverted input
    """

    def __init__(self):
        self.pins = [
            None,
            0,
            0,
            0,
            0,
            0,
            0,
            None,
            0,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            0]

    def run(self):

        output = {}

        demux = DEMUX(1)
        demux.selectLines(self.pins[3], self.pins[2], self.pins[1])

        if (self.pins[6] == 0 or (self.pins[4] == 1 and self.pins[5] == 1)):
            output = {15: 1, 14: 1, 13: 1, 12: 1, 11: 1, 10: 1, 9: 1, 7: 1}

        elif (self.pins[6] == 1 and (self.pins[4] == 0 and self.pins[5] == 0)):

            output[15] = NOT(demux.output()[0]).output()
            output[14] = NOT(demux.output()[1]).output()
            output[13] = NOT(demux.output()[2]).output()
            output[12] = NOT(demux.output()[3]).output()
            output[11] = NOT(demux.output()[4]).output()
            output[10] = NOT(demux.output()[5]).output()
            output[9] = NOT(demux.output()[6]).output()
            output[7] = NOT(demux.output()[7]).output()

        if self.pins[8] == 0 and self.pins[16] == 1:
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_74139(Base_16pin):

    """
    This is a dual 1:4 demultiplexer(2:4 decoder) with output being inverted input
    """

    def __init__(self):
        self.pins = [
            None,
            0,
            0,
            0,
            None,
            None,
            None,
            None,
            0,
            None,
            None,
            None,
            None,
            0,
            0,
            0,
            0]

    def run(self):

        output = {}

        demux1 = DEMUX(1)
        demux1.selectLines(self.pins[3], self.pins[2])

        demux2 = DEMUX(1)
        demux2.selectLines(self.pins[13], self.pins[14])

        if (self.pins[1] == 1 and self.pins[15] == 1):
            output = {12: 1, 11: 1, 10: 1, 9: 1, 7: 1, 6: 1, 5: 1, 4: 1}

        elif (self.pins[1] == 0 and self.pins[15] == 1):

            output[12] = 1
            output[11] = 1
            output[10] = 1
            output[9] = 1
            output[4] = NOT(demux1.output()[0]).output()
            output[5] = NOT(demux1.output()[1]).output()
            output[6] = NOT(demux1.output()[2]).output()
            output[7] = NOT(demux1.output()[3]).output()

        elif (self.pins[1] == 1 and self.pins[15] == 0):

            output[7] = 1
            output[6] = 1
            output[5] = 1
            output[4] = 1
            output[12] = NOT(demux2.output()[0]).output()
            output[11] = NOT(demux2.output()[1]).output()
            output[10] = NOT(demux2.output()[2]).output()
            output[9] = NOT(demux2.output()[3]).output()

        elif (self.pins[1] == 0 and self.pins[15] == 0):

            output[4] = NOT(demux1.output()[0]).output()
            output[5] = NOT(demux1.output()[1]).output()
            output[6] = NOT(demux1.output()[2]).output()
            output[7] = NOT(demux1.output()[3]).output()
            output[12] = NOT(demux2.output()[0]).output()
            output[11] = NOT(demux2.output()[1]).output()
            output[10] = NOT(demux2.output()[2]).output()
            output[9] = NOT(demux2.output()[3]).output()

        if self.pins[8] == 0 and self.pins[16] == 1:
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_74156(Base_16pin):

    """
    This is a dual 1:4 demultiplexer(2:4 decoder) with one output being inverted input
    while the other same as the input with open collector
    """

    def __init__(self):
        self.pins = [
            None,
            0,
            0,
            0,
            None,
            None,
            None,
            None,
            0,
            None,
            None,
            None,
            None,
            0,
            0,
            0,
            0]

    def run(self):

        output = {}

        demux1 = DEMUX(self.pins[1])
        demux1.selectLines(self.pins[3], self.pins[13])

        demux2 = DEMUX(NOT(self.pins[15]).output())
        demux2.selectLines(self.pins[3], self.pins[13])

        if (self.pins[2] == 1 and self.pins[14] == 1):
            output = {12: 1, 11: 1, 10: 1, 9: 1, 7: 1, 6: 1, 5: 1, 4: 1}

        elif (self.pins[2] == 0 and self.pins[14] == 1):

            output[12] = 1
            output[11] = 1
            output[10] = 1
            output[9] = 1
            output[4] = NOT(demux1.output()[3]).output()
            output[5] = NOT(demux1.output()[2]).output()
            output[6] = NOT(demux1.output()[1]).output()
            output[7] = NOT(demux1.output()[0]).output()

        elif (self.pins[2] == 1 and self.pins[14] == 0):

            output[7] = 1
            output[6] = 1
            output[5] = 1
            output[4] = 1
            output[12] = NOT(demux2.output()[3]).output()
            output[11] = NOT(demux2.output()[2]).output()
            output[10] = NOT(demux2.output()[1]).output()
            output[9] = NOT(demux2.output()[0]).output()

        elif (self.pins[2] == 0 and self.pins[14] == 0):

            output[4] = NOT(demux1.output()[3]).output()
            output[5] = NOT(demux1.output()[2]).output()
            output[6] = NOT(demux1.output()[1]).output()
            output[7] = NOT(demux1.output()[0]).output()
            output[12] = NOT(demux2.output()[3]).output()
            output[11] = NOT(demux2.output()[2]).output()
            output[10] = NOT(demux2.output()[1]).output()
            output[9] = NOT(demux2.output()[0]).output()

        if self.pins[8] == 0 and self.pins[16] == 1:
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")


class IC_74155(Base_16pin):

    """
    This is a dual 1:4 demultiplexer(2:4 decoder) with one output being inverted input
    while the other same as the input
    """

    def __init__(self):
        self.pins = [
            None,
            0,
            0,
            0,
            None,
            None,
            None,
            None,
            0,
            None,
            None,
            None,
            None,
            0,
            0,
            0,
            0]

    def run(self):

        output = {}

        demux1 = DEMUX(self.pins[1])
        demux1.selectLines(self.pins[3], self.pins[13])

        demux2 = DEMUX(NOT(self.pins[15]).output())
        demux2.selectLines(self.pins[3], self.pins[13])

        if (self.pins[2] == 1 and self.pins[14] == 1):
            output = {12: 1, 11: 1, 10: 1, 9: 1, 7: 1, 6: 1, 5: 1, 4: 1}

        elif (self.pins[2] == 0 and self.pins[14] == 1):

            output[12] = 1
            output[11] = 1
            output[10] = 1
            output[9] = 1
            output[4] = NOT(demux1.output()[3]).output()
            output[5] = NOT(demux1.output()[2]).output()
            output[6] = NOT(demux1.output()[1]).output()
            output[7] = NOT(demux1.output()[0]).output()

        elif (self.pins[2] == 1 and self.pins[14] == 0):

            output[7] = 1
            output[6] = 1
            output[5] = 1
            output[4] = 1
            output[12] = NOT(demux2.output()[3]).output()
            output[11] = NOT(demux2.output()[2]).output()
            output[10] = NOT(demux2.output()[1]).output()
            output[9] = NOT(demux2.output()[0]).output()

        elif (self.pins[2] == 0 and self.pins[14] == 0):

            output[4] = NOT(demux1.output()[3]).output()
            output[5] = NOT(demux1.output()[2]).output()
            output[6] = NOT(demux1.output()[1]).output()
            output[7] = NOT(demux1.output()[0]).output()
            output[12] = NOT(demux2.output()[3]).output()
            output[11] = NOT(demux2.output()[2]).output()
            output[10] = NOT(demux2.output()[1]).output()
            output[9] = NOT(demux2.output()[0]).output()

        if self.pins[8] == 0 and self.pins[16] == 1:
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print("Ground and VCC pins have not been configured correctly.")
