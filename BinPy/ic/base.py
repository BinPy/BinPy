"""
This module includes all the base classes for different ICs.
"""


class IC:
    """
    This is a base class for IC
    """
    def __init__(self):
        pass	    
    
    def setIC(self, pin_conf):
        """
        This method takes a dictionary with key:pin_no and value:pin_value
        """
        for i in pin_conf:
	    self.pins[i] = pin_conf[i]

class Base_5pin(IC):
    """
    This method takes base class for IC's having 5 pins
    """
    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>5:
	    raise Exception("ERROR: There are only 5 pins in this IC")
        self.pins[pin_no] = pin_value

class Base_14pin(IC):
    """
    This method takes base class for IC's having 14 pins
    """
    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>14:
	    raise Exception("ERROR: There are only 14 pins in this IC")
        self.pins[pin_no] = pin_value

class Base_16pin(IC):
    """
    This method takes base class for IC's having 16 pins
    """
    def setPin(self, pin_no, pin_value):
        if pin_no<1 or pin_no>16:
	    raise Exception("ERROR: There are only 16 pins in this IC")
        self.pins[pin_no] = pin_value