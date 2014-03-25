"""
This module includes all the base classes for different ICs.
"""
from __future__ import print_function
from BinPy import *
import sys

try:
    _V = chr(9474)
    _H = chr(9472)
    _HVD = chr(9488)
    _HVU = chr(9496)
    _VHU = chr(9484)
    _VHD = chr(9492)
    _N = chr(10)
    _U = chr(9697)
    _LT = chr(9508)
    _RT = chr(9500)
except:
    _V = unichr(9474)
    _H = unichr(9472)
    _HVD = unichr(9488)
    _HVU = unichr(9496)
    _VHU = unichr(9484)
    _VHD = unichr(9492)
    _N = unichr(10)
    _U = unichr(9697)
    _LT = unichr(9508)
    _RT = unichr(9500)


class IC:

    """
    This is a base class for IC
    """
    outputConnector = {}

    def __init__(self):
        pass

    def setOutput(self, index, value):
        if not isinstance(value, Connector):
            raise Exception("ERROR: Expecting a connector class object")
        value.tap(self, 'output')
        self.outputConnector[index] = value
        try:
            output = self.run()
        except:
            print("Invalid Argument")

    def setIC(self, param_dict):
        """
        If pin class is not used this method then it takes a dictionary with the format { PINNO:PINVALUE, ... }
        Else it takes a dictionary of dictionaries with the format ->
        { PINNO:{PARAM1:VAL1, PARAM2:VAL2, ... }, PINNO2:{PARAM1:VAL1, PARAM2:VAL2, ... } , ... }
        """
        for pin in param_dict:
            if not self.uses_pincls:
                self.pins[pin] = param_dict[pin]
            else:
                self.pins[pin].setPinParam(param_dict[pin])

    def drawIC(self):
        try:

            if (self.total_pins in [14, 16]):

                top = "\n\n              " + _VHU + \
                    _H * 9 + _U + _H * 9 + _HVD + _N
                bottom = "              " + _VHD + _H * 19 + _HVU + "  "
                diag = top

                ic_number = str(self.__class__.__name__.split('_')[-1])
                ic_name = ' ' * 2 + ic_number + ' ' * 10

                # IC number is obtained by the __class__.__name__ parameter
                # assuming the naming of the class is such that last 4 digits
                # correspond to the IC Number.

                for i in range(1, (self.total_pins // 2) + 1):

                    j = self.total_pins - i + 1
                    if self.uses_pincls:
                        v1 = 'Z' if self.pins[i].value is None else str(
                            self.pins[i].value)
                        v2 = 'Z' if self.pins[j].value is None else str(
                            self.pins[j].value)

                        f = (
                            self.pins[i].pin_tag,
                            v1,
                            str(i),
                            ic_name[i],
                            str(j),
                            v2,
                            self.pins[j].pin_tag)

                    else:
                        v1 = 'Z' if self.pins[i] is None else str(self.pins[i])
                        v2 = 'Z' if self.pins[j] is None else str(self.pins[j])

                        f = ('   ', v1, str(i), ic_name[i], str(j), v2, '   ')
                    diag += "              |                   |\n"
                    diag += " %3s [%1s]    ---| %2s      %1s     %2s  |---    [%1s] %3s\n" % f
                    diag += "              |                   |\n"

                diag += bottom
                diag = diag.replace(
                    "---|",
                    _H *
                    2 +
                    _LT).replace(
                    "|---",
                    _RT +
                    _H *
                    2).replace(
                    '|',
                    _V)
                print(diag)

            else:
                raise Exception("ERROR: IC not supported")
        except:
            print("ERROR: Draw Failed - " + sys.exc_info()[1].args[0])


class Base_5pin(IC):

    """
    This method takes base class for IC's having 5 pins
    """
    total_pins = 5
    uses_pincls = False

    def setPin(self, pin_no, pin_value):
        if pin_no < 1 or pin_no > 5:
            raise Exception("ERROR: There are only 5 pins in this IC")
        if not self.uses_pincls:
            self.pins[pin_no] = pin_value
        else:
            self.pins[pin_no].setPinParam(pin_value)


class Base_14pin(IC):

    """
    This method takes base class for IC's having 14 pins
    """
    total_pins = 14
    uses_pincls = False

    def setPin(self, pin_no, pin_value):
        if pin_no < 1 or pin_no > 14:
            raise Exception("ERROR: There are only 14 pins in this IC")
        if not self.uses_pincls:
            self.pins[pin_no] = pin_value
        else:
            self.pins[pin_no].setPinParam(pin_value)

    def setPinParam(self, pin_no, parm_dict):
        if pin_no < 1 or pin_no > 14:
            raise Exception("ERROR: There are only 14 pins in this IC")
        if uses_pincls:
            self.pins[pin_no].setPinParam(parm_dict)
        else:
            raise Exception("ERROR: IC Does not use Pinset class")


class Base_16pin(IC):

    """
    This method takes base class for IC's having 16 pins
    """
    total_pins = 16
    uses_pincls = False

    def setPin(self, pin_no, pin_value):
        if pin_no < 1 or pin_no > 16:
            raise Exception("ERROR: There are only 16 pins in this IC")
        if not self.uses_pincls:
            self.pins[pin_no] = pin_value
        else:
            self.pins[pin_no].setPinParam(pin_value)

    def SetPinParam(self, pin_no, parm_dict):
        if pin_no < 1 or pin_no > 16:
            raise Exception("ERROR: There are only 16 pins in this IC")
        if uses_pincls:
            self.pins[pin_no].setPinParam(parm_dict)
        else:
            raise Exception("ERROR: IC Does not use Pinset class")


class Pin():

    """
    Pin class for defining a particular pin of an IC

    Sample param_dict for a pin :
    { 'value':0, 'desc':'IN1: Input 1 of Mux', 'can_vary':True }

    First 3 characters of desc will be used as pin_tag

    """

    def __init__(self, pin_no, param_dict={}):

        self.pin_no = pin_no
        self.pin_tag = '   '
        self.__doc__ = ''
        self.can_vary = True
        self.setPinParam(param_dict)

    def setPinParam(self, param_dict):
        if isinstance(param_dict, dict):
            # If a dictionary of parameters is passed, store the contents of the dictionary to the
            # respective parameters
            for param in param_dict:
                if param == 'value':
                    self.value = param_dict[param]
                elif param == 'pin_tag':
                    if len(param_dict[param]) >= 3:
                        self.pin_tag = param_dict[param][:3].upper()
                elif param == 'desc':
                    self.__doc__ = param_dict[param]
                    if len(self.__doc__) >= 3:
                        self.pin_tag = self.__doc__[:3]
                elif param == 'can_vary':
                    self.can_vary = bool(param_dict[param])
                else:
                    print("ERROR: Unknown Parameters passed")
        elif (isinstance(param_dict, int)) and (param_dict in [0, 1, None]):
            # If the value is passed , store the value
            val = param_dict
            self.value = val
        else:
            raise Exception('ERROR: Unrecognized parameter passed.')

    def __str__(self):
        return str(self.value)

    def __call__(self):
        """ The call method returns the logic value of the pin """
        # This method can be used in IC implementations
        return logic(self.value)


def pinlist_quick(first_arg):
    """Defines a method to quickly convert a list of logic states to pin instances"""
    if isinstance(first_arg, list):
        # Quickly converts a list of Logic values to a list of Pin instances
        listofpins = list()
        for i in range(len(first_arg)):
            listofpins.append(
                Pin(i + 1, {'value': first_arg[i], 'desc': '   ', 'can_vary': True}))
        return listofpins
    else:
        raise Exception("ERROR: Unknown parameter type passed")


class logic():

    """
    Implements methods of AND OR and EXOR using BinPy library Gate modules
    Remaps all basic python implementation of gates on variable of type bool to BinPy's implementation of the same
    """

    def __init__(self, value=0):
        if value is bool:
            self.value = int(value)
        else:
            self.value = value
        # Tri state logic can be introduced later on ...

    def __add__(self, right):
        '''OR Gate equivalent'''
        return logic(OR(self.value, right.value).output())
        # Returns a logic instance corresponding to the boolean value of the
        # output of BinPy's OR Gate implementation

    def __or__(self, right):
        '''OR Gate equivalent'''
        return logic(OR(self.value, right.value).output())
        # Returns a logic instance corresponding to the boolean value of the
        # output of BinPy's OR Gate implementation

    def __xor__(self, right):
        '''XOR Gate'''
        return logic(XOR(self.value, right.value).output())
        # Returns a logic instance corresponding to the boolean value of the
        # output of BinPy's XOR Gate implementation

    def __mul__(self, right):
        '''AND Gate'''
        return logic(AND(self.value, right.value).output())
        # Returns a logic instance corresponding to the boolean value of the
        # output of BinPy's AND Gate implementation

    def __and__(self, right):
        '''AND Gate'''
        return logic(AND(self.value, right.value).output())
        # Returns a logic instance corresponding to the boolean value of the
        # output of BinPy's AND Gate implementation

    def __invert__(self):
        '''NOT Gate'''
        return logic(NOT(self.value).output())
        # Returns a logic instance corresponding to the boolean value of the
        # output of BinPy's NOT Gate implementation

    def __call__(self):
        '''Returns the binary equivalent of the logic value of self'''
        return int(self.value)

    def __int__(self):
        return int(self.value)

    def __str__(self):
        return str(int(value))
