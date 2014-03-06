"""
This module has all the classes of ICs belonging to 4000 series.

Please note that the length of list self.pins is 1 more than the number of actual pins. This is so because pin0
is not used as a general term referring to the first pin of the IC. Zeroth index of the self.pins is not being used.
"""

from __future__ import print_function
from BinPy.Gates.gates import *
from BinPy.ic.base import *

######## IC's with 14 pins #################################

class IC_4081(Base_14pin):
    """
    This is a Quad 2 Input AND gate IC
    """
    def __init__(self):
        
        self.pins = [None,0,0,None,None,0,0,0,0,0,None,None,0,0,1]
        #Example of quick conversion from list of pins to list of pin instances
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
    
    def run(self):
        output = {}
        output[3]  =  (  self.pins[1]()  & self.pins[2]()    )()
        output[4]  =  (  self.pins[5]()  & self.pins[6]()    )()
        output[10] =  (  self.pins[9]()  & self.pins[3]()    )()
        output[11] =  (  self.pins[12]() & self.pins[13]()   )()
        
        #Pin class object when called returns its logic state.
        #Logic class object when called returns the boolean binary equivalent of its state.
        
        #Output is a dict of logic values of each pin.
        
        #Uncomment to set the output pins to the respective logic values
        self.setIC(output)
        #Uncomment to draw the current I/O configuration of IC
        #self.drawIC()
        
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")

class IC_4082(Base_14pin):
    """
    This is a Dual 4 Input AND gate IC
    """
    def __init__(self):
        
        self.pins = [None,None,0,0,0,0,0,0,0,0,None,None,0,0,1]
        self.pins = pinlist_quick(self.pins)
        self.uses_pincls = True
        
        #Example of proper use of pin class
        self.setIC ( { 1 : {'desc':'Q1 : Output of AND gate 1'},
                       2 : {'desc':'A1 : Input 1 of AND gate 1'},
                       3 : {'desc':'B1 : Input 2 of AND gate 1'},
                       4 : {'desc':'C1 : Input 3 of AND gate 1'},
                       5 : {'desc':'D1 : Input 4 of AND gate 1'},
                       6 : {'desc':'NC '},
                       7 : {'desc':'GND'},
                       8 : {'desc':'NC '},
                       9 : {'desc':'D2 : Input 4 of AND gate 2'},
                       10: {'desc':'C2 : Input 3 of AND gate 2'},
                       11: {'desc':'B2 : Input 2 of AND gate 2'},
                       12: {'desc':'A2 : Input 1 of AND gate 2'},
                       13: {'desc':'Q2 : Output of AND gate 2'},
                       14: {'desc':'VCC'}
                     } ) 
    def run(self):
        output = {}
        output[1]   =  (  self.pins[2]()  &  self.pins[3]()  &  self.pins[4]()  &  self.pins[5]()  )()
        output[13]  =  (  self.pins[9]()  &  self.pins[10]() &  self.pins[11]() &  self.pins[12]() )()
        
        #Pin class object when called returns its logic state as a logic class object which has overloaded operators.
        #Logic class object when called returns the boolean binary equivalent of its state.
        
        #Uncomment to set the output pins to the respective logic values
        self.setIC(output)
        #Uncomment to draw the current I/O configuration of IC
        #self.drawIC()
        
        
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            return output
        else:
            print ("Ground and VCC pins have not been configured correctly.")
