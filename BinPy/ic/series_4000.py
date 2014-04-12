"""
This module has all the classes of ICs belonging to 4000 series.

Please note that the length of list self.pins is 1 more than the number of
actual pins. This is so because pin0 is not used as a general term referring
to the first pin of the IC. Zeroth index of the self.pins is not being used.

ICs in this module:
[4000, 4001, 4002, 4008, 4009, 4010, 4011, 4012, 4013, 4015, 4017, 4019, 4020, 4023, 4025, 4068, 4069, 4070, 4071, 4072, 4073
 4075, 4077, 4078, 4081, 4082]
"""

from __future__ import print_function
from BinPy.Gates import *
from BinPy.ic import *
from BinPy.Combinational import *

#################################
# IC's with 14 pins
#################################


class IC_4000(Base_14pin):

    """
    Dual 3 Input NOR gate + one NOT gate IC.
    Pin_6 = NOR(Pin_3, Pin_4, Pin_5)
    Pin_10 = NOR(Pin_11, Pin_12, Pin_13)
    Pin_9 = NOT(Pin_8)
    """

    def __init__(self):
        self.pins = [None, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'NC'},
                    2: {'desc': 'NC'},
                    3: {'desc': 'A1: Input 1 of NOR gate 1'},
                    4: {'desc': 'B1: Input 2 of NOR gate 1'},
                    5: {'desc': 'C1: Input 3 of NOR gate 1'},
                    6: {'desc': 'Q1: Output of NOR gate 1'},
                    7: {'desc': 'GND'},
                    8: {'desc': 'B2: Input of NOT gate'},
                    9: {'desc': 'Q2: Output of NOT gate'},
                    10: {'desc': 'Q3: Output of NOR gate 2'},
                    11: {'desc': 'C3: Input 3 of NOR gate 2'},
                    12: {'desc': 'B3: Input 2 of NOR gate 2'},
                    13: {'desc': 'A3: Input 1 of NOR gate 2'},
                    14: {'desc': 'VCC'}
                    })

    def run(self):
        output = {}
        output[6] = NOR(self.pins[3].value, self.pins[4].value,
                        self.pins[5].value).output()
        output[10] = NOR(self.pins[11].value, self.pins[12].value,
                         self.pins[13].value).output()
        output[9] = NOT(self.pins[8].value).output()
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4001(Base_14pin):

    """
    Quad 2 input NOR gate
    Pin_3 = NOR(Pin_1, Pin_2)
    Pin_4 = NOR(Pin_5, Pin_6)
    Pin_10 = NOR(Pin_8, Pin_9)
    Pin_11 = NOR(Pin_12, Pin_13)
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'A1: Input 1 of NOR gate 1'},
                    2: {'desc': 'B1: Input 2 of NOR gate 1'},
                    3: {'desc': 'Q1: Output of NOR gate 1'},
                    4: {'desc': 'Q2: Output of NOR gate 2'},
                    5: {'desc': 'B2: Input 2 of NOR gate 2'},
                    6: {'desc': 'A2: Input 1 of NOR gate 2'},
                    7: {'desc': 'GND'},
                    8: {'desc': 'A3: Input 1 of NOR gate 3'},
                    9: {'desc': 'B3: Input 2 of NOR gate 3'},
                    10: {'desc': 'Q3: Output of NOR gate 3'},
                    11: {'desc': 'Q4: Output of NOR gate 4'},
                    12: {'desc': 'B4: Input 2 of NOR gate 4'},
                    13: {'desc': 'A4: Input 1 of NOR gate 4'},
                    14: {'desc': 'VCC'}
                    })

    def run(self):
        output = {}
        output[3] = NOR(self.pins[1].value, self.pins[2].value).output()
        output[4] = NOR(self.pins[5].value, self.pins[6].value).output()
        output[10] = NOR(self.pins[8].value, self.pins[9].value).output()
        output[11] = NOR(self.pins[12].value, self.pins[13].value).output()
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            self.setIC(output)
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4002(Base_14pin):

    """
    Dual 4 input NOR gate
    Pin_1 = NOR(Pin_2, Pin_3, Pin_4, Pin_5)
    Pin_13 = NOR(Pin_9, Pin_10, Pin_11, Pin_12)
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, 0, 0, 0]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'Q1: Output of NOR gate 1'},
                    2: {'desc': 'A1: Input 1 of NOR gate 1'},
                    3: {'desc': 'B1: Input 2 of NOR gate 1'},
                    4: {'desc': 'C1: Input 3 of NOR gate 1'},
                    5: {'desc': 'D1: Input 4 of NOR gate 1'},
                    6: {'desc': 'NC'},
                    7: {'desc': 'GND'},
                    8: {'desc': 'NC'},
                    9: {'desc': 'D2: Input 4 of NOR gate 2'},
                    10: {'desc': 'C2: Input 3 of NOR gate 2'},
                    11: {'desc': 'B2: Input 2 of NOR gate 2'},
                    12: {'desc': 'A2: Input 1 of NOR gate 2'},
                    13: {'desc': 'Q2: Output of NOR gate 2'},
                    14: {'desc': 'VCC'}
                    })

    def run(self):
        output = {}
        output[1] = NOR(self.pins[2].value, self.pins[3].value,
                        self.pins[4].value, self.pins[5].value).output()
        output[13] = NOR(self.pins[9].value, self.pins[10].value,
                         self.pins[11].value, self.pins[12].value).output()
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            self.setIC(output)
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4011(Base_14pin):

    """
    Quad 2 input NAND gate
    Pin_3 = NAND(Pin_1, Pin_2)
    Pin_4 = NAND(Pin_5, Pin_6)
    Pin_10 = NAND(Pin_8, Pin_9)
    Pin_11 = NAND(Pin_12, Pin_13)
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'A1: Input 1 of NAND gate 1'},
                    2: {'desc': 'B1: Input 2 of NAND gate 1'},
                    3: {'desc': 'Q1: Output of NAND gate 1'},
                    4: {'desc': 'Q2: Output of NAND gate 2'},
                    5: {'desc': 'B2: Input 2 of NAND gate 2'},
                    6: {'desc': 'A2: Input 1 of NAND gate 2'},
                    7: {'desc': 'GND'},
                    8: {'desc': 'A3: Input 1 of NAND gate 3'},
                    9: {'desc': 'B3: Input 2 of NAND gate 3'},
                    10: {'desc': 'Q3: Output of NAND gate 3'},
                    11: {'desc': 'Q4: Output of NAND gate 4'},
                    12: {'desc': 'B4: Input 2 of NAND gate 4'},
                    13: {'desc': 'A4: Input 1 of NAND gate 4'},
                    14: {'desc': 'VCC'}
                    })

    def run(self):
        output = {}
        output[3] = NAND(self.pins[1].value, self.pins[2].value).output()
        output[4] = NAND(self.pins[5].value, self.pins[6].value).output()
        output[10] = NAND(self.pins[8].value, self.pins[9].value).output()
        output[11] = NAND(self.pins[12].value, self.pins[13].value).output()
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4012(Base_14pin):

    """
    Dual 4 input NAND gate
    Pin_1 = NAND(Pin_2, Pin_3, Pin_4, Pin_5)
    Pin_13 = NAND(Pin_9, Pin_10, Pin_11, Pin_12)
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, 0, 0, 0]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'Q1: Output of NAND gate 1'},
                    2: {'desc': 'A1: Input 1 of NAND gate 1'},
                    3: {'desc': 'B1: Input 2 of NAND gate 1'},
                    4: {'desc': 'C1: Input 3 of NAND gate 1'},
                    5: {'desc': 'D1: Input 4 of NAND gate 1'},
                    6: {'desc': 'NC'},
                    7: {'desc': 'GND'},
                    8: {'desc': 'NC'},
                    9: {'desc': 'D2: Input 4 of NAND gate 2'},
                    10: {'desc': 'C2: Input 3 of NAND gate 2'},
                    11: {'desc': 'B2: Input 2 of NAND gate 2'},
                    12: {'desc': 'A2: Input 1 of NAND gate 2'},
                    13: {'desc': 'Q2: Output of NAND gate 2'},
                    14: {'desc': 'VCC'}
                    })

    def run(self):
        output = {}
        output[1] = NAND(self.pins[2].value, self.pins[3].value,
                         self.pins[4].value, self.pins[5].value).output()
        output[13] = NAND(self.pins[9].value, self.pins[10].value,
                          self.pins[11].value, self.pins[12].value).output()
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4013(Base_14pin):

    """
    CMOS Dual D type Flip Flop
    """

    def __init__(self):
        self.pins = [None, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = False
        self.setIC({1: {'desc': 'Q1'},
                    2: {'desc': '~Q1'},
                    3: {'desc': 'CLK1'},
                    4: {'desc': 'RST1'},
                    5: {'desc': 'D1'},
                    6: {'desc': 'SET1'},
                    7: {'desc': 'GND'},
                    8: {'desc': 'SET2'},
                    9: {'desc': 'D2'},
                    10: {'desc': 'RST2'},
                    11: {'desc': 'CLK2'},
                    12: {'desc': '~Q2'},
                    13: {'desc': 'Q2'},
                    14: {'desc': 'VCC'}
                    })

    def run(self):
        output = {}
        if not (isinstance(self.pins[3], Clock) and
                isinstance(self.pins[11],
                           Clock)):
            raise Exception("Error: Invalid Clock Input")
        ff1 = DFlipFlop(self.pins[5], Connector(1), self.pins[3].A,
                        clear=self.pins[6], preset=self.pins[4])
        while True:
            if self.pins[3].A.state == 0:
                ff1.trigger()
                break
        while True:
            if self.pins[3].A.state == 1:
                ff1.trigger()
                break
        output[1] = ff1.state()[0]
        output[2] = ff1.state()[1]

        ff2 = DFlipFlop(self.pins[9], Connector(1), self.pins[11].A,
                        clear=self.pins[8], preset=self.pins[10])
        while True:
            if self.pins[11].A.state == 0:
                ff2.trigger()
                break
        while True:
            if self.pins[11].A.state == 1:
                ff2.trigger()
                break
        output[13] = ff2.state()[0]
        output[12] = ff2.state()[1]

        if self.pins[7] == 0 and self.pins[14] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4023(Base_14pin):

    """
    Triple 3 input NAND gate
    Pin_6 = NAND(Pin_3, Pin_4, Pin_5)
    Pin_9 = NAND(Pin_1, Pin_2, Pin_8)
    Pin_10 = NAND(Pin_11, Pin_12, Pin_13)
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'C2: Input 3 of NAND gate 2'},
                    2: {'desc': 'B2: Input 2 of NAND gate 2'},
                    3: {'desc': 'C1: Input 3 of NAND gate 1'},
                    4: {'desc': 'B1: Input 2 of NAND gate 1'},
                    5: {'desc': 'A1: Input 1 of NAND gate 1'},
                    6: {'desc': 'Q1: Output of NAND gate 1'},
                    7: {'desc': 'GND'},
                    8: {'desc': 'A2: Input 1 of NAND gate 2'},
                    9: {'desc': 'Q2: Output of NAND gate 2'},
                    10: {'desc': 'Q3: Output of NAND gate 3'},
                    11: {'desc': 'A3: Input 1 of NAND gate 3'},
                    12: {'desc': 'B3: Input 2 of NAND gate 3'},
                    13: {'desc': 'C3: Input 3 of NAND gate 3'},
                    14: {'desc': 'VCC'}
                    })

    def run(self):
        output = {}
        output[6] = NAND(self.pins[3].value, self.pins[4].value,
                         self.pins[5].value).output()
        output[9] = NAND(self.pins[1].value, self.pins[2].value,
                         self.pins[8].value).output()
        output[10] = NAND(self.pins[11].value, self.pins[12].value,
                          self.pins[13].value).output()
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4025(Base_14pin):

    """
    Triple 3 input NOR gate
    Pin_6 = NOR(Pin_3, Pin_4, Pin_5)
    Pin_9 = NOR(Pin_1, Pin_2, Pin_8)
    Pin_10 = NOR(Pin_11, Pin_12, Pin_13)
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'C2: Input 3 of NOR gate 2'},
                    2: {'desc': 'B2: Input 2 of NOR gate 2'},
                    3: {'desc': 'C1: Input 3 of NOR gate 1'},
                    4: {'desc': 'B1: Input 2 of NOR gate 1'},
                    5: {'desc': 'A1: Input 1 of NOR gate 1'},
                    6: {'desc': 'Q1: Output of NOR gate 1'},
                    7: {'desc': 'GND'},
                    8: {'desc': 'A2: Input 1 of NOR gate 2'},
                    9: {'desc': 'Q2: Output of NOR gate 2'},
                    10: {'desc': 'Q3: Output of NOR gate 3'},
                    11: {'desc': 'A3: Input 1 of NOR gate 3'},
                    12: {'desc': 'B3: Input 2 of NOR gate 3'},
                    13: {'desc': 'C3: Input 3 of NOR gate 3'},
                    14: {'desc': 'VCC'}
                    })

    def run(self):
        output = {}
        output[6] = NOR(self.pins[3].value, self.pins[4].value,
                        self.pins[5].value).output()
        output[9] = NOR(self.pins[1].value, self.pins[2].value,
                        self.pins[8].value).output()
        output[10] = NOR(self.pins[11].value, self.pins[12].value,
                         self.pins[13].value).output()
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4030(Base_14pin):

    """
    Quad 2-input XOR gate
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': '1A'},
                    2: {'desc': '1B'},
                    3: {'desc': '1Y'},
                    4: {'desc': '2Y'},
                    5: {'desc': '2A'},
                    6: {'desc': '2B'},
                    7: {'desc': 'GND'},
                    8: {'desc': '3A'},
                    9: {'desc': '3B'},
                    10: {'desc': '3Y'},
                    11: {'desc': '4Y'},
                    12: {'desc': '4A'},
                    13: {'desc': '4B'},
                    14: {'desc': 'VCC'}
                    })

    def run(self):
        output = {}
        output[3] = XOR(self.pins[1].value, self.pins[2].value).output()
        output[4] = XOR(self.pins[5].value, self.pins[6].value).output()
        output[10] = XOR(self.pins[8].value, self.pins[9].value).output()
        output[11] = XOR(self.pins[12].value, self.pins[13].value).output()
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4068(Base_14pin):

    """
    8 input NAND gate
    Pin_13 = NAND(Pin_2, Pin_3, Pin_4, Pin_5, Pin_9, Pin_10, Pin_11, Pin_12)
    """

    def __init__(self):
        self.pins = [None, None, 0, 0, 0, 0, None, 0, None, 0, 0, 0, 0, 0, 0]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'NC'},
                    2: {'desc': 'Input 1 of NAND gate'},
                    3: {'desc': 'Input 2 of NAND gate'},
                    4: {'desc': 'Input 3 of NAND gate'},
                    5: {'desc': 'Input 4 of NAND gate'},
                    6: {'desc': 'NC'},
                    7: {'desc': 'GND'},
                    8: {'desc': 'NC'},
                    9: {'desc': 'Input 5 of NAND gate'},
                    10: {'desc': 'Input 6 of NAND gate'},
                    11: {'desc': 'Input 7 of NAND gate'},
                    12: {'desc': 'Input 8 of NAND gate'},
                    13: {'desc': 'Output of NAND gate'},
                    14: {'desc': 'VCC'}
                    })

    def run(self):
        output = {}
        output[13] = NAND(self.pins[2].value, self.pins[3].value,
                          self.pins[4].value, self.pins[5].value,
                          self.pins[9].value, self.pins[10].value,
                          self.pins[11].value, self.pins[12].value).output()
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4069(Base_14pin):

    """
    Hex NOT gate
    Pin_2 = NOT(Pin_1)
    Pin_4 = NOT(Pin_3)
    Pin_6 = NOT(Pin_5)
    Pin_8 = NOT(Pin_9)
    Pin_10 = NOT(Pin_11)
    Pin_12 = NOT(Pin_13)
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'Input of NOT gate 1'},
                    2: {'desc': 'Output of NOT gate 1'},
                    3: {'desc': 'Input of NOT gate 2'},
                    4: {'desc': 'Output of NOT gate 2'},
                    5: {'desc': 'Input of NOT gate 3'},
                    6: {'desc': 'Output of NOT gate 3'},
                    7: {'desc': 'GND'},
                    8: {'desc': 'Output of NOT gate 4'},
                    9: {'desc': 'Input of NOT gate 4'},
                    10: {'desc': 'Output of NOT gate 5'},
                    11: {'desc': 'Input of NOT gate 5'},
                    12: {'desc': 'Output of NOT gate 6'},
                    13: {'desc': 'Input of NOT gate 6'},
                    14: {'desc': 'VCC'}
                    })

    def run(self):
        output = {}
        output[2] = NOT(self.pins[1].value).output()
        output[4] = NOT(self.pins[3].value).output()
        output[6] = NOT(self.pins[5].value).output()
        output[8] = NOT(self.pins[9].value).output()
        output[10] = NOT(self.pins[11].value).output()
        output[12] = NOT(self.pins[13].value).output()
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4070(Base_14pin):

    """
    Quad 2 input XOR gate
    Pin_3 = XOR(Pin_1, Pin_2)
    Pin_4 = XOR(Pin_5, Pin_6)
    Pin_10 = XOR(Pin_8, Pin_9)
    Pin_11 = XOR(Pin_12, Pin_13)
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'A1: Input 1 of XOR gate 1'},
                    2: {'desc': 'B1: Input 2 of XOR gate 1'},
                    3: {'desc': 'Q1: Output of XOR gate 1'},
                    4: {'desc': 'Q2: Output of XOR gate 2'},
                    5: {'desc': 'B2: Input 2 of XOR gate 2'},
                    6: {'desc': 'A2: Input 1 of XOR gate 2'},
                    7: {'desc': 'GND'},
                    8: {'desc': 'A3: Input 1 of XOR gate 3'},
                    9: {'desc': 'B3: Input 2 of XOR gate 3'},
                    10: {'desc': 'Q3: Output of XOR gate 3'},
                    11: {'desc': 'Q4: Output of XOR gate 4'},
                    12: {'desc': 'B4: Input 2 of XOR gate 4'},
                    13: {'desc': 'A4: Input 1 of XOR gate 4'},
                    14: {'desc': 'VCC'}
                    })

    def run(self):
        output = {}
        output[3] = XOR(self.pins[1].value, self.pins[2].value).output()
        output[4] = XOR(self.pins[5].value, self.pins[6].value).output()
        output[10] = XOR(self.pins[8].value, self.pins[9].value).output()
        output[11] = XOR(self.pins[12].value, self.pins[13].value).output()
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4071(Base_14pin):

    """
    Quad 2 input OR gate
    Pin_3 = OR(Pin_1, Pin_2)
    Pin_4 = OR(Pin_5, Pin_6)
    Pin_10 = OR(Pin_8, Pin_9)
    Pin_11 = OR(Pin_12, Pin_13)
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'A1: Input 1 of OR gate 1'},
                    2: {'desc': 'B1: Input 2 of OR gate 1'},
                    3: {'desc': 'Q1: Output of OR gate 1'},
                    4: {'desc': 'Q2: Output of OR gate 2'},
                    5: {'desc': 'B2: Input 2 of OR gate 2'},
                    6: {'desc': 'A2: Input 1 of OR gate 2'},
                    7: {'desc': 'GND'},
                    8: {'desc': 'A3: Input 1 of OR gate 3'},
                    9: {'desc': 'B3: Input 2 of OR gate 3'},
                    10: {'desc': 'Q3: Output of OR gate 3'},
                    11: {'desc': 'Q4: Output of OR gate 4'},
                    12: {'desc': 'B4: Input 2 of OR gate 4'},
                    13: {'desc': 'A4: Input 1 of OR gate 4'},
                    14: {'desc': 'VCC'}
                    })

    def run(self):
        output = {}
        output[3] = OR(self.pins[1].value, self.pins[2].value).output()
        output[4] = OR(self.pins[5].value, self.pins[6].value).output()
        output[10] = OR(self.pins[8].value, self.pins[9].value).output()
        output[11] = OR(self.pins[12].value, self.pins[13].value).output()
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4072(Base_14pin):

    """
    Dual 4 input OR gate
    Pin_1 = OR(Pin_2, Pin_3, Pin_4, Pin_5)
    Pin_13 = OR(Pin_9, Pin_10, Pin_11, Pin_12)
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, 0, 0, 0]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'Q1: Output of OR gate 1'},
                    2: {'desc': 'A1: Input 1 of OR gate 1'},
                    3: {'desc': 'B1: Input 2 of OR gate 1'},
                    4: {'desc': 'C1: Input 3 of OR gate 1'},
                    5: {'desc': 'D1: Input 4 of OR gate 1'},
                    6: {'desc': 'NC'},
                    7: {'desc': 'GND'},
                    8: {'desc': 'NC'},
                    9: {'desc': 'D2: Input 4 of OR gate 2'},
                    10: {'desc': 'C2: Input 3 of OR gate 2'},
                    11: {'desc': 'B2: Input 2 of OR gate 2'},
                    12: {'desc': 'A2: Input 1 of OR gate 2'},
                    13: {'desc': 'Q2: Output of OR gate 2'},
                    14: {'desc': 'VCC'}
                    })

    def run(self):
        output = {}
        output[1] = OR(self.pins[2].value, self.pins[3].value,
                       self.pins[4].value, self.pins[5].value).output()
        output[13] = OR(self.pins[9].value, self.pins[10].value,
                        self.pins[11].value, self.pins[12].value).output()
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4073(Base_14pin):

    """
    Triple 3 input AND gate
    Pin_6 = AND(Pin_3, Pin_4, Pin_5)
    Pin_9 = AND(Pin_1, Pin_2, Pin_8)
    Pin_10 = AND(Pin_11, Pin_12, Pin_13)
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'C2: Input 3 of AND gate 2'},
                    2: {'desc': 'B2: Input 2 of AND gate 2'},
                    3: {'desc': 'C1: Input 3 of AND gate 1'},
                    4: {'desc': 'B1: Input 2 of AND gate 1'},
                    5: {'desc': 'A1: Input 1 of AND gate 1'},
                    6: {'desc': 'Q1: Output of AND gate 1'},
                    7: {'desc': 'GND'},
                    8: {'desc': 'A2: Input 1 of AND gate 2'},
                    9: {'desc': 'Q2: Output of AND gate 2'},
                    10: {'desc': 'Q3: Output of AND gate 3'},
                    11: {'desc': 'A3: Input 1 of AND gate 3'},
                    12: {'desc': 'B3: Input 2 of AND gate 3'},
                    13: {'desc': 'C3: Input 3 of AND gate 3'},
                    14: {'desc': 'VCC'}
                    })

    def run(self):
        output = {}
        output[6] = AND(self.pins[3].value, self.pins[4].value,
                        self.pins[5].value).output()
        output[9] = AND(self.pins[1].value, self.pins[2].value,
                        self.pins[8].value).output()
        output[10] = AND(self.pins[11].value, self.pins[12].value,
                         self.pins[13].value).output()
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4075(Base_14pin):

    """
    Triple 3 input OR gate
    Pin_6 = OR(Pin_3, Pin_4, Pin_5)
    Pin_9 = OR(Pin_1, Pin_2, Pin_8)
    Pin_10 = OR(Pin_11, Pin_12, Pin_13)
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'C2: Input 3 of OR gate 2'},
                    2: {'desc': 'B2: Input 2 of OR gate 2'},
                    3: {'desc': 'C1: Input 3 of OR gate 1'},
                    4: {'desc': 'B1: Input 2 of OR gate 1'},
                    5: {'desc': 'A1: Input 1 of OR gate 1'},
                    6: {'desc': 'Q1: Output of OR gate 1'},
                    7: {'desc': 'GND'},
                    8: {'desc': 'A2: Input 1 of OR gate 2'},
                    9: {'desc': 'Q2: Output of OR gate 2'},
                    10: {'desc': 'Q3: Output of OR gate 3'},
                    11: {'desc': 'A3: Input 1 of OR gate 3'},
                    12: {'desc': 'B3: Input 2 of OR gate 3'},
                    13: {'desc': 'C3: Input 3 of OR gate 3'},
                    14: {'desc': 'VCC'}
                    })

    def run(self):
        output = {}
        output[6] = OR(self.pins[3].value, self.pins[4].value,
                       self.pins[5].value).output()
        output[9] = OR(self.pins[1].value, self.pins[2].value,
                       self.pins[8].value).output()
        output[10] = OR(self.pins[11].value, self.pins[12].value,
                        self.pins[13].value).output()
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4077(Base_14pin):

    """
    Quad 2 input XNOR gate
    Pin_3 = XNOR(Pin_1, Pin_2)
    Pin_4 = XNOR(Pin_5, Pin_6)
    Pin_10 = XNOR(Pin_8, Pin_9)
    Pin_11 = XNOR(Pin_12, Pin_13)
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'A1: Input 1 of XNOR gate 1'},
                    2: {'desc': 'B1: Input 2 of XNOR gate 1'},
                    3: {'desc': 'Q1: Output of XNOR gate 1'},
                    4: {'desc': 'Q2: Output of XNOR gate 2'},
                    5: {'desc': 'B2: Input 2 of XNOR gate 2'},
                    6: {'desc': 'A2: Input 1 of XNOR gate 2'},
                    7: {'desc': 'GND'},
                    8: {'desc': 'A3: Input 1 of XNOR gate 3'},
                    9: {'desc': 'B3: Input 2 of XNOR gate 3'},
                    10: {'desc': 'Q3: Output of XNOR gate 3'},
                    11: {'desc': 'Q4: Output of XNOR gate 4'},
                    12: {'desc': 'B4: Input 2 of XNOR gate 4'},
                    13: {'desc': 'A4: Input 1 of XNOR gate 4'},
                    14: {'desc': 'VCC'}
                    })

    def run(self):
        output = {}
        output[3] = XNOR(self.pins[1].value, self.pins[2].value).output()
        output[4] = XNOR(self.pins[5].value, self.pins[6].value).output()
        output[10] = XNOR(self.pins[8].value, self.pins[9].value).output()
        output[11] = XNOR(self.pins[12].value, self.pins[13].value).output()
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4078(Base_14pin):

    """
    8 input NOR gate
    Pin_13 = NOR(Pin_2, Pin_3, Pin_4, Pin_5, Pin_9, Pin_10, Pin_11, Pin_12)
    """

    def __init__(self):
        self.pins = [None, None, 0, 0, 0, 0, None, 0, None, 0, 0, 0, 0, 0, 0]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'NC'},
                    2: {'desc': 'Input 1 of NOR gate'},
                    3: {'desc': 'Input 2 of NOR gate'},
                    4: {'desc': 'Input 3 of NOR gate'},
                    5: {'desc': 'Input 4 of NOR gate'},
                    6: {'desc': 'NC'},
                    7: {'desc': 'GND'},
                    8: {'desc': 'NC'},
                    9: {'desc': 'Input 5 of NOR gate'},
                    10: {'desc': 'Input 6 of NOR gate'},
                    11: {'desc': 'Input 7 of NOR gate'},
                    12: {'desc': 'Input 8 of NOR gate'},
                    13: {'desc': 'Output of NOR gate'},
                    14: {'desc': 'VCC'}
                    })

    def run(self):
        output = {}
        output[13] = NOR(self.pins[2].value, self.pins[3].value,
                         self.pins[4].value, self.pins[5].value,
                         self.pins[9].value, self.pins[10].value,
                         self.pins[11].value, self.pins[12].value).output()
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4081(Base_14pin):

    """
    Quad 2 input AND gate
    Pin_3 = AND(Pin_1, Pin_2)
    Pin_4 = AND(Pin_5, Pin_6)
    Pin_10 = AND(Pin_8, Pin_9)
    Pin_11 = AND(Pin_12, Pin_13)
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'A1: Input 1 of AND gate 1'},
                    2: {'desc': 'B1: Input 2 of AND gate 1'},
                    3: {'desc': 'Q1: Output of AND gate 1'},
                    4: {'desc': 'Q2: Output of AND gate 2'},
                    5: {'desc': 'B2: Input 2 of AND gate 2'},
                    6: {'desc': 'A2: Input 1 of AND gate 2'},
                    7: {'desc': 'GND'},
                    8: {'desc': 'A3: Input 1 of AND gate 3'},
                    9: {'desc': 'B3: Input 2 of AND gate 3'},
                    10: {'desc': 'Q3:Output of AND gate 3'},
                    11: {'desc': 'Q4:Output of AND gate 4'},
                    12: {'desc': 'B4: Input 2 of AND gate 4'},
                    13: {'desc': 'A4: Input 1 of AND gate 4'},
                    14: {'desc': 'VCC'}
                    })

    def run(self):
        output = {}
        output[3] = AND(self.pins[1].value, self.pins[2].value).output()
        output[4] = AND(self.pins[5].value, self.pins[6].value).output()
        output[10] = AND(self.pins[8].value, self.pins[9].value).output()
        output[11] = AND(self.pins[12].value, self.pins[13].value).output()
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4082(Base_14pin):

    """
    Dual 4 input AND gate
    Pin_1 = AND(Pin_2, Pin_3, Pin_4, Pin_5)
    Pin_13 = AND(Pin_9, Pin_10, Pin_11, Pin_12)
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, 0, 0, 0]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'Q1: Output of AND gate 1'},
                    2: {'desc': 'A1: Input 1 of AND gate 1'},
                    3: {'desc': 'B1: Input 2 of AND gate 1'},
                    4: {'desc': 'C1: Input 3 of AND gate 1'},
                    5: {'desc': 'D1: Input 4 of AND gate 1'},
                    6: {'desc': 'NC'},
                    7: {'desc': 'GND'},
                    8: {'desc': 'NC'},
                    9: {'desc': 'D2: Input 4 of AND gate 2'},
                    10: {'desc': 'C2: Input 3 of AND gate 2'},
                    11: {'desc': 'B2: Input 2 of AND gate 2'},
                    12: {'desc': 'A2: Input 1 of AND gate 2'},
                    13: {'desc': 'Q2: Output of AND gate 2'},
                    14: {'desc': 'VCC'}
                    })

    def run(self):
        output = {}
        output[1] = AND(self.pins[2].value, self.pins[3].value,
                        self.pins[4].value, self.pins[5].value).output()
        output[13] = AND(self.pins[9].value, self.pins[10].value,
                         self.pins[11].value, self.pins[12].value).output()
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:

            print ("Ground and VCC pins have not been configured correctly.")

