PyIC
====
This package will serve as a base to develop circuit based applications or logical games on top of it. This package does not depend on any libraries other that pure Python
How to use
---------
```python
from PyIC import *
gates = Gates()
print gates.XOR(1, 1, 1)

#Operations
operator = Operation()
operator.add([1,0,1,1],[1,1])
operator.subtract([1,0,1,1],[1,1])
```
<strong>Output</strong><br/>
```python
1
{'carry': 0, 'sum': [1, 1, 1, 0]}
{'carry': 1, 'difference': [1, 0, 0, 0]}
```
Available Resources
-------------------
* All basic logic gates (NOT, OR, NOR, AND, NAND, XOR, XNOR)
* Combinational logics
	* Adder
	* Subtractor
	* Multiplyer
	* MUX
		* 2:1
		* 4:1
		* 8:1
		* 16:1
	* DMUX
		* 1:2
		* 1:4
		* 1:8
		* 1:16
	* Decoder