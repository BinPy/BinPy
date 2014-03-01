__To Show how Pin class works__

* __Quick Summary:__

Initializing a Pin:

```
BinPy:3> pin_of_an_ic = Pin(1,{'value':0})
BinPy:4> d = {'value':1,'desc':'RST: Reset - Active High Resets the IC'}
BinPy:5> pin_of_an_ic.setPinParam(d)
```

Only currently supported attibutes can be set for a pin instance:
```
BinPy:6> pin_of_an_ic.setPinParam({'foo':'bar'})
ERROR: Unknown Parameters passed
```

* __Building an IC using Pin class:__

```
class IC_ICNO(Base_14pin):
    """
    Some docstring
    """
    
    def __init__(self):
        
```
Set the initial values of pins as a list. Do not use the zeroth element.
```
        self.pins = [None,0,0,None,None,0,0,0,0,0,None,None,0,0,1]
```
To quickly convert this list to a list of pin instances use the `pinlist_quick()` method:

```
        #Example of quick conversion from list of pins to list of pin instances
        self.pins = pinlist_quick(self.pins)
```
Set the `uses_pincls` attribute to `True`

```
        self.uses_pincls = True
```
To extensively use all the functionalities of the Pin class especially the pin_tag part:

Make a dictionary with the format { pin_no: dictionary_of_pin_attributes }
The dictionary_of_pin_attributes should contain:

`value`(if you have not specified it earlier) and `desc`

The description is of the format:

"ABC: Blah blah blah"

Where ABC is a 3 letter Pin Tag.

If you do not want any Pin Tag. Leave 3 spaces instead.

See The below example:

```

        d = {   1 : {'desc':'Q1 : Output of AND gate 1'},
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
            }
```
Then invoke `self.setIC() method with the parameter d:
```
        self.setIC(d)
```


Define a `run` method for the IC
``` 
    def run(self):
```
Create an empty output dictionary

```
        output = {}
```
Define the output equations for the output pins using overloaded operators of logic instance

Note that the pin instance ( say `self.pins[i]` ) retuns a logic instance initiated with its value:

i.e `self.pins[1]()` retuns a logic instance equivalent to `logic(self.pins[1].value)`

i.e if `self.pins[1]` has a `value` of `1`, it returns `logic(1)`

```
        output[3]  =  (  self.pins[1]()  & self.pins[2]()    )()
        output[4]  =  (  self.pins[5]()  & self.pins[6]()    )()
        output[10] =  (  self.pins[9]()  & self.pins[3]()    )()
        output[11] =  (  self.pins[12]() & self.pins[13]()   )()
```
Now this `output` is a dict of logic values of each pin.

Now set the Pins of the ic based on the current output :
```
        self.setIC(output)
```
If you want to draw the current configuration of the IC use the `drawIC()` method:

```
        self.drawIC()
```

Write some error handling codes to take care of erroneous inputs to an IC:

```
        if self.pins[7].value == 0 and self.pins[14].value == 1:
            return output
        else:
            print "Ground and VCC pins have not been configured correctly."
```

Voila! Your very own IC is configured using pin class.