#################################
# IC's with 16 pins
#################################


class IC_4008(Base_16pin):

    """
    4 Bit Binary Full Adder
    """

    def __init__(self):
        self.pins = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None,
                     None, 0, 0]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'A3'},
                    2: {'desc': 'B2'},
                    3: {'desc': 'A2'},
                    4: {'desc': 'B1'},
                    5: {'desc': 'A1'},
                    6: {'desc': 'B0'},
                    7: {'desc': 'A0'},
                    8: {'desc': 'VSS'},
                    9: {'desc': 'C0'},
                    10: {'desc': 'S0'},
                    11: {'desc': 'S1'},
                    12: {'desc': 'S2'},
                    13: {'desc': 'S3'},
                    14: {'desc': 'C4'},
                    15: {'desc': 'B3'},
                    16: {'desc': 'VDD'},
                    })

    def run(self):
        output = {}
        ff = FullAdder(self.pins[7].value, self.pins[6].value,
                       self.pins[9].value).output()
        output[10] = ff[0]
        ff = FullAdder(self.pins[5].value, self.pins[4].value, ff[1]).output()
        output[11] = ff[0]
        ff = FullAdder(self.pins[3].value, self.pins[2].value, ff[1]).output()
        output[12] = ff[0]
        ff = FullAdder(self.pins[1].value, self.pins[15].value, ff[1]).output()
        output[13] = ff[0]
        output[14] = ff[1]

        if self.pins[8].value == 0 and self.pins[16].value == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4009(Base_16pin):

    """
    Hex Inverter with Level Shifted output
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
            0,
            0,
            None,
            0,
            None,
            0,
            0,
            None,
            1]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'VCC'},
                    2: {'desc': 'Y1'},
                    3: {'desc': 'A1'},
                    4: {'desc': 'Y2'},
                    5: {'desc': 'A2'},
                    6: {'desc': 'Y3'},
                    7: {'desc': 'A3'},
                    8: {'desc': 'VSS'},
                    9: {'desc': 'A4'},
                    10: {'desc': 'Y4'},
                    11: {'desc': 'A5'},
                    12: {'desc': 'Y5'},
                    13: {'desc': ''},
                    14: {'desc': 'A6'},
                    15: {'desc': 'Y6'},
                    16: {'desc': 'VDD'},
                    })

    def run(self):
        output = {}
        output[2] = NOT(self.pins[3].value).output()
        output[4] = NOT(self.pins[5].value).output()
        output[6] = NOT(self.pins[7].value).output()
        output[10] = NOT(self.pins[9].value).output()
        output[12] = NOT(self.pins[11].value).output()
        output[15] = NOT(self.pins[14].value).output()

        if self.pins[8].value == 0 and self.pins[16].value == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4010(Base_16pin):

    """
    Hex Buffer with Level Shifted output
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
            0,
            0,
            None,
            0,
            None,
            0,
            0,
            None,
            1]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        self.setIC({1: {'desc': 'VCC'},
                    2: {'desc': 'Y1'},
                    3: {'desc': 'A1'},
                    4: {'desc': 'Y2'},
                    5: {'desc': 'A2'},
                    6: {'desc': 'Y3'},
                    7: {'desc': 'A3'},
                    8: {'desc': 'VSS'},
                    9: {'desc': 'A4'},
                    10: {'desc': 'Y4'},
                    11: {'desc': 'A5'},
                    12: {'desc': 'Y5'},
                    13: {'desc': ''},
                    14: {'desc': 'A6'},
                    15: {'desc': 'Y6'},
                    16: {'desc': 'VDD'},
                    })

    def run(self):
        output = {}
        output[2] = self.pins[3].value
        output[4] = self.pins[5].value
        output[6] = self.pins[7].value
        output[10] = self.pins[9].value
        output[12] = self.pins[11].value
        output[15] = self.pins[14].value

        if self.pins[8].value == 0 and self.pins[16].value == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4015(Base_16pin):

    """
    Dual 4 Stage static shift Register
    """

    def __init__(self):
        self.pins = [None, 0, None, None, None, None, 0, 0, 0, 0, None, None,
                     None, None, 0, 0, 0]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = False
        self.setIC({1: {'desc': 'CLKB'},
                    2: {'desc': 'Q4'},
                    3: {'desc': 'Q3'},
                    4: {'desc': 'Q2'},
                    5: {'desc': 'Q1'},
                    6: {'desc': 'RST1'},
                    7: {'desc': 'DA'},
                    8: {'desc': 'VSS'},
                    9: {'desc': 'CLKA'},
                    10: {'desc': 'Q4'},
                    11: {'desc': 'Q3'},
                    12: {'desc': 'Q2'},
                    13: {'desc': 'Q1'},
                    14: {'desc': 'RSTB'},
                    15: {'desc': 'DB'},
                    16: {'desc': 'VDD'}

                    })

    def run(self):
        output = {}
        if not (isinstance(self.pins[1], Clock) and
                isinstance(self.pins[9], Clock)):
            raise Exception("Error: Invalid Clock Input")
        sr1 = ShiftRegister([self.pins[7],
                             self.pins[4],
                             self.pins[3],
                             self.pins[2]],
                            self.pins[1],
                            NOT(self.pins[6]).output())
        sr2 = ShiftRegister([self.pins[15],
                             self.pins[12],
                             self.pins[11],
                             self.pins[10]],
                            self.pins[9],
                            NOT(self.pins[14]).output())
        sr1 = sr1.output()
        output[5] = sr1[0]
        output[4] = sr1[1]
        output[3] = sr1[2]
        output[2] = sr1[3]
        sr2 = sr2.output()
        output[13] = sr2[0]
        output[12] = sr2[1]
        output[11] = sr2[2]
        output[10] = sr2[3]

        if self.pins[8] == 0 and self.pins[16] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4017(Base_16pin):

    """
    CMOS Counters
    """

    def __init__(self):
        self.pins = [None, None, None, None, None, None, None, None, 0, None,
                     None, None, None, 0, 0, 0, 1]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = False
        self.setIC({1: {'desc': '5'},
                    2: {'desc': '1'},
                    3: {'desc': '0'},
                    4: {'desc': '2'},
                    5: {'desc': '6'},
                    6: {'desc': '7'},
                    7: {'desc': '3'},
                    8: {'desc': 'VSS'},
                    9: {'desc': '8'},
                    10: {'desc': '4'},
                    11: {'desc': '9'},
                    12: {'desc': 'carry'},
                    13: {'desc': 'CLKI'},
                    14: {'desc': 'CLK'},
                    15: {'desc': 'RST'},
                    16: {'desc': 'VDD'}

                    })
        self.step = 0

    def run(self):
        output = {}
        if not (isinstance(self.pins[13], Clock) and
                isinstance(self.pins[14], Clock)):
            raise Exception("Error: Invalid Clock Input")
        counter = DecadeCounter(self.pins[14].A,
                                clear=Connector(NOT(self.pins[15]).output()))
        for i in range(self.step):
            counter.trigger()
        self.step += 1
        out = list(map(str, counter.state()))
        out = ''.join(out)
        out = int(out, 2)
        if out <= 4:
            output[12] = 1
        else:
            output[12] = 0
        for i in range(1, 12):
            output[i] = 0

        if out == 5:
            output[1] = 1
        elif out == 1:
            output[2] = 1
        elif out == 0:
            output[3] = 1
        elif out == 2:
            output[4] = 1
        elif out == 6:
            output[5] = 1
        elif out == 7:
            output[6] = 1
        elif out == 3:
            output[7] = 1
        elif out == 8:
            output[9] = 1
        elif out == 4:
            output[10] = 1
        elif out == 9:
            output[11] = 1

        if self.pins[8] == 0 and self.pins[16] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4019(Base_16pin):

    """
    8-to-4 line non-inverting data selector/multiplexer with OR function
    """

    def __init__(self):
        self.pins = [None, None, None, None, None, None, None, None, 0, None,
                     None, None, None, 0, 0, 0, 1]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = False
        self.setIC({1: {'desc': '4A1'},
                    2: {'desc': '3A0'},
                    3: {'desc': '3A1'},
                    4: {'desc': '2A0'},
                    5: {'desc': '2A1'},
                    6: {'desc': '1A0'},
                    7: {'desc': '1A1'},
                    8: {'desc': 'GND'},
                    9: {'desc': 'S0'},
                    10: {'desc': 'Y1'},
                    11: {'desc': 'Y2'},
                    12: {'desc': 'Y3'},
                    13: {'desc': 'Y4'},
                    14: {'desc': 'S1'},
                    15: {'desc': '4A0'},
                    16: {'desc': 'VCC'}

                    })

    def run(self):
        output = {}
        output[10] = OR(AND(self.pins[9], self.pins[6]).output(),
                        AND(self.pins[14], self.pins[7]).output()).output()

        output[11] = OR(AND(self.pins[9], self.pins[4]).output(),
                        AND(self.pins[14], self.pins[5]).output()).output()
        output[12] = OR(AND(self.pins[9], self.pins[2]).output(),
                        AND(self.pins[14], self.pins[3]).output()).output()

        output[13] = OR(AND(self.pins[9], self.pins[1]).output(),
                        AND(self.pins[14], self.pins[15]).output()).output()

        if self.pins[8] == 0 and self.pins[16] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4020(Base_16pin):

    """
    CMOS 14 BIT asynchornous binary counter with reset
    """

    def __init__(self):
        self.pins = [None, None, None, None, None, None, None, None, 0, None,
                     0, 0, None, None, None, None, 1]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = False
        self.setIC({1: {'desc': 'Q11'},
                    2: {'desc': 'Q12'},
                    3: {'desc': 'Q13'},
                    4: {'desc': 'Q5'},
                    5: {'desc': 'Q4'},
                    6: {'desc': 'Q6'},
                    7: {'desc': 'Q3'},
                    8: {'desc': 'VSS'},
                    9: {'desc': 'Q0'},
                    10: {'desc': 'CLK'},
                    11: {'desc': 'RST'},
                    12: {'desc': 'Q8'},
                    13: {'desc': 'Q7'},
                    14: {'desc': 'Q9'},
                    15: {'desc': 'Q10'},
                    16: {'desc': 'VCC'}

                    })
        self.step = 0

    def run(self):
        output = {}
        if not (isinstance(self.pins[10], Clock)):
            raise Exception("Error: Invalid Clock Input")
        counter = Stage14Counter(self.pins[10].A,
                                 clear=Connector(NOT(self.pins[11]).output()))
        for i in range(self.step):
            counter.trigger()
        self.step += 1
        out = list(map(str, counter.state()))
        out = ''.join(out)
        out = int(out, 2)
        for i in range(1, 16):
            if i != 10 and i != 11:
                output[i] = 0

        if out == 11:
            output[1] = 1
        elif out == 12:
            output[2] = 1
        elif out == 13:
            output[3] = 1
        elif out == 5:
            output[4] = 1
        elif out == 4:
            output[5] = 1
        elif out == 6:
            output[6] = 1
        elif out == 3:
            output[7] = 1
        elif out == 0:
            output[9] = 1
        elif out == 8:
            output[12] = 1
        elif out == 7:
            output[13] = 1
        elif out == 9:
            output[14] = 1
        elif out == 10:
            output[15] = 1

        if self.pins[8] == 0 and self.pins[16] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4022(Base_16pin):

    """
    CMOS Octal Counter
    """

    def __init__(self):
        self.pins = [None, None, None, None, None, None, None, None, 0, None,
                     None, None, None, 0, 0, 0, 1]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = False
        self.setIC({1: {'desc': '1'},
                    2: {'desc': '0'},
                    3: {'desc': '2'},
                    4: {'desc': '5'},
                    5: {'desc': '6'},
                    6: {'desc': ''},
                    7: {'desc': '3'},
                    8: {'desc': 'VSS'},
                    9: {'desc': ''},
                    10: {'desc': '7'},
                    11: {'desc': '4'},
                    12: {'desc': 'carry'},
                    13: {'desc': 'CLKI'},
                    14: {'desc': 'CLK'},
                    15: {'desc': 'RST'},
                    16: {'desc': 'VDD'}

                    })
        self.step = 0

    def run(self):
        output = {}
        if not (isinstance(self.pins[13], Clock) and
                isinstance(self.pins[14], Clock)):
            raise Exception("Error: Invalid Clock Input")
        counter = OctalCounter(self.pins[14].A,
                               clear=Connector(NOT(self.pins[15]).output()))
        for i in range(self.step):
            counter.trigger()
        self.step += 1
        out = list(map(str, counter.state()))
        out = ''.join(out)
        out = int(out, 2)
        if out <= 3:
            output[12] = 1
        else:
            output[12] = 0
        for i in range(1, 12):
            output[i] = 0

        if out == 5:
            output[4] = 1
        elif out == 1:
            output[1] = 1
        elif out == 0:
            output[2] = 1
        elif out == 2:
            output[3] = 1
        elif out == 6:
            output[5] = 1
        elif out == 7:
            output[10] = 1
        elif out == 3:
            output[7] = 1
        elif out == 4:
            output[11] = 1

        if self.pins[8] == 0 and self.pins[16] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4027(Base_16pin):

    """
    Dual JK flip flops with set and reset
    """

    def __init__(self):
        self.pins = [None, None, None, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, None, None, 1]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = False
        self.setIC({1: {'desc': 'Q1'},
                    2: {'desc': '~Q1'},
                    3: {'desc': 'CLK1'},
                    4: {'desc': 'RST1'},
                    5: {'desc': 'K1'},
                    6: {'desc': 'J1'},
                    7: {'desc': 'SET1'},
                    8: {'desc': 'GND'},
                    9: {'desc': 'SET2'},
                    10: {'desc': 'J2'},
                    11: {'desc': 'K2'},
                    12: {'desc': 'RST2'},
                    13: {'desc': 'CLK2'},
                    14: {'desc': '~Q2'},
                    15: {'desc': 'Q2'},
                    16: {'desc': 'VCC'}

                    })

    def run(self):
        output = {}
        if not (isinstance(self.pins[13], Clock) and
                isinstance(self.pins[3], Clock)):
            raise Exception("Error: Invalid Clock Input")
        ff1 = JKFlipFlop(self.pins[6], self.pins[5], Connector(1),
                         self.pins[3].A, self.pins[4], self.pins[7])

        ff2 = JKFlipFlop(self.pins[10], self.pins[11], Connector(1),
                         self.pins[13].A, self.pins[12], self.pins[9])
        while True:
            if self.pins[3].A.state == 1:
                ff1.trigger()
                break

        while True:
            if self.pins[3].A.state == 0:
                ff1.trigger()
                break
        output[1], output[2] = ff1.state()
        while True:
            if self.pins[13].A.state == 1:
                ff2.trigger()
                break

        while True:
            if self.pins[13].A.state == 1:
                ff2.trigger()
                break
        output[15], output[14] = ff2.state()

        if self.pins[8] == 0 and self.pins[16] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4028(Base_16pin):

    """
    1-of-10 no-inverting decoder/demultiplexer
    """

    def __init__(self):
        self.pins = [None, None, None, None, None, None, None, None, 0, None,
                     0, 0, 0, 0, None, None, 1]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = False
        self.setIC({1: {'desc': 'Y4'},
                    2: {'desc': 'Y2'},
                    3: {'desc': 'Y0'},
                    4: {'desc': 'Y7'},
                    5: {'desc': 'Y9'},
                    6: {'desc': 'Y5'},
                    7: {'desc': 'Y6'},
                    8: {'desc': 'GND'},
                    9: {'desc': 'Y8'},
                    10: {'desc': 'S0'},
                    11: {'desc': 'S3'},
                    12: {'desc': 'S2'},
                    13: {'desc': 'S1'},
                    14: {'desc': 'Y1'},
                    15: {'desc': 'Y3'},
                    16: {'desc': 'VCC'}

                    })

    def run(self):
        output = {}
        d = DEMUX(1)
        d.selectLines(self.pins[10], self.pins[13], self.pins[12],
                      self.pins[11])
        d = d.output()[:10]
        output[1] = d[4]
        output[2] = d[2]
        output[3] = d[0]
        output[4] = d[7]
        output[5] = d[9]
        output[6] = d[5]
        output[7] = d[6]
        output[9] = d[8]
        output[14] = d[1]
        output[15] = d[3]

        if self.pins[8] == 0 and self.pins[16] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")


