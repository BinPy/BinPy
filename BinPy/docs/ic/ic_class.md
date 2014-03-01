<h3>Usage of the IC class to create your own Base_NOOFPINS class</h3>
<br>
<br>
__1. IC class is the super most base class for all other IC's__


The IC class contains the following methods :
<br>
<br>

* `setIC(self, param_dict)` Method to set the pins of IC's to the respective logic states.<br>
It can handle both IC's defined via Pin class and those not defined via the Pin class.

Usage:<br>
```
ic = IC_ICNO()
p = {1:0,2:1,3:1,4:1}
```
Note that partial initialization is permitted. The other pins will be having the configuration as defined
at the time of coding. Or the last assigned value ( if assigned earlier using `setIC()` method
```
ic.setIC(p)
```



For an IC using `Pin` class the parameter dictionary *can* (the above initialization will work for both types of IC's though )
be more elaborately defined as:

```
d = {   1 : {'value':1, desc':'Q1 : Output of AND gate 1'},
        2 : {'value':1, 'desc':'A1 : Input 1 of AND gate 1'},
        3 : {'value':0, 'desc':'B1 : Input 2 of AND gate 1'},
        4 : {'value':1, 'desc':'C1 : Input 3 of AND gate 1'},
        5 : {'value':0, 'desc':'D1 : Input 4 of AND gate 1'},
        6 : {'value':0, 'desc':'NC '},
        7 : {'value':0, 'desc':'GND'},
        8 : {'value':0, 'desc':'NC '},
        9 : {'value':1, 'desc':'D2 : Input 4 of AND gate 2'},
        10: {'value':1, 'desc':'C2 : Input 3 of AND gate 2'},
        11: {'value':0, 'desc':'B2 : Input 2 of AND gate 2'},
        12: {'value':0, 'desc':'A2 : Input 1 of AND gate 2'},
        13: {'value':0, 'desc':'Q2 : Output of AND gate 2'},
        14: {'value':1, 'desc':'VCC'}
    }
```

The above parameter dictionary when passed will define the pin tags of the IC.
<br><br><br>


* `drawIC()` method: Which draws the current configuration of an IC:

Usage:
```
#Using a non pin class IC
ic = IC_7400()
ic.drawIC()
```
Output:
```
               _________ ________  
              |         U       |
              |                 |
     [0]   ---|  1           14 |---   [0]    
              |                 |
              |                 |
     [0]   ---|  2     7     13 |---   [0]    
              |                 |
              |                 |
     [Z]   ---|  3     4     12 |---   [0]    
              |                 |
              |                 |
     [0]   ---|  4     0     11 |---   [Z]    
              |                 |
              |                 |
     [0]   ---|  5     0     10 |---   [0]    
              |                 |
              |                 |
     [Z]   ---|  6            9 |---   [0]    
              |                 |
              |                 |
     [0]   ---|  7            8 |---   [Z]    
              |                 |
              |_________________|  

```

Z - Is for the 3rd state of Tristated Pins [ The disconnected state or High impedance state ] This is shown when the pin value is `None`

For Pin class IC's with `pin_tag` defined for all the pins, the pin_tags are shown besides each pin.

Usage:
```
ic = IC_4082
ic.drawIC()
```

Output:
```
               _________ ________  
              |         U       |
              |                 |
 Q1  [Z]   ---|  1           14 |---   [1] VCC
              |                 |
              |                 |
 A1  [0]   ---|  2     4     13 |---   [0] Q2 
              |                 |
              |                 |
 B1  [0]   ---|  3     0     12 |---   [0] A2 
              |                 |
              |                 |
 C1  [0]   ---|  4     8     11 |---   [Z] B2 
              |                 |
              |                 |
 D1  [0]   ---|  5     2     10 |---   [Z] C2 
              |                 |
              |                 |
 NC  [0]   ---|  6            9 |---   [0] D2 
              |                 |
              |                 |
 GND [0]   ---|  7            8 |---   [0] NC 
              |                 |
              |_________________|  

```
<br><br>

__2. Use this IC class to derive other classes of IC's Such as `Base_14pin`:__

```
class Base_14pin(IC):
    """
    Some doc string
    """
    total_pins = 14
```
Set the uses_pincls to false to maintain compatibility with non pin class IC's
```
    uses_pincls = False
```

Define a setPin method accepting individual Pin_nos and its values as parameters:

```
    def setPin(self, pin_no, pin_value):
```
Handle unexpected inputs
```
        if pin_no<1 or pin_no>14:
            raise Exception("ERROR: There are only 14 pins in this IC")
```
Finally define how the pins will be updated when the uses_pincls is True and also when it is not.
* When the IC uses Pin class:
```
        if not self.uses_pincls:
            self.pins[pin_no] = pin_value
```
* When the IC does not use pin class:
Pass the pin value ( which could be a parameter dictionary ) to the `setPinParam()` method of the particular pin no ( `self.pins[pin_no]` )
```
        else:
            self.pins[pin_no].setPinParam(pin_value)
```
* Define a method to To set Pin Parameters if Pin class is used:
```
    def setPinParam(self,pin_no,parm_dict):
        if pin_no<1 or pin_no>14:
            raise Exception("ERROR: There are only 14 pins in this IC")
        if uses_pincls:
            self.pins[pin_no].setPinParam(parm_dict)
        else:
            raise Exception("ERROR: IC Does not use Pinset class")
```



