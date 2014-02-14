
"""
    This file has all the classes of ICs belong to 7400 series
"""
from BinPy import Gates
import sys

class IC_7400:
    """
    This is a Quad 2 input NAND gate IC
    """
    def __init__(self):
        self.pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>14:
            raise Exception("ERROR: there are only 14 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        output[3] = self.gates.NAND(self.pins[1],self.pins[2])
        output[6] = self.gates.NAND(self.pins[4],self.pins[5])
        output[8] = self.gates.NAND(self.pins[9],self.pins[10])
        output[11] = self.gates.NAND(self.pins[12],self.pins[13])
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_741G00:
    '''
    This is a single 2 input NAND gate IC
    '''
    def __init__(self):
        self.pins = [None,0,0,0,None,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>5:
            raise Exception("ERROR: there are only 5 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        output[4] = self.gates.NAND(self.pins[1],self.pins[2])
        if self.pins[3] == 0 and self.pins[5] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


class IC_7401:
    '''
    This is a Quad 2 input NAND gate IC
    '''
    def __init__(self):
        self.pins = [None,None,0,0,None,0,0,0,0,0,None,0,0,None,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>14:
            raise Exception("ERROR: there are only 14 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        output[1] = self.gates.NAND(self.pins[2],self.pins[3])
        output[4] = self.gates.NAND(self.pins[5],self.pins[6])
        output[10] = self.gates.NAND(self.pins[8],self.pins[9])
        output[13] = self.gates.NAND(self.pins[11],self.pins[12])
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


class IC_7402:
    '''
    This is a Quad 2 input NOR gate IC
    '''
    def __init__(self):
        self.pins = [None,None,0,0,None,0,0,0,0,0,None,0,0,None,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>14:
            raise Exception("ERROR: there are only 14 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        output[1] = self.gates.NOR(self.pins[2],self.pins[3])
        output[4] = self.gates.NOR(self.pins[5],self.pins[6])
        output[10] = self.gates.NOR(self.pins[8],self.pins[9])
        output[13] = self.gates.NOR(self.pins[11],self.pins[12])
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


class IC_741G02:
    '''
    This is a single 2 input NOR gate IC
    '''
    def __init__(self):
        self.pins = [None,0,0,0,None,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>5:
            raise Exception("ERROR: there are only 14 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        output[4] = self.gates.NOR(self.pins[1],self.pins[2])
        if self.pins[3] == 0 and self.pins[5] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


class IC_7403:
    '''
    This is a Quad 2 input NAND gate IC
    '''
    def __init__(self):
        self.pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>14:
            raise Exception("ERROR: there are only 14 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        output[3] = self.gates.NAND(self.pins[1],self.pins[2])
        output[6] = self.gates.NAND(self.pins[4],self.pins[5])
        output[8] = self.gates.NAND(self.pins[9],self.pins[10])
        output[11] = self.gates.NAND(self.pins[12],self.pins[13])
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


class IC_741G03:
    '''
    This is a single 2 input NAND gate IC
    '''
    def __init__(self):
        self.pins = [None,0,0,0,None,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>5:
            raise Exception("ERROR: there are only 5 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        output[4] = self.gates.NAND(self.pins[1],self.pins[2])
        if self.pins[3] == 0 and self.pins[5] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


class IC_7404:
    '''
    This is hex inverter IC
    '''
    def __init__(self):
        self.pins = [None,0,None,0,None,0,None,0,None,0,None,0,None,0,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>14:
            raise Exception("ERROR: there are only 14 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        output[2] = self.gates.NOT(self.pins[1])
        output[4] = self.gates.NOT(self.pins[3])
        output[6] = self.gates.NOT(self.pins[5])
        output[8] = self.gates.NOT(self.pins[9])
        output[10] = self.gates.NOT(self.pins[11])
        output[12] = self.gates.NOT(self.pins[13])
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


class IC_741G04:
    '''
    This is a single inverter IC
    '''
    def __init__(self):
        self.pins = [None,None,0,0,None,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>5:
            raise Exception("ERROR: there are only 5 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        output[4] = self.gates.NOT(self.pins[2])
        if self.pins[3] == 0 and self.pins[5] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


class IC_7405:
    '''
    This is hex inverter IC
    '''
    def __init__(self):
        self.pins = [None,0,None,0,None,0,None,0,None,0,None,0,None,0,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>14:
            raise Exception("ERROR: there are only 14 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        output[2] = self.gates.NOT(self.pins[1])
        output[4] = self.gates.NOT(self.pins[3])
        output[6] = self.gates.NOT(self.pins[5])
        output[8] = self.gates.NOT(self.pins[9])
        output[10] = self.gates.NOT(self.pins[11])
        output[12] = self.gates.NOT(self.pins[13])
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

class IC_741G05:
    '''
    This is a single inverter IC
    '''
    def __init__(self):
        self.pins = [None,None,0,0,None,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>5:
            raise Exception("ERROR: there are only 5 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        output[4] = self.gates.NOT(self.pins[2])
        if self.pins[3] == 0 and self.pins[5] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


class IC_7408:
    '''
    This is a Quad 2 input AND gate IC
    '''
    def __init__(self):
        self.pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>14:
            raise Exception("ERROR: there are only 14 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        output[3] = self.gates.AND(self.pins[1],self.pins[2])
        output[6] = self.gates.AND(self.pins[4],self.pins[5])
        output[8] = self.gates.AND(self.pins[9],self.pins[10])
        output[11] = self.gates.AND(self.pins[12],self.pins[13])
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


class IC_741G08:
    '''
    This is a single 2 input AND gate IC
    '''
    def __init__(self):
        self.pins = [None,0,0,0,None,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>5:
            raise Exception("ERROR: there are only 5 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        output[4] = self.gates.AND(self.pins[1],self.pins[2])
        if self.pins[3] == 0 and self.pins[5] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

#IC_7409 and IC_741G09 to be added

class IC_7410:
    '''
    This is a Triple 3 input NAND gate IC
    '''
    def __init__(self):
        self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,None,0,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>14:
            raise Exception("ERROR: there are only 14 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        output[12] = self.gates.NAND(self.pins[1],self.pins[2],self.pins[13])
        output[6] = self.gates.NAND(self.pins[3],self.pins[4],self.pins[5])
        output[8] = self.gates.NAND(self.pins[9],self.pins[10],self.pins[11])
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


class IC_7411:
    '''
    This is a Triple 3 input AND gate IC
    '''
    def __init__(self):
        self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,None,0,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>14:
            raise Exception("ERROR: there are only 14 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        output[12] = self.gates.AND(self.pins[1],self.pins[2],self.pins[13])
        output[6] = self.gates.AND(self.pins[3],self.pins[4],self.pins[5])
        output[8] = self.gates.AND(self.pins[9],self.pins[10],self.pins[11])
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


class IC_7412:
    '''
    This is a Triple 3 input NAND gate IC with open collector outputs
    '''
    def __init__(self):
        self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,None,0,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>14:
            raise Exception("ERROR: there are only 14 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        output[12] = self.gates.NAND(self.pins[1],self.pins[2],self.pins[13])
        output[6] = self.gates.NAND(self.pins[3],self.pins[4],self.pins[5])
        output[8] = self.gates.NAND(self.pins[9],self.pins[10],self.pins[11])
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."



# IC_7413,IC_7414,IC_741G14to be added


class IC_7415:
    '''
    This is a Triple 3 input AND gate IC with open collector outputs
    '''
    def __init__(self):
        self.pins = [None,0,0,0,0,0,None,0,None,0,0,0,None,0,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>14:
            raise Exception("ERROR: there are only 14 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        output[12] = self.gates.AND(self.pins[1],self.pins[2],self.pins[13])
        output[6] = self.gates.AND(self.pins[3],self.pins[4],self.pins[5])
        output[8] = self.gates.AND(self.pins[9],self.pins[10],self.pins[11])
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly." 

# IC_7416,IC_7417,IC_741G17,IC_7418,IC_7419 to be added

class IC_7420:
    '''
    This is a is a dual 4-input NAND gate
    '''
    def __init__(self):
        self.pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>14:
            raise Exception("ERROR: there are only 14 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        
        output[6] = self.gates.NAND(self.pins[1],self.pins[2],self.pins[4],self.pins[5])
        output[8] = self.gates.NAND(self.pins[9],self.pins[10],self.pins[12],self.pins[13])
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."


class IC_7421:
    '''
    This is a is a dual 4-input AND gate
    '''
    def __init__(self):
        self.pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>14:
            raise Exception("ERROR: there are only 14 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        
        output[6] = self.gates.AND(self.pins[1],self.pins[2],self.pins[4],self.pins[5])
        output[8] = self.gates.AND(self.pins[9],self.pins[10],self.pins[12],self.pins[13])
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly." 

class IC_7422:
    '''
    This is a is a dual 4-input NAND gate with open collector outputs
    '''
    def __init__(self):
        self.pins = [None,0,0,None,0,0,None,0,None,0,0,None,0,0,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>14:
            raise Exception("ERROR: there are only 14 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        
        output[6] = self.gates.NAND(self.pins[1],self.pins[2],self.pins[4],self.pins[5])
        output[8] = self.gates.NAND(self.pins[9],self.pins[10],self.pins[12],self.pins[13])
        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

#IC 7422 to IC 7441 TBA

class IC_7442:
    '''
    This is a BCD to Decimal decoder
    BCD Digits are in order of A B C D where pin 15 = A, pin 12 = D
    '''

    #Datasheet here, http://pdf1.alldatasheet.com/datasheet-pdf/view/126658/TI/SN7443.html

    def __init__(self):
        self.pins = [None,None,None,None,None,None,None,0,None,None,None,0,0,0,0,0,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]
    
    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>16:
            raise Exception("ERROR: There are only 16 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):

        output = {}

        inputlist = []
        for i in xrange(12, 16, 1):
            inputlist.append(self.pins[i])
        
        invalidlist = [[1,0,1,0], [1,0,1,1], [1,1,0,0], [1,1,0,1], [1,1,1,0], [1,1,1,1]]

        if inputlist in invalidlist:
            raise Exception("ERROR: Invalid BCD number")

        output[1] = self.gates.NAND(self.gates.NOT(self.pins[15]), self.gates.NOT(self.pins[14]),
                        self.gates.NOT(self.pins[13]), self.gates.NOT(self.pins[12]))

        output[2] = self.gates.NAND(self.pins[15], self.gates.NOT(self.pins[14]),
                        self.gates.NOT(self.pins[13]), self.gates.NOT(self.pins[12]))

        output[3] = self.gates.NAND(self.gates.NOT(self.pins[15]), self.pins[14],
                        self.gates.NOT(self.pins[13]), self.gates.NOT(self.pins[12]))

        
        output[4] = self.gates.NAND(self.pins[15], self.pins[14],
                        self.gates.NOT(self.pins[13]), self.gates.NOT(self.pins[12]))

        output[5] = self.gates.NAND(self.gates.NOT(self.pins[15]), self.gates.NOT(self.pins[14]),
                        self.pins[13], self.gates.NOT(self.pins[12]))

        output[6] = self.gates.NAND(self.pins[15], self.gates.NOT(self.pins[14]),
                        self.pins[13], self.gates.NOT(self.pins[12]))

        output[7] = self.gates.NAND(self.gates.NOT(self.pins[15]), self.pins[14],
                        self.pins[13], self.gates.NOT(self.pins[12]))

        output[9] = self.gates.NAND(self.pins[15], self.pins[14],
                        self.pins[13], self.gates.NOT(self.pins[12]))

        output[10] = self.gates.NAND(self.gates.NOT(self.pins[15]), self.gates.NOT(self.pins[14]),
                        self.gates.NOT(self.pins[13]), self.pins[12])

        output[11] = self.gates.NAND(self.pins[15], self.gates.NOT(self.pins[14]),
                        self.gates.NOT(self.pins[13]), self.pins[12])


        if self.pins[8] == 0 and self.pins[16] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly. "



class IC_7443:
    '''
    This is an excess-3 to Decimal decoder
    Excess-3 binary digits are in order of A B C D, where pin 15 = A and pin 12 = D
    '''

    #Datasheet here, http://pdf1.alldatasheet.com/datasheet-pdf/view/126658/TI/SN7443.html

    def __init__(self):
        self.pins = [None,None,None,None,None,None,None,0,None,None,None,0,0,0,0,0,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]
    
    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>16:
            raise Exception("ERROR: There are only 16 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):

        output = {}

        inputlist = []
        for i in xrange(12, 16, 1):
            inputlist.append(self.pins[i])
        
        invalidlist = [[0,0,0,0], [0,0,0,1], [0,0,1,0], [1,1,0,1], [1,1,1,0], [1,1,1,1]]

        if inputlist in invalidlist:
            raise Exception("ERROR: Invalid Pin configuration")

        output[1] = self.gates.NAND(self.pins[15], self.pins[14],
                        self.gates.NOT(self.pins[13]), self.gates.NOT(self.pins[12]))

        output[2] = self.gates.NAND(self.gates.NOT(self.pins[15]), self.gates.NOT(self.pins[14]),
                        self.pins[13], self.gates.NOT(self.pins[12]))

        output[3] = self.gates.NAND((self.pins[15]), self.gates.NOT(self.pins[14]),
                        self.pins[13], self.gates.NOT(self.pins[12]))

        
        output[4] = self.gates.NAND(self.gates.NOT(self.pins[15]), self.pins[14],
                        self.pins[13], self.gates.NOT(self.pins[12]))

        output[5] = self.gates.NAND(self.pins[15], self.pins[14],
                        self.pins[13], self.gates.NOT(self.pins[12]))

        output[6] = self.gates.NAND(self.gates.NOT(self.pins[15]), self.gates.NOT(self.pins[14]),
                        self.gates.NOT(self.pins[13]), self.pins[12])

        output[7] = self.gates.NAND(self.pins[15], self.gates.NOT(self.pins[14]),
                        self.gates.NOT(self.pins[13]), self.pins[12])

        output[9] = self.gates.NAND(self.gates.NOT(self.pins[15]), self.pins[14],
                        self.gates.NOT(self.pins[13]), self.pins[12])

        output[10] = self.gates.NAND(self.pins[15], self.pins[14],
                        self.gates.NOT(self.pins[13]), self.pins[12])

        output[11] = self.gates.NAND(self.gates.NOT(self.pins[15]), self.gates.NOT(self.pins[14]),
                        self.pins[13], self.pins[12])


        if self.pins[8] == 0 and self.pins[16] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly. "



class IC_7444:
    '''
    This is an excess-3 gray code to Decimal decoder
    Excess-3 gray code digits are in order of A B C D, where pin 15 = A and pin 12 = D
    '''

    #Datasheet here, http://www.datasheetarchive.com/dlmain/Datasheets-8/DSA-151326.pdf

    def __init__(self):
        self.pins = [None,None,None,None,None,None,None,0,None,None,None,0,0,0,0,0,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]
    
    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>16:
            raise Exception("ERROR: There are only 16 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):

        output = {}

        inputlist = []
        for i in xrange(12, 16, 1):
            inputlist.append(self.pins[i])
        
        invalidlist = [[0,0,0,0], [0,0,0,1], [0,0,1,1], [1,0,0,0], [1,0,0,1], [1,0,1,1]]

        if inputlist in invalidlist:
            raise Exception("ERROR: Invalid Pin configuration")

        output[1] = self.gates.NAND(self.gates.NOT(self.pins[15]), self.pins[14],
                        self.gates.NOT(self.pins[13]), self.gates.NOT(self.pins[12]))

        output[2] = self.gates.NAND(self.gates.NOT(self.pins[15]), self.pins[14],
                        self.pins[13], self.gates.NOT(self.pins[12]))

        output[3] = self.gates.NAND((self.pins[15]), self.pins[14],
                        self.pins[13], self.gates.NOT(self.pins[12]))

        
        output[4] = self.gates.NAND(self.pins[15], self.gates.NOT(self.pins[14]),
                        self.pins[13], self.gates.NOT(self.pins[12]))

        output[5] = self.gates.NAND(self.gates.NOT(self.pins[15]), self.gates.NOT(self.pins[14]),
                        self.pins[13], self.gates.NOT(self.pins[12]))

        output[6] = self.gates.NAND(self.gates.NOT(self.pins[15]), self.gates.NOT(self.pins[14]),
                        self.pins[13], self.pins[12])

        output[7] = self.gates.NAND(self.pins[15], self.gates.NOT(self.pins[14]),
                        self.pins[13], self.pins[12])

        output[9] = self.gates.NAND(self.pins[15], self.pins[14],
                        self.pins[13], self.pins[12])

        output[10] = self.gates.NAND(self.gates.NOT(self.pins[15]), self.pins[14],
                        self.pins[13], self.pins[12])

        output[11] = self.gates.NAND(self.gates.NOT(self.pins[15]), self.pins[14],
                        self.gates.NOT(self.pins[13]), self.pins[12])


        if self.pins[8] == 0 and self.pins[16] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly. "


class IC_7451:
    '''
    This is a dual 2-wide 2-input AND-OR Invert gate
    '''
    #Datasheet here, http://www.unitechelectronics.com/7451-7497data.htm

    def __init__(self):
        self.pins = [0,0,0,0,0,None,0,None,0,0,0,0,0,0,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>14:
            raise Exception("ERROR: there are only 14 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
    

        output[6] = self.gates.NOR(self.gates.AND(self.pins[2],self.pins[3]),
                        self.gates.AND(self.pins[4],self.pins[5]))
        output[8] = self.gates.NOR(self.gates.AND(self.pins[1], self.pins[13], self.pins[12]), 
                        self.gates.AND(self.pins[11],self.pins[10],self.pins[9]))

        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

#todo : IC 7452 and 7453


class IC_7454:
    '''
    This is a 4-wide 2-input AND-OR Invert gate
    '''
    #Datasheet here, http://www.unitechelectronics.com/7451-7497data.htm

    def __init__(self):
        self.pins = [0,0,0,0,0,None,0,None,0,0,0,0,0,0,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>14:
            raise Exception("ERROR: there are only 14 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        temp = []

        temp.append(self.gates.OR(self.gates.AND(self.pins[1], self.pins[2]),
                        self.gates.AND(self.pins[3], self.pins[4], self.pins[5])))
        temp.append(self.gates.OR(self.gates.AND(self.pins[9], self.pins[10], self.pins[11]),
                        self.gates.AND(self.pins[12], self.pins[13])))

        output[6] = self.gates.NOR(temp[0], temp[1])

        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."



class IC_7455:
    '''
    This is a 4-wide 2-input AND-OR Invert gate
    '''
    #Datasheet here, http://www.unitechelectronics.com/7451-7497data.htm

    def __init__(self):
        self.pins = [0,0,0,0,None,None,0,None,None,0,0,0,0,0,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>14:
            raise Exception("ERROR: there are only 14 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}
        temp = []

        temp.append(self.gates.AND(self.pins[1], self.pins[2],
                        self.pins[3], self.pins[4]))
        temp.append(self.gates.AND(self.pins[10], self.pins[11],
                        self.pins[12], self.pins[13]))

        output[8] = self.gates.NOR(temp[0], temp[1])

        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."

#todo : IC 7456 and 7457


class IC_7458:
    '''
    This is a 2-input and 3-input AND-OR gate
    '''
    #Datasheet here, http://www.unitechelectronics.com/7451-7497data.htm

    def __init__(self):
        self.pins = [0,0,0,0,0,None,0,None,0,0,0,0,0,0,0]
        self.gates = Gates()

    def setIC(self,pin_conf):
        '''
        This method takes a dictionary with key:pin_no and value:pin_value
        '''
        for i in pin_conf:
            self.pins[i] = pin_conf[i]

    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>14:
            raise Exception("ERROR: there are only 14 pins in this IC")
        self.pins[pin_no] = pin_value

    def run(self):
        output = {}

        output[6] = self.gates.OR(self.gates.AND(self.pins[2], self.pins[3]),
                        self.gates.AND(self.pins[4], self.pins[5]))
        output[8] = self.gates.OR(self.gates.AND(self.pins[1], self.pins[13], self.pins[12]),
                        self.gates.AND(self.pins[11], self.pins[10], self.pins[9]))

        if self.pins[7] == 0 and self.pins[14] == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."