class IC_4029(Base_16pin):

    """
    4-bit synchronous binary/decade up/down counter
    """

    def __init__(self):
        self.pins = [0, 0, None, 0, 0, 0, None, 0, 0, None,
                     0, None, 0, 0, None, 0, 1]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = False
        """
      self.setIC({1: {'desc': 'Y4'},
                    2: {'desc': 'Y2'},
                    3: {'desc': 'Y0'},
                    4: {'desc': 'Y7'},
                    5: {'desc': 'Y9'},
                    6: {'desc': 'Y5'},
                    7: {'desc': 'Y6'},
                    8: {'desc': 'GND'},
                    9: {'desc': 'Y8'},
                    10: {'desc': 'S0'},
                    11: {'desc': 'S3'},
                    12: {'desc': 'S2'},
                    13: {'desc': 'S1'},
                    14: {'desc': 'Y1'},
                    15: {'desc': 'Y3'},
                    16: {'desc': 'VCC'}

                    })
        """
        self.steps = 0
        self.state = [0, 0, 0, 0]

    def run(self):
        output = {}

        if not isinstance(self.pins[15], Clock):
            raise Exception("Error: Invalid Clock Input")
        c = BinaryCounter(4, self.pins[15].A)
        while self.arraytoint(self.state) != self.arraytoint(c.trigger()):
            pass

        if self.pins[1] == 1:
            preset = self.arraytoint(self.pins[4], self.pins[12],
                                     self.pins[13], self.pins[3])
            while preset != self.arraytoint(c.trigger()):
                pass

        if self.pins[10] == 1:
            if self.pins[9] == 1:
                output[6], output[11], output[14], output[2] = c.trigger()
                self.state = c.state()
                if self.arraytoint(self.state) == 15:
                    output[7] = 1
            elif self.pins[9] == 0:
                arr = c.trigger()
                output[6], output[11], output[14], output[2] = arr
                self.state = arr
                if self.arraytoint(arr) == 10:
                    self.state = [0, 0, 0, 0]
                    output[6], output[11], output[14], output[2] = [0, 0, 0, 0]

        elif self.pins[10] == 0:
            if self.pins[9] == 0:
                d = NBitDownCounter(4, self.pins[15].A)
                while self.arraytoint(self.state) != self.arraytoint(d.trigger()):
                    pass
                arr = d.trigger()
                output[6], output[11], output[14], output[2] = arr
                self.state = arr
                if self.arraytoint(arr) > 10:
                    self.state = [1, 0, 0, 1]
                    output[6], output[11], output[14], output[2] = [1, 0, 0, 1]
            elif self.pins[9] == 1:
                d = NBitDownCounter(4, self.pins[15].A)
                while self.arraytoint(self.state) != self.arraytoint(d.trigger()):
                    pass
                arr = d.trigger()
                output[6], output[11], output[14], output[2] = arr
                self.state = arr
                if self.arraytoint(arr) == 0:
                    output[7] = 0

        if self.pins[8] == 0 and self.pins[16] == 1:
            self.setIC(output)
            for i in self.outputConnector:
                self.outputConnector[i].state = output[i]
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")

    def arraytoint(self, inputs):
        inputs = list(map(str, inputs))
        inputs = ''.join(inputs)
        inputs = int(inputs, 2)
        return inputs
