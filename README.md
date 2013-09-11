What is BinPy?
---------------
This package will serve as a base to develop circuit based applications or logical games on top of it. 
This package does not depend on any external library other than pure Python.

How to use
----------

```python
from BinPy import *
gates = Gates()
print gates.XOR(1, 1, 1)

#Operations
operator = Operation()
print operator.add([1,0,1,1],[1,1])
print operator.subtract([1,0,1,1],[1,1])

#Combinational Logic
myMUX = MUX()
print "MUX Out: ", myMUX.run([1,0,0,0,1,1,1,1],[0,0,1])

#Algorithms 
#Includes the Quine-McCluskey algorithm for solving K-Maps
FinalEquation = QM(['A','B'])
print "Minimized Boolean Equation : " , FinalEquation.get_function(qm.solve([0,1,2],[])[1])


#IC
myIC = IC_7400()
p = {1:1,2:0,4:0,5:0,7:0,10:1,9:1,13:0,12:0,14:1}
myIC.setIC(p)
print "IC_7400 Out: ", myIC.run()

myIC1 = IC_7401()
p = {2:0,3:1,5:0,6:0,7:0,8:1,9:1,11:0,12:0,14:1}
myIC1.setIC(p)
print "IC_7401 Out: ", myIC1.run()
```
<strong>Output</strong><br/>
```python
1
{'carry': 0, 'sum': [1, 1, 1, 0]}
{'carry': 1, 'difference': [1, 0, 0, 0]}
MUX Out:  0
IC_7400 Out:  {8: 0, 11: 1, 3: 1, 6: 1}
IC_7401 Out:  {1: 1, 10: 0, 4: 1, 13: 1}
Minimized Boolean Equation : ((NOT B) OR (NOT A))
```
Available Resources
-------------------
* All basic logic gates (NOT, OR, NOR, AND, NAND, XOR, XNOR)
* Combinational logics
	* Adder
	* Subtractor
	* Multiplyer
	* MUX (2:1, 4:1, 8:1, 16:1)
	
* IC
	* 7400
	* 741G00
	* 7401
	* 7402
	* 7403
* Algorithms
	* Quine-McCluskey Algorithm (To find minimized Boolean Equation)
	* Moore Machine Optimizer

Future Works
------------
* Introduction of all ICs
* Introduction of problem solving algorithms
* Addition of Microprocessors and Analog Devices
* Graphical representation of the circuit
* ...
