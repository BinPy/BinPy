"""
This module has all the classes of ICs belonging to 7400 series.

Please note that the length of list self.pins is 1 more than the number of actual pins. This is so because pin0
is not used as a general term referring to the first pin of the IC. Zeroth index of the self.pins is not being used.
"""

from BinPy import *
from base import *

######## IC's with 14 pins #################################

class IC_7400(Base_14pin):
    """
    This is a Quad 2 Input NAND gate IC
    """
    def __init__(self):
        self.pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]
    
    def run(self):
        output = {}
        output[3] = NAND(self.pins[1],self.pins[2]).output()
        output[6] = NAND(self.pins[4],self.pins[5]).output()
        output[8] = NAND(self.pins[9],self.pins[10]).output()
        output[11] =NAND(self.pins[12],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7401(Base_14pin):
    """
    This is a Quad 2-input open-collector NAND gate IC
    """
    def __init__(self):
        self.pins = [None,None,0,0,None,0,0,0,0,0,None,0,0,None,0]
    
    def run(self):
        output = {}
        output[1] = NAND(self.pins[2],self.pins[3]).output()
        output[4] = NAND(self.pins[5],self.pins[6]).output()
        output[10] = NAND(self.pins[8],self.pins[9]).output()
        output[13] =NAND(self.pins[11],self.pins[12]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7402(Base_14pin):
    """
    This is a Quad 2-input NOR gate IC
    """
    def __init__(self):
        self.pins = [None,None,0,0,None,0,0,0,0,0,None,0,0,None,0]
    
    def run(self):
        output = {}
        output[1] = NOR(self.pins[2],self.pins[3]).output()
        output[4] = NOR(self.pins[5],self.pins[6]).output()
        output[10] = NOR(self.pins[8],self.pins[9]).output()
        output[13] =NOR(self.pins[11],self.pins[12]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7403(Base_14pin):
    """
    This is a Quad 2-input open-collector NAND gate IC
    """
    def __init__(self):
        self.pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]
    
    def run(self):
        output = {}
        output[3] = NAND(self.pins[1],self.pins[2]).output()
        output[6] = NAND(self.pins[4],self.pins[5]).output()
        output[8] = NAND(self.pins[9],self.pins[10]).output()
        output[11] =NAND(self.pins[12],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7404(Base_14pin):
    """
    This is a hex inverter IC
    """
    def __init__(self):
        self.pins = [None,0,None,0,None,0,None,0,None,0,None,0,None,0,0]
    
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

class IC_7405(Base_14pin):
    """
    This is hex open-collector inverter IC
    """
    def __init__(self):
        self.pins = [None,0,None,0,None,0,None,0,None,0,None,0,None,0,0]
        
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

class IC_7408(Base_14pin):
    """
    This is a Quad 2 input AND gate IC
    """
    def __init__(self):
        self.pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]
        
    def run(self):
        output = {}
        output[3] = AND(self.pins[1],self.pins[2]).output()
        output[6] = AND(self.pins[4],self.pins[5]).output()
        output[8] = AND(self.pins[9],self.pins[10]).output()
        output[11] = AND(self.pins[12],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7410(Base_14pin):
    """
    This is a Triple 3 input NAND gate IC
    """
    def __init__(self):
        self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,None,0,0]
        
    def run(self):
        output = {}
        output[12] = NAND(self.pins[1],self.pins[2],self.pins[13]).output()
        output[6] = NAND(self.pins[3],self.pins[4],self.pins[5]).output()
        output[8] = NAND(self.pins[9],self.pins[10],self.pins[11]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7411(Base_14pin):
    """
    This is a Triple 3 input AND gate IC
    """
    def __init__(self):
        self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,None,0,0]
        
    def run(self):
        output = {}
        output[12] = AND(self.pins[1],self.pins[2],self.pins[13]).output()
        output[6] = AND(self.pins[3],self.pins[4],self.pins[5]).output()
        output[8] = AND(self.pins[9],self.pins[10],self.pins[11]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7412(Base_14pin):
    """
    This is a Triple 3 input NAND gate IC with open collector outputs
    """
    def __init__(self):
        self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,None,0,0]
        
    def run(self):
        output = {}
        output[12] = NAND(self.pins[1],self.pins[2],self.pins[13]).output()
        output[6] = NAND(self.pins[3],self.pins[4],self.pins[5]).output()
        output[8] = NAND(self.pins[9],self.pins[10],self.pins[11]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7413(Base_14pin):
    """
    This is a dual 4 input NAND gate IC
    """
    def __init__(self):
        self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,0,0,0]
        
    def run(self):
        output = {}
        output[6] = NAND(self.pins[1],self.pins[2],self.pins[4],self.pins[5]).output()
        output[8] = NAND(self.pins[9],self.pins[10],self.pins[12],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7415(Base_14pin):
    """
    This is a Triple 3 input AND gate IC with open collector outputs
    """
    def __init__(self):
        self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,None,0,0]
        
    def run(self):
        output = {}
        output[12] = AND(self.pins[1],self.pins[2],self.pins[13]).output()
        output[6] = AND(self.pins[3],self.pins[4],self.pins[5]).output()
        output[8] = AND(self.pins[9],self.pins[10],self.pins[11]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7416(Base_14pin):
    """
    This is a Hex open-collector high-voltage inverter
    """
    def __init__(self):
        self.pins = [None,0,None,0,None,0,None,0,None,0,None,0,None,0,0]
        
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

class IC_7417(Base_14pin):
    """
    This is a Hex open-collector high-voltage buffer
    """
    def __init__(self):
        self.pins = [None,0,None,0,None,0,None,0,None,0,None,0,None,0,0]
        
    def run(self):
        output = {}
        output[2] = self.pins[1]
	output[4] = self.pins[3]
	output[6] = self.pins[5]
	output[8] = self.pins[9]
	output[10] = self.pins[11]
	output[12] = self.pins[13]
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7418(Base_14pin):
    """
    This is a Dual 4-input NAND gates with schmitt-trigger inputs.
    """
    def __init__(self):
        self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,0,0,0]
        
    def run(self):
        output = {}
        output[6] = NAND(self.pins[1],self.pins[2],self.pins[4],self.pins[5]).output()
        output[8] = NAND(self.pins[9],self.pins[10],self.pins[12],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7419(Base_14pin):
    """
    This is a Hex inverters with schmitt-trigger line-receiver inputs.
    """
    def __init__(self):
        self.pins = [None,0,None,0,None,0,None,0,None,0,None,0,None,0,0]
        
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

class IC_7420(Base_14pin):
    """
    This is a dual 4-input NAND gate
    """
    def __init__(self):
        self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,0,0,0]
        
    def run(self):
        output = {}        
        output[6] = NAND(self.pins[1],self.pins[2],self.pins[4],self.pins[5]).output()
        output[8] = NAND(self.pins[9],self.pins[10],self.pins[12],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7421(Base_14pin):
    """
    This is a dual 4-input AND gate
    """
    def __init__(self):
        self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,0,0,0]
        
    def run(self):
        output = {}        
        output[6] = AND(self.pins[1],self.pins[2],self.pins[4],self.pins[5]).output()
        output[8] = AND(self.pins[9],self.pins[10],self.pins[12],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7422(Base_14pin):
    """
    This is a dual 4-input NAND gate with open collector outputs
    """
    def __init__(self):
        self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,0,0,0]
        
    def run(self):
        output = {}        
        output[6] = NAND(self.pins[1],self.pins[2],self.pins[4],self.pins[5]).output()
        output[8] = NAND(self.pins[9],self.pins[10],self.pins[12],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7424(Base_14pin):
    """
    This is a Quad 2-input NAND gates with schmitt-trigger line-receiver inputs
    """
    def __init__(self):
        self.pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]
        
    def run(self):
        output = {}        
        output[3] = NAND(self.pins[1],self.pins[2]).output()
        output[6] = NAND(self.pins[4],self.pins[5]).output()
        output[8] = NAND(self.pins[10],self.pins[9]).output()
        output[11] = NAND(self.pins[12],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7425(Base_14pin):
    """
    This is a Dual 4-Input NOR Gate with Strobe
    """
    def __init__(self):
        self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,0,0,0]
        
    def run(self):
        output = {}        
        output[6] = NOR(self.pins[1],self.pins[2],self.pins[3],self.pins[4],self.pins[5]).output()
        output[8] = NOR(self.pins[9],self.pins[10],self.pins[11],self.pins[12],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7426(Base_14pin):
    """
    This is a Quad 2-input open-collector high-voltage NAND gates.
    """
    def __init__(self):
        self.pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]
        
    def run(self):
        output = {}        
        output[3] = NAND(self.pins[1],self.pins[2]).output()
        output[6] = NAND(self.pins[4],self.pins[5]).output()
        output[8] = NAND(self.pins[9],self.pins[10]).output()
        output[11] = NAND(self.pins[12],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7427(Base_14pin):
    """
    This is a Triple 3-Input NOR Gate
    """
    def __init__(self):
        self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,None,0,0]
        
    def run(self):
        output = {}        
        output[6] = NOR(self.pins[3],self.pins[4],self.pins[5]).output()
        output[8] = NOR(self.pins[9],self.pins[10],self.pins[11]).output()
        output[12] = NOR(self.pins[1],self.pins[2],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7428(Base_14pin):
    """
    This is a Quad 2-input NOR gates with buffered outputs.
    """
    def __init__(self):
        self.pins = [None,None,0,0,None,0,0,0,0,0,None,0,0,None,0]
        
    def run(self):
        output = {}        
        output[1] = NOR(self.pins[2],self.pins[3]).output()
        output[4] = NOR(self.pins[5],self.pins[6]).output()
        output[10] = NOR(self.pins[8],self.pins[9]).output()
        output[13] = NOR(self.pins[11],self.pins[12]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7430(Base_14pin):
    """
    This is a 8-Input NAND Gate
    """
    def __init__(self):
        self.pins = [None,0,0,0,0,0,0,0,None,0,0,0,0,0,0]
        
    def run(self):
        output = {}        
        output[8] = NAND(self.pins[1],self.pins[2],self.pins[3],self.pins[4],self.pins[5],self.pins[6],self.pins[11],self.pins[12]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7432(Base_14pin):
    """
    This is a Quad 2-Input OR Gate
    """
    def __init__(self):
        self.pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]
        
    def run(self):
        output = {}        
        output[3] = OR(self.pins[1],self.pins[2]).output()
        output[6] = OR(self.pins[4],self.pins[5]).output()
        output[8] = OR(self.pins[9],self.pins[10]).output() 
        output[11] = OR(self.pins[12],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7433(Base_14pin):
    """
    This is a Quad 2-input open-collector NOR gate
    """
    def __init__(self):
        self.pins = [None,None,0,0,None,0,0,0,0,0,None,0,0,None,0]
        
    def run(self):
        output = {}        
        output[1] = NOR(self.pins[2],self.pins[3]).output()
        output[4] = NOR(self.pins[5],self.pins[6]).output()
        output[10] = NOR(self.pins[8],self.pins[9]).output()
        output[13] = NOR(self.pins[11],self.pins[12]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7437(Base_14pin):
    """
    This is a Quad 2-input NAND gates with buffered output
    """
    def __init__(self):
        self.pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]
        
    def run(self):
        output = {}        
        output[3] = NAND(self.pins[1],self.pins[2]).output()
        output[6] = NAND(self.pins[4],self.pins[5]).output()
        output[8] = NAND(self.pins[9],self.pins[10]).output()
        output[11] = NAND(self.pins[12],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7438(Base_14pin):
    """
    This is a Quad 2-Input NAND Buffer with Open Collector Output
    """
    def __init__(self):
        self.pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]
        
    def run(self):
        output = {}        
        output[3] = NAND(self.pins[1],self.pins[2]).output()
        output[6] = NAND(self.pins[4],self.pins[5]).output()
        output[8] = NAND(self.pins[9],self.pins[10]).output()
        output[11] = NAND(self.pins[12],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7440(Base_14pin):
    """
    This is a Dual 4-Input NAND Buffer
    """
    def __init__(self):
        self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,0,0,0]
        
    def run(self):
        output = {}        
        output[6] = NAND(self.pins[1],self.pins[2],self.pins[4],self.pins[5]).output()
        output[8] = NAND(self.pins[9],self.pins[10],self.pins[12],self.pins[13]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."



class IC_7451(Base_14pin):
    """
    This is a dual 2-wide 2-input AND-OR Invert gate
    """
    #Datasheet here, http://www.unitechelectronics.com/7451-7497data.htm

    def __init__(self):
        self.pins = [None,0,0,0,0,None,0,None,0,0,0,0,0,0,0]
        
    def run(self):
        output = {}
        output[6] = NOR(AND(self.pins[2],self.pins[3]).output(),
			AND(self.pins[4],self.pins[5]).output()).output()
        output[8] = NOR(AND(self.pins[1], self.pins[13], self.pins[12]).output(),
			AND(self.pins[11],self.pins[10],self.pins[9]).output()).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7454(Base_14pin):
    """
    This is a 4-wide 2-input AND-OR Invert gate
    """
    #Datasheet here, http://www.unitechelectronics.com/7451-7497data.htm

    def __init__(self):
        self.pins = [None,0,0,0,0,None,0,None,0,0,0,0,0,0,0]
        
    def run(self):
        output = {}
        temp = []
        temp.append(OR(AND(self.pins[1], self.pins[2]).output(),
			AND(self.pins[3], self.pins[4], self.pins[5]).output()).output())
        temp.append(OR(AND(self.pins[9], self.pins[10], self.pins[11]).output(),
			AND(self.pins[12], self.pins[13]).output()).output())
        output[6] = NOR(temp[0], temp[1]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7455(Base_14pin):
    """
    This is a 4-wide 2-input AND-OR Invert gate
    """
    #Datasheet here, http://www.unitechelectronics.com/7451-7497data.htm

    def __init__(self):
        self.pins = [None,0,0,0,0,0,0,0,None,0,0,0,0,0,0]
        
    def run(self):
        output = {}
        temp = []
        temp.append(AND(self.pins[1], self.pins[2],
                        self.pins[3], self.pins[4]).output())
        temp.append(AND(self.pins[10], self.pins[11],
                        self.pins[12], self.pins[13]).output())
        output[8] = NOR(temp[0], temp[1]).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7458(Base_14pin):
    """
    This is a 2-input and 3-input AND-OR gate
    """
    #Datasheet here, http://www.unitechelectronics.com/7451-7497data.htm

    def __init__(self):
        self.pins = [None,0,0,0,0,None,0,None,0,0,0,0,0,0,0]
        
    def run(self):
        output = {}
        output[6] = OR(AND(self.pins[2], self.pins[3]).output(),
			AND(self.pins[4], self.pins[5]).output()).output()
        output[8] = OR(AND(self.pins[1], self.pins[13], self.pins[12]).output(),
			AND(self.pins[11], self.pins[10], self.pins[9]).output()).output()
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7464(Base_14pin):
    """
    This is a 4-2-3-2 input AND-OR-invert gate
    """

    #Datasheet here, http://www.skot9000.com/ttl/datasheets/64.pdf

    def __init__(self):
        self.pins = [None,0,0,0,0,0,0,0,None,0,0,0,0,0,0]

    def run(self):
        output = {}
        output[8] = NOR(AND(self.pins[2],self.pins[3]).output(),
                        AND(self.pins[9],self.pins[10]).output(),
                        AND(self.pins[1],self.pins[11],self.pins[13],self.pins[12]).output(),
                        AND(self.pins[4],self.pins[5],self.pins[6]).output()).output()

        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly"

class IC_7486(Base_14pin):
    """
    This is a quad 2-input exclusive OR gate
    """

    #Datasheet here, http://www.skot9000.com/ttl/datasheets/86.pdf

    def __init__(self):
        self.pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]

    def run(self):
        output = {}
        
        output[3] = XOR(self.pins[1],self.pins[2]).output()

        output[6] = XOR(self.pins[4],self.pins[5]).output()
        
        output[8] = XOR(self.pins[9],self.pins[10]).output()

        output[11] = XOR(self.pins[12],self.pins[13]).output()
        
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly"

class IC_74260(Base_14pin):
    """
    This is a dual 5-input NOR gate
    """

    #Datasheet here, http://www.skot9000.com/ttl/datasheets/260.pdf

    def __init__(self):
        self.pins = [None,0,0,0,0,None,None,0,0,0,0,0,0,0,0]

    def run(self):
        output = {}
        
        output[5] = NOR(self.pins[1],self.pins[2],self.pins[3],
                      self.pins[12],self.pins[13]).output()

        output[6] = NOR(self.pins[4],self.pins[8],self.pins[9],
                      self.pins[10],self.pins[11]).output()
        
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly"

######## IC's with 5 pins #################################

class IC_741G00(Base_5pin):
    """
    This is a single 2 input NAND gate IC
    """
    def __init__(self):
        self.pins = [None,0,0,0,None,0]
        
    def run(self):
        output = {}    
        output[4] = NAND(self.pins[1],self.pins[2]).output()
        if self.pins[3] == 0 and self.pins[5] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_741G02(Base_5pin):
    """
    This is a single 2 input NOR gate IC
    """
    def __init__(self):
        self.pins = [None,0,0,0,None,0]
        
    def run(self):
        output = {}
        output[4] = NOR(self.pins[1],self.pins[2]).output()
        if self.pins[3] == 0 and self.pins[5] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_741G03(Base_5pin):
    """
    This is a single 2 input NAND gate IC
    """
    def __init__(self):
        self.pins = [None,0,0,0,None,0]
        
    def run(self):
        output = {}     
        output[4] = NAND(self.pins[1],self.pins[2]).output()
        if self.pins[3] == 0 and self.pins[5] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_741G04(Base_5pin):
    """
    This is a single inverter IC
    """
    def __init__(self):
        self.pins = [None,None,0,0,None,0]
        
    def run(self):
        output = {}        
        output[4] = NOT(self.pins[2]).output()
        if self.pins[3] == 0 and self.pins[5] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_741G05(Base_5pin):
    """
    This is a single 2 input NAND gate IC
    """
    def __init__(self):
        self.pins = [None,None,0,0,None,0]
        
    def run(self):
        output = {}        
        output[4] = NOT(self.pins[2]).output()
        if self.pins[3] == 0 and self.pins[5] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_741G08(Base_5pin):
    """
    This is a single 2 input AND gate IC
    """
    def __init__(self):
        self.pins = [None,0,0,0,None,0]
        
    def run(self):
        output = {}        
        output[4] = AND(self.pins[1],self.pins[2]).output()
        if self.pins[3] == 0 and self.pins[5] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


######## IC's with 16 pins #################################

class IC_7431(Base_16pin):
    """
    This is a Hex delay element. 
    """
    def __init__(self):
        self.pins = [None,0,None,0,None,0,0,None,0,None,0,0,None,0,None,0,0]
        
    def run(self):
        output = {}        
        output[2] = NOT(self.pins[1]).output()
        output[7] = NAND(self.pins[5],self.pins[6]).output()
        output[14] = NOT(self.pins[15]).output()
        output[9] = NAND(self.pins[10],self.pins[11]).output()
        output[4] = self.pins[3]
        output[12] = self.pins[13]

        if self.pins[8] == 0 and self.pins[16] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7442(Base_16pin):
    """
    This is a BCD to Decimal decoder
    BCD Digits are in order of A B C D where pin 15 = A, pin 12 = D 
    """
    def __init__(self):
        self.pins = [None,None,None,None,None,None,None,None,0,None,None,None,0,0,0,0,0]
        
    def run(self):
        output = {}        
        inputlist = []
        for i in xrange(12, 16, 1):
            inputlist.append(self.pins[i])
        
        invalidlist = [[1,0,1,0], [1,0,1,1], [1,1,0,0], [1,1,0,1], [1,1,1,0], [1,1,1,1]]

        if inputlist in invalidlist:
            raise Exception("ERROR: Invalid BCD number")

        output[1] = NAND(NOT(self.pins[15]).output(), NOT(self.pins[14]).output(),
                        NOT(self.pins[13]).output(), NOT(self.pins[12]).output()).output()

        output[2] = NAND(self.pins[15], NOT(self.pins[14]).output(),
                        NOT(self.pins[13]).output(), NOT(self.pins[12]).output()).output()

        output[3] = NAND(NOT(self.pins[15]).output(), self.pins[14],
                        NOT(self.pins[13]).output(), NOT(self.pins[12]).output()).output()

        
        output[4] = NAND(self.pins[15], self.pins[14],
                        NOT(self.pins[13]).output(), NOT(self.pins[12]).output()).output()

        output[5] = NAND(NOT(self.pins[15]).output(), NOT(self.pins[14]).output(),
                        self.pins[13], NOT(self.pins[12]).output()).output()

        output[6] = NAND(self.pins[15], NOT(self.pins[14]).output(),
                        self.pins[13], NOT(self.pins[12]).output()).output()

        output[7] = NAND(NOT(self.pins[15]).output(), self.pins[14],
                        self.pins[13], NOT(self.pins[12]).output()).output()

        output[9] = NAND(self.pins[15], self.pins[14],
                        self.pins[13], NOT(self.pins[12]).output()).output()

        output[10] = NAND(NOT(self.pins[15]).output(), NOT(self.pins[14]).output(),
                        NOT(self.pins[13]).output(), self.pins[12]).output()

        output[11] = NAND(self.pins[15], NOT(self.pins[14]).output(),
                        NOT(self.pins[13]).output(), self.pins[12]).output()


        if self.pins[8] == 0 and self.pins[16] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7443(Base_16pin):
    """
    This is an excess-3 to Decimal decoder
    Excess-3 binary digits are in order of A B C D, where pin 15 = A and pin 12 = D
    """
    def __init__(self):
        self.pins = [None,None,None,None,None,None,None,None,0,None,None,None,0,0,0,0,0]
        
    def run(self):
        output = {}        
        inputlist = []
        for i in xrange(12, 16, 1):
            inputlist.append(self.pins[i])
        
        invalidlist = [[0,0,0,0], [0,0,0,1], [0,0,1,0], [1,1,0,1], [1,1,1,0], [1,1,1,1]]

        if inputlist in invalidlist:
            raise Exception("ERROR: Invalid Pin configuration")

        output[1] = NAND(self.pins[15], self.pins[14],
                       NOT(self.pins[13]).output(), NOT(self.pins[12]).output()).output()

        output[2] = NAND(NOT(self.pins[15]).output(), NOT(self.pins[14]).output(),
                        self.pins[13], NOT(self.pins[12]).output()).output()

        output[3] = NAND(self.pins[15], NOT(self.pins[14]).output(),
                        self.pins[13], NOT(self.pins[12]).output()).output()

        
        output[4] = NAND(NOT(self.pins[15]).output(), self.pins[14],
                        self.pins[13], NOT(self.pins[12]).output()).output()

        output[5] = NAND(self.pins[15], self.pins[14],
                        self.pins[13], NOT(self.pins[12]).output()).output()

        output[6] = NAND(NOT(self.pins[15]).output(), NOT(self.pins[14]).output(),
                        NOT(self.pins[13]).output(), self.pins[12]).output()

        output[7] = NAND(self.pins[15], NOT(self.pins[14]).output(),
                        NOT(self.pins[13]).output(), self.pins[12]).output()

        output[9] =NAND(NOT(self.pins[15]).output(), self.pins[14],
                       NOT(self.pins[13]).output(), self.pins[12]).output()

        output[10] = NAND(self.pins[15], self.pins[14],
                        NOT(self.pins[13]).output(), self.pins[12]).output()

        output[11] = NAND(NOT(self.pins[15]).output(), NOT(self.pins[14]).output(),
                        self.pins[13], self.pins[12]).output()


        if self.pins[8] == 0 and self.pins[16] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7444(Base_16pin):
    """
    This is an excess-3 gray code to Decimal decoder
    Excess-3 gray code digits are in order of A B C D, where pin 15 = A and pin 12 = D
    """
    def __init__(self):
        self.pins = [None,None,None,None,None,None,None,None,0,None,None,None,0,0,0,0,0]
        
    def run(self):
        output = {}        
        inputlist = []
        for i in xrange(12, 16, 1):
            inputlist.append(self.pins[i])
        
        invalidlist = [[0,0,0,0], [0,0,0,1], [0,0,1,1], [1,0,0,0], [1,0,0,1], [1,0,1,1]]

        if inputlist in invalidlist:
            raise Exception("ERROR: Invalid Pin configuration")

        output[1] = NAND(NOT(self.pins[15]).output(), self.pins[14],
                        NOT(self.pins[13]).output(), NOT(self.pins[12]).output()).output()

        output[2] = NAND(NOT(self.pins[15]).output(), self.pins[14],
                        self.pins[13], NOT(self.pins[12]).output()).output()

        output[3] = NAND((self.pins[15]), self.pins[14],
                        self.pins[13], NOT(self.pins[12]).output()).output()
       
        output[4] = NAND(self.pins[15], NOT(self.pins[14]).output(),
                        self.pins[13], NOT(self.pins[12]).output()).output()

        output[5] = NAND(NOT(self.pins[15]).output(), NOT(self.pins[14]).output(),
                        self.pins[13], NOT(self.pins[12]).output()).output()

        output[6] = NAND(NOT(self.pins[15]).output(), NOT(self.pins[14]).output(),
                        self.pins[13], self.pins[12]).output()

        output[7] = NAND(self.pins[15], NOT(self.pins[14]).output(),
                        self.pins[13], self.pins[12]).output()

        output[9] = NAND(self.pins[15], self.pins[14],
                        self.pins[13], self.pins[12]).output()

        output[10] = NAND(NOT(self.pins[15]).output(), self.pins[14],
                        self.pins[13], self.pins[12]).output()

        output[11] = NAND(NOT(self.pins[15]).output(), self.pins[14],
                       NOT(self.pins[13]).output(), self.pins[12]).output()


        if self.pins[8] == 0 and self.pins[16] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_7445(Base_16pin):

    """
    This is a Four-to-Ten (BCD to Decimal) DECODER
    datasheet at http://www.skot9000.com/ttl/datasheets/45.pdf
    """
    def __init__(self):
        self.pins = [None,None,None,None,None,None,None,None,0,None,None,None,0,0,0,0,0]

    def run(self):
        output = {}
        inputlist = []
        for i in xrange(12, 16, 1):
            inputlist.append(self.pins[i])
        
        invalidlist = [[1,0,1,0], [1,0,1,1], [1,1,0,0], [1,1,0,1], [1,1,1,0], [1,1,1,1]]

        if inputlist in invalidlist:
            raise Exception("ERROR: Invalid Pin configuration")

        output[1] = NAND(NOT(self.pins[15]).output(),NOT(self.pins[14]).output(),
                      NOT(self.pins[13]).output(),NOT(self.pins[12]).output()).output()

        output[2] = NAND(self.pins[15],NOT(self.pins[14]).output(),
                      NOT(self.pins[13]).output(),NOT(self.pins[12]).output()).output()

        output[3] = NAND(NOT(self.pins[15]).output(),self.pins[14],
                      NOT(self.pins[13]).output(),NOT(self.pins[12]).output()).output()

        output[4] = NAND(NOT(self.pins[15]).output(),self.pins[14],
                      NOT(self.pins[13]).output(),NOT(self.pins[12]).output()).output()

        output[5] = NAND(NOT(self.pins[15]).output(),NOT(self.pins[14]).output(),
                      self.pins[13],NOT(self.pins[12]).output()).output()

        output[6] = NAND(self.pins[15],NOT(self.pins[14]).output(),
                      self.pins[13],NOT(self.pins[12]).output()).output()

        output[7] = NAND(NOT(self.pins[15]).output(),self.pins[14],
                      self.pins[13],NOT(self.pins[12]).output()).output()

        output[9] = NAND(self.pins[15],self.pins[14],
                      self.pins[13],NOT(self.pins[12]).output()).output()

        output[10] = NAND(NOT(self.pins[15]).output(),NOT(self.pins[14]).output(),
                      NOT(self.pins[13]).output(),self.pins[12]).output()

        output[11] = NAND(self.pins[15],NOT(self.pins[14]).output(),
                      NOT(self.pins[13]).output(),self.pins[12]).output()

        if self.pins[8] == 0 and self.pins[16] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_74133(Base_16pin):
    """
    This is a 13-input NAND gate
    """

    #Datasheet here, http://www.skot9000.com/ttl/datasheets/133.pdf

    def __init__(self):
        self.pins = [None,0,0,0,0,0,0,0,0,None,0,0,0,0,0,0,0]

    def run(self):
        output = {}

        output[9] = NAND(self.pins[1],self.pins[2],self.pins[3],self.pins[4],
                      self.pins[5],self.pins[6],self.pins[7],self.pins[10],
                      self.pins[11],self.pins[12],self.pins[13],self.pins[14],
                      self.pins[15]).output()

        if self.pins[8] == 0 and self.pins[16] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly"


