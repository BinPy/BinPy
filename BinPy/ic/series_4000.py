"""
This module has all the classes of ICs belonging to 4000 series.

Please note that the length of list self.pins is 1 more than the number of actual pins. This is so because pin0
is not used as a general term referring to the first pin of the IC. Zeroth index of the self.pins is not being used.
"""

from BinPy import *
from base import *

######## IC's with 14 pins #################################

class IC_4000(Base_14pin):
    """
    Dual 3 Input NOR gate + one NOT gate IC.
    Pin_6 = NOR(Pin_3, Pin_4, Pin_5)
    Pin_10 = NOR(Pin_11, Pin_12, Pin_13)
    Pin_9 = NOT(Pin_8)
    """
    def __init__(self):
        self.pins = [None,None,None,0,0,0,0,0,0,0,0,0,0,0,0]
    
    def run(self):
        output = {}
        output[6] = NOR(self.pins[3],self.pins[4],self.pins[5]).output()
        output[10] = NOR(self.pins[11],self.pins[12],self.pins[13]).output()
        output[9] = NOT(self.pins[8]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."
            

class IC_4001(Base_14pin):
    """
    Quad 2 input NOR gate
    Pin_3 = NOR(Pin_1, Pin_2)
    Pin_4 = NOR(Pin_5, Pin_6)
    Pin_10 = NOR(Pin_8, Pin_9)
    Pin_11 = NOR(Pin_12, Pin_13)
    """
    def __init__(self):
        self.pins = [None,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    def run(self):
        output = {}
        output[3] = NOR(self.pins[1],self.pins[2]).output()
        output[4] = NOR(self.pins[5],self.pins[6]).output()
        output[10] = NOR(self.pins[8],self.pins[9]).output()
        output[11] = NOR(self.pins[12],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


class IC_4002(Base_14pin):
    """
    Dual 4 input NOR gate
    Pin_1 = NOR(Pin_2, Pin_3, Pin_4, Pin_5)
    Pin_13 = NOR(Pin_9, Pin_10, Pin_11, Pin_12)    
    """
    def __init__(self):
        self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,0,0,0]
    
    def run(self):
        output = {}
        output[1] = NOR(self.pins[2],self.pins[3],self.pins[4],self.pins[5]).output()
        output[13] = NOR(self.pins[9],self.pins[10],self.pins[11],self.pins[12]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


class IC_4011(Base_14pin):
    """
    Quad 2 input NAND gate
    Pin_3 = NAND(Pin_1, Pin_2)
    Pin_4 = NAND(Pin_5, Pin_6)
    Pin_10 = NAND(Pin_8, Pin_9)
    Pin_11 = NAND(Pin_12, Pin_13)
    """
    def __init__(self):
        self.pins = [None,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    def run(self):
        output = {}
        output[3] = NAND(self.pins[1],self.pins[2]).output()
        output[4] = NAND(self.pins[5],self.pins[6]).output()
        output[10] = NAND(self.pins[8],self.pins[9]).output()
        output[11] = NAND(self.pins[12],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


class IC_4012(Base_14pin):
    """
    Dual 4 input NAND gate
    Pin_1 = NAND(Pin_2, Pin_3, Pin_4, Pin_5)
    Pin_13 = NAND(Pin_9, Pin_10, Pin_11, Pin_12)    
    """
    def __init__(self):
        self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,0,0,0]
    
    def run(self):
        output = {}
        output[1] = NAND(self.pins[2],self.pins[3],self.pins[4],self.pins[5]).output()
        output[13] = NAND(self.pins[9],self.pins[10],self.pins[11],self.pins[12]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."
            

class IC_4023(Base_14pin):
    """
    Triple 3 input NAND gate
    Pin_6 = NAND(Pin_3, Pin_4, Pin_5)
    Pin_9 = NAND(Pin_1, Pin_2, Pin_8)
    Pin_10 = NAND(Pin_11, Pin_12, Pin_13)
    """
    def __init__(self):
        self.pins = [None,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    def run(self):
        output = {}
        output[6] = NAND(self.pins[3],self.pins[4],self.pins[5]).output()
        output[9] = NAND(self.pins[1],self.pins[2],self.pins[8]).output()
        output[10] = NAND(self.pins[11],self.pins[12],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


class IC_4025(Base_14pin):
    """
    Triple 3 input NOR gate
    Pin_6 = NOR(Pin_3, Pin_4, Pin_5)
    Pin_9 = NOR(Pin_1, Pin_2, Pin_8)
    Pin_10 = NOR(Pin_11, Pin_12, Pin_13)
    """
    def __init__(self):
        self.pins = [None,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    def run(self):
        output = {}
        output[6] = NOR(self.pins[3],self.pins[4],self.pins[5]).output()
        output[9] = NOR(self.pins[1],self.pins[2],self.pins[8]).output()
        output[10] = NOR(self.pins[11],self.pins[12],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


class IC_4068(Base_14pin):
    """
    8 input NAND gate
    Pin_13 = NAND(Pin_2, Pin_3, Pin_4, Pin_5, Pin_9, Pin_10, Pin_11, Pin_12)
    """
    def __init__(self):
        self.pins = [None,None,0,0,0,0,None,0,None,0,0,0,0,0,0]
    
    def run(self):
        output = {}
        output[13] = NAND(self.pins[2],self.pins[3],self.pins[4],
                          self.pins[5],self.pins[9],self.pins[10],
                          self.pins[11],self.pins[12]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


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
        self.pins = [None,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    def run(self):
        output = {}
        output[2] = NOT(self.pins[1]).output()
        output[4] = NOT(self.pins[3]).output()
        output[6] = NOT(self.pins[5]).output()
        output[8] = NOT(self.pins[9]).output()
        output[10] = NOT(self.pins[11]).output()
        output[12] = NOT(self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


class IC_4070(Base_14pin):
    """
    Quad 2 input XOR gate
    Pin_3 = XOR(Pin_1, Pin_2)
    Pin_4 = XOR(Pin_5, Pin_6)
    Pin_10 = XOR(Pin_8, Pin_9)
    Pin_11 = XOR(Pin_12, Pin_13)
    """
    def __init__(self):
        self.pins = [None,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    def run(self):
        output = {}
        output[3] = XOR(self.pins[1],self.pins[2]).output()
        output[4] = XOR(self.pins[5],self.pins[6]).output()
        output[10] = XOR(self.pins[8],self.pins[9]).output()
        output[11] = XOR(self.pins[12],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